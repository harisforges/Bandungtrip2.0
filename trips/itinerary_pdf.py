"""Shared renderer for the trip itinerary PDFs.

A trip is a cover (summary table, numbered book-now list, practical notes)
plus one page per day. Day rows are either a stop or a travel leg:

    ("stop", time, place, area, duration, note)
    ("move", text, "", "", "", "")

Used by vietnam/ and thailand/. Kiki's Indonesian driver PDF predates this
and keeps its own renderer — different columns, different audience.
"""

import html
import os
import shutil
import subprocess
import urllib.parse

CSS = """
@page { size: A4; margin: 13mm 12mm 12mm; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: #1b1b1b; font-size: 10pt; line-height: 1.35; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }

.cover-head { background:#15764F; color:#fff; padding:14px 18px; border-radius:6px; }
.cover-head .k { font-size:9pt; letter-spacing:2.5px; text-transform:uppercase; opacity:.85; }
.cover-head h1 { font-size:19pt; line-height:1.1; margin:6px 0 8px; font-weight:700; }
.cover-head .s { font-size:10pt; opacity:.95; }

h2 { font-size:11.5pt; margin:9px 0 5px; padding-bottom:4px; border-bottom:2px solid #15764F; color:#15764F; }
h2.alt { color:#B23A16; border-bottom-color:#B23A16; }

.sum { width:100%; border-collapse:collapse; }
.sum th { background:#EDEDE7; font-size:8.5pt; text-transform:uppercase; letter-spacing:.6px;
          text-align:left; padding:5px 7px; border:1px solid #CFCFC6; }
.sum td { padding:3.5px 7px; border:1px solid #CFCFC6; font-size:8.8pt; vertical-align:top; }
.sum td.d { font-weight:700; white-space:nowrap; }
.sum tr:nth-child(even) td { background:#FAFAF7; }

.notebox { border:1px solid #E3C7A6; background:#FDF6EC; border-radius:5px; padding:8px 12px; }
.notebox .row { display:flex; gap:9px; padding:2px 0; }
.notebox .row + .row { border-top:1px dotted #E3C7A6; }
.notebox .num { flex:0 0 15px; height:15px; border-radius:3px; background:#B23A16; color:#fff;
                font-size:8pt; font-weight:700; text-align:center; line-height:15px; }
.notebox .txt { flex:1; font-size:8.5pt; }
.notebox .txt > b { display:block; }
.notebox .txt span { color:#4A4A44; }

.ct { display:flex; flex-wrap:wrap; }
.ct .c { width:50%; padding:2.5px 10px 2.5px 0; font-size:8.4pt; }
.ct.three .c { width:33.33%; font-size:8pt; padding-right:8px; }
.ct .c > b { display:block; color:#222; }
.ct .c span { color:#4A4A44; }

.dayhead { color:#fff; padding:12px 16px; border-radius:6px 6px 0 0; }
.dayhead .n { font-size:8.5pt; letter-spacing:2.5px; text-transform:uppercase; opacity:.9; }
.dayhead h1 { font-size:17pt; font-weight:700; margin:2px 0 3px; }
.dayhead .dt { font-size:10pt; opacity:.95; }
.daymeta { display:flex; border:1px solid #D8D8D0; border-top:none; }
.daymeta div { flex:1; padding:7px 12px; font-size:9pt; border-right:1px solid #E6E6DF; }
.daymeta div:last-child { border-right:none; }
.daymeta span { display:block; font-size:7.5pt; letter-spacing:1px; text-transform:uppercase; color:#7A7A72; }
.outfit { border:1px solid #D8D8D0; border-top:none; background:#F1F5F2; padding:6px 12px; font-size:9pt; color:#15764F; }

.sched { width:100%; border-collapse:collapse; margin-top:10px; }
.sched th { background:#EDEDE7; font-size:8pt; text-transform:uppercase; letter-spacing:.7px;
            text-align:left; padding:5px 7px; border:1px solid #CFCFC6; }
.sched td { border:1px solid #D8D8D0; padding:5px 7px; font-size:9.5pt; vertical-align:top; }
.sched td.jam { width:56px; font-weight:700; white-space:nowrap; font-size:10pt; }
.sched td.tuj { width:33%; }
.sched td.tuj b { font-size:10pt; }
.sched td.tuj .area { display:block; color:#5C5C55; font-size:8.5pt; margin-top:2px; }
.sched td.tuj a { display:block; color:#1a5fb4; font-size:8pt; margin-top:2px; text-decoration:none; }
.sched td.lama { width:60px; text-align:center; font-size:8.5pt; color:#444; }
.sched td.cat { font-size:9pt; color:#33332E; }
.sched tr.move td { background:#F1F5F2; color:#15764F; font-weight:700; font-size:9pt;
                    text-align:center; padding:5px; }
.compact .sched td { padding:3px 6px; font-size:8.8pt; }
.compact .sched td.tuj b, .compact .sched td.jam { font-size:9.2pt; }
.compact .dnotes li { font-size:8.5pt; }

.dnotes { margin-top:10px; border-left:4px solid #B26C12; background:#FDF8EF; padding:9px 12px; }
.dnotes b.h { display:block; font-size:8.5pt; text-transform:uppercase; letter-spacing:1px; color:#8A5A10; margin-bottom:4px; }
.dnotes li { margin-left:15px; font-size:9pt; padding:1px 0; }

.sign { margin-top:7px; border:1px dashed #B9B9AF; border-radius:5px; padding:7px 12px; font-size:8.3pt; color:#55554E; }
.foot { margin-top:12px; font-size:8pt; color:#84847C; text-align:center; }
"""


