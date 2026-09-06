#!/usr/bin/env python3
"""Da Lat → Mui Ne → Saigon, 8-12 September 2026.

Da Lat cut to two days and one night, then the sand dunes, then a last night
in Saigon so the flight home is a taxi ride rather than a connection.

Run:    python3 dalat-muine-saigon/build_trip_pdf.py
Output: dalat-muine-saigon/Itinerary-DaLat-MuiNe-Saigon.html  +  .pdf
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from trips import itinerary_pdf as engine  # noqa: E402

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
GUESTS = "Haris Haikal &amp; Aina Izzaty"

DAYS = [
    dict(
        n="DAY 1", date="Tuesday, 8 September", title="Fly in — one evening in Da Lat",
        color="#46688C",
        outfit="<b>Soft blue + brown</b> — café theme, and it's cool enough for layers",
        start="Morning MAS from KLIA", finish="~21.30", sleep="Da Lat (1 night only)",
        rows=[
            ("stop", "morning", "KUL → SGN — Malaysia Airlines", "KLIA", "~2h",
             "MH750 / MH758 / MH766, about 7 a day. Take one landing in Saigon by early afternoon. Vietnam is <b>1 hour behind Malaysia</b>."),
            ("stop", "~12.30", "Connect at Tan Son Nhat", "Saigon — T2 international, T1 domestic", "~3h",
             "Separate tickets means collecting bags, walking to T1 and checking in again. Three hours is the safe margin."),
            ("stop", "~15.30", "SGN → DLI — Vietnam Airlines or Vietjet", "Tan Son Nhat T1", "55 min",
             "Six a day, last departure 17:30. Book it the same day as the MAS leg."),
            ("move", "Lien Khuong airport &rarr; Da Lat city &mdash; 30 km, ~40 min", "", "", "", ""),
            ("stop", "~17.30", "Check in — Da Lat", "City centre, near the lake", "45 min",
             "One night only, so stay central and don't unpack properly."),
            ("stop", "~18.30", "Xuan Huong Lake", "City centre", "1h",
             "The lake loop at dusk, lit up and busy with locals. Five minutes from anywhere central."),
            ("stop", "~19.45", "Dinner + L'angfarm Center", "Da Lat centre", "1.5h",
             "Dried fruit, artichoke tea, jam, coffee, macadamia — buy the whole lot tonight, because you leave tomorrow. They vacuum-pack."),
            ("stop", "~21.15", "Da Lat Night Market", "Cho Dem, centre", "45 min",
             "Right there and open late. Grilled corn, banh trang nuong, hot soy milk if you still have room."),
        ],
        notes=[
            "Da Lat is at 1,500 m — 17–24°C and about 17°C tonight. This is the only cold evening of the trip; the jacket earns its place today and tomorrow at dawn.",
            "<b>Simpler alternative:</b> AirAsia flies KUL → Da Lat direct (AK571, 2h10) but only ~4 days a week. If 8 September is one, take it and skip Saigon entirely on the way in.",
            "Set the alarm for 04.30. Tomorrow starts in the dark and it's worth it.",
        ],
    ),
    dict(
        n="DAY 2", date="Wednesday, 9 September", title="Dawn clouds, hydrangeas, then the pass to the sea",
        color="#D4749B",
        outfit="<b>Black leather + white</b> for the 05.00 cloud hunt (it's cold) &middot; change into <b>soft pink + white</b> after breakfast",
        start="05.00", finish="~21.00", sleep="<b>Move</b> → Mui Ne (2 nights)",
        compact=True,
        rows=[
            ("stop", "05.00", "Thác Mây &amp; Chill — cloud hunting at dawn",
             "Dốc số 9, Trại Mát — 15–20 min east", "2h",
             "It opens at <b>05:00</b> exactly so you can watch cloud pour into the ravine below you at first light. Cold, dark, worth it. This is the leather-jacket hour."),
            ("move", "~20 min back to the hotel", "", "", "", ""),
            ("stop", "~07.30", "Breakfast + change", "Da Lat centre", "1h",
             "Swap into the pink and white for the flower stop."),
            ("stop", "~08.45", "Suối Bình Yên + Hydrangea Street",
             "Hoa Cẩm Tú Cầu st, Ward 3 — 10–15 min out", "1.5h",
             "A stream-side garden café, deliberately slow — and it sits on <b>Hydrangea Street</b>, so the cẩm tú cầu fields are right there. They flower May to December, so they're out now."),
            ("move", "~25 min south on QL20", "", "", "", ""),
            ("stop", "~10.45", "Datanla — new alpine coaster", "QL20, ~5 km south", "1.25h",
             "The rebuilt coaster down through the forest, and the falls at the bottom. You control the brake. It's on the road out of town, so it costs you no detour."),
            ("stop", "~12.15", "Lunch, then collect the bags", "Da Lat / Đức Trọng", "45 min",
             "Eat before the pass — there is not much on QL28B."),
            ("move", "DRIVE: Da Lat &rarr; Mui Ne on QL28B over the Đại Ninh pass &mdash; 155 km, 3.5&ndash;4 hours", "", "", "", ""),
            ("stop", "~16.45", "Drop bags — Mui Ne", "Mui Ne / Ham Tien beach strip", "20 min",
             "Straight in, bags down, back out. You're chasing the sunset."),
            ("stop", "~17.15", "Red Sand Dunes (Đồi Hồng) for sunset",
             "~10 min from the Mui Ne strip", "1.5h",
             "Orange dunes right by the road, best in the last hour of light. Kids rent plastic sleds; the dunes photograph far bigger than they are."),
            ("stop", "~19.30", "Seafood dinner", "Mui Ne fishing-village end", "1.5h",
             "Pick from the tanks. Cheaper and better at the village end than on the resort strip."),
        ],
        notes=[
            "<b>Leave Da Lat by 12.45.</b> QL28B climbs down the Đại Ninh pass and you want it in daylight — it's a good road but a serious one.",
            "If the morning slips, drop Datanla. It's the one stop that isn't unique to this trip.",
            "You descend from 1,500 m to sea level today: 17°C at dawn, 31°C by dinner. Pack the jacket away at the bottom of the bag after this morning.",
        ],
    ),
    dict(
        n="DAY 3", date="Thursday, 10 September", title="Mui Ne — white dunes at sunrise, red canyon after",
        color="#1E7FA8",
        outfit="<b>Blue + yellow</b> — sand, sky and sea all day",
        start="05.00", finish="~21.00", sleep="Mui Ne (night 2)",
        rows=[
            ("stop", "05.00", "White Sand Dunes (Bàu Trắng) — sunrise",
             "~35 km northeast, ~45 min", "2.5h",
             "The big pale dunes, and the only genuine desert in Vietnam. Go for sunrise: cool, empty, and the light is the whole point. Jeeps and quad bikes wait at the entrance — agree the price before you get in."),
            ("stop", "~07.45", "Bàu Trắng lotus lake", "Beside the dunes", "45 min",
             "A freshwater lake right against the sand, fringed with lotus. The contrast of water, lotus and desert in one frame is the shot people come for."),
            ("move", "~45 min back to Mui Ne", "", "", "", ""),
            ("stop", "~09.30", "Breakfast back on the strip", "Ham Tien", "1h", ""),
            ("stop", "~10.45", "Fairy Stream (Suối Tiên)", "Ham Tien, off the main road", "1.25h",
             "Wade barefoot up a warm ankle-deep stream between red and white sandstone walls. Ten minutes in it opens into a small canyon. Leave the shoes at the entrance."),
            ("stop", "~12.15", "Lunch", "Mui Ne", "1h", ""),
            ("stop", "~13.30", "Beach and pool — the hot hours", "Your resort", "2.5h",
             "This is the point of Mui Ne. Do nothing until four."),
            ("stop", "~16.15", "Fishing village + Ông Địa rock beach", "Mui Ne village end", "1.5h",
             "Round blue coracle boats pulled up on the sand — the most photographed thing in Mui Ne after the dunes. Best in late afternoon when the fleet is in."),
            ("stop", "~18.00", "Sunset on the beach + kite surfers", "Ham Tien strip", "1h",
             "Mui Ne is Vietnam's kite-surfing capital and the wind gets up late afternoon."),
            ("stop", "~19.30", "Dinner", "Mui Ne", "1.5h", ""),
        ],
        notes=[
            "Two early starts in a row, then an afternoon doing nothing. That's the deal — the dunes are only good at the ends of the day.",
            "<b>Agree jeep and quad prices before starting</b>, and confirm whether the fee is per person or per vehicle.",
            "Sun here is much stronger than Da Lat: hat, sunscreen, water. Sand gets everywhere — leave the good camera bag in the room.",
        ],
    ),
    dict(
        n="DAY 4", date="Friday, 11 September", title="Down the expressway to Saigon",
        color="#A8763A",
        outfit="<b>Cream fairytale</b> — the colonial quarter and the café apartment",
        start="08.00", finish="~22.00", sleep="<b>Move</b> → Saigon (night 4)",
        rows=[
            ("stop", "08.00", "Slow morning — beach or pool", "Mui Ne", "2h",
             "No rush. The drive is short today."),
            ("stop", "~10.15", "Checkout", "Mui Ne", "30 min", ""),
            ("move", "DRIVE: Mui Ne &rarr; Saigon on the Dầu Giây&ndash;Phan Thiết expressway &mdash; 200&ndash;220 km, 2.5&ndash;3 hours", "", "", "", ""),
            ("stop", "~13.45", "Check in — District 1", "Ben Thanh / Nguyen Hue area", "45 min",
             "Stay in District 1 and the whole afternoon is walkable."),
            ("stop", "~15.00", "The Café Apartment, 42 Nguyễn Huệ", "Nguyen Hue walking street", "2h",
             "A nine-storey 1960s apartment block where every flat is now a café or a tiny shop, each with its own balcony over the street. Ride the lift to the top and work down — this is the cream-outfit location."),
            ("stop", "~17.15", "Nguyễn Huệ walking street + Saigon Post Office",
             "District 1", "1.25h",
             "The post office is Gustave Eiffel-era colonial iron and tiles, and still a working post office — send yourselves a postcard. Book Street is round the corner."),
            ("stop", "~18.45", "Bến Thành Market + Saigon Square", "District 1", "1.5h",
             "The last shopping of the trip. Bến Thành for souvenirs, Saigon Square for clothes and bags. Bargain hard — start at about 40%."),
            ("stop", "~20.30", "Rooftop dinner", "District 1", "1.5h",
             "Saigon does rooftops properly. Book one with a view down Nguyen Hue."),
        ],
        notes=[
            "The expressway has cut this drive to under three hours — it used to be five. Book a private car; the bus takes twice as long.",
            "Saigon in September is hot and wet, with a heavy shower most afternoons that clears in an hour. The café apartment and the market are both fine in rain.",
            "Pack tonight. Tomorrow is only a taxi ride and a flight.",
        ],
    ),
    dict(
        n="DAY 5", date="Saturday, 12 September", title="Fly home from Saigon",
        color="#6B6A52",
        outfit="<b>Khaki + black</b> — travel day",
        start="08.00", finish="KUL", sleep="—",
        rows=[
            ("stop", "08.00", "Breakfast + last Vietnamese coffee", "District 1", "1.5h",
             "Cà phê sữa đá one more time. Buy beans on the way back if you didn't in Da Lat."),
            ("stop", "~10.30", "Checkout", "District 1", "30 min", ""),
            ("move", "Hotel &rarr; Tan Son Nhat airport (SGN) &mdash; 8 km, 30&ndash;45 min in traffic", "", "", "", ""),
            ("stop", "~12.00", "Check-in + immigration", "Tan Son Nhat T2", "2h buffer",
             "International departures, Terminal 2. Saigon traffic is the variable, not the airport."),
            ("stop", "afternoon", "SGN → KUL — Malaysia Airlines", "Tan Son Nhat T2", "~2h",
             "MH750 / MH758 / MH766. Malaysia is 1 hour ahead, so you land later on the clock than the flight time suggests."),
        ],
        notes=[
            "<b>This is why the last night is in Saigon:</b> no domestic connection on the day you fly home. Just a taxi.",
            "Tan Son Nhat is inside the city — no long airport road, but the traffic getting there is real.",
        ],
    ),
]

TRIP = dict(
    doc_title="Da Lat, Mui Ne &amp; Saigon — 8-12 September 2026",
    kicker="Plan B &middot; three stops &middot; Bandung is off (Anak Krakatau)",
    title="Da Lat &rarr; Mui Ne &rarr; Saigon<br>8 &ndash; 12 September 2026",
    subtitle=(f"{GUESTS} &middot; Malaysia Airlines both ways &middot; two nights of driving, no flying in between<br>"
              "Da Lat in two days and one night, the dunes for two, Saigon for the last."),
    travellers=GUESTS,
    country="Vietnam",
    no_map=("Breakfast", "Lunch", "Dinner", "Check in", "Checkout", "Connect", "Drop bags",
            "Slow morning", "Beach and pool", "Sunset on", "KUL →", "SGN →", "DLI →"),
    summary_title="The Five Days",
    summary_head=("Day", "Date", "Where", "The point of the day", "Outfit"),
    summary_rows=[
        ("Day 1", "Tue, 8 Sep", "Fly in → Da Lat", "Lake, L'angfarm, night market", "Soft blue + brown"),
        ("Day 2", "Wed, 9 Sep", "Da Lat → <b>Mui Ne</b>",
         "Dawn clouds, hydrangeas, coaster, then the pass", "Black leather am · pink + white"),
        ("Day 3", "Thu, 10 Sep", "Mui Ne", "White dunes at sunrise, Fairy Stream, beach", "Blue + yellow"),
        ("Day 4", "Fri, 11 Sep", "Mui Ne → <b>Saigon</b>", "Café apartment, post office, Bến Thành", "Cream fairytale"),
        ("Day 5", "Sat, 12 Sep", "Fly home", "Taxi to the airport, nothing else", "Khaki + black"),
    ],
    book_now_head="Book Tonight, In This Order",
    book_now=[
        ("Ask Malaysia Airlines to reroute the CGK ticket to Saigon",
         "MAS flies KUL–Saigon ~7 times a day (MH750 / MH758 / MH766). If they cancel Jakarta, ask to be moved to Saigon rather than refunded. <b>+60 3-7843-3000</b>"),
        ("MAS KUL → SGN on 8 Sept (morning), SGN → KUL on 12 Sept (afternoon)",
         "Only the outbound needs a domestic connection — the way home is a straight flight from Saigon."),
        ("Domestic: SGN → Da Lat on 8 Sept",
         "Vietnam Airlines or Vietjet, 55 min, six a day, last one 17:30. Leave three hours to connect."),
        ("Two private cars, booked ahead",
         "9 Sept: Da Lat → Mui Ne on <b>QL28B</b> (155 km, 3.5–4h), pickup 12.45. 11 Sept: Mui Ne → Saigon on the expressway (2.5–3h), pickup ~10.30."),
        ("Hotels: 1 night Da Lat (8th), 2 nights Mui Ne (9–10), 1 night Saigon (11th)",
         "Da Lat central; Mui Ne on the Ham Tien beach strip; Saigon in District 1 near Nguyen Hue."),
        ("A car for Day 2 morning and Day 3 sunrise",
         "Day 2 needs an <b>04.40 pickup</b> for the cloud hunt; Day 3 an 04.30 for the white dunes. The Mui Ne hotel can arrange a jeep."),
        ("Cancel or move the Bandung bookings",
         "Holiday Inn Pasteur, Swiss-Belresort Dago, Fairfield CGK — ask for a waiver citing the airport closure. Message Kiki."),
        ("Insurance, eSIM, offline maps", "Re-issue for Vietnam; keep the Bandung paperwork for the claim."),
    ],
    know_cols=3,
    good_to_know=[
        ("Visa", "Visa-free for Malaysians, 30 days. Carry hotel bookings and onward tickets."),
        ("Three climates", "Da Lat 17–24°C and cool at dawn; Mui Ne 25–31°C and bright; Saigon 30°C+ and humid."),
        ("Weather honesty", "Mui Ne is one of Vietnam's driest regions but September still averages ~217 mm over ~20 days — lighter and shorter than elsewhere, not dry."),
        ("Money", "Vietnamese dong. Cash for dune jeeps, market bargaining and small cafés."),
        ("Getting around", "Grab in Da Lat and Saigon. In Mui Ne everything is on one strip — taxis and hotel cars."),
        ("Two early starts", "05.00 on Days 2 and 3. Both are for light you cannot get later. The afternoons are deliberately empty."),
    ],
    sign=("<b>MAS out:</b> _______________ &nbsp; <b>SGN → DLI:</b> _______________ &nbsp; "
          "<b>MAS home:</b> _______________ &nbsp; <b>QL28B car:</b> _______________<br>"
          "<b>Da Lat hotel:</b> _______________ &nbsp; <b>Mui Ne hotel:</b> _______________ &nbsp; "
          "<b>Saigon hotel:</b> _______________ &nbsp; <i>Checked 6 Sept 2026.</i>"),
    days=DAYS,
    extra_page=dict(
        color="#2F6B4F",
        kicker="SPARE PAGE",
        title="What one night in Da Lat costs you",
        subtitle="The nine places off your list that didn't fit — and what to add if you find more time",
        rows=[
            ("Euro Garden Cầu Đất", "25 km southeast of Da Lat",
             "<b>The biggest loss.</b> 7.2 ha at 1,650 m — flower fields, a miniature castle and Eiffel Tower, a railway café. If you ever add a Da Lat night, this is the one."),
            ("Lạc Hư Cổ Trấn + Miền Du Mục", "Lâm Văn Thạnh rd, Xuân Trường",
             "Both on the same road east: a Chinese ancient-town set, and a nomad tent café on a pine hill. A half-day for the pair — they'd pair with Euro Garden on one eastern day."),
            ("Pink Valley + Langbiang", "Lạc Dương, 12–22 km north",
             "Rose valley and the mountain, ten minutes apart. They sit on the road to Nha Trang, not the road to Mui Ne — which is why they fall out of this version."),
            ("Mongo Land + Floating Town", "Tà Nung, 15–17 km southwest",
             "Mongolian yurts, horses and archery; then wooden houses standing out of an emerald lake. Both on the western road, a half-day for the pair."),
            ("KDL Sinh Thái Cao Nguyên Hoa", "Tà Nung area",
             "Flower-highland eco park, next to the two above. Confirm hours locally — it's recent."),
            ("Happy Hill", "Đá Tiên, Tuyen Lam lake, 12 km south",
             "Film-set park with windmills and staged photo corners. Closes 17:30. Nearest of the lot to the road out."),
            ("Bàu Trắng lotus lake", "Beside the White Dunes, Mui Ne",
             "<b>Already on Day 3</b> — lotus against desert sand, right where the jeeps drop you."),
            ("Kê Gà lighthouse + dragon fruit farms", "~60 km southwest of Mui Ne",
             "If you want one more Mui Ne outing: an 1890s lighthouse on an island you reach by boat, through miles of dragon-fruit trellises that get lit at night."),
            ("Mekong Delta day trip", "From Saigon, ~2h each way",
             "Only if you swap the Saigon night for two. Floating markets and — right now, in flood season — the pink water lilies."),
        ],
        notes=[
            "One night in Da Lat buys you the dawn cloud hunt, the hydrangeas and the coaster. Everything above needs a second night.",
            "<b>If you do add a Da Lat night:</b> spend it on the eastern road — Euro Garden, Lạc Hư Cổ Trấn and Miền Du Mục in one day, no backtracking.",
            "Cao Nguyên Hoa and Miền Du Mục are both recent; re-confirm their hours locally before counting on them.",
        ],
    ),
)

if __name__ == "__main__":
    engine.write(TRIP,
                 os.path.join(OUT_DIR, "Itinerary-DaLat-MuiNe-Saigon.html"),
                 os.path.join(OUT_DIR, "Itinerary-DaLat-MuiNe-Saigon.pdf"))
