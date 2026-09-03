#!/usr/bin/env python3
"""Bikin jadwal PDF versi sopir (Pak Kiki) dari itinerary Bandung 7-12 Sept 2026.

Jalankan:  python3 kiki/build_kiki_pdf.py
Hasil:     kiki/Jadwal-Sopir-Kiki-Bandung.html  +  .pdf
"""

import html
import os
import shutil
import subprocess
import urllib.parse

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(OUT_DIR, "Jadwal-Sopir-Kiki-Bandung.html")
PDF_PATH = os.path.join(OUT_DIR, "Jadwal-Sopir-Kiki-Bandung.pdf")

GUESTS = "Haris Haikal &amp; Aina Izzaty"

# ---------------------------------------------------------------- data harian
# tipe baris:  ("stop", jam, tujuan, area/alamat, lama, catatan)
#              ("drive", teks, "", "", "", "")
DAYS = [
    dict(
        n="HARI 1", date="Minggu, 7 September 2026", title="Jemput Bandara + Keliling Kota Bandung",
        color="#B26C12",
        start="Jemput di CGK ± 10.00 WIB", finish="± 21.00 di hotel",
        hotel="Holiday Inn Bandung Pasteur (malam 1)",
        rows=[
            ("stop", "09.20", "Pesawat tamu mendarat — CGK Terminal 3",
             "Bandara Soekarno-Hatta, kedatangan internasional", "—",
             "Malaysia Airlines dari Kuala Lumpur. Tunggu di pintu kedatangan Terminal 3, bawa papan nama <b>HARIS &amp; AINA</b>. Imigrasi + bagasi biasanya 30-45 menit."),
            ("stop", "± 10.00", "Berangkat dari bandara ke Bandung", "", "—",
             "Bantu angkat 2 koper besar. Tamu baru terbang pagi buta — boleh langsung jalan, mampir rest area kalau mereka minta."),
            ("drive", "PERJALANAN: CGK &rarr; Bandung lewat Tol Cipularang &mdash; &plusmn; 3 &ndash; 3,5 jam", "", "", "", ""),
            ("stop", "± 13.00", "Check-in Holiday Inn Bandung Pasteur",
             "Jl. Dr. Djunjunan No. 96, Pasteur, Bandung 40162", "45 menit",
             "Tamu taruh koper &amp; istirahat sebentar. Kiki boleh makan siang di sini."),
            ("drive", "&plusmn; 10 menit", "", "", "", ""),
            ("stop", "± 14.30", "Jalan Braga + Kopi Toko Djawa", "Jl. Braga, Bandung Wetan", "1,5 jam",
             "Tamu jalan kaki di sepanjang Braga, foto-foto, ngopi. Parkir di sekitar Braga / Braga City Walk."),
            ("drive", "&plusmn; 10 menit", "", "", "", ""),
            ("stop", "± 16.30", "Hello Summer Cafe", "Kota Bandung — cek Google Maps", "1,5 jam",
             "Kafe tema pantai. Tamu foto-foto + minum."),
            ("drive", "&plusmn; 15 menit", "", "", "", ""),
            ("stop", "± 19.00", "Nara Park", "Kota Bandung — cek Google Maps", "1,5 jam",
             "Makan malam di taman tepi danau."),
            ("drive", "&plusmn; 15 menit balik ke hotel", "", "", "", ""),
            ("stop", "± 21.00", "Antar kembali ke Holiday Inn Pasteur", "", "selesai",
             "Konfirmasi jam jemput besok: <b>06.30 pagi</b>."),
        ],
        notes=[
            "Hari ini santai — tamu baru sampai, jangan dipadatkan.",
            "Total nyetir dalam kota hari ini hanya &plusmn; 50 menit. Yang panjang cuma tol dari Jakarta.",
        ],
    ),
    dict(
        n="HARI 2", date="Senin, 8 September 2026", title="Ciwidey — Kawah Putih & Kawah Rengganis",
        color="#15764F",
        start="06.30 dari hotel (TEPAT WAKTU)", finish="± 21.30 di hotel",
        hotel="Holiday Inn Bandung Pasteur (malam 2)",
        rows=[
            ("stop", "06.30", "Berangkat dari hotel — <b>tepat waktu</b>", "", "—",
             "Wajib pagi. Kalau sampai Kawah Putih lewat jam 10 sudah kabut dan penuh. Mobil siap 06.20."),
            ("drive", "PERJALANAN: Bandung &rarr; Ciwidey (Rancabali) &mdash; &plusmn; 2,5 jam", "", "", "", ""),
            ("stop", "± 09.00", "Kawah Putih", "Ciwidey / Rancabali, Kabupaten Bandung", "1,5 jam",
             "Parkir di bawah, tamu naik shuttle (ontang-anting) ke kawah. Ingatkan tamu bawa jaket — di atas dingin."),
            ("drive", "&plusmn; 30 menit", "", "", "", ""),
            ("stop", "± 11.15", "Cibuni + Kawah Rengganis", "Rancabali, Ciwidey", "2 – 2,5 jam",
             "Air panas, mandi lumpur, jembatan gantung, zipline. Tamu akan basah &amp; kotor — <b>siapkan alas plastik / handuk di jok mobil</b>. Di sana cuma ada ruang ganti, tidak ada kamar mandi."),
            ("drive", "&plusmn; 10 menit", "", "", "", ""),
            ("stop", "± 14.00", "Makan siang — warung sekitar Ciwidey", "", "45 menit",
             "Kiki boleh pilihkan warung Sunda favorit. Tamu Muslim dari Malaysia — pastikan halal."),
            ("drive", "PERJALANAN: Ciwidey &rarr; Bandung &mdash; &plusmn; 2,5 jam", "", "", "", ""),
            ("stop", "± 17.30", "Kembali ke Holiday Inn Pasteur", "", "2 jam",
             "Tamu mandi &amp; ganti baju. Kiki istirahat / makan."),
            ("drive", "&plusmn; 10 menit", "", "", "", ""),
            ("stop", "± 19.30", "Makan malam — Iga Galabag", "Kota Bandung — cek Google Maps", "1,5 jam", ""),
            ("drive", "&plusmn; 10 menit balik ke hotel", "", "", "", ""),
            ("stop", "± 21.30", "Antar kembali ke Holiday Inn Pasteur", "", "selesai",
             "Besok jemput <b>09.00</b> — dan besok pindah hotel, koper ikut mobil."),
        ],
        notes=[
            "Hari paling jauh: total nyetir &plusmn; 6 jam. Isi bensin penuh malam sebelumnya.",
            "Jalan ke Ciwidey berkelok — tamu minum obat anti-mabuk, jalan santai saja.",
            "Kalau ada penjual strawberry / warung susu murah di jalan pulang, tamu senang kalau ditawari mampir.",
        ],
    ),
    dict(
        n="HARI 3", date="Selasa, 9 September 2026", title="Kafe Seni Dago — <b>pindah hotel</b>",
        color="#6D2E5B",
        start="09.00 dari hotel", finish="± 19.30 check-in hotel baru",
        hotel="PINDAH ke Swiss-Belresort Dago Heritage (malam 3)",
        rows=[
            ("stop", "09.00", "Checkout Holiday Inn Pasteur + berangkat", "Jl. Dr. Djunjunan No. 96", "—",
             "<b>PENTING:</b> semua koper masuk mobil pagi ini dan ikut sepanjang hari. Malam nanti check-in di hotel lain."),
            ("drive", "&plusmn; 30 menit ke arah Dago Atas", "", "", "", ""),
            ("stop", "± 09.30", "Congo Gallery &amp; Café", "Dago Atas, Bandung", "1,5 jam", "Sarapan / brunch."),
            ("drive", "&plusmn; 25 menit", "", "", "", ""),
            ("stop", "± 11.30", "Lawangwangi Creative Space", "Dago Giri, Bandung Utara", "1,5 jam",
             "Kafe galeri di tepi tebing. Makan siang di sini."),
            ("drive", "&plusmn; 20 menit", "", "", "", ""),
            ("stop", "± 13.30", "Gia's Garage", "Bandung Utara — cek Google Maps", "1 jam", "Kafe taman bunga."),
            ("drive", "&plusmn; 20 menit", "", "", "", ""),
            ("stop", "± 15.00", "Dago Bakery Punclut", "Punclut, Ciumbuleuit", "1 jam", "Kafe bentuk kastil. Ngopi sore."),
            ("drive", "&plusmn; 20 menit", "", "", "", ""),
            ("stop", "± 16.30", "Mercusuar Cafe &amp; Resto", "Bandung Utara — cek Google Maps", "2 jam",
             "Kafe mercusuar di bukit. Tamu mau lihat matahari terbenam + lampu kota. Makan malam di sini."),
            ("drive", "&plusmn; 30 menit ke hotel baru", "", "", "", ""),
            ("stop", "± 19.30", "Check-in Swiss-Belresort Dago Heritage",
             "Lapangan Golf Dago Atas No. 78, Bandung 40135", "selesai",
             "Bantu turunkan koper. Besok jemput <b>07.30 pagi</b> — hari paling padat."),
        ],
        notes=[
            "Nyetir hari ini ringan (&plusmn; 2,5 jam total), semua di area Dago / Bandung Utara.",
            "Semua tempat hari ini kafe &amp; galeri — tamu pakai baju rapi, tidak ada kegiatan berat.",
            "Jangan sampai ada barang tamu tertinggal di Holiday Inn saat checkout.",
        ],
    ),
    dict(
        n="HARI 4", date="Rabu, 10 September 2026", title="Lembang & Cikole — hari paling padat",
        color="#C0437A", compact=True,
        start="07.30 dari hotel", finish="± 21.30 di hotel",
        hotel="Swiss-Belresort Dago Heritage (malam 4)",
        rows=[
            ("stop", "07.30", "Berangkat dari Swiss-Belresort", "", "—", "Hari penuh dari pagi sampai malam. Mobil siap 07.20."),
            ("drive", "&plusmn; 50 menit ke Cikole, Lembang", "", "", "", ""),
            ("stop", "± 08.30", "Strobilus Cafe &amp; Resto", "Cikole, Lembang", "1 jam",
             "Sarapan di hutan pinus. Buka jam 09.00 — kalau kepagian, tunggu sebentar di parkiran."),
            ("drive", "&plusmn; 10 menit", "", "", "", ""),
            ("stop", "± 10.00", "Orchid Forest Cikole", "Cikole, Lembang", "1,5 jam", "Hutan pinus + taman anggrek."),
            ("drive", "&plusmn; 30 menit turun ke Lembang", "", "", "", ""),
            ("stop", "± 12.00", "Farmhouse Susu Lembang", "Jl. Raya Lembang", "1 jam", "Makan siang di sekitar sini."),
            ("stop", "± 13.30", "The Great Asia Africa", "Jl. Raya Lembang — sebelah Farmhouse", "1,5 jam",
             "<b>Jalan kaki dari Farmhouse.</b> Cukup parkir sekali untuk dua tempat ini."),
            ("drive", "&plusmn; 15 menit", "", "", "", ""),
            ("stop", "± 15.00", "Floating Market Lembang", "Jl. Grand Hotel, Lembang", "1,5 jam", "Perahu + perosotan pelangi + jajanan."),
            ("drive", "&plusmn; 35 menit ke Maribaya", "", "", "", ""),
            ("stop", "± 17.00", "The Lodge Maribaya", "Cibodas, Lembang", "2 jam", "Ayunan langit, sepeda gantung, pemandangan lembah."),
            ("drive", "&plusmn; 10 menit", "", "", "", ""),
            ("stop", "± 20.00", "Hutan Mycelia", "Lembang / Bandung Utara — cek Google Maps", "1 jam",
             "<b>Baru buka jam 18.00</b> — hutan glow-in-the-dark, memang harus malam. Jangan datang sebelum gelap."),
            ("drive", "PERJALANAN: balik ke Dago &mdash; &plusmn; 1 jam (jalan malam, hati-hati)", "", "", "", ""),
            ("stop", "± 21.30", "Antar kembali ke Swiss-Belresort Dago", "", "selesai",
             "Besok jemput <b>09.30</b> setelah checkout — hari terakhir di Bandung."),
        ],
        notes=[
            "Jadwal padat 07.30 – 21.30. Tolong bantu jaga waktu, kalau satu tempat molor yang lain ikut mundur.",
            "Total nyetir &plusmn; 3,5 jam, tapi terpecah-pecah. Jalan Lembang macet siang &amp; akhir pekan — ambil jalan alternatif kalau perlu.",
            "Kalau waktu mepet, yang paling bisa dipotong: Floating Market. Hutan Mycelia jangan dilewat, cuma bisa malam.",
        ],
    ),
    dict(
        n="HARI 5", date="Kamis, 11 September 2026", title="Belanja Oleh-Oleh + Kembali ke Jakarta",
        color="#7A5410",
        start="09.30 dari hotel", finish="± 16.30 di hotel bandara",
        hotel="PINDAH ke Fairfield by Marriott, dekat Bandara Soekarno-Hatta (malam 5)",
        rows=[
            ("stop", "08.00", "Tamu sarapan di hotel", "", "1,5 jam", "Kiki datang jam 09.20, koper masuk mobil."),
            ("stop", "± 09.30", "Checkout + belanja oleh-oleh", "Kartika Sari, Amanda Brownies, Cibaduyut", "2 jam",
             "Bolu gulung Kartika Sari, brownies Amanda, sepatu kulit Cibaduyut. Kiki bantu pilih cabang yang paling searah jalan ke tol."),
            ("stop", "± 11.30", "Makan siang terakhir di Bandung", "", "1 jam", "Kiki boleh rekomendasikan tempat."),
            ("stop", "± 13.00", "<b>Berangkat ke Jakarta — paling lambat jam 13.00</b>", "", "—",
             "Kalau lewat jam 13.00, kena macet sore di Cipularang / Jakarta."),
            ("drive", "PERJALANAN: Bandung &rarr; Bandara Soekarno-Hatta &mdash; &plusmn; 3 &ndash; 3,5 jam", "", "", "", ""),
            ("stop", "± 16.30", "Check-in Fairfield by Marriott",
             "Jl. Husein Sastranegara No. 88, Tangerang (5-10 menit dari bandara)", "selesai",
             "Tugas hari ini selesai setelah antar ke hotel. <b>Konfirmasi</b> apakah Kiki menginap dekat sana atau kembali besok pagi."),
        ],
        notes=[
            "Malam ini tamu makan malam di sekitar hotel — jalan kaki / Grab, tidak perlu mobil (kecuali diminta).",
            "Total nyetir &plusmn; 3,5 jam tol + keliling kota pagi.",
        ],
    ),
    dict(
        n="HARI 6", date="Jumat, 12 September 2026", title="Antar ke Bandara — Pulang ke Malaysia",
        color="#5B6560",
        start="09.30 dari hotel", finish="± 10.00 selesai",
        hotel="—",
        rows=[
            ("stop", "07.30", "Tamu sarapan di hotel", "", "1 jam", "Mobil siap jam 09.20."),
            ("stop", "± 09.30", "Checkout → antar ke <b>CGK Terminal 3</b>",
             "Bandara Soekarno-Hatta, Terminal 3 keberangkatan internasional", "± 10 menit",
             "<b>Terminal 3, bukan Terminal 2.</b> Malaysia Airlines ada di Terminal 3."),
            ("stop", "± 10.00", "Turunkan tamu + koper di keberangkatan", "", "selesai",
             "Pesawat jam 12.00 siang, tamu butuh 2 jam untuk check-in &amp; imigrasi. Sampai jumpa &amp; terima kasih, Pak Kiki 🙏"),
        ],
        notes=[
            "Hotel hanya 5-10 menit dari terminal, jadi pagi ini santai — tapi tetap jangan telat, penerbangan internasional.",
        ],
    ),
]

