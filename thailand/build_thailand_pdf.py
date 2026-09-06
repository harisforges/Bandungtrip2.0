#!/usr/bin/env python3
"""Plan B itinerary — Chiang Mai & the north, 7-12 September 2026.

Second alternative to Bandung after Anak Krakatau closed CGK. One hotel for
all five nights, day trips out; no driver to arrange. Phuket deliberately
left out — already done last year.

Run:    python3 thailand/build_thailand_pdf.py
Output: thailand/Itinerary-Thailand-Chiang-Mai.html  +  .pdf
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from trips import itinerary_pdf as engine  # noqa: E402

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
GUESTS = "Haris Haikal &amp; Aina Izzaty"

DAYS = [
    dict(
        n="DAY 1", date="Monday, 7 September", title="Fly to Chiang Mai + Old City",
        color="#B26C12", outfit="Summer outfit — but carry a scarf/shawl for the temples",
        start="09.50 from KLIA", finish="~21.00", sleep="Chiang Mai (all 5 nights)",
        rows=[
            ("stop", "09.50", "KUL → CNX — Malaysia Airlines MH772",
             "KLIA", "2h 40m",
             "Lands 11.40. MH792 (11.50→13.40) and AirAsia AK856 (13.30→15.10) are the other same-day options. Thailand is <b>1 hour behind Malaysia</b>."),
            ("stop", "~12.30", "Check in — Old City or Nimman",
             "Chiang Mai", "1h",
             "One hotel for the whole trip. Old City = temples on your doorstep; Nimman = cafés and a younger feel. Both fine."),
            ("stop", "~14.00", "Wat Phra Singh + Wat Chedi Luang",
             "Old City, inside the moat", "2h",
             "The two big ones, 10 minutes apart on foot. <b>Shoulders and knees covered</b> — this applies to both of you at every temple."),
            ("move", "~15 min by Grab", "", "", "", ""),
            ("stop", "~16.30", "Nimmanhaemin — One Nimman + a café",
             "Nimmanhaemin Road", "2h",
             "Chiang Mai's café district: Ristr8to, Graph, Akha Ama. This is the Braga-and-Kopi-Toko-Djawa slot."),
            ("stop", "~19.00", "Dinner — khao soi, then the Night Bazaar",
             "Chang Klan Road", "2h",
             "Khao soi is the northern dish to try first. Night Bazaar is touristy but good for a first evening."),
        ],
        notes=[
            "Easy first day on purpose — one flight, no long transfer, unlike the Bandung and Hanoi versions.",
            "Grab and Bolt both work here. Songthaews (red trucks) are ~30–40 THB a hop in the city — flag one down and say where.",
            "Green season: showers tend to come late afternoon or overnight. Keep a light rain shell in the day bag.",
        ],
    ),
    dict(
        n="DAY 2", date="Tuesday, 8 September", title="Doi Inthanon — the roof of Thailand",
        color="#15764F", outfit="Emerald denim casual — green terraces, cool mountain air",
        start="07.30", finish="~18.30", sleep="Chiang Mai",
        rows=[
            ("stop", "07.30", "Depart with your booked car + driver", "", "—",
             "Book a private day tour the night before — hotel desk, Klook or GetYourGuide. This replaces Kiki for the day."),
            ("move", "DRIVE: Chiang Mai &rarr; Doi Inthanon National Park &mdash; ~2 hours", "", "", "", ""),
            ("stop", "~09.30", "Twin Royal Pagodas + gardens",
             "Doi Inthanon, 2,565 m", "1.5h",
             "The King and Queen pagodas with terraced gardens between them. <b>Cold and windy up here</b> — 15–20°C, bring the jacket you packed for Kawah Putih."),
            ("stop", "~11.15", "Ang Ka nature trail + summit point",
             "Doi Inthanon summit", "45 min",
             "Short boardwalk through mossy cloud forest. Thailand's highest point is a marker, not a view — the trail is the good part."),
            ("move", "~30 min down the mountain", "", "", "", ""),
            ("stop", "~12.30", "Ban Mae Klang Luang — rice terraces + Karen coffee village",
             "Doi Inthanon foothills", "2.5h",
             "Vivid green terraces in September, hill-tribe village, coffee grown on the slope. Lunch here at a terrace restaurant."),
            ("move", "~20 min", "", "", "", ""),
            ("stop", "~15.30", "Wachirathan Waterfall", "Doi Inthanon National Park", "1h",
             "Thunderous in green season and throws spray a long way — this is the wettest you'll get all trip, which is the fun of it."),
            ("move", "DRIVE: back to Chiang Mai &mdash; ~2 hours", "", "", "", ""),
            ("stop", "~18.30", "Back in the city — dinner nearby", "", "—",
             "Long day. Keep dinner close to the hotel."),
        ],
        notes=[
            "Longest driving day of the trip, ~4 hours total — this is the Ciwidey day of the Thailand plan.",
            "National park entry is charged per person at the gate; your driver will stop for it.",
            "Winding mountain road — the motion-sickness tablets from your checklist earn their place today.",
        ],
    ),
    dict(
        n="DAY 3", date="Wednesday, 9 September", title="Mae Rim valley — gardens, cafés, sticky waterfall",
        color="#6D2E5B", outfit="Cream elegant — botanic gardens and forest cafés",
        start="09.00", finish="~19.30", sleep="Chiang Mai",
        rows=[
            ("stop", "09.00", "Depart north into the Mae Sa valley", "", "—",
             "Grab works for this, but a half-day car is easier with several stops."),
            ("move", "~40 min", "", "", "", ""),
            ("stop", "~09.45", "Queen Sirikit Botanic Garden",
             "Mae Rim district", "2.5h",
             "Glasshouses, orchids and a canopy walkway through the treetops. The elegant-outfit location of the trip."),
            ("move", "~30 min", "", "", "", ""),
            ("stop", "~13.00", "Lunch at a valley café",
             "Mae Rim / Mae Sa valley", "1.5h",
             "The Giant (a treehouse café) or Fern Forest. Chiang Mai's answer to Lawangwangi and Congo."),
            ("move", "~40 min north", "", "", "", ""),
            ("stop", "~15.30", "Bua Tong Sticky Waterfalls",
             "Si Lanna National Park, Mae Taeng", "2h",
             "Limestone falls you can genuinely walk <i>up</i> — the rock grips your feet. Free entry. Bring a change of clothes: this is the Cibuni of this trip, minus the mud."),
            ("move", "~1 hour back to the city", "", "", "", ""),
            ("stop", "~18.30", "Dinner in Nimman", "Nimmanhaemin", "1.5h", ""),
        ],
        notes=[
            "Mon Jam's famous flower fields are a cool-season thing (Nov–Feb). In September the valley is green and misty instead — beautiful, but manage expectations.",
            "Sticky Waterfalls: sandals or shoes you don't mind soaking, and the towel from the packing list.",
            "This is the easy-driving day: everything is within 40 minutes of the city.",
        ],
    ),
    dict(
        n="DAY 4", date="Thursday, 10 September", title="Chiang Rai — White, Blue and Black",
        color="#C0437A", outfit="Cute pink &amp; white — the temples are the colour palette",
        start="07.30 sharp", finish="~20.30", sleep="Chiang Mai",
        compact=True,
        rows=[
            ("stop", "07.30", "Depart on the Chiang Rai day tour", "", "—",
             "A ~13-hour day. Book a small-group or private tour; it runs to a fixed timetable."),
            ("move", "DRIVE: Chiang Mai &rarr; Chiang Rai &mdash; ~3 hours each way", "", "", "", ""),
            ("stop", "~10.30", "Wat Rong Khun — the White Temple",
             "Chiang Rai", "1.5h",
             "All white and mirrored glass. The most photographed building in northern Thailand — go straight to the bridge before the coaches arrive."),
            ("stop", "~12.15", "Lunch in Chiang Rai", "Chiang Rai town", "1h", ""),
            ("stop", "~13.30", "Wat Rong Suea Ten — the Blue Temple",
             "Chiang Rai", "1h",
             "Electric blue and gold inside. Pink and white against that blue is the photo of the day."),
            ("stop", "~15.00", "Baan Dam — the Black House",
             "Nang Lae, Chiang Rai", "1.5h",
             "The dark counterpoint to the White Temple: an artist's compound of black timber halls. Odd and memorable."),
            ("move", "DRIVE: back to Chiang Mai &mdash; ~3 hours", "", "", "", ""),
            ("stop", "~20.30", "Back at the hotel", "", "—", "Late finish. Keep tomorrow gentle."),
        ],
        notes=[
            "The one genuinely long day — 6 hours in the car for three of the north's signature sights. Worth it, but do not add anything else to today.",
            "Snacks and water in the day bag; stops are at the tour's discretion.",
            "If the forecast is heavy all day, swap this with Day 5 — the temples are better in dry light.",
        ],
    ),
    dict(
        n="DAY 5", date="Friday, 11 September", title="Doi Suthep + city, markets and massage",
        color="#7A5410", outfit="Smart casual — temple-appropriate again",
        start="08.30", finish="~21.00", sleep="Chiang Mai",
        rows=[
            ("stop", "08.30", "Wat Phra That Doi Suthep",
             "Doi Suthep, 30 min from the Old City", "2h",
             "Chiang Mai's landmark temple on the mountain. Go early — the cloud rolls in later and the crowds arrive with it. 300 steps up, or the funicular."),
            ("move", "~30 min back down", "", "", "", ""),
            ("stop", "~11.30", "Lunch + coffee in the Old City", "Old City", "1.5h", ""),
            ("stop", "~13.30", "Warorot Market", "Wichayanon Road, by the river", "1.5h",
             "Where locals shop: dried fruit, northern sausage, textiles, chilli pastes. This is the Kartika Sari slot — souvenirs and edible gifts."),
            ("move", "~10 min", "", "", "", ""),
            ("stop", "~15.30", "Wua Lai silver street + handicrafts",
             "Wua Lai Road, south of the moat", "1.5h",
             "Silverwork, lacquer, Lanna crafts. Sunday walking street runs here — you'll miss it, but the shops are open daily."),
            ("stop", "~17.30", "Thai massage", "Old City", "1.5h",
             "Two hours of Thai or oil massage costs less than a taxi ride home. Book a slot mid-afternoon."),
            ("stop", "~19.30", "Farewell dinner", "Old City or riverside", "1.5h",
             "Riverside restaurants on the Ping are the nicer end. Pack tonight."),
        ],
        notes=[
            "Everything today is 10–30 minutes apart by Grab. No tour needed.",
            "Doi Suthep is an active temple — the strictest dress code of the trip. Cover shoulders and knees, shoes off inside.",
            "Leave room in the bags: Warorot and Wua Lai are where the souvenirs actually happen.",
        ],
    ),
    dict(
        n="DAY 6", date="Saturday, 12 September", title="Fly home",
        color="#5B6560", outfit="Comfy travel outfit",
        start="Depends on flight", finish="KUL", sleep="—",
        rows=[
            ("stop", "08.00", "Breakfast + last café", "Chiang Mai", "1.5h",
             "The airport is only 15–20 minutes from anywhere in the city, so there's no rush."),
            ("stop", "~10.30", "Checkout → Chiang Mai Airport (CNX)",
             "~20 min by Grab", "—",
             "Small, easy airport — international departures are straightforward."),
            ("stop", "~11.30", "Check-in + immigration", "CNX", "2h buffer",
             "Standard 2 hours for an international flight."),
            ("stop", "afternoon", "CNX → KUL", "", "~2h 40m",
             "Confirm your return time when you book the outbound — Malaysia is 1 hour ahead."),
        ],
        notes=[
            "CNX is the easiest airport exit of any version of this trip — 20 minutes from the hotel.",
        ],
    ),
]

TRIP = dict(
    doc_title="Thailand — Chiang Mai &amp; the North, 7-12 September 2026",
    kicker="Plan B &middot; option 2 &middot; Bandung is off (Anak Krakatau)",
    title="Thailand — Chiang Mai &amp; the North<br>7 &ndash; 12 September 2026",
    subtitle=(f"{GUESTS} &middot; one hotel for five nights, day trips out, no driver to arrange<br>"
              "Green season: waterfalls at full flow, terraces vivid green, low season prices."),
    travellers=GUESTS,
    country="Thailand",
    no_map=("Breakfast", "Lunch", "Dinner", "Depart", "Check in", "Checkout", "Back in",
            "Back at", "KUL →", "CNX →", "Thai massage"),
    summary_head=("Day", "Date", "Shape", "Where", "Driving"),
    summary_rows=[
        ("Day 1", "Mon, 7 Sep", "Fly + city", "Old City, Nimman cafés", "none"),
        ("Day 2", "Tue, 8 Sep", "Mountain day", "Doi Inthanon", "~4h"),
        ("Day 3", "Wed, 9 Sep", "Gardens + cafés", "Mae Rim, Bua Tong falls", "~2h"),
        ("Day 4", "Thu, 10 Sep", "Long day out", "Chiang Rai temples", "<b>~6h</b>"),
        ("Day 5", "Fri, 11 Sep", "Temple + markets", "Doi Suthep, Warorot", "~1h"),
        ("Day 6", "Sat, 12 Sep", "Fly home", "CNX → KUL", "20 min"),
    ],
    book_now_head="Book Tonight, In This Order",
    book_now=[
        ("Ask Malaysia Airlines to reroute, don't cancel",
         "MAS runs two of the three daily KUL–Chiang Mai flights (MH772 09:50→11:40, MH792 11:50→13:40). If they cancel CGK, ask to be moved onto their Chiang Mai service instead of refunded. <b>+60 3-7843-3000</b>"),
        ("Flights KUL → CNX on 7 Sept, and the return on 12 Sept",
         "8 flights a week on the route: MH772, MH792, and AirAsia AK856 (13:30→15:10). 2h 40m."),
        ("TDAC — Thailand Digital Arrival Card",
         "Mandatory for every entry, filed online at <b>tdac.immigration.go.th</b> before you arrive. The Thai equivalent of the Indonesian e-CD — don't skip it."),
        ("Hotel — five nights, one place",
         "Old City or Nimman. No hotel switch in this version, so unpack once."),
        ("Two day tours with car + driver",
         "Doi Inthanon (Day 2) and Chiang Rai (Day 4). Hotel desk, Klook or GetYourGuide. Book both tonight — they leave early."),
        ("Cancel or move the Bandung bookings",
         "Holiday Inn Pasteur, Swiss-Belresort Dago, Fairfield CGK — ask for a waiver citing the airport closure. Message Kiki."),
        ("Insurance, eSIM, offline maps",
         "Re-issue the insurance for Thailand and keep the Bandung cancellation paperwork for the claim. Signal is fine in the city, patchy on Doi Inthanon."),
    ],
    know_cols=3,
    good_to_know=[
        ("Visa", "Visa-free for Malaysians — the 60-day exemption still applies on 7 Sept (30 days from 15 Sept, irrelevant for 5 nights)."),
        ("Money", "Thai baht. Cards fine in the city; cash for markets, temples, park entry."),
        ("Getting around", "Grab and Bolt everywhere; songthaews ~30–40 THB a hop. The two mountain days come with a driver."),
        ("Weather", "Green season: ~33°C, humid, ~18 rainy days in September. Showers come late afternoon or overnight — mornings are the clear window."),
        ("Temple dress", "Shoulders and knees covered at every temple, both of you. A light scarf handles it."),
        ("Why here", "Waterfalls at full flow, terraces at their greenest, and the quietest, cheapest month of the year."),
    ],
    sign=("<b>Flight out:</b> _________________ &nbsp; <b>Flight home:</b> _________________ &nbsp; "
          "<b>Booking ref:</b> _________________<br>"
          "<b>Doi Inthanon tour:</b> _________________ &nbsp; <b>Chiang Rai tour:</b> _________________ &nbsp; "
          "<i>Checked 6 Sept 2026 — confirm fares and availability.</i>"),
    days=DAYS,
)

if __name__ == "__main__":
    engine.write(TRIP,
                 os.path.join(OUT_DIR, "Itinerary-Thailand-Chiang-Mai.html"),
                 os.path.join(OUT_DIR, "Itinerary-Thailand-Chiang-Mai.pdf"))
