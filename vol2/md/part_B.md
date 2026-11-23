# Part B: The Shipper And Receiver

Supplying a Continent · Vol. 2 · Australian Logistics

## Who This Part Is For

Part B is for the person who buys freight and the person who receives it: the freight coordinator, the warehouse manager who books the trucks and runs the dock, the importer bringing in containers, the business owner who pays the carrier invoices. Its promise is simple: **know what a consignment should cost before the invoice arrives, and know what it really cost once it is on your floor.**

Every chapter ends in a tool. Every rate in the tools is editable, and each one says when its figures were last checked.

| If you want to know | Use |
| --- | --- |
| What weight the carrier will charge you for | T01 Cubic and chargeable weight |
| Which carrier is really cheapest on each lane | T02 Carrier rate comparer |
| Whether a carrier's fuel levy follows diesel both ways | T03 Fuel levy tracker |
| What was overcharged on an invoice, and why | T04 Freight invoice audit |
| Road, rail, air or sea for one shipment | T05 Mode chooser |
| A one page price and transit table for the office | T06 Lane cost and transit table |
| What freight costs you per order, month by month | T07 Freight cost per order |
| Which carriers earn more of your work | T08 Carrier scorecard |
| What an imported product really costs once it reaches your door | T29 Landed cost calculator |
| Who is booked at your dock, and how long each truck waited | T30 Dock booking and receiving log |

## Chapter 1: Parcel, Pallet, LTL Or Full Load

The service you book decides how you are charged, so pick it before you ask for a price. Four services cover almost everything a warehouse sends by road.

[[sketch B01 fifth]]

| Service | What it is | How it is priced | Best for |
| --- | --- | --- | --- |
| Parcel or courier | Items handled one by one through depots and sorting | Per item, by weight or cubic weight, by zone | Cartons a person can lift, ecommerce orders |
| Pallet network (LTL) | Your pallets share a truck with other customers' freight, through depots | Per pallet, or basic charge plus rate per kg | One to a few pallets |
| Part load | Your freight takes part of a truck, often without a depot stop | Per metre of deck or per pallet space | Several pallets that should not be rehandled |
| Full truck load (FTL) | The whole truck is yours, door to door | Per truck, per trip | Most of a semi, or anything that must not be touched |

&#91;embedded content: Choosing the service · 3 questions\]

The half a semi rule is a starting point, not a law: a 13.6 m semi takes 22 standard Australian pallets (T12), so at 11 pallets or more a full load quote is worth getting. Urgency moves the answer: an overnight need can make a dedicated truck cheaper than a missed delivery. Value and fragility move it too, because every depot transfer is another forklift touching your freight.

For freight that could go by rail, air or sea as well as road, use **T05 Mode chooser**: it knocks out any mode that misses your deadline, then scores the rest on cost and service.

## Chapter 2: The Carrier Landscape

No single carrier is cheapest everywhere, so most shippers run two or three: one for parcels, one for pallets, and a specialist for the hard lanes. The table groups the main names by what they are built for; ownership is shown where it was confirmed in November 2026.

| Carrier | Built for | Owner (confirmed Nov 2026) |
| --- | --- | --- |
| Australia Post and StarTrack | Parcels and express to every postcode, including remote | Australia Post (government business enterprise) |
| Team Global Express | National parcels and pallet freight, express and general | Allegro Funds (bought from Toll in 2021) |
| Toll | Contract logistics, intermodal, large accounts | Japan Post Holdings |
| Border Express | National general and express freight | Pacific Equity Partners (from March 2025) |
| Mainfreight | Pallet and LTL freight, plus warehousing | Mainfreight Limited (listed on the NZX) |
| Northline | The north and west: Darwin, the Kimberley, central Australia | Private, Australian owned |
| Direct Freight Express | National road express, regional reach | Private, Australian family owned |
| CouriersPlease | Metro parcels and ecommerce | Pacific Equity Partners (with Border Express, from March 2025) |
| FedEx (including TNT) and Aramex | Parcels, express and international | FedEx Corporation; the Aramex group, majority owned by Abu Dhabi's ADQ since 2025 |
| Regional and local carriers | One region or city done well, often cheaper inside it | Local |
| Freight aggregators and brokers | One login and one invoice across many carriers | Various |

Three questions sort a carrier before you ask for rates:

1. **Does it own the lane or subcontract it?** A carrier that hands your Perth freight to another network adds a transfer, a day and a damage risk.
2. **What cubic factor and minimum charge does it use?** These matter more than the headline rate per kg (Chapter 3).
3. **How is its fuel levy set, and where is it published?** (Chapter 4.)

A broker or aggregator is not a carrier. You gain choice and one invoice, but a damage claim still depends on the carrier that moved the freight, and your own Chain of Responsibility duties stay with you (Chapter 7). Ask who the carrier is before you book.

## Chapter 3: How A Rate Card Works

A road express price is built from five parts, and you can check every one: the zone pair, the basic charge, the rate per kg, the minimum charge and the chargeable weight. The fuel levy and any surcharges go on top.

