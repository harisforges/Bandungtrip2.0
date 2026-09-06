#!/usr/bin/env python3
"""Da Lat & Nha Trang — flowers first, then the dry coast. 8-12 September 2026.

The version built around Aina's six outfit themes and around weather:
Da Lat's flower farms are in season and cultivated year-round, Nha Trang is
the driest corner of Vietnam this week. Flown on Malaysia Airlines to Saigon
with short domestic hops either end.

Run:    python3 dalat-nhatrang/build_dalat_nhatrang_pdf.py
Output: dalat-nhatrang/Itinerary-DaLat-NhaTrang.html  +  .pdf
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from trips import itinerary_pdf as engine  # noqa: E402

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
GUESTS = "Haris Haikal &amp; Aina Izzaty"

DAYS = [
    dict(
        n="DAY 1", date="Tuesday, 8 September", title="KUL → Saigon → Da Lat",
        color="#46688C",
        outfit="<b>Soft blue + brown</b> — café theme, for the first Da Lat evening",
        start="Morning MAS out of KLIA", finish="~21.00", sleep="Da Lat (nights 1–2)",
        rows=[
            ("stop", "morning", "KUL → SGN — Malaysia Airlines", "KLIA", "~2h",
             "MH750 / MH758 / MH766 — about 7 a day, so pick one landing in Saigon by early afternoon. Vietnam is <b>1 hour behind Malaysia</b>."),
            ("stop", "~12.30", "Connect at Tan Son Nhat", "Saigon — international T2, domestic T1", "~3h",
             "On separate tickets you must <b>collect your bags, walk to T1 and check in again</b>. Allow three hours; it is a short walk but the queues are not."),
            ("stop", "~15.30", "SGN → DLI — Vietnam Airlines or Vietjet", "Tan Son Nhat T1", "55 min",
             "Six a day, last one 17:30. Book this the same day as the MAS leg so a delay doesn't strand you."),
            ("move", "Lien Khuong airport &rarr; Da Lat city &mdash; 30 km, ~40 min", "", "", "", ""),
            ("stop", "~17.30", "Check in — Da Lat", "Da Lat city", "1h",
             "Da Lat sits at 1,500 m: 17–24°C, the coolest part of the trip. Jacket out of the bag tonight."),
            ("stop", "~19.00", "Evening café + dinner", "Da Lat centre", "2h",
             "An Cafe, Still Cafe or La Viet Coffee — wood, warm light, mountain air. This is the soft-blue-and-brown evening."),
        ],
        notes=[
            "Long travel day but no long road transfer, unlike the Bandung and Sapa versions.",
            "<b>Simpler alternative:</b> AirAsia flies KUL → Da Lat direct (AK571, 2h10) — but only ~4 days a week, so check whether 8 September is one of them. If it is, take it and skip the Saigon connection entirely.",
            "Grab works in Da Lat. Book the airport car through the hotel if you land after dark.",
        ],
    ),
    dict(
        n="DAY 2", date="Wednesday, 9 September", title="Flower day — hydrangeas and the farms",
        color="#D4749B",
        outfit="<b>Soft pink + white</b> all day &middot; evening switch to <b>black leather + white</b> for the night market",
        start="08.30", finish="~21.00", sleep="Da Lat (night 2)",
        rows=[
            ("stop", "08.30", "Trai Mat hydrangea field (cẩm tú cầu)",
             "Trai Mat, ~7 km east of the centre", "2h",
             "Two hectares of hydrangeas down a hillside — blue, violet and pink. <b>In season now:</b> they flower May to December. Go early for soft light and an empty field."),
            ("move", "~10 min", "", "", "", ""),
            ("stop", "~10.45", "Linh Phuoc Pagoda", "Trai Mat", "1h",
             "The mosaic dragon temple — built from broken pottery and glass. Right next to the hydrangeas, so it costs you nothing to add."),
            ("stop", "~12.15", "Lunch in town", "Da Lat centre", "1h", ""),
            ("stop", "~13.45", "Da Lat Flower Park (Vườn hoa thành phố)",
             "By Xuan Huong Lake", "1.5h",
             "The city's permanent flower garden by the lake — beds replanted year-round, which is why September still works here."),
            ("move", "~15 min", "", "", "", ""),
            ("stop", "~15.45", "A greenhouse flower farm + the market flower street",
             "Da Lat outskirts / Cho Da Lat", "1.5h",
             "Da Lat grows most of Vietnam's cut flowers under glass. Ask the hotel which farm is currently open to visitors — they rotate."),
            ("stop", "~17.30", "Back to the hotel, change", "", "1h",
             "Swap into the black leather and white — evenings here drop to 17–19°C, the one place on this trip cold enough for it."),
            ("stop", "~19.00", "Da Lat Night Market + a pine-forest café",
             "Cho Dem, city centre", "2h",
             "Grilled corn, banh trang nuong, hot soy milk. The night market stairs are the classic Da Lat photo."),
        ],
        notes=[
            "<b>Gardens in the morning.</b> September is Da Lat's wettest month and the rain is an afternoon and evening habit — front-load anything outdoors.",
            "Light rain shell in the day bag, always. It passes in bursts, then clears.",
            "Flower farms are working businesses; some charge a small entry, some want you to buy a bunch. Both are fine.",
        ],
    ),
    dict(
        n="DAY 3", date="Thursday, 10 September", title="Fairytale morning, then the mountain road to the sea",
        color="#A8763A",
        outfit="<b>Cream fairytale</b> — the storybook buildings are the backdrop",
        start="08.00", finish="~20.30", sleep="<b>Move</b> → Nha Trang (nights 3–4)",
        rows=[
            ("stop", "08.00", "Crazy House (Hằng Nga Guesthouse)", "Huynh Thuc Khang, Da Lat", "1h",
             "The tree-and-cave house — the single most fairytale building in Vietnam. Go at opening; the stairs are narrow and it jams up by ten."),
            ("move", "~10 min", "", "", "", ""),
            ("stop", "~09.30", "Da Lat Railway Station", "Quang Trung, Da Lat", "1h",
             "1930s art-deco station in yellow and cream, with the old cog railway carriages. The cream outfit was made for this one."),
            ("move", "~10 min", "", "", "", ""),
            ("stop", "~11.00", "Domaine de Marie church + Da Lat Palace grounds",
             "Da Lat", "1h",
             "Pink-washed convent church and the colonial-era palace lawns. Quiet, and quietly grand."),
            ("stop", "~12.15", "Lunch + checkout", "Da Lat", "1.5h",
             "Bags in the car before you eat — the driver picks you up from the restaurant."),
            ("move", "DRIVE: Da Lat &rarr; Nha Trang on QL27C &mdash; 135 km, ~3h05", "", "", "", ""),
            ("stop", "~17.15", "Check in — Nha Trang", "Tran Phu beachfront", "1h",
             "You've dropped from 1,500 m to sea level: 28–32°C now. Jacket back in the bag for good."),
            ("stop", "~19.00", "Seafood dinner by the water", "Nha Trang", "1.5h", ""),
        ],
        notes=[
            "<b>Take QL27C, not QL27B.</b> 135 km and ~3 hours through pine forest and the Khanh Le pass, against 179 km and ~4 hours the other way. It is one of the best drives in Vietnam — ask the driver to stop at the pass.",
            "Book a private car the day before. Grab does not do this route properly.",
            "Leave Da Lat by 13.30 so you cross the pass in daylight.",
        ],
    ),
    dict(
        n="DAY 4", date="Friday, 11 September", title="Nha Trang — the dry day",
        color="#1E7FA8",
        outfit="<b>Blue + yellow</b> — sea, sand, and Po Nagar's ochre brick",
        start="08.00", finish="~21.00", sleep="Nha Trang (night 4)",
        rows=[
            ("stop", "08.00", "Po Nagar Cham Towers", "Hai Thang Tu, north of the river", "1.5h",
             "Eighth-century Cham brick towers on a hill above the river — deep ochre and gold against the sky. Blue and yellow against that brick is the shot of the day. Shoulders covered inside."),
            ("move", "~15 min", "", "", "", ""),
            ("stop", "~10.00", "Hon Chong Promontory", "North Nha Trang", "1h",
             "Stacked granite boulders over the bay, with the islands behind. Short stop, big view."),
            ("stop", "~11.30", "Beach time — Tran Phu beachfront", "Nha Trang city beach", "1.5h",
             "Six kilometres of sand right in front of the city. Loungers are cheap; the water is calm this side of October."),
            ("stop", "~13.00", "Seafood lunch", "Nha Trang", "1h", ""),
            ("stop", "~14.30", "Island boat trip <i>or</i> the Vinpearl cable car",
             "Cau Da pier / Vinpearl", "3h",
             "Pick one. The boat visits Hon Mun and Hon Tam for snorkelling; the cable car runs three kilometres over the sea to the island resort. Both are weather-dependent — decide in the morning."),
            ("stop", "~17.45", "Sunset on the beach", "Tran Phu", "1h",
             "Nha Trang faces east, so sunset lights the mountains behind you rather than the sea. Still the best hour of the day."),
            ("stop", "~19.30", "Dinner + pack", "Nha Trang", "1.5h", ""),
        ],
        notes=[
            "<b>This is the dry half of the trip.</b> Nha Trang has the shortest rainy season in Vietnam and roughly 300 sunny days a year — its wet season doesn't start until October.",
            "Hot and humid, 28–32°C. Sunscreen matters more here than anywhere else on the trip.",
            "Everything today is 10–20 minutes apart by Grab.",
        ],
    ),
    dict(
        n="DAY 5", date="Saturday, 12 September", title="Fly home — Nha Trang → Saigon → KUL",
        color="#6B6A52",
        outfit="<b>Khaki + black</b> — travel day",
        start="08.00", finish="KUL", sleep="—",
        rows=[
            ("stop", "08.00", "Breakfast + last beach walk", "Nha Trang", "1.5h", ""),
            ("move", "Nha Trang &rarr; Cam Ranh airport (CXR) &mdash; 35&ndash;40 km, ~45 min", "", "", "", ""),
            ("stop", "~10.15", "Checkout → Cam Ranh airport", "Cam Ranh (CXR)", "—",
             "The airport is well south of the city — leave more time than the distance suggests."),
            ("stop", "~12.00", "CXR → SGN — Vietnam Airlines or Vietjet", "Cam Ranh", "1h 05m",
             "Seven a day, from 04:00 to 21:50, so there's plenty of choice to fit the MAS leg."),
            ("stop", "~14.00", "Connect at Tan Son Nhat", "Saigon — domestic T1 → international T2", "~3h",
             "Same drill in reverse: collect bags at T1, walk to T2, check in for MAS."),
            ("stop", "late afternoon", "SGN → KUL — Malaysia Airlines", "Tan Son Nhat T2", "~2h",
             "MH750 / MH758 / MH766 again. Malaysia is 1 hour ahead, so you land later on the clock than the flight time suggests."),
        ],
        notes=[
            "<b>Simpler alternative:</b> AirAsia flies Cam Ranh → KUL direct — about 4 days a week. If 12 September is one, it saves you the whole Saigon connection.",
            "Book the two domestic legs and the two MAS legs as one itinerary if any agent will do it — otherwise a delay on the domestic hop is your problem, not the airline's.",
        ],
    ),
]

TRIP = dict(
    doc_title="Da Lat &amp; Nha Trang — 8-12 September 2026",
    kicker="Plan B &middot; flowers + dry weather &middot; Bandung is off (Anak Krakatau)",
    title="Da Lat &amp; Nha Trang<br>8 &ndash; 12 September 2026",
    subtitle=(f"{GUESTS} &middot; flown Malaysia Airlines via Saigon &middot; no driver to arrange<br>"
              "Hydrangeas are in season in Da Lat; Nha Trang is the driest corner of Vietnam this week."),
    travellers=GUESTS,
    country="Vietnam",
    no_map=("Breakfast", "Lunch", "Dinner", "Check in", "Checkout", "Connect", "Back to",
            "KUL →", "SGN →", "CXR →", "Evening café", "Beach time", "Sunset", "A greenhouse"),
    summary_head=("Day", "Date", "Where", "Outfit theme", "Sleep"),
    summary_rows=[
        ("Day 1", "Tue, 8 Sep", "Fly in via Saigon, café evening", "Soft blue + brown", "Da Lat"),
        ("Day 2", "Wed, 9 Sep", "Hydrangeas, flower park, farms", "Soft pink + white · pm black leather", "Da Lat"),
        ("Day 3", "Thu, 10 Sep", "Fairytale Da Lat, then QL27C down", "Cream fairytale", "<b>Move</b> → Nha Trang"),
        ("Day 4", "Fri, 11 Sep", "Cham towers, beach, islands", "Blue + yellow", "Nha Trang"),
        ("Day 5", "Sat, 12 Sep", "Fly home via Saigon", "Khaki + black", "—"),
    ],
    book_now_head="Book Tonight, In This Order",
    book_now=[
        ("Ask Malaysia Airlines to reroute the CGK ticket to Saigon",
         "MAS flies KUL–Saigon ~7 times a day (MH750 / MH758 / MH766, ~2h). If they cancel Jakarta, ask to be moved to Saigon rather than refunded. <b>+60 3-7843-3000</b>"),
        ("MAS: KUL → SGN on 8 Sept (morning) and SGN → KUL on 12 Sept (late afternoon)",
         "Leave yourself three hours on each side for the domestic connection."),
        ("Domestic: SGN → Da Lat on 8 Sept, Cam Ranh → SGN on 12 Sept",
         "Vietnam Airlines or Vietjet. SGN–DLI 55 min, 6 a day, last 17:30. CXR–SGN 1h05, 7 a day."),
        ("Or check the AirAsia directs first",
         "KUL → Da Lat (AK571, 2h10) and Cam Ranh → KUL both run ~4 days a week. If 8 and 12 Sept are operating days, that's two flights instead of four."),
        ("Hotels: 2 nights Da Lat (8–9), 2 nights Nha Trang (10–11)",
         "Da Lat: near Xuan Huong Lake or the centre. Nha Trang: on the Tran Phu beachfront, bay view."),
        ("Private car, Da Lat → Nha Trang on 10 Sept",
         "Specify <b>QL27C</b>, the 135 km mountain route, and a pickup around 13.30."),
        ("Cancel or move the Bandung bookings",
         "Holiday Inn Pasteur, Swiss-Belresort Dago, Fairfield CGK — ask for a waiver citing the airport closure. Message Kiki."),
        ("Insurance, eSIM, offline maps",
         "Re-issue the insurance for Vietnam; keep the Bandung paperwork for the claim."),
    ],
    know_cols=3,
    good_to_know=[
        ("Visa", "Visa-free for Malaysians, 30 days. Carry hotel bookings and onward tickets."),
        ("Money", "Vietnamese dong. Cards fine in both cities; cash for markets and flower farms."),
        ("Getting around", "Grab and Xanh SM in Da Lat and Nha Trang. Only the mountain crossing needs a booked car."),
        ("Two climates", "Da Lat 17–24°C, cool nights, afternoon rain. Nha Trang 28–32°C and dry. Pack for both."),
        ("Saigon connection", "Domestic is T1, international T2. On separate tickets you re-check bags — allow 3 hours."),
        ("If you fly on the 9th", "Drop Day 1: land in Da Lat that evening, fold the flowers and the fairytale into the 10th, drive down on the 11th, fly home the 12th. Three nights, same six themes."),
    ],
    sign=("<b>MAS out:</b> _______________ &nbsp; <b>SGN → DLI:</b> _______________ &nbsp; "
          "<b>CXR → SGN:</b> _______________ &nbsp; <b>MAS home:</b> _______________<br>"
          "<b>Da Lat hotel:</b> _______________ &nbsp; <b>Nha Trang hotel:</b> _______________ &nbsp; "
          "<b>QL27C car:</b> _______________ &nbsp; <i>Checked 6 Sept 2026.</i>"),
    days=DAYS,
)

if __name__ == "__main__":
    engine.write(TRIP,
                 os.path.join(OUT_DIR, "Itinerary-DaLat-NhaTrang.html"),
                 os.path.join(OUT_DIR, "Itinerary-DaLat-NhaTrang.pdf"))