def strip_tags(s):
    out, depth = [], 0
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth = max(0, depth - 1)
        elif depth == 0:
            out.append(ch)
    return html.unescape("".join(out)).strip()


def maps_link(name, area, fallback):
    q = urllib.parse.quote(f"{strip_tags(name)} {strip_tags(area) or fallback}")
    return f"https://www.google.com/maps/search/?api=1&amp;query={q}"


def render_day(d, travellers, country, no_map):
    rows = []
    for r in d["rows"]:
        if r[0] == "move":
            rows.append(f'<tr class="move"><td colspan="4">{r[1]}</td></tr>')
            continue
        _, t, place, area, dur, note = r
        link = ""
        if not strip_tags(place).startswith(no_map):
            link = f'<a href="{maps_link(place, area, country)}">&#128205; Open in Google Maps</a>'
        area_html = f'<span class="area">{area}</span>' if area else ""
        rows.append(
            f'<tr><td class="jam">{t}</td>'
            f'<td class="tuj"><b>{place}</b>{area_html}{link}</td>'
            f'<td class="lama">{dur}</td>'
            f'<td class="cat">{note}</td></tr>'
        )
    notes = "".join(f"<li>{n}</li>" for n in d["notes"])
    compact = " compact" if d.get("compact") else ""
    return f"""
<div class="page{compact}">
  <div class="dayhead" style="background:{d['color']}">
    <div class="n">{d['n']}</div>
    <h1>{d['title']}</h1>
    <div class="dt">{d['date']}</div>
  </div>
  <div class="daymeta">
    <div><span>Start</span>{d['start']}</div>
    <div><span>Finish</span>{d['finish']}</div>
    <div><span>Sleep</span>{d['sleep']}</div>
  </div>
  <div class="outfit"><b>Outfit:</b> {d['outfit']}</div>
  <table class="sched">
    <tr><th>Time</th><th>Where</th><th>How long</th><th>Notes</th></tr>
    {''.join(rows)}
  </table>
  <div class="dnotes"><b class="h">Notes for the day</b><ul>{notes}</ul></div>
  <div class="foot">{country} · {travellers} · {d['n']} · times are estimates, shuffle freely</div>
</div>"""