| Part | What it means | Where people get caught |
| --- | --- | --- |
| Zone pair | The price is set per origin zone and destination zone, not by distance | Two suburbs the same distance away can sit in different zones |
| Basic charge | A fixed amount per consignment | Splitting one delivery into several con notes pays it several times |
| Rate per kg | Charged on the chargeable weight | Compared alone, it hides the cubic factor |
| Minimum charge | The least a consignment can cost | Small items to a far zone often pay the minimum |
| Chargeable weight | The higher of dead weight and cubic weight, rounded up to the next kg | Bulky light freight is charged on its size |

Cubic weight is length × width × height in metres × the number of items × the carrier's cubic factor. Road express commonly uses 250 kg per cubic metre and air 167; your contract decides.

**Worked example (rates from the T06 sample, Sydney to Melbourne):** three cartons, each 60 × 40 × 40 cm and 12 kg.

| Step | Working | Result |
| --- | --- | --- |
| Dead weight | 3 × 12 kg | 36 kg |
| Cubic weight | 3 × 0.6 × 0.4 × 0.4 m × 250 | 72 kg |
| Chargeable weight | Higher of the two | 72 kg |
| Freight | $12.50 basic + 72 kg × $0.42 | $42.74 |
| Minimum check | Freight is above the $25.00 minimum | $42.74 |
| Fuel levy | $42.74 × 28.4% | $12.14 |
| Price before GST |  | $54.88 |
| GST | 10% | $5.49 |
| Total |  | $60.37 |

[[sketch B02 quarter]]

Half the charge here is for air: the cartons weigh 36 kg but are charged as 72. A carton sized to its contents, or packed on a pallet with other orders, is the cheapest freight saving most warehouses have.

Why the same box costs more to Perth than to Parramatta: Perth sits in a distant zone with a higher basic charge and rate per kg, and the freight crosses the Nullarbor by road or rail. Remote postcodes add a surcharge on top (Chapter 5).

**Tools:** T01 works out chargeable weight line by line and shows how much you pay for air. T06 turns your agreed rates into a one page price table by weight break. T02 compares carriers on your own freight, not their headline rates. T07 spreads freight across your orders, so you can see which orders lose money on delivery.

## Chapter 4: Fuel Levies

A fuel levy is a percentage added to the freight charge to cover diesel moving away from the price the rates were built on. It is legitimate, and it can also be the quietest price rise on the invoice.

How carriers set them: most publish a levy each month (some each week) on a fuel surcharge page, tied to a diesel price index. Levies differ by service, so one carrier can run several at once. In November 2026, Team Global Express listed three levies on its fuel surcharge page: 40.27%, 28.40% and 28.97%, depending on the service.

A fair levy moves with the fuel part of the carrier's cost, not the whole price:

```latex
\text{Levy} = \frac{\text{current diesel} - \text{base diesel}}{\text{base diesel}} \times \text{fuel share of cost}
```

If fuel is 38% of a carrier's cost and diesel rises from a 200 c/L base to 248.3 c/L, a fair levy is about 9.2%, not the 24% a levy that follows the pump would give (T10 shows the working).

How to check one:

1. Ask the carrier for the base diesel price and the fuel share behind its levy, in writing.
2. Each month, record its published levy beside the diesel price in **T03 Fuel levy tracker**.
3. Watch the ratchet test in T03: a levy that rises when diesel rises but never falls when diesel falls is a price rise, and a topic for your next rate review.
4. Check the levy on each invoice against the month of the con note date, not the invoice date (T04 does this).

If you engage owner drivers or small fleets directly, the Fair Work Commission's fuel cost recovery order (Road Transport Contractual Chain Order) applies again from 23 November 2026. Rates must be adjusted for fuel at least each calendar month, or you can pay an agreed fuel levy that is also adjusted at least monthly and that you have taken reasonable steps to make sure covers the extra cost. The obligations end once the weekly national average terminal gate price for diesel stays below $2.00 a litre for four weeks in a row.

&#91;embedded content: AIP national average retail diesel, yearly averages 2016 to 2025; 2026 point is the single week to 23 Aug 2026. Checked as at November 2026.\]

Diesel has stepped up rather than drifted: the 2022 jump never fully unwound, and the August 2026 week sat well above the trend line. Check the base diesel price behind every rate card against this chart. A base set in 2020 makes any levy look big, and a base set in 2022 makes it look small.

## Chapter 5: Surcharges And Extras

The rate card gets you to the base price. Surcharges are where a quote and an invoice drift apart. Most are fair charges for real extra work; the problem is that nobody told the carrier about the extra work at booking, so it turns up after the fact with no chance to avoid it.