SUMMARY = [
    ("Hari 1", "Min, 7 Sep", "10.00 (jemput CGK)", "21.00", "Jakarta &rarr; Bandung, kota", "Holiday Inn Pasteur"),
    ("Hari 2", "Sen, 8 Sep", "<b>06.30</b>", "21.30", "Ciwidey (selatan)", "Holiday Inn Pasteur"),
    ("Hari 3", "Sel, 9 Sep", "09.00", "19.30", "Dago &amp; Punclut", "<b>Pindah</b> &rarr; Swiss-Belresort Dago"),
    ("Hari 4", "Rab, 10 Sep", "07.30", "21.30", "Lembang &amp; Cikole (utara)", "Swiss-Belresort Dago"),
    ("Hari 5", "Kam, 11 Sep", "09.30", "16.30", "Oleh-oleh &rarr; Jakarta", "<b>Pindah</b> &rarr; Fairfield dekat bandara"),
    ("Hari 6", "Jum, 12 Sep", "09.30", "10.00", "Antar ke CGK Terminal 3", "—"),
]

BIG_NOTES = [
    ("Hari 2 berangkat 06.30 pagi", "Kawah Putih berkabut &amp; penuh setelah jam 10. Ini jam paling penting sepanjang trip."),
    ("Hari 2 tamu basah &amp; berlumpur", "Setelah Cibuni Rengganis tidak ada kamar mandi. Siapkan alas plastik/handuk untuk jok mobil."),
    ("Hari 3 pindah hotel", "Checkout Holiday Inn pagi, koper ikut mobil seharian, check-in Swiss-Belresort Dago malam."),
    ("Hari 4 paling padat", "07.30 sampai 21.30. Hutan Mycelia baru buka jam 18.00, jadi memang selesai malam."),
    ("Hari 5 berangkat ke Jakarta maksimal jam 13.00", "Supaya tidak kena macet sore di Cipularang."),
    ("Hari 6 Terminal 3", "Malaysia Airlines di CGK Terminal 3, bukan Terminal 2."),
    ("Tamu Muslim dari Malaysia", "Semua tempat makan harus halal. Bahasa Melayu &amp; Indonesia mirip, komunikasi mudah."),
]