def render_extra(trip):
    """Optional closing pages: reference tables (food, hotels, places that didn't fit)."""
    pages = trip.get("extra_pages") or ([trip["extra_page"]] if trip.get("extra_page") else [])
    return "".join(render_extra_page(trip, x) for x in pages)


def render_extra_page(trip, x):
    def cell(name, area):
        if x.get("no_maps"):
            return f'<b>{name}</b>'
        link = maps_link(name, area, trip["country"])
        return f'<b>{name}</b><a href="{link}">&#128205; Open in Google Maps</a>'

    rows = "".join(
        f'<tr><td class="tuj">{cell(name, area)}</td>'
        f'<td class="lama" style="width:118px">{area}</td>'
        f'<td class="cat">{note}</td></tr>'
        for name, area, note in x["rows"]
    )
    head = x.get("col_heads", ("Place", "Where", "Why, and when to slot it in"))
    return f"""
<div class="page">
  <div class="dayhead" style="background:{x['color']}">
    <div class="n">{x['kicker']}</div>
    <h1>{x['title']}</h1>
    <div class="dt">{x['subtitle']}</div>
  </div>
  <table class="sched" style="margin-top:0">
    <tr><th>{head[0]}</th><th>{head[1]}</th><th>{head[2]}</th></tr>
    {rows}
  </table>
  <div class="dnotes"><b class="h">{x.get("notes_head", "How to use this page")}</b><ul>{''.join(f'<li>{n}</li>' for n in x['notes'])}</ul></div>
  <div class="foot">{trip['country']} · {trip['travellers']} · {x.get('foot', 'reference')}</div>
</div>"""


def build_html(trip):
    summary = "".join(
        '<tr>' + "".join(
            f'<td class="d">{c}</td>' if i < 2 else f'<td>{c}</td>'
            for i, c in enumerate(row)
        ) + '</tr>'
        for row in trip["summary_rows"]
    )
    heads = "".join(f"<th>{h}</th>" for h in trip["summary_head"])
    book = "".join(
        f'<div class="row"><div class="num">{i+1}</div><div class="txt"><b>{t}</b><span>{s}</span></div></div>'
        for i, (t, s) in enumerate(trip["book_now"])
    )
    three = " three" if trip.get("know_cols") == 3 else ""
    summary_title = trip.get("summary_title", "The Six Days")
    know = "".join(f'<div class="c"><b>{a}</b><span>{b}</span></div>' for a, b in trip["good_to_know"])

    cover = f"""
<div class="page">
  <div class="cover-head">
    <div class="k">{trip['kicker']}</div>
    <h1>{trip['title']}</h1>
    <div class="s">{trip['subtitle']}</div>
  </div>

  <h2>{summary_title}</h2>
  <table class="sum"><tr>{heads}</tr>{summary}</table>

  <h2 class="alt">{trip['book_now_head']}</h2>
  <div class="notebox">{book}</div>

  <h2>Good To Know</h2>
  <div class="ct{three}">{know}</div>

  <div class="sign">{trip['sign']}</div>
</div>"""

    days = "".join(
        render_day(d, trip["travellers"], trip["country"], trip["no_map"])
        for d in trip["days"]
    )
    return (f'<!DOCTYPE html>\n<html lang="en"><head><meta charset="UTF-8">\n'
            f'<title>{trip["doc_title"]}</title>\n<style>{CSS}</style></head>'
            f'<body>{cover}{days}{render_extra(trip)}</body></html>')


def find_chromium():
    for n in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        p = shutil.which(n)
        if p:
            return p
    return subprocess.run(["bash", "-lc", "ls /opt/pw-browsers/*/chrome-linux/chrome 2>/dev/null | head -1"],
                          capture_output=True, text=True).stdout.strip() or None


def write(trip, html_path, pdf_path):
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(build_html(trip))
    print("HTML :", html_path)
    chrome = find_chromium()
    if not chrome:
        print("Chromium not found — open the HTML and Print to PDF manually.")
        return
    subprocess.run([chrome, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
                    "file://" + os.path.abspath(html_path)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("PDF  :", pdf_path)