| Surcharge | What triggers it | How to avoid or reduce it | What to check on the invoice |
| --- | --- | --- | --- |
| Tail lift | No dock or forklift at pickup or delivery | Tell the carrier at booking; ask the receiver whether they have a forklift | Was a tail lift truck actually sent? Was it booked? |
| Residential delivery | Delivery address is a home, not a business | Flag it at booking so it is quoted, not added | Address type on the con note |
| Heavy or awkward item | Single item over the carrier's handling limit, or needs two people | Palletise heavy items; check the carrier's single item limit before booking | Item weight on the con note matches what you sent |
| Oversize or overlength | Freight longer, wider or taller than the standard size for that service | Break down the load where you can; ask for an oversize rate in the rate card | Measured dimensions against your packing record |
| Dangerous goods | Any item classed as dangerous goods for transport | Declare it at booking with the right paperwork; undeclared DG is a safety and legal problem, not just a cost | DG declaration on the con note |
| Waiting time | Truck held past the free time at pickup or delivery | Have freight ready and paperwork done before the truck arrives; agree free time in writing | Arrival and departure times against the free time |
| Futile pickup or redelivery | Freight not ready, site closed, receiver refused or not home | Confirm ready times and receiver hours before booking | Was the failure actually on your side? |
| Time slot or booking fee | Receiver requires a booked delivery slot | Load the receiver's booking rules into your customer data once | Slot fee only on consignments that needed one |
| Hand unload | No pallet; cartons loaded loose | Palletise when volume makes it worth it | Was the freight really loose? |
| Remote or outer area | Delivery postcode outside the carrier's standard zones | Check the postcode against the carrier's zone list at quote time | Postcode zone on the invoice matches the zone list |
| Peak or seasonal | Busy periods such as the lead up to Christmas | Book early; ask for the dates and rates in writing before the peak | Charge falls inside the published dates |
| Tolls | Route uses toll roads (common with linehaul and metro trucks) | Agree whether tolls are included or passed through | Toll charges match the route; see T16 |

Three habits stop most surprise surcharges:

1. **Book with the full picture.** Weight, dimensions, address type, dock or no dock, DG, receiver hours. The booking checklist in Chapter 6 covers all of it.
2. **Get the list in writing.** Every surcharge the carrier can apply, with its price, should be in the rate card or its schedule. A surcharge that is not on the list should not be on the invoice.
3. **Track them by cause.** Log every surcharge in T04 against the reason. If waiting time keeps hitting one site, the fix is at that site, not in the carrier negotiation.

## Chapter 6: From Booking To Proof Of Delivery

Every consignment leaves a paper trail. If the trail is complete, a claim, a dispute or an audit takes minutes. If it has gaps, you pay whatever the carrier says.

### The Booking Checklist

| Give the carrier | Why it matters |
| --- | --- |
| Pickup and delivery addresses, with address type (business or home) | Sets the zone and any residential surcharge |
| Ready time, close time and receiver hours | Stops futile pickups and failed deliveries |
| Number of items, weight and dimensions of each | Sets the chargeable weight; disputes start here |
| Packaging type: carton, pallet, crate, loose | Decides the truck, handling and hand unload charges |
| Dock, forklift or tail lift needed at each end | Decides the truck that turns up |
| Dangerous goods: yes or no, with class and paperwork | Legal and safety requirement, not optional |
| Booking or time slot needed at delivery | Avoids a wasted trip and a redelivery fee |
| Pallet account details (CHEP, Loscam or plain pallets) | Pallets that go missing are billed to someone; make sure it is not you |
| Your reference: order or PO number | Lets you match the invoice to the order later (T04, T07) |
| Declared value and whether you want extra cover | Carrier liability is usually limited; see Chapter 8 |

### The Five Records To Keep

| Stage | Record | Who creates it | Keep it because |
| --- | --- | --- | --- |
| 1. Booking | Booking confirmation with the details above | You, confirmed by the carrier | It is the order the carrier agreed to |
| 2. Dispatch | Con note (consignment note) signed by the driver | You or the carrier's system | Proves what was handed over, how many items and in what condition |
| 3. Labels | One label per item, showing the con note number and "1 of 3" style item count | You | A missing item is traced by its label number |
| 4. Transit | Tracking scans | Carrier | Shows where it went missing or got delayed |
| 5. Delivery | Proof of delivery (POD): name, signature, date, time, photo if offered | Receiver and driver | Starts the claim clock; without it a lost item is your word against theirs |

### Making The POD Count

- Ask receivers to count items and look for damage **before** they sign. Damage noted on the POD is a claim; damage found next week is an argument.
- If the receiver cannot check (driver in a hurry, freight wrapped), they should sign as unchecked rather than sign it as received in good order.
- Pull PODs for every consignment over a set value, or every consignment to a new customer, within a day of delivery. Do not wait for the customer to complain.
- Store PODs with the order, not in the carrier portal only. Portals often keep history for a limited time.

### When The Tracking Goes Quiet

No scan for one business day past the expected delivery is the point to act. Ask the carrier for the last physical scan and depot, ask the receiver to check their dock, and log the date you raised it. Late raised enquiries are the most common reason lost freight claims stall.

## Chapter 7: Your Chain Of Responsibility Duties