CONTACTS = [
    ("Tamu &mdash; Haris Haikal", "HP / WA: __________________"),
    ("Tamu &mdash; Aina Izzaty", "HP / WA: __________________"),
    ("Holiday Inn Bandung Pasteur", "Jl. Dr. Djunjunan No. 96 &middot; (022) 2060123"),
    ("Swiss-Belresort Dago Heritage", "Lap. Golf Dago Atas No. 78 &middot; (022) 2045-9999"),
    ("Fairfield by Marriott CGK", "Jl. Husein Sastranegara No. 88 &middot; (021) 5084-0000"),
    ("Darurat", "Polisi 110 &middot; Ambulans 118 / 119 &middot; Umum 112"),
]


def maps_link(name, area):
    q = urllib.parse.quote(f"{strip_tags(name)} {area or 'Bandung'}".strip())
    return f"https://www.google.com/maps/search/?api=1&amp;query={q}"


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


NO_MAP = ("Berangkat", "Checkout", "Makan siang", "Tamu sarapan", "Turunkan", "Pesawat",
          "Antar kembali", "Kembali ke", "Check-in Holiday", "Check-in Swiss", "Check-in Fairfield")

CSS = """
@page { size: A4; margin: 13mm 12mm 12mm; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: #1b1b1b; font-size: 10pt; line-height: 1.35; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }

.cover-head { background:#15764F; color:#fff; padding:14px 18px; border-radius:6px; }
.cover-head .k { font-size:9pt; letter-spacing:2.5px; text-transform:uppercase; opacity:.85; }
.cover-head h1 { font-size:21pt; line-height:1.1; margin:6px 0 8px; font-weight:700; }
.cover-head .s { font-size:10pt; opacity:.95; }
.cover-head .s b { font-weight:700; }

h2 { font-size:11.5pt; margin:11px 0 5px; padding-bottom:4px; border-bottom:2px solid #15764F; color:#15764F; }
h2.alt { color:#B23A16; border-bottom-color:#B23A16; }

table { width:100%; border-collapse:collapse; }
.sum th { background:#EDEDE7; font-size:8.5pt; text-transform:uppercase; letter-spacing:.6px;
          text-align:left; padding:6px 7px; border:1px solid #CFCFC6; }
.sum td { padding:4px 7px; border:1px solid #CFCFC6; font-size:9pt; vertical-align:top; }
.sum td.d { font-weight:700; white-space:nowrap; }
.sum tr:nth-child(even) td { background:#FAFAF7; }

.notebox { border:1px solid #E3C7A6; background:#FDF6EC; border-radius:5px; padding:8px 12px; }
.notebox .row { display:flex; gap:9px; padding:2.5px 0; }
.notebox .row + .row { border-top:1px dotted #E3C7A6; }
.notebox .num { flex:0 0 16px; height:16px; border-radius:50%; background:#B23A16; color:#fff;
                font-size:8pt; font-weight:700; text-align:center; line-height:16px; }
.notebox .txt { flex:1; font-size:9pt; }
.notebox .txt b { display:block; }
.notebox .txt span { color:#4A4A44; }

.ct { display:flex; flex-wrap:wrap; }
.ct .c { width:50%; padding:3px 10px 3px 0; font-size:8.8pt; }
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

.sched { width:100%; border-collapse:collapse; margin-top:10px; }
.sched th { background:#EDEDE7; font-size:8pt; text-transform:uppercase; letter-spacing:.7px;
            text-align:left; padding:5px 7px; border:1px solid #CFCFC6; }
.sched td { border:1px solid #D8D8D0; padding:5px 7px; font-size:9.5pt; vertical-align:top; }
.compact .sched td { padding:3px 6px; font-size:8.8pt; }
.compact .sched td.tuj b { font-size:9.2pt; }
.compact .sched td.jam { font-size:9.2pt; }
.compact .sched tr.drive td { font-size:8.2pt; padding:3px; }
.compact .dnotes li { font-size:8.5pt; }
.sched td.jam { width:52px; font-weight:700; white-space:nowrap; font-size:10pt; }
.sched td.tuj { width:34%; }
.sched td.tuj b { font-size:10pt; }
.sched td.tuj .area { display:block; color:#5C5C55; font-size:8.5pt; margin-top:2px; }
.sched td.tuj a { display:block; color:#1a5fb4; font-size:8pt; margin-top:2px; text-decoration:none; word-break:break-all; }
.sched td.lama { width:62px; text-align:center; font-size:8.5pt; color:#444; }
.sched td.cat { font-size:9pt; color:#33332E; }
.sched tr.drive td { background:#F1F5F2; color:#15764F; font-weight:700; font-size:9pt;
                     text-align:center; padding:5px; letter-spacing:.3px; }

.dnotes { margin-top:10px; border-left:4px solid #B26C12; background:#FDF8EF; padding:9px 12px; }
.dnotes b { display:block; font-size:8.5pt; text-transform:uppercase; letter-spacing:1px; color:#8A5A10; margin-bottom:4px; }
.dnotes li { margin-left:15px; font-size:9pt; padding:1px 0; }

.sign { margin-top:8px; border:1px dashed #B9B9AF; border-radius:5px; padding:8px 12px; font-size:8.6pt; color:#55554E; }
.foot { margin-top:12px; font-size:8pt; color:#84847C; text-align:center; }
"""


