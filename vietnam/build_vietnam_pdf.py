#!/usr/bin/env python3
"""Plan B itinerary — Hanoi & Sapa, 7-12 September 2026.

Replaces the Bandung trip after the Anak Krakatau eruption closed CGK.
Same six days, same outfit themes, no driver needed.

Run:    python3 vietnam/build_vietnam_pdf.py
Output: vietnam/Itinerary-Vietnam-Hanoi-Sapa.html  +  .pdf
"""

import html
import os
import shutil
import subprocess
import urllib.parse

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(OUT_DIR, "Itinerary-Vietnam-Hanoi-Sapa.html")
PDF_PATH = os.path.join(OUT_DIR, "Itinerary-Vietnam-Hanoi-Sapa.pdf")

GUESTS = "Haris Haikal &amp; Aina Izzaty"

# rows:  ("stop", time, place, area, duration, note)
#        ("move", text, "", "", "", "")
DAYS = [
    dict(
        n="DAY 1", date="Monday, 7 September", title="Fly to Hanoi &rarr; straight up to Sapa",
        color="#B26C12", outfit="Comfy travel outfit — layers, Sapa is cool on arrival",
        start="Very early KLIA", finish="~16.00 in Sapa",
        sleep="Sapa (nights 1–3)",
        rows=[
            ("stop", "06.05", "KUL → HAN — earliest departure",
             "KLIA (check which terminal your airline uses)", "3h 25m",
             "AirAsia has the 06.05; Malaysia Airlines, Vietjet, Vietnam Airlines and Batik also fly this route — about 4+ departures a day, so there is room to move. Vietnam is <b>1 hour behind Malaysia</b>."),
            ("stop", "~08.30", "Land at Noi Bai (HAN), Terminal 2", "Hanoi", "~1h",
             "Immigration is visa-free for Malaysians (30 days). Grab a SIM/eSIM and VND cash at the airport, and eat before the transfer."),
            ("move", "TRANSFER: Noi Bai &rarr; Sapa by limousine van &mdash; ~5.5&ndash;6.5 hours, book in advance", "", "", "", ""),
            ("stop", "~15.30", "Check in — Sapa town", "Sapa, Lao Cai province", "1h",
             "Vans pick up in the arrivals hall and drive straight up, no need to go into Hanoi first. Rest stop halfway."),
            ("stop", "~17.00", "Sapa Stone Church + Sapa Lake", "Sapa town centre", "1h",
             "Easy first evening on foot. The church square is the town's meeting point."),
            ("stop", "~18.30", "Dinner in town + Sapa night market", "Sapa town centre", "2h",
             "Grilled skewers, hotpot, salmon (Sapa farms it). Cool evening — bring the jacket out."),
        ],
        notes=[
            "Long travel day by design, exactly like the old Day 1 — a flight then a long road transfer.",
            "Book the Noi Bai→Sapa van <b>before you fly</b>; the good ones sell out and you do not want to negotiate at 08.30 with luggage.",
            "Sapa sits at ~1,500 m. Nights are 15–18°C. The warm layer you packed for Kawah Putih is exactly right.",
        ],
    ),
    dict(
        n="DAY 2", date="Tuesday, 8 September", title="Golden rice terraces — Muong Hoa valley",
        color="#15764F", outfit="Emerald denim casual — green denim against gold terraces",
        start="08.30", finish="~20.00",
        sleep="Sapa (night 2)",
        rows=[
            ("stop", "08.30", "Breakfast, then out", "", "—",
             "Ask the hotel about the day's weather. Mornings are the clear window in September."),
            ("stop", "~09.00", "Cat Cat Village", "2 km from Sapa town", "2.5h",
             "Terraces, waterfall, H'Mong village, and the swing/photo spots. Walk down, take a xe om or car back up — it is steep."),
            ("move", "~20 min by car", "", "", "", ""),
            ("stop", "~12.00", "Lunch in town", "Sapa town centre", "1h", ""),
            ("stop", "~13.30", "Muong Hoa Valley — Lao Chai &amp; Ta Van",
             "Muong Hoa valley, below Sapa town", "3.5h",
             "<b>The reason to be here this week.</b> The terraces are gold and being harvested in the first half of September, with buffaloes and farmers still working them. Hire a car or a local guide for the loop; easy walking sections between viewpoints."),
            ("move", "~30 min back up to town", "", "", "", ""),
            ("stop", "~18.00", "Sunset café over the valley", "Sapa town, valley-facing", "1.5h",
             "Viettrekking, The Haven, or any terrace café on the ridge. Golden hour over the terraces is the shot of the trip."),
            ("stop", "~19.30", "Dinner — Sapa local", "Sapa town centre", "1.5h", ""),
        ],
        notes=[
            "September light is soft and warm early and late — plan the terrace photos for before 10.00 and after 16.00.",
            "Take a light rain shell. Showers pass through and then it clears.",
            "Shoes with grip: the terrace paths are clay and slippery after rain.",
        ],
    ),
    dict(
        n="DAY 3", date="Wednesday, 9 September", title="Fansipan summit + Sapa cafés",
        color="#6D2E5B", outfit="Cream elegant — the pagodas and cloud decks suit it",
        start="09.00", finish="~20.00",
        sleep="Sapa (night 3)",
        rows=[
            ("stop", "09.00", "Sun World Fansipan Legend — cable car",
             "Station is ~10 min from Sapa town", "4h",
             "Record-holding cable car to Indochina's highest peak (3,143 m). Pagoda complex, gardens and cloud sea at the top. <b>It is cold and windy up there</b> — cream outfit plus the warm layer."),
            ("move", "~15 min back to town", "", "", "", ""),
            ("stop", "~13.30", "Lunch in town", "Sapa town centre", "1h", ""),
            ("stop", "~15.00", "Sapa café afternoon", "Sapa town centre", "2.5h",
             "Cong Caphe for coconut coffee, then a valley-view terrace. This is the Braga-and-Congo part of the old plan, transplanted."),
            ("stop", "~18.00", "Sapa market — souvenirs", "Sapa town centre", "1h",
             "Brocade, indigo textiles, and the H'Mong embroidery. Bargaining expected, politely."),
            ("stop", "~19.30", "Dinner + pack", "", "1.5h",
             "Long road day tomorrow — bags ready tonight."),
        ],
        notes=[
            "If the summit is fogged in, flip this day with Day 2 — the cable car is worth a clear morning.",
            "Buy the cable car ticket at the station or online; it includes the funicular from the station up to the cable car.",
        ],
    ),
    dict(
        n="DAY 4", date="Thursday, 10 September", title="Back to Hanoi — Old Quarter evening",
        color="#C0437A", outfit="Cute pink &amp; white — Hanoi's yellow colonial walls are the backdrop",
        start="08.00 from Sapa", finish="~21.30",
        sleep="Hanoi Old Quarter (nights 4–5)",
        rows=[
            ("stop", "08.00", "Checkout, board the van back", "Sapa town", "—",
             "Morning departures are the most comfortable. Confirm the seat the night before."),
            ("move", "TRANSFER: Sapa &rarr; Hanoi &mdash; ~5.5&ndash;6 hours down the expressway", "", "", "", ""),
            ("stop", "~14.00", "Check in — Hanoi Old Quarter", "Hoan Kiem district", "1h",
             "Stay inside the Old Quarter or the French Quarter and you can walk most of the next two days."),
            ("stop", "~15.30", "Hoan Kiem Lake + Ngoc Son Temple", "Hoan Kiem", "1.5h",
             "The red bridge is the classic Hanoi photo. Five minutes from the Old Quarter."),
            ("move", "10 min walk", "", "", "", ""),
            ("stop", "~17.00", "Egg coffee — Cafe Giang or Note Coffee", "Old Quarter", "1h",
             "Cà phê trứng, the Hanoi original. Note Coffee is the wall-of-sticky-notes one."),
            ("stop", "~18.30", "St Joseph's Cathedral + Nha Tho street", "Hoan Kiem", "1h",
             "Neo-gothic cathedral, café street either side, best light just before dark."),
            ("stop", "~20.00", "Dinner + Ta Hien street", "Old Quarter", "1.5h",
             "Bun cha, pho, banh mi. Ta Hien is the busy corner street — lively, safe, loud."),
        ],
        notes=[
            "Hanoi in September is warm and humid, ~28–32°C — the opposite of Sapa. Pack the layers away.",
            "Weekend evenings the Old Quarter goes car-free, but you arrive Thursday, so expect normal traffic.",
            "Crossing the road: walk slowly and steadily, do not stop. The scooters flow around you.",
        ],
    ),
    dict(
        n="DAY 5", date="Friday, 11 September", title="Hanoi full day — temples, cafés, souvenirs",
        color="#7A5410", outfit="Elegant modern — cream and refined, same as the old Day 3",
        start="08.30", finish="~21.00",
        sleep="Hanoi Old Quarter (night 5)",
        rows=[
            ("stop", "08.30", "Breakfast — pho at a street shop", "Old Quarter", "45 min",
             "Pho bo or pho ga, plastic stools, best breakfast of the trip."),
            ("stop", "~09.30", "Temple of Literature", "Dong Da, ~10 min by Grab", "1.5h",
             "Vietnam's first university, 1070. Courtyards, red gates, calligraphy — the elegant-outfit location of the day."),
            ("move", "~15 min by Grab", "", "", "", ""),
            ("stop", "~11.30", "Tran Quoc Pagoda + West Lake", "Tay Ho", "1.5h",
             "Oldest pagoda in Hanoi, on a causeway in the lake. Lunch at a West Lake café after."),
            ("move", "~15 min by Grab", "", "", "", ""),
            ("stop", "~14.30", "Hanoi Train Street (from a café)", "Tran Phu / Phung Hung area", "1h",
             "The track is barricaded — you go in as a café customer. Check the day's train times with the café; they know."),
            ("stop", "~16.00", "Souvenirs — Hang Gai silk street", "Old Quarter", "1.5h",
             "Silk, lacquerware, ceramics, and Vietnamese coffee beans. This is the Kartika Sari slot of the old plan."),
            ("stop", "~18.00", "Sunset — Long Bien Bridge or a rooftop", "Old Quarter edge", "1h", ""),
            ("stop", "~19.30", "Farewell dinner", "French Quarter or Old Quarter", "1.5h",
             "Cha ca la vong (turmeric fish) is the Hanoi speciality worth planning around."),
        ],
        notes=[
            "Everything today is 10–15 minutes apart by Grab or Xanh SM. No driver needed.",
            "If it rains hard, swap Train Street for the Ceramic Mosaic wall or a coffee crawl — Hanoi is a good rain city.",
            "Pack tonight and keep the coffee/silk in carry-on if it's fragile.",
        ],
    ),
    dict(
        n="DAY 6", date="Saturday, 12 September", title="Fly home",
        color="#5B6560", outfit="Comfy travel outfit",
        start="Depends on flight", finish="KUL",
        sleep="—",
        rows=[
            ("stop", "08.00", "Breakfast + last walk", "Old Quarter", "1.5h",
             "Hoan Kiem Lake in the morning is full of people exercising — a nice last hour."),
            ("stop", "~10.30", "Checkout → Noi Bai Airport (HAN)", "~45 min by Grab or hotel car", "—",
             "International departures are Terminal 2. Allow for traffic on the bridge."),
            ("stop", "~11.30", "Check-in + immigration", "Noi Bai Terminal 2", "2h buffer",
             "Standard 2 hours for an international departure."),
            ("stop", "afternoon", "HAN → KUL", "", "~3h 25m",
             "Vietnam is 1 hour behind, so you land in Malaysia later on the clock than the flight time suggests."),
        ],
        notes=[
            "Book the return on whichever airline you flew out with if you want one booking reference for the whole trip.",
        ],
    ),
]