Chain of Responsibility (CoR) means a truck that is overloaded, badly restrained or driven by a tired driver is not only the driver's problem. If your business sends, packs, loads, receives or schedules freight on a heavy vehicle, you are in the chain, and handing the job to a carrier does not hand over your duty.

The Heavy Vehicle National Law (HVNL) applies in every state and territory except Western Australia and the Northern Territory. WA has its own chain of responsibility rules under its road traffic laws; check the WA rules if you send freight there or from there.

### What The Law Asks Of You

- **The primary duty (HVNL section 26C):** do everything reasonably practicable to make sure your part of the transport activity is safe.
- **No pressure (section 26E):** you must not ask, direct or require a driver or another party, directly or indirectly, to do something that would break a speed, fatigue, mass, dimension, load restraint or vehicle standard rule.
- **No bad contracts (section 26F):** you must not make a contract or deal that would encourage or reward those breaches.
- **Executives (section 26D):** directors and managers must take due diligence steps to make sure the business meets its duty.

The top penalty for a Category 1 breach of the primary duty is $4,230,550 for a corporation, and for an individual $436,850, five years in jail, or both (NHVR penalty list for 1 August 2026 to 30 June 2027).

> ### Data Note
>
> Penalty amounts are indexed each 1 July. Recheck them against the NHVR schedule of penalties every year, on the dates in Part G, Chapter 3.

### Your Duties By Role

| Your role | Where it goes wrong | What reasonable steps look like |
| --- | --- | --- |
| Consignor (you send it) | Wrong weights on paperwork; freight not ready so the driver waits then rushes | Weigh or measure what you send; accurate weights on the con note; realistic ready times |
| Packer | Freight packed so it cannot be restrained; pallets overhanging or unstable | Packing standards for each product; stable, wrapped, square pallets; heavy at the bottom |
| Loading manager and loader | Overloaded axles; poor load placement; load not restrained | Check gross and axle mass before the truck leaves (T11 Axle load, T12 Trailer load planner); restraint checked before release (T13) |
| Consignee (you receive it) | Delivery windows nobody can meet legally; long queues that eat into driver hours | Booking windows that allow for legal driving; queue time measured and fixed |
| Scheduler | Delivery promises that only work if the driver speeds or skips rest | Transit times built from legal driving hours (T14), not from the customer's wish |
| Anyone who contracts carriers | Rates so low the carrier can only make money by cutting corners | Rates that cover a legal trip (T09 shows what a truck really costs per km); no reward for impossible speed |

### Six Questions To Ask Every Carrier

1. How do you manage fatigue and driver hours?
2. Are you NHVAS or Trucksafe accredited, or how else do you show your safety system?
3. How do you check mass and load restraint before departure?
4. What do you need from us so your drivers are never rushed at our dock?
5. Who do we call if one of your drivers raises a safety concern on our site?
6. When were your vehicles last maintenance checked, and can we see the records?

Record the answers. If something goes wrong, the question is what your business did to reduce the risk; a file with these answers and your follow up is part of that story. The subcontractor onboarding checklist (T27) works as a starting point for a shipper's version.

## Chapter 8: Invoice Audit And Claims

Freight invoices are built by systems from scans, measurements and codes. Each step can go wrong, and the errors rarely fall in your favour. Checking every line sounds like a lot of work until you see how few patterns cause most of the errors.

### What T04 Checks On Every Line

| Check | Common error it catches |
| --- | --- |
| Duplicate con note | The same consignment billed twice, often across two invoices |
| Chargeable weight | Charged weight higher than the greater of dead weight and cubic weight |
| Rate | Price does not match the agreed lane rate, basic charge or minimum |
| Fuel levy | Wrong levy percentage for the month, or levy charged on extras that should not carry it |
| Extras | A surcharge that is not on your agreed list, or charged at the wrong price |
| GST | GST on the wrong base, or on items that should not carry it |

Every line with a problem gets a reason and an amount to claim back. The Summary sheet totals the claim by carrier and by reason.

&#91;embedded content: Invoice audit loop, using T04 Freight invoice audit and T08 Carrier scorecard\]

The loop matters more than any single credit note. If one carrier's cubic measurements are wrong every month, a credit each month is a tax on your time. Show them the T08 trend and ask for the scanner at their depot to be checked.

### Making A Claim For Loss Or Damage

1. **Note it on the POD.** Damage or a short count noted at delivery is the strongest evidence you will have (Chapter 6).
2. **Tell the carrier in writing straight away.** Carrier terms set short notice periods for damage and loss. Read yours before you need them, and put the dates in your claims register.
3. **Keep the goods and the packaging.** Carriers often ask to inspect. Photos of the outer packaging, the damage and the label help.
4. **Send the claim pack:** con note, POD, photos, invoice for the goods (your cost, not the sale price unless the terms say otherwise), and repair or replacement quotes.
5. **Chase it on a date.** Put a follow up date in the register. T08 scores claims paid within 30 days for a reason.