def render_day(d):
    rows = []
    for r in d["rows"]:
        if r[0] == "drive":
            rows.append(f'<tr class="drive"><td colspan="4">&#128663;&nbsp; {r[1]}</td></tr>')
            continue
        _, jam, tuj, area, lama, cat = r
        plain = strip_tags(tuj)
        link = ""
        if not plain.startswith(NO_MAP):
            link = f'<a href="{maps_link(tuj, area)}">\U0001F4CD Buka di Google Maps</a>'
        area_html = f'<span class="area">{area}</span>' if area else ""
        rows.append(
            f'<tr><td class="jam">{jam}</td>'
            f'<td class="tuj"><b>{tuj}</b>{area_html}{link}</td>'
            f'<td class="lama">{lama}</td>'
            f'<td class="cat">{cat}</td></tr>'
        )
    notes = "".join(f"<li>{n}</li>" for n in d["notes"])
    return f"""
<div class="page{' compact' if d.get('compact') else ''}">
  <div class="dayhead" style="background:{d['color']}">
    <div class="n">{d['n']}</div>
    <h1>{d['title']}</h1>
    <div class="dt">{d['date']}</div>
  </div>
  <div class="daymeta">
    <div><span>Mulai</span>{d['start']}</div>
    <div><span>Selesai</span>{d['finish']}</div>
    <div><span>Menginap</span>{d['hotel']}</div>
  </div>
  <table class="sched">
    <tr><th>Jam</th><th>Tujuan</th><th>Lama</th><th>Catatan untuk Pak Kiki</th></tr>
    {''.join(rows)}
  </table>
  <div class="dnotes"><b>Catatan hari ini</b><ul>{notes}</ul></div>
  <div class="foot">Jadwal Bandung {GUESTS} &middot; {d['n']} &middot; jam bersifat perkiraan, Pak Kiki boleh menyesuaikan dengan lalu lintas</div>
</div>"""