SUMMARY = [
    ("Day 1", "Mon, 7 Sep", "Fly + transfer", "KUL → Hanoi → Sapa", "Sapa"),
    ("Day 2", "Tue, 8 Sep", "Golden terraces", "Cat Cat, Muong Hoa valley", "Sapa"),
    ("Day 3", "Wed, 9 Sep", "Mountain + cafés", "Fansipan, Sapa town", "Sapa"),
    ("Day 4", "Thu, 10 Sep", "Transfer + city", "Sapa → Hanoi Old Quarter", "<b>Move</b> → Hanoi"),
    ("Day 5", "Fri, 11 Sep", "Full day Hanoi", "Temples, cafés, souvenirs", "Hanoi"),
    ("Day 6", "Sat, 12 Sep", "Fly home", "Hanoi → KUL", "—"),
]

BOOK_TONIGHT = [
    ("Ask Malaysia Airlines to reroute, don't cancel",
     "MAS flies KUL–Hanoi themselves. If they cancel the CGK flight, ask to be moved onto their Hanoi service instead of taking the refund — cheapest way to switch. <b>+60 3-7843-3000</b>"),
    ("Flights KUL → HAN, 7 Sept",
     "~4+ departures a day, earliest 06.05 (AirAsia); also Vietnam Airlines, Vietjet, Batik. 3h 25m. Book the 12 Sept return at the same time."),
    ("Noi Bai → Sapa transfer, 7 Sept",
     "Limousine van direct from the airport, ~5.5–6.5 hours, meets you in arrivals. Book before you fly."),
    ("Sapa → Hanoi transfer, 10 Sept morning", "Same operators, book both legs together if you can."),
    ("Hotels: 3 nights Sapa (7–9), 2 nights Hanoi Old Quarter (10–11)",
     "Sapa: valley-view room is worth it. Hanoi: stay inside Hoan Kiem so you can walk."),
    ("Cancel or move the Bandung side",
     "Holiday Inn Pasteur, Swiss-Belresort Dago, Fairfield CGK — ask for a waiver citing the airport closure. Message Kiki."),
    ("Travel insurance", "Re-issue for Vietnam, and keep the Bandung cancellation paperwork for the claim."),
    ("eSIM for Vietnam + download offline maps", "Sapa and the valley have patchy signal, same as the highlands."),
]