### Know What The Carrier Will Actually Pay

Most carrier terms limit what they will pay for loss or damage, often to a set amount per consignment or per kilogram, unless you buy extra cover. Before you send high value freight:

- Read the liability clause in the carrier's terms and write the limit in your carrier file.
- Compare the carrier's extra cover with your own transit insurance. Your insurer may cover more for less, but check whether they need the carrier's liability preserved.
- Never sign away the carrier's liability on your own documents without checking with your insurer.

This is general information, not legal advice. For a large claim, or a disputed one, get advice before you sign any release.

## Chapter 9: Measuring Carrier Performance

Every carrier says its on time rate is in the high nineties. Yours might be, measured their way. Measure it your way, on your own freight, every month, and the quarterly review becomes a conversation about facts instead of feelings.

### The Six Measures In T08

| Measure | Default weight | Full marks at | Zero at | Where the number comes from |
| --- | --- | --- | --- | --- |
| On time delivery | 30 | 97% | 85% | Delivery date on the POD against the agreed transit time for the lane (T06) |
| Damage per 1,000 consignments | 20 | 1 | 8 | Your damage claims register |
| Claims paid within 30 days | 10 | 95% | 50% | Claims register: date lodged against date paid |
| Invoice accuracy (lines with no error) | 20 | 98% | 85% | T04 audit summary |
| Missed pickups per 1,000 bookings | 10 | 2 | 15 | Your dispatch log |
| POD within 24 hours | 10 | 98% | 80% | Date the POD reached you against the delivery date |

Each measure earns full marks at its target and drops in a straight line to zero at its floor. Weights add to 100, and every weight and target can be changed to suit your business. A score of 85 or more is green, 70 to 84 is amber, under 70 is red.

### Measure It Your Way

- **On time means against your agreed transit time,** not the carrier's own estimate on the day. A carrier that quietly adds a day to the estimate can show 99% on time while your customers wait.
- **In full counts too.** A delivery that arrives on time with one carton missing is not a success. If you track DIFOT (delivered in full, on time), use it in place of the on time measure.
- **Count per 1,000,** not raw numbers, so a large carrier and a small one compare fairly.
- **Use the same data source each month.** A change in how you measure looks like a change in performance.

### The Review Rhythm

| How often | What happens | Who |
| --- | --- | --- |
| Every invoice | T04 audit, disputes raised | Accounts or logistics |
| Monthly | T08 updated; any red measure gets a call to the carrier | Logistics lead |
| Quarterly | Review meeting with each main carrier: trend, causes, actions with owners and dates | Logistics lead and carrier account manager |
| Yearly, or after two red quarters | Rates tested against the market with T02; tender if needed | Logistics lead and finance |

A scorecard nobody acts on is just a report. The rule that makes it work: every red measure gets a cause and an action with a name and a date, and the next quarter shows whether it worked.

## Chapter 10: State By State Shipping Traps

Australia runs on one set of road rules for heavy vehicles, except where it does not. These are the differences that most often catch shippers out. Rules and prices change; each one below was checked in November 2026.

| Where | The trap | What to do |
| --- | --- | --- |
| Western Australia | Not under the Heavy Vehicle National Law. WA has its own chain of responsibility, mass and access rules, and its own permits | If you send freight into or out of WA, ask your carrier how they meet WA rules; do not assume your HVNL paperwork covers it |
| Northern Territory | Also outside the HVNL, with its own rules. Long distances, road trains and wet season closures in the north | Build realistic transit times; ask the carrier for its wet season plan before November |
| Victoria | Bigger combinations are tightly limited: A doubles only, and B triples by permit only | Do not plan a Victorian leg on the same vehicle type as a Queensland or NT leg without checking |
| Sydney | Truck tolls are roughly three times the car toll on most motorways. Trucks travelling through between the M1 and M2 must use NorthConnex, with a $215 fine for using Pennant Hills Road instead | Ask whether tolls are in the rate or passed through, and check them with T16 |
| Melbourne | CityLink caps each heavy vehicle trip: $38.32 by day for October to December 2026, less at night, and the caps change every quarter. EastLink charges trucks by toll zone, capped at $21.33 a trip until 30 June 2027 | Small, frequent metro deliveries can attract repeated tolls; check the route |
| Tasmania | Everything crosses Bass Strait, so there is a sea leg, a ferry or ship cut off time, and extra handling | Allow for the sailing schedule in transit times. Check whether your goods qualify for the Tasmanian Freight Equalisation Scheme |
| Interstate produce and plants | Biosecurity rules restrict fruit, vegetables, plants and soil entering some states and regions (WA, Tasmania and parts of SA are the strictest) | Check the destination state's entry conditions before you book; a load stopped at the border is not the carrier's fault |
| Remote and outer areas | Many carriers do not cover remote postcodes themselves and hand freight to an agent, adding days and cost | Check the postcode against the carrier's zone list at quote time; ask who does the last leg |
| Public holidays | Each state has its own public holidays, and some are local (show days, cup days) | Check holidays at both ends before promising a delivery date |

