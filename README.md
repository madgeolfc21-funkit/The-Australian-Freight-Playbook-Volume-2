# The Australian Freight Playbook · Volume 2

**Shipping, driving, running and growing a freight business in every state and territory.**

One free book for the three people every consignment depends on: the shipper who buys it, the driver who moves it and the operator who runs the trucks. Plain words, checked figures and 28 free Excel tools.

November 2026 edition · Review draft · Free to share with credit, not for sale (CC BY NC 4.0)

## Get the Book

📘 **[Download the PDF](The_Australian_Freight_Playbook_Volume_2_Review_Draft.pdf)** (97 pages, A4)

| Part | Title | Who it is for |
|---|---|---|
| A | Freight Basics | Everyone: the shared language, map and rules |
| B | The Shipper | The person who buys freight |
| C | The Driver | The person behind the wheel |
| D | The Operator | The business that runs the trucks |
| E | Growing the Business | From one truck to a 3PL |
| F | Rail, Air, Sea and Last Mile | The other modes, at working depth |
| G | Numbers and Tool Index | KPIs, the 28 tools, the update calendar and the gaps |

## The 28 Tools

Every tool is a standalone Excel workbook in the [tools](tools) folder. Rates sit in yellow cells you can edit, and every workbook shows the date its figures were checked. Open the **Start here** sheet first.

| Tool | Workbook | Part | For | What it answers |
|---|---|---|---|---|
| T01 | [Cubic and chargeable weight](tools/T01_Cubic_and_Chargeable_Weight.xlsx) | A | Shipper | What will I be charged on, and how much is air? |
| T02 | [Carrier rate comparer](tools/T02_Carrier_Rate_Comparer.xlsx) | B | Shipper | Which carrier is cheapest on my own freight? |
| T03 | [Fuel levy tracker](tools/T03_Fuel_Levy_Tracker.xlsx) | B | Shipper | Is each carrier's fuel levy fair, and does it fall when diesel falls? |
| T04 | [Freight invoice audit](tools/T04_Freight_Invoice_Audit.xlsx) | B | Shipper | What on this invoice is wrong, and what do I claim back? |
| T05 | [Mode chooser](tools/T05_Mode_Chooser.xlsx) | F | Shipper | Road, rail, air or sea for this shipment? |
| T06 | [Lane cost and transit table](tools/T06_Lane_Cost_and_Transit_Table.xlsx) | B | Shipper | What does each lane cost and take, by weight break? |
| T07 | [Freight cost per order](tools/T07_Freight_Cost_per_Order.xlsx) | B | Shipper | Which orders lose money on freight? |
| T08 | [Carrier scorecard](tools/T08_Carrier_Scorecard.xlsx) | B | Shipper | How is each carrier performing, out of 100? |
| T09 | [Truck cost per km](tools/T09_Truck_Cost_per_km.xlsx) | D | Operator | What does each km really cost? |
| T10 | [Rate card and quote builder](tools/T10_Rate_Card_and_Quote_Builder.xlsx) | D | Operator | What should I charge, and does the job make money? |
| T11 | [Axle load and pallet placement](tools/T11_Axle_Load_and_Pallet_Placement.xlsx) | D | Operator, driver | Is every axle group legal with this load? |
| T12 | [Trailer load planner](tools/T12_Trailer_Load_Planner.xlsx) | D | Operator, shipper | How many pallets fit, and does weight or space run out first? |
| T13 | [Load restraint lashings](tools/T13_Load_Restraint_Lashings.xlsx) | D | Driver, operator | How many lashings does this load need? |
| T14 | [Trip and hours planner](tools/T14_Trip_and_Hours_Planner.xlsx) | C | Driver | Does this trip fit the work and rest rules? |
| T15 | [Fuel and FTC estimator](tools/T15_Fuel_and_FTC_Estimator.xlsx) | D | Operator | What will fuel cost, and what can I claim back? |
| T16 | [Toll estimator](tools/T16_Toll_Estimator.xlsx) | D | Operator | What do the tolls cost on this run? |
| T17 | [Maintenance schedule](tools/T17_Maintenance_Schedule.xlsx) | D | Operator | What is due next, by km or date? |
| T18 | [Fleet utilisation](tools/T18_Fleet_Utilisation.xlsx) | D | Operator | Is each truck earning its keep? |
| T19 | [Lease, buy or hire](tools/T19_Lease_Buy_or_Hire.xlsx) | D | Operator | Which way to get the next truck? |
| T20 | [Owner driver or employee](tools/T20_Owner_Driver_or_Employee.xlsx) | E | Operator | Is this driver an employee or a contractor, and what does each cost? |
| T21 | [Road train trip planner](tools/T21_Road_Train_Trip_Planner.xlsx) | D | Operator, driver | Is this road train allowed on every leg, and where must it split? |
| T22 | [Emissions calculator](tools/T22_Emissions_Calculator.xlsx) | D, F | All | What are my Scope 1, 2 and 3 emissions? |
| T23 | [Growth stage readiness](tools/T23_Growth_Stage_Readiness.xlsx) | E | Operator | Am I ready for the next stage? |
| T24 | [First employee true cost](tools/T24_First_Employee_True_Cost.xlsx) | E | Operator | What does a driver really cost? |
| T25 | [SMS starter kit](tools/T25_SMS_Starter_Kit.xlsx) | D | Operator | Where do I start a safety management system? |
| T26 | [Driver daily pack](tools/T26_Driver_Daily_Pack.xlsx) | C | Driver | Pre start, defects and fitness check for today |
| T27 | [Subcontractor onboarding](tools/T27_Subcontractor_Onboarding.xlsx) | E | Operator | Is this subcontractor ready to run for me? |
| T28 | [Truck purchase checker](tools/T28_Truck_Purchase_Checker.xlsx) | E | Operator | Should I buy this truck? |

## Operator Forms Pack

[Volume2_Forms_Pack.xlsx](tools/Volume2_Forms_Pack.xlsx) holds three printable forms for Part D:

| Form | Use it |
|---|---|
| Load restraint sign off | Before every departure. Flags a load with too few lashings and blocks the sign off until every check is answered |
| CoR self audit | Once a year and after any serious incident. Scores your Chain of Responsibility controls across six areas |
| DG checklist | For every dangerous goods load, before loading and again before departure |

## Keeping It Current

Fuel, tolls, wages, fines and registration change on fixed dates. Part G, Chapter 3 has the update calendar: what changes, when, and which tools need their figures rechecked. Each tool has a **checked as at** date, so you can see at a glance which ones are due.

## How the Repository Is Laid Out

```
The_Australian_Freight_Playbook_Volume_2_Review_Draft.pdf   the finished book
tools/                                                      28 workbooks and the forms pack
source/md/                                                  the text of Parts A to G
source/img/                                                 the charts and flowcharts
source/template.html                                        page design and layout engine
source/build.py, source/render.js                           build scripts
```

### Rebuilding the PDF

You only need this if you change the text in `source/md`.

```
pip install markdown
pnpm add playwright
pnpm exec playwright install chromium
python3 source/build.py
node source/render.js
```

The layout engine keeps every table whole, never leaves a heading at the bottom of a page, and fills any leftover space with a notes panel or a part summary.

## Important

General guidance only, not legal, tax or financial advice. Rules differ by state and change often. Check the regulator for your exact situation before you act: the NHVR, your state road authority, the ATO and the Fair Work Ombudsman.

## Licence

The book and the tools are licensed under [Creative Commons Attribution NonCommercial 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Share and adapt them freely with credit; do not sell them. The Inter font in `source/fonts` is under the SIL Open Font License (see `source/fonts/OFL.txt`).