GOOD_TO_KNOW = [
    ("Visa", "Malaysians: visa-free, 30 days. Carry proof of onward travel and hotel bookings."),
    ("Money", "Vietnamese dong (VND). Cards work in cities; Sapa markets and villages are cash."),
    ("Getting around", "Grab and Xanh SM (electric taxis) everywhere in Hanoi. In Sapa: hotel cars, xe om, or a hired car for the valley. No driver to arrange."),
    ("Weather", "Sapa 18–25°C, cool nights, passing showers. Hanoi warm and humid, 28–32°C. Pack a rain shell and one warm layer."),
    ("Time", "Vietnam is UTC+7 — one hour behind Malaysia, same as Jakarta was."),
    ("Why now", "Sapa's terraces are gold and being harvested in the first half of September — your exact dates."),
]


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


NO_MAP = ("Breakfast", "Checkout", "Lunch", "Dinner", "Check in", "Check-in", "Land at",
          "KUL →", "HAN →", "Sunset café", "Pack", "Souvenirs")


def maps_link(name, area):
    q = urllib.parse.quote(f"{strip_tags(name)} {strip_tags(area) or 'Vietnam'}")
    return f"https://www.google.com/maps/search/?api=1&amp;query={q}"


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
.notebox .txt b { display:block; }
.notebox .txt span { color:#4A4A44; }

.ct { display:flex; flex-wrap:wrap; }
.ct .c { width:50%; padding:2.5px 10px 2.5px 0; font-size:8.4pt; }
.ct .c b { display:block; color:#222; }
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

.dnotes { margin-top:10px; border-left:4px solid #B26C12; background:#FDF8EF; padding:9px 12px; }
.dnotes b.h { display:block; font-size:8.5pt; text-transform:uppercase; letter-spacing:1px; color:#8A5A10; margin-bottom:4px; }
.dnotes li { margin-left:15px; font-size:9pt; padding:1px 0; }

.sign { margin-top:7px; border:1px dashed #B9B9AF; border-radius:5px; padding:7px 12px; font-size:8.3pt; color:#55554E; }
.foot { margin-top:12px; font-size:8pt; color:#84847C; text-align:center; }
"""


def render_day(d):
    rows = []
    for r in d["rows"]:
        if r[0] == "move":
            rows.append(f'<tr class="move"><td colspan="4">{r[1]}</td></tr>')
            continue
        _, t, place, area, dur, note = r
        plain = strip_tags(place)
        link = ""
        if not plain.startswith(NO_MAP):
            link = f'<a href="{maps_link(place, area)}">&#128205; Open in Google Maps</a>'
        area_html = f'<span class="area">{area}</span>' if area else ""
        rows.append(
            f'<tr><td class="jam">{t}</td>'
            f'<td class="tuj"><b>{place}</b>{area_html}{link}</td>'
            f'<td class="lama">{dur}</td>'
            f'<td class="cat">{note}</td></tr>'
        )
    notes = "".join(f"<li>{n}</li>" for n in d["notes"])
    return f"""
<div class="page">
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
  <div class="foot">Vietnam · {GUESTS} · {d['n']} · times are estimates, shuffle freely</div>
</div>"""


def build_html():
    summary = "".join(
        f'<tr><td class="d">{a}</td><td class="d">{b}</td><td>{c}</td><td>{e}</td><td>{f}</td></tr>'
        for a, b, c, e, f in SUMMARY
    )
    book = "".join(
        f'<div class="row"><div class="num">{i+1}</div><div class="txt"><b>{t}</b><span>{s}</span></div></div>'
        for i, (t, s) in enumerate(BOOK_TONIGHT)
    )
    know = "".join(f'<div class="c"><b>{a}</b><span>{b}</span></div>' for a, b in GOOD_TO_KNOW)

    cover = f"""
<div class="page">
  <div class="cover-head">
    <div class="k">Plan B &middot; Bandung is off (Anak Krakatau)</div>
    <h1>Vietnam — Hanoi &amp; Sapa<br>7 &ndash; 12 September 2026</h1>
    <div class="s">{GUESTS} &middot; same six days, same outfit themes, no driver needed<br>
    Sapa's rice terraces are gold and being harvested in exactly this window.</div>
  </div>

  <h2>The Six Days</h2>
  <table class="sum">
    <tr><th>Day</th><th>Date</th><th>Shape</th><th>Where</th><th>Sleep</th></tr>
    {summary}
  </table>

  <h2 class="alt">Book Tonight, In This Order</h2>
  <div class="notebox">{book}</div>

  <h2>Good To Know</h2>
  <div class="ct">{know}</div>

  <div class="sign">
    <b>Flight out:</b> ______________________ &nbsp; <b>Flight home:</b> ______________________ &nbsp;
    <b>Booking ref:</b> ______________________<br>
    <b>Sapa van (out):</b> ______________________ &nbsp; <b>Sapa van (back):</b> ______________________<br>
    Flight times and frequencies checked 6 Sept 2026 — confirm live availability and fares when booking.
  </div>
</div>"""

    days = "".join(render_day(d) for d in DAYS)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<title>Vietnam — Hanoi &amp; Sapa, 7-12 September 2026</title>
<style>{CSS}</style></head><body>{cover}{days}</body></html>"""


def find_chromium():
    for n in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        p = shutil.which(n)
        if p:
            return p
    return subprocess.run(["bash", "-lc", "ls /opt/pw-browsers/*/chrome-linux/chrome 2>/dev/null | head -1"],
                          capture_output=True, text=True).stdout.strip() or None


def main():
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(build_html())
    print("HTML :", HTML_PATH)
    chrome = find_chromium()
    if not chrome:
        print("Chromium not found — open the HTML and Print to PDF manually.")
        return
    subprocess.run([chrome, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={PDF_PATH}",
                    "file://" + HTML_PATH], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("PDF  :", PDF_PATH)


if __name__ == "__main__":
    main()