A practical habit: keep a one page lane sheet for each regular route, listing transit time, tolls, cut off times and any rule above that applies. T06 has a column for notes on each lane.

## Chapter 11: Receiving At Your Dock

Every consignment in this part ends at someone's dock. When that dock is yours, most of the book still applies, just from the other side: the booking, the records and the claims all run backwards. Three jobs belong to the receiver alone: running the dock bookings, checking the freight at the door, and deciding when to refuse it.

### Run The Dock On Bookings

A dock with no bookings works until three trucks arrive at once. Then drivers queue, their work hours burn while they wait, and the queue becomes your Chain of Responsibility problem as well as theirs (Chapter 7).

| Set | Why it matters |
| --- | --- |
| Slots by door and by time | Spreads arrivals across the day so no door is double booked |
| Slot length by load type | A pallet load and a loose loaded container take very different times; book each for what it is |
| Booking cut off | Gives you time to plan labour and floor space before the truck turns up |
| What happens when a truck is late or early | One clear rule, applied the same to every carrier, stops the arguments |
| Free time before waiting charges | Agree it in writing so waiting time charges (Chapter 5) are fair both ways |
| Who to call on the day | One name and number for carriers when they are running late |

Measure turnaround on every truck: arrival time, start of unload, departure. **T30 Dock booking and receiving log** keeps the bookings and the times in one place and shows which carriers and which suppliers wait longest. Long waits that keep coming back are a dock problem to fix, not a carrier problem to bill.

### The Check At The Door

Check before anyone signs, because the signature on the proof of delivery is where your claim rights start (Chapter 6).

[[sketch B06 third]]

1. **Count the items** against the con note and your order or advance shipping notice.
2. **Look at the outside:** crushed corners, torn wrap, wet cartons, broken pallets, tilted stacks.
3. **Check labels and references** match your order number.
4. **For containers,** check the seal number against the paperwork before you cut it, and photograph the doors before they open.
5. **For chilled or frozen freight,** check the temperature against your receiving rule.
6. **Write every problem on the proof of delivery,** with the count, before you sign. If there is no time to check, sign as unchecked.

### When To Refuse A Load

| Problem | Refuse? | What to do |
| --- | --- | --- |
| Goods you did not order, or not on the booking | Yes | Refuse at the door and tell the supplier the same day |
| Visible damage to some items | Usually accept the rest | Note the damaged items on the POD, photograph them, and start the claim (Chapter 8) |
| Load shifted or collapsed in the trailer | Do not unload until it is safe | Stop work, photograph it, and agree with the carrier how it will be made safe |
| Chilled or frozen freight outside its temperature range | Yes, if your food safety rule says so | Record the reading on the POD and tell the supplier straight away |
| Freight not packed or labelled to your supplier standard | Accept the first time, with a note | Send the supplier your standard and charge back repeat failures as your standard allows |

### Set A Supplier Delivery Standard

Most problems at the door start at the supplier's dispatch bay. A one page standard, sent with every new purchase order, fixes them at the source. Cover the pallet type and the largest height and weight you accept, how pallets must be wrapped, what goes on each label, when the advance shipping notice is due, how to book a slot, and what you charge back when the standard is not met. Keep it short enough that the supplier's forklift driver will actually read it.

## Chapter 12: Importing A Container

A container from overseas passes through more hands than any domestic consignment, and every one of them can send you a bill. The clock starts at the wharf, so knowing who does what before the ship arrives is how you avoid paying for days you did not need.

### Who Does What

| Party | What they do | What they can charge you for |
| --- | --- | --- |
| Overseas supplier | Packs and loads the container, and books the freight if the terms say so | The goods, plus freight if the price includes it |
| Freight forwarder | Arranges the sea freight and often the local delivery | Freight, handling and document fees |
| Shipping line | Owns or leases the container and carries it by sea | Sea freight, and detention if the empty comes back late |
| Stevedore | Runs the container terminal at the port | Storage once free days run out; access charges to the truck carrier, passed on to you |
| Customs broker | Lodges your import declaration and works out duty and GST | The broker's fee, plus the government charges it pays for you |
| Container carrier | Collects the box from the terminal on a booked time slot and delivers it | Cartage, side loader or drop trailer hire, waiting time |
| Empty container park | Takes the empty box back for the shipping line | Park fees, often charged through the carrier |
| Australian Border Force and the Department of Agriculture | Clear the goods for customs and biosecurity | Import processing charge, biosecurity charge, inspections if needed |

### The Path Of A Box

1. **Agree the terms** with your supplier, so both sides know who pays for what and where (Chapter 13).
2. **The ship sails.** Your broker lodges the import declaration before arrival, so it can be cleared quickly.
3. **The ship arrives** and the box is unloaded at the terminal. Free storage days start.
4. **Customs and biosecurity clear the goods,** or hold them for an inspection.
5. **Your carrier books a time slot** at the terminal, collects the box and delivers it to your dock, on a side loader or a drop trailer.
6. **You unpack it** within the free days for the container.
7. **The carrier returns the empty** to the park named on the shipping line's delivery order. The clock stops there, not when you finish unpacking.

