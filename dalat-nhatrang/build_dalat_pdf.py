#!/usr/bin/env python3
"""Da Lat, 8-12 September 2026 — built around Haris & Aina's own shortlist.

Fourteen places they picked, grouped by direction so the days don't zigzag,
plus a page of nearby options. No churches, no temples. Flown Malaysia
Airlines via Saigon.

Run:    python3 dalat-nhatrang/build_dalat_pdf.py
Output: dalat-nhatrang/Itinerary-DaLat.html  +  .pdf
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from trips import itinerary_pdf as engine  # noqa: E402

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
GUESTS = "Haris Haikal &amp; Aina Izzaty"

DAYS = [
    dict(
        n="DAY 1", date="Tuesday, 8 September", title="Fly in — lake evening + L'angfarm",
        color="#46688C",
        outfit="<b>Soft blue + brown</b> — café theme for the first evening",
        start="Morning MAS from KLIA", finish="~21.30", sleep="Da Lat (4 nights, one hotel)",
        rows=[
            ("stop", "morning", "KUL → SGN — Malaysia Airlines", "KLIA", "~2h",
             "MH750 / MH758 / MH766, about 7 a day. Take one landing in Saigon by early afternoon. Vietnam is <b>1 hour behind Malaysia</b>."),
            ("stop", "~12.30", "Connect at Tan Son Nhat", "Saigon — T2 international, T1 domestic", "~3h",
             "On separate tickets you collect bags, walk to T1 and check in again. Three hours is the safe margin."),
            ("stop", "~15.30", "SGN → DLI — Vietnam Airlines or Vietjet", "Tan Son Nhat T1", "55 min",
             "Six a day, last departure 17:30."),
            ("move", "Lien Khuong airport &rarr; Da Lat city &mdash; 30 km, ~40 min", "", "", "", ""),
            ("stop", "~17.30", "Check in — Da Lat", "City centre", "1h",
             "One hotel for all four nights. Stay near Xuan Huong Lake and the centre is walkable."),
            ("stop", "~18.30", "Xuan Huong Lake", "City centre", "1h",
             "The lake loop at dusk, lit up and full of locals. Five minutes from anywhere central — a gentle first evening."),
            ("stop", "~19.45", "Dinner + L'angfarm Center", "Da Lat centre", "1.5h",
             "Da Lat's specialty-food store — dried fruit, artichoke tea, jam, coffee, macadamia. Do a first pass now and buy properly on the last morning so you're not carrying it all week."),
        ],
        notes=[
            "Da Lat sits at 1,500 m — 17–24°C, and evenings drop to about 17°C. Jacket out of the bag tonight.",
            "<b>Simpler alternative:</b> AirAsia flies KUL → Da Lat direct (AK571, 2h10), but only ~4 days a week — check whether 8 September is one, and if so skip the Saigon connection entirely.",
            "Grab works fine in Da Lat. For the out-of-town days, a car with driver by the day is easier and not expensive.",
        ],
    ),
    dict(
        n="DAY 2", date="Wednesday, 9 September", title="East — dawn clouds, Cau Dat, the old town",
        color="#A8763A",
        outfit="<b>Cream fairytale</b> — Euro Garden's castle and the ancient town",
        start="05.00 (yes, really)", finish="~20.00", sleep="Da Lat",
        compact=True,
        rows=[
            ("stop", "05.00", "Thác Mây &amp; Chill — cloud hunting at dawn",
             "Dốc số 9, Trại Mát — 15–20 min east", "2h",
             "It opens at <b>05:00</b> precisely so you can watch cloud fill the ravine below you at first light. This is the one early start of the trip and it is the reason to make it."),
            ("move", "~30 min further east on QL20", "", "", "", ""),
            ("stop", "~08.00", "Breakfast at Cau Dat Farm", "Cầu Đất, QL20", "1h",
             "Tea-hill breakfast on the way — coffee grown on the slope you're looking at."),
            ("stop", "~09.15", "Euro Garden Cầu Đất", "QL20, ~25 km southeast (30–45 min)", "2.5h",
             "7.2 hectares at 1,650 m: seasonal flower fields, a miniature French castle, an Eiffel Tower, and a railway café. The cream-fairytale location of the trip."),
            ("stop", "~12.00", "Lunch — Cau Dat tea hills", "Cầu Đất", "1h",
             "The tea terraces themselves are right here and free to walk."),
            ("move", "~25 min back toward Xuân Trường", "", "", "", ""),
            ("stop", "~13.45", "Lạc Hư Cổ Trấn", "Lâm Văn Thạnh road, Xuân Trường", "2h",
             "Stone houses, tiled roofs and a blue lake done as a Chinese ancient town. ~120,000 VND including a drink; open 05:00–20:00. There's a gong performance area in the evening."),
            ("move", "~5 min — same road", "", "", "", ""),
            ("stop", "~16.00", "Miền Du Mục", "Lâm Văn Thạnh road, Xuân Trường", "2.5h",
             "Canvas tents on grass looking out over pine hills — the nomad camp café. Built for sitting still, so don't rush it: stay for sunset."),
            ("move", "~25 min back to the city", "", "", "", ""),
            ("stop", "~19.30", "Dinner in town", "Da Lat centre", "1h", ""),
        ],
        notes=[
            "Everything today is on the same eastern road, so nothing doubles back. Book the car the night before with a 04.40 pickup.",
            "Cloud hunting needs a clear-ish dawn. If it's pouring at 04.30, sleep in and start at Euro Garden instead — you can try again Friday.",
            "Cầu Đất is at 1,650 m and genuinely cold before sunrise. Jacket, and something warm to drink.",
        ],
    ),
    dict(
        n="DAY 3", date="Thursday, 10 September", title="North — Pink Valley, Langbiang, the quiet stream",
        color="#D4749B",
        outfit="<b>Soft pink + white</b> all day &middot; evening switch to <b>black leather + white</b>",
        start="07.45", finish="~21.00", sleep="Da Lat",
        rows=[
            ("stop", "07.45", "Drive north to Lạc Dương", "", "—", "Opens at 07:00, so an early arrival gets you an empty valley."),
            ("stop", "~08.30", "Pink Valley (Thung Lũng Hồng)",
             "Lat village, Lạc Dương — 22 km north", "2.5h",
             "A rose valley done as a romantic European garden. 100,000 VND entry, open 07:00–17:00. Pink and white here is the obvious pairing — and the light is best before eleven."),
            ("move", "~20 min", "", "", "", ""),
            ("stop", "~11.30", "Langbiang", "Lạc Dương — ~12 km north", "2.5h",
             "The mountain over Da Lat. Take the jeep up to the Radar Peak viewpoint rather than walking — save your legs. Cloud comes and goes all day; wait it out with a coffee at the top."),
            ("stop", "~14.15", "Lunch in Lạc Dương", "Lạc Dương town", "1h", ""),
            ("move", "~30 min back toward the city", "", "", "", ""),
            ("stop", "~15.45", "Suối Bình Yên", "Hoa Cẩm Tú Cầu street, Ward 3 — 10–15 min out", "2h",
             "A stream-side garden café, deliberately slow. It sits on <b>Hydrangea Street</b>, so the hydrangea fields are right there — they flower May to December, so they're in season now."),
            ("stop", "~18.00", "Back to the hotel, change", "", "1h",
             "Into the black leather and white — evenings here drop to about 17°C, the one place cold enough to wear it."),
            ("stop", "~19.15", "Da Lat Night Market", "Cho Dem, city centre", "2h",
             "Grilled corn, banh trang nuong, hot soy milk. The market stairs are the classic Da Lat night photo."),
        ],
        notes=[
            "Pink Valley and Langbiang are both in Lạc Dương, 10 minutes apart — one direction, no backtracking.",
            "Langbiang jeeps are shared or private; private costs a little more and lets you stop for photos.",
            "Suối Bình Yên is the trip's designated do-nothing hour. Take the book, not the itinerary.",
        ],
    ),
    dict(
        n="DAY 4", date="Friday, 11 September", title="West to Tà Nung, then the coaster",
        color="#1E7FA8",
        outfit="<b>Blue + yellow</b> — bright day, lake water and open grassland",
        start="07.45", finish="~20.00", sleep="Da Lat",
        compact=True,
        rows=[
            ("stop", "07.45", "Drive southwest on the Tà Nung road", "", "—",
             "A pretty pine-forest road in its own right. All three morning stops are on it."),
            ("stop", "~08.15", "Mongo Land", "Tà Nung commune — 17 km southwest", "2h",
             "Mongolian steppe done as a theme park: yurts, horse riding, archery, nomad dress-up, a rainbow slide and a pet farm. Open 07:00–17:00."),
            ("move", "~10 min — same road", "", "", "", ""),
            ("stop", "~10.30", "Floating Town", "Tà Nung route — 15–17 km", "2h",
             "Dark-tiled wooden houses standing out of an emerald lake. 100,000 VND including a drink and parking. The houses face west, so it photographs best later — but morning is calmer water."),
            ("stop", "~12.45", "KDL Sinh Thái Cao Nguyên Hoa", "Tà Nung area", "1.5h",
             "Flower-highland eco park, and lunch nearby. <b>Confirm the exact spot and opening hours with your hotel the night before</b> — I could not verify them from here."),
            ("move", "~40 min back through the city, then south on QL20", "", "", "", ""),
            ("stop", "~15.00", "Happy Hill", "Đá Tiên, Hoa Phượng Tím st, Ward 4 — 12 km", "1.5h",
             "Film-set park on Tuyen Lam lake — windmills, colour, staged photo corners. Open 07:00–17:30, so this has to come before the coaster."),
            ("move", "~15 min", "", "", "", ""),
            ("stop", "~16.45", "Datanla — new alpine coaster", "QL20, ~5 km south of the city", "1.5h",
             "The rebuilt alpine coaster down through the forest, and the falls at the bottom. You control the brake; go once slow for the video, once fast for fun."),
            ("stop", "~19.00", "Dinner in town", "Da Lat centre", "1h", ""),
        ],
        notes=[
            "<b>The full day of the four.</b> If it slips, drop Cao Nguyên Hoa — it's the least certain of the three morning stops.",
            "Happy Hill closes at 17:30 and Datanla's last coaster runs late afternoon, so keep the 15.00 arrival at Happy Hill honest.",
            "Elephant Falls and Nam Ban village are further along the same Tà Nung road — see the nearby page if you want to stretch the morning.",
        ],
    ),
    dict(
        n="DAY 5", date="Saturday, 12 September", title="Last morning, then home",
        color="#6B6A52",
        outfit="<b>Khaki + black</b> — travel day",
        start="08.00", finish="KUL", sleep="—",
        rows=[
            ("stop", "08.00", "Breakfast + last café", "Da Lat centre", "1h", ""),
            ("stop", "~09.15", "L'angfarm Center — the real shop", "Da Lat centre", "45 min",
             "Buy the dried fruit, artichoke tea, jam and coffee now, on the way out, so it travels once. They vacuum-pack."),
            ("move", "Da Lat &rarr; Lien Khuong airport (DLI) &mdash; 30 km, ~40 min", "", "", "", ""),
            ("stop", "~11.30", "DLI → SGN — Vietnam Airlines or Vietjet", "Lien Khuong", "55 min", ""),
            ("stop", "~13.30", "Connect at Tan Son Nhat", "Saigon — T1 domestic → T2 international", "~3h",
             "Collect bags at T1, walk to T2, check in for MAS."),
            ("stop", "late afternoon", "SGN → KUL — Malaysia Airlines", "Tan Son Nhat T2", "~2h",
             "Malaysia is 1 hour ahead, so you land later on the clock than the flight time suggests."),
        ],
        notes=[
            "Lien Khuong is 30 km south of the city — leave more time than the distance suggests, especially on a Saturday.",
            "If AirAsia's Cam Ranh or Da Lat direct happens to fly on the 12th, it saves the whole Saigon connection.",
        ],
    ),
]

TRIP = dict(
    doc_title="Da Lat — 8-12 September 2026",
    kicker="Plan B &middot; your own shortlist &middot; Bandung is off (Anak Krakatau)",
    title="Da Lat<br>8 &ndash; 12 September 2026",
    subtitle=(f"{GUESTS} &middot; Malaysia Airlines via Saigon &middot; one hotel, four nights<br>"
              "All fourteen of your places, grouped by direction. No churches, no temples."),
    travellers=GUESTS,
    country="Da Lat, Vietnam",
    no_map=("Breakfast", "Lunch", "Dinner", "Check in", "Checkout", "Connect", "Drive",
            "KUL →", "SGN →", "DLI →", "Back to"),
    summary_title="The Five Days",
    summary_head=("Day", "Date", "Direction", "Your places", "Outfit"),
    summary_rows=[
        ("Day 1", "Tue, 8 Sep", "Fly in + city", "Xuan Huong Lake, L'angfarm", "Soft blue + brown"),
        ("Day 2", "Wed, 9 Sep", "East — Trại Mát &rarr; Cầu Đất",
         "Thác Mây, Euro Garden, Lạc Hư Cổ Trấn, Miền Du Mục", "Cream fairytale"),
        ("Day 3", "Thu, 10 Sep", "North — Lạc Dương",
         "Pink Valley, Langbiang, Suối Bình Yên", "Soft pink + white · pm black leather"),
        ("Day 4", "Fri, 11 Sep", "West — Tà Nung, then south",
         "Mongo Land, Floating Town, Cao Nguyên Hoa, Happy Hill, Datanla coaster", "Blue + yellow"),
        ("Day 5", "Sat, 12 Sep", "Fly home", "L'angfarm run", "Khaki + black"),
    ],
    book_now_head="Book Tonight, In This Order",
    book_now=[
        ("Ask Malaysia Airlines to reroute the CGK ticket to Saigon",
         "MAS flies KUL–Saigon ~7 times a day (MH750 / MH758 / MH766). If they cancel Jakarta, ask to be moved to Saigon rather than refunded. <b>+60 3-7843-3000</b>"),
        ("MAS KUL → SGN on 8 Sept (morning), SGN → KUL on 12 Sept (late afternoon)",
         "Three hours on each side for the domestic connection."),
        ("Domestic: SGN → Da Lat on 8 Sept, Da Lat → SGN on 12 Sept",
         "Vietnam Airlines or Vietjet, 55 min, six a day, last one 17:30. Or check AirAsia's KUL–Da Lat direct first (~4 days a week)."),
        ("Hotel — four nights, one place, near Xuan Huong Lake", "You never change hotels on this version."),
        ("Car with driver for days 2, 3 and 4",
         "Day 2 needs a <b>04.40 pickup</b> for the dawn cloud hunt. Book all three days with the same driver through the hotel — cheaper and he'll learn what you want."),
        ("Check Cao Nguyên Hoa and Miền Du Mục opening hours",
         "Both are recent and their hours move. The hotel desk will know; so will their Facebook pages."),
        ("Cancel or move the Bandung bookings",
         "Holiday Inn Pasteur, Swiss-Belresort Dago, Fairfield CGK — ask for a waiver citing the airport closure. Message Kiki."),
        ("Insurance, eSIM, offline maps", "Re-issue for Vietnam; keep the Bandung paperwork for the claim."),
    ],
    know_cols=3,
    good_to_know=[
        ("Visa", "Visa-free for Malaysians, 30 days. Carry hotel bookings and onward tickets."),
        ("Money", "Vietnamese dong, cash for entry tickets. Most of these places charge 100–120k a head."),
        ("Weather", "17–24°C, cool nights. September is Da Lat's wettest month — rain comes afternoon and evening, so outdoor stops are front-loaded."),
        ("Entry fees", "Floating Town 100k and Lạc Hư Cổ Trấn 120k both include a drink. Pink Valley 100k."),
        ("Getting around", "Grab in the city; a booked car by the day for the out-of-town clusters."),
        ("Want the beach too?", "Nha Trang is 135 km on QL27C, about 3 hours — the separate Da Lat + Nha Trang plan swaps Day 4 for the dry coast."),
    ],
    sign=("<b>MAS out:</b> _______________ &nbsp; <b>SGN → DLI:</b> _______________ &nbsp; "
          "<b>DLI → SGN:</b> _______________ &nbsp; <b>MAS home:</b> _______________<br>"
          "<b>Hotel:</b> _______________ &nbsp; <b>Driver:</b> _______________ &nbsp; "
          "<i>Places and hours checked 6 Sept 2026 — re-confirm the newer spots locally.</i>"),
    days=DAYS,
    extra_page=dict(
        color="#2F6B4F",
        kicker="SPARE PAGE",
        title="Nearby, if you have time",
        subtitle="Swap-ins and add-ons, listed by which day they fit",
        rows=[
            ("Thác Voi (Elephant Falls) + Nam Ban village", "25 km southwest",
             "<b>Add to Day 4.</b> Further along the same Tà Nung road as Mongo Land — a big, loud waterfall you climb down beside, and a silk-weaving village. Thunderous in green season."),
            ("Đồi chè Cầu Đất (tea hills)", "25 km southeast",
             "<b>Already on Day 2</b> — the terraces surround Euro Garden. Free to walk; best in the early cloud."),
            ("Ma Rừng Lữ Quán", "Lạc Dương, ~20 km north",
             "<b>Add to Day 3.</b> A forest camp and garden in the pines past Langbiang — quiet, ramshackle, very photogenic."),
            ("Đankia – Suối Vàng (Golden Stream)", "Lạc Dương, ~17 km north",
             "<b>Add to Day 3.</b> Big open reservoir and grassland under Langbiang. Best in late light."),
            ("Hồ Tuyền Lâm + Clay Tunnel", "6–10 km south",
             "<b>Add to Day 4.</b> Both are minutes from Happy Hill. The Clay Tunnel is a sculpted red-clay history of Da Lat — odd and good."),
            ("Thác Pongour", "50 km south, ~1h15",
             "<b>Half-day of its own.</b> The biggest waterfall in the region, seven tiers wide — at its most powerful right now in the wet season. Worth swapping a cluster for if you want one big nature day."),
            ("Trại Mát hydrangea fields", "7 km east",
             "<b>Already on Day 3</b> via Suối Bình Yên — the fields are on the same Hydrangea Street. In flower May to December."),
            ("Nha Trang", "135 km on QL27C, ~3h",
             "The dry-coast alternative: leave after Day 3, spend Days 4–5 on the beach, fly home from Cam Ranh. Separate PDF."),
        ],
        notes=[
            "Nothing here is required — the four days already hold your fourteen places.",
            "Use this page when a stop closes, the rain sets in, or something turns out to be a fifteen-minute photo stop rather than an afternoon.",
            "If you only add one: Elephant Falls on Day 4, because it's already on your route.",
        ],
    ),
)

if __name__ == "__main__":
    engine.write(TRIP,
                 os.path.join(OUT_DIR, "Itinerary-DaLat.html"),
                 os.path.join(OUT_DIR, "Itinerary-DaLat.pdf"))