def build_html():
    summary_rows = "".join(
        f'<tr><td class="d">{a}</td><td class="d">{b}</td><td>{c}</td><td>{e}</td><td>{f}</td><td>{g}</td></tr>'
        for a, b, c, e, f, g in SUMMARY
    )
    big_notes = "".join(
        f'<div class="row"><div class="num">{i+1}</div><div class="txt"><b>{t}</b><span>{s}</span></div></div>'
        for i, (t, s) in enumerate(BIG_NOTES)
    )
    contacts = "".join(f'<div class="c"><b>{a}</b><span>{b}</span></div>' for a, b in CONTACTS)

    cover = f"""
<div class="page">
  <div class="cover-head">
    <div class="k">Jadwal untuk Pak Kiki &middot; Sopir</div>
    <h1>Perjalanan Bandung<br>7 &ndash; 12 September 2026</h1>
    <div class="s">Tamu: <b>{GUESTS}</b> (2 orang, dari Malaysia)<br>
    6 hari &middot; jemput di Bandara Soekarno-Hatta, antar kembali ke Bandara Soekarno-Hatta</div>
  </div>

  <h2>Ringkasan 6 Hari</h2>
  <table class="sum">
    <tr><th>Hari</th><th>Tanggal</th><th>Jemput</th><th>Selesai</th><th>Area</th><th>Menginap</th></tr>
    {summary_rows}
  </table>

  <h2 class="alt">Yang Paling Penting Diingat</h2>
  <div class="notebox">{big_notes}</div>

  <h2>Kontak</h2>
  <div class="ct">{contacts}</div>

  <div class="sign">
    <b>Nomor Pak Kiki:</b> ____________________ &nbsp; <b>Plat mobil:</b> ____________________<br>
    <b>Biaya:</b> bensin, tol, dan parkir mohon simpan struknya &mdash; diganti oleh tamu. Makan Pak Kiki ditanggung tamu.
    Semua jam perkiraan &mdash; boleh disesuaikan dengan lalu lintas.
  </div>
</div>"""

    days = "".join(render_day(d) for d in DAYS)
    return f"""<!DOCTYPE html>
<html lang="id"><head><meta charset="UTF-8">
<title>Jadwal Sopir — Bandung 7-12 September 2026</title>
<style>{CSS}</style></head><body>{cover}{days}</body></html>"""


def find_chromium():
    for c in ("/opt/pw-browsers/chromium/chrome-linux/chrome",
              "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"):
        if os.path.exists(c):
            return c
    for n in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        p = shutil.which(n)
        if p:
            return p
    hits = subprocess.run(["bash", "-lc", "ls /opt/pw-browsers/*/chrome-linux/chrome 2>/dev/null | head -1"],
                          capture_output=True, text=True).stdout.strip()
    return hits or None


def main():
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(build_html())
    print("HTML :", HTML_PATH)

    chrome = find_chromium()
    if not chrome:
        print("Chromium tidak ditemukan — buka HTML lalu Print to PDF secara manual.")
        return
    subprocess.run([chrome, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={PDF_PATH}",
                    "file://" + HTML_PATH], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("PDF  :", PDF_PATH)


if __name__ == "__main__":
    main()