> ### Data Note
>
> Free days are set by each shipping line and terminal, and the storage days and the container days are counted separately. Ask your forwarder for both before the ship sails, and diary the last free day of each.

[[sketch B07 half]]

### The Clock Starts At The Wharf

Two different charges run on two different clocks:

| Charge | Where the box is | Who charges it | Stops when |
| --- | --- | --- | --- |
| Storage (often called demurrage) | Full, at the terminal | Usually the stevedore | The full box leaves the terminal |
| Detention | Out of the terminal, full or empty | The shipping line | The empty box is returned to the named park |

Free days are short. One major shipping line's tariff for April 2026 gives 3 days of free wharf storage and 8 days of free container use on imports, then charges from about $116 a day for a 20 foot dry box, rising the longer you keep it. Check your own line's tariff when you book, and plan the unpack before the ship arrives.

### Charges That Land On You

| Charge | Who sets it | What to know |
| --- | --- | --- |
| Customs duty | The customs tariff | Many goods carry a 5% general rate, and many from free trade partners come in free. Your broker classifies the goods and checks the rate |
| GST on imports | The ATO, collected at the border | 10% of the value of the taxable importation: the customs value, plus duty, plus the international transport and insurance. Claimable as a credit if you are registered and the goods are for your business |
| Import processing charge | Australian Border Force | For an electronic declaration: $50 for goods over $1,000 and under $10,000, and $152 for $10,000 or more |
| Biosecurity charge | Department of Agriculture | $71 per full import declaration for sea cargo from 1 July 2026, plus inspection fees if the goods are directed for one |
| Terminal access charge | The stevedore, charged to the truck carrier | Passed on to you in the carrier's invoice. The ACCC reported $642 million collected in these charges in the 2024 to 2025 financial year |
| Cartage, side loader and waiting time | Your container carrier | Get a quote that lists every item, including the empty return |

Goods with a total value of $1,000 or less can come in without a full import declaration, but almost any container load is over that line.

**Pallets and containers do not match.** A standard Australian pallet is 1165 mm square, so a 20 foot container takes 10 of them on the floor and a 40 foot container takes 20. Many overseas suppliers load cartons loose to fill the box, which is cheaper to ship and much slower to unpack. Decide which you want before the order is placed, and book your dock and labour for it.

## Chapter 13: Landed Cost

The price on the supplier's invoice is not what an imported product costs you. Landed cost is everything it takes to get the goods onto your floor, divided by the number of units. It is the number your selling price has to beat.

```latex
\text{Landed cost per unit} = \frac{\text{goods} + \text{freight} + \text{insurance} + \text{duty} + \text{charges} + \text{local delivery}}{\text{units}}
```

GST is left out when you can claim it back. If you cannot, add it in.

### Who Pays For What

The sale terms decide which costs are already in the supplier's price. These are the common ones, from the Incoterms rules:

| Term | The supplier pays for | You pay for |
| --- | --- | --- |
| EXW (Ex Works) | The goods, ready at its own premises | Everything from its door to yours, including export clearance |
| FOB (Free on Board) | The goods, loaded onto the ship at the overseas port | Sea freight, insurance and everything in Australia |
| CIF (Cost, Insurance and Freight) | The goods, sea freight and basic insurance to the Australian port | Everything from the Australian port to your door |
| DDP (Delivered Duty Paid) | Everything to your door, including duty and GST | Unloading at your dock |

### Worked Example

One 20 foot container of 1,000 units bought FOB, with 5% duty. Freight, broker and delivery amounts are examples; put in your own quotes.

| Cost | Working | Amount |
| --- | --- | --- |
| Goods (FOB) | 1,000 units × $40.00 | $40,000 |
| Sea freight | Example quote | $3,000 |
| Insurance | Example quote | $200 |
| Customs duty | 5% of the $40,000 customs value | $2,000 |
| Import processing charge | Electronic, $10,000 or more | $152 |
| Biosecurity charge | Sea cargo | $71 |
| Customs broker | Example fee | $250 |
| Port, terminal and cartage | Example carrier quote | $900 |
| Unpack | Example labour | $300 |
| **Landed cost** | Before GST | **$46,873** |
| **Per unit** | $46,873 ÷ 1,000 | **$46.87** |

The goods cost $40.00 a unit at the overseas port and $46.87 on your floor: 17% more. The GST at the border is 10% of $45,200 (the $40,000 customs value, plus the $2,000 duty, plus the $3,200 freight and insurance), so $4,520. You pay it before the goods are released and claim it back on your next activity statement.

**T29 Landed cost calculator** does this for each shipment, splits the cost across mixed products by value or by volume, and shows how the landed cost per unit moves when the freight, the exchange rate or the duty rate changes.

## Chapter 14: Tools, Forms And The Monthly Routine

Every tool is an Excel workbook with yellow cells for your inputs, blue cells that do the working and orange cells for the answer. Every rate and limit can be edited, and each tool shows the date its figures were checked.

| Tool | Use it when | Chapter |
| --- | --- | --- |
| T01 Cubic and chargeable weight | Before you book, to see what you will be charged for and how much air you are paying to move | 3 |
| T02 Carrier rate comparer | Choosing or retendering carriers, using your own freight profile | 2, 9 |
| T03 Fuel levy tracker | Monthly, to log each carrier's levy against diesel and run the ratchet test | 4 |
| T04 Freight invoice audit | Every invoice, before you pay | 5, 8 |
| T05 Mode chooser | Freight that could go by road, rail, sea or air | 1 |
| T06 Lane cost and transit table | Turning agreed rates into a one page price and transit list for each lane | 3, 10 |
| T07 Freight cost per order | Pricing delivery to your customers, or checking which orders lose money on freight | 3 |
| T08 Carrier scorecard | Monthly scores and the quarterly review | 9 |
| T29 Landed cost calculator | Pricing an imported product, or checking a supplier quote against another | 12, 13 |
| T30 Dock booking and receiving log | Running dock bookings and measuring how long each truck waits | 11 |

### Forms In This Part

| Form | Where | What it does |
| --- | --- | --- |
| Booking checklist | Chapter 6 | Everything the carrier needs to quote and deliver without surprises |
| Five records to keep | Chapter 6 | The paper trail from booking to proof of delivery |
| Six questions for every carrier | Chapter 7 | Your Chain of Responsibility starting file |
| Claim pack | Chapter 8 | What to send so a claim is paid, not parked |
| Lane sheet | Chapter 10 | One page of traps and timings for each regular route |
| Check at the door | Chapter 11 | Six checks before anyone signs for freight |
| Supplier delivery standard | Chapter 11 | One page of rules for how suppliers pack, label and book |

### The Monthly Routine

| When | Job | Tool |
| --- | --- | --- |
| Every booking | Full details on the booking; check chargeable weight on anything bulky | T01 |
| Every invoice | Audit before payment; dispute wrong lines with evidence | T04 |
| First week of the month | Log each carrier's new fuel levy against diesel | T03 |
| First week of the month | Update the scorecard for last month; call about any red measure | T08 |
| Each quarter | Carrier review meetings; refresh lane prices and transit times | T06, T08 |
| Every import | Landed cost before the order is confirmed; unpack booked before the ship arrives | T29 |
| Every week | Review dock waiting times by carrier and supplier | T30 |
| Each year | Test rates against the market; check freight cost per order still works | T02, T07 |

About an hour a week keeps the whole system running for a business sending a few hundred consignments a month. The first month takes longer, while you load your rates and lanes.

### Sources

- [NHVR, Penalty and infringement amounts, 1 August 2026 to 30 June 2027](https://www.nhvr.gov.au/document/909)
- [Fair Work Ombudsman, Fuel cost recovery: road transport order](https://www.fairwork.gov.au/about-us/workplace-laws/fair-work-commission-orders/fuel-cost-recovery-road-transport-order)
- [Transport for NSW, Pennant Hills Road regulation](https://www.transport.nsw.gov.au/operations/roads-and-waterways/business-and-industry/heavy-vehicles/road-access/pennant-hills-road)
- [Linkt, CityLink toll pricing](https://www.linkt.com.au/using-toll-roads/about-toll-roads/citylink/toll-pricing/melbourne)
- [EastLink, Tolls from 1 July 2026 to 30 June 2027](https://www.eastlink.com.au/tolls)
- [Australian Border Force, Import declarations](https://www.abf.gov.au/importing-exporting-and-manufacturing/importing/how-to-import/import-declaration)
- [Australian Border Force, Import processing charges](https://www.abf.gov.au/importing-exporting-and-manufacturing/importing/cost-of-importing-goods/charges/import-processing-charge)
- [Australian Customs Notice 2026/23, Biosecurity cost recovery charge](https://www.abf.gov.au/help-and-support-subsite/CustomsNotices/2026-23.pdf)
- [Australian Taxation Office, GST and imported goods](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/international-transactions/gst-and-imported-goods/)
- [ACCC, Container stevedoring monitoring reports](https://www.accc.gov.au/about-us/publications/serial-publications/container-stevedoring-monitoring-reports)
- [Ocean Network Express Australia, Demurrage and detention tariff from 1 April 2026](https://au.one-line.com/)
- [International Chamber of Commerce, Incoterms rules](https://iccwbo.org/business-solutions/incoterms-rules/)
- [Singapore Post, Completion of the sale of Freight Management Holdings](https://www.singpost.com/)
- [Northline, Who we are](https://www.northline.com.au/)
- Carrier fuel surcharge pages and AIP terminal gate and retail diesel prices, checked November 2026

*Figures in this Part were checked in November 2026. Rates, levies, tolls and penalties change; check the source before you rely on a number.*
