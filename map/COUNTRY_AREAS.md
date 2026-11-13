# How the country areas are drawn

The map's "Country areas" layer gives each country an approximate extent, built from the circuit Xuanzang states for
it (國周N里). This file explains each step, the numbers used, and what the result can and cannot show. Kapiśa is worked
through in full in the second half. The code is `scripts/country_areas.py`. Its output is `data/country_areas.tsv`
(one row per country, with every figure below) and `map/country_areas.json` (the outlines on the map).

**What the areas are not.** They are not historical borders. They turn a stated size into a shape around the study's
point for the capital, using only the borders the text names and the lie of the land. The capital need not have been
central. Rivers have moved since the 7th century. The circuits are rounded figures. And the scale of the li varies
(see step 2).

## The method, step by step

### 1. The circuit

The script reads the circuit from the country's passage in the Xiyu ji:
- **Which figure:** the first 周N里 before the capital is described (國大都城…). Failing that, the first one that is
  not a city's (城周N里).
- **Ranges** such as 四五千 ("four or five thousand") take the mean.
- **"Over" and "less than":** 餘 ("over") is ignored, and 減 ("less than") takes 0.9 of the figure.
- **Breadth and length instead of a circuit:** Bāmiyān and Khwārazm give 東西X里，南北Y里. These are taken as an
  ellipse X by Y li.
- **No figure:** 14 countries have no circuit and are not drawn. They are the six hearsay countries of SE Asia,
  Rāmagrāma and Kuśinagara ("deserted"), Laṅgala, Fulin, the Women's country, 稽疆那, Nārikela and Wakhan.

### 2. The scale of the li

The circuit is converted to kilometres at the median straight-line km per li of the route legs in the country's own
juan (`route/li_regions.tsv`). A juan without a figure takes 0.24 km. Using the juan's own li means that where
Xuanzang's distances run long, as in the Deccan, his circuits are scaled down to match.

### 3. The target area

The target is the area of a region whose perimeter equals the circuit and whose compactness is 0.75 of a circle's:
A = 0.75 × P² / 4π. A true circle (1.0) would assume perfectly round countries. 0.75 allows for ordinary irregular
outlines.

### 4. Growing the countries

The area is grown on a 0.08° grid of land cells:
- **Start:** each country starts from the study's point for its capital (`data/study_view.tsv`). All the countries grow
  at once, cell by cell, nearest cells first.
- **Who takes a cell:** the country that reaches it first.
- **When growth stops:** when the country reaches its target area or 1.6 times the radius of a circle of that area
  (the "cap"). The sea also stops it.

So neighbours that press on each other meet roughly half-way, and a country with room becomes roughly round. A country
drawn at less than 98% of its target is marked "hemmed in by neighbours, the sea or the radius cap". 130 countries are
drawn: 80 at full size and 50 hemmed in.

### 5. Rivers named as borders

`data/country_borders.tsv` (curated) lists ten river borders of nine countries, such as 東臨信度河 ("on the east it
borders the Indus"). Phrases about the capital city (國大都城西臨…) describe the city, not the country, and are left
out.

How a named river works:
- **Course:** taken from Natural Earth's 1:10m river centrelines and widened by one cell.
- **No crossing:** the country may not cross the river. Beyond the river's ends its line is carried on straight, so
  the country cannot go round it.
- **Pull towards the river:** the country grows more readily towards the named side. A step in that direction counts
  for as little as 0.6 of its length. So the country reaches the river wherever its area allows.
- **Only the named country:** the river does not bind the neighbour on the other side.

Each river border is checked: does the river actually lie on the named side of the capital? One check fails: Śatadru's
西臨大河 (note on 04.05).

### 6. Mountains named as borders

The same table has 13 mountain borders, of two kinds. Both rest on a test for **high ground**: ground standing a set
rise above the capital's valley floor. The valley floor is the lowest of the 3×3 cells around the capital, since a
single cell's mean height can take in the valley sides.

The rise is set by region, at roughly half the relief between the valley floors and the heights around them:

| Region | Rise | Countries |
|---|---|---|
| Tian Shan and Ferghana | 1000 m | Agni, Ferghana |
| Oxus and Hindu Kush | 1200 m | Khuttal, Kapiśa, Lampāka, Nagarahāra |
| Western Himalaya | 1500 m | Kashmir, Kulūta, Srughna, Brahmapura |
| Central India | 250 m | Kosala |
| Any other country | 1500 m | none at present |

Heights come from the AWS terrain tiles. The coarse grid is built from zoom-5 tiles; the drainage basins use a 0.01°
grid built from zoom-8 tiles (`scripts/terrain_grid.py`).

**(a) A range on one side.** These are 北背雪山 ("backed by the snow mountains on the north"), 北背大山 and 東接葱嶺.
- **The border:** the range's crest. On that side, the near foot of the range is the first high ground; the crest is
  the highest ground within 60 km beyond the foot.
- **What the country may take:** the near slope up to the crest, and nothing beyond it.
- **Exception:** a range on one side never cuts into the country's own drainage basin (see b).

**(b) Mountains all round.** These are 山周四境 (Ferghana, Nagarahāra, Kulūta, Brahmapura), 四境負山 (Kashmir), 四面據山
(Agni), 山嶺周境 (Kosala) and 三陲黑嶺 (Kapiśa, Lampāka). They are read as a border at the crest of the ring, so the
country is given its river's drainage basin up to the watershed:
- **Drainage:** every land cell is given one downhill neighbour by Priority-Flood, run from the sea and the grid's edge.
  This fills pits and gives flat ground a direction. A cell's basin is everything that drains to it.
- **Where the basin is measured from:** not the capital, which may stand above a confluence, but the gorge by which
  the river leaves the ring. Each gorge is chosen by hand and snapped to the modelled channel below the capital:

  | Country | Gorge |
  |---|---|
  | Agni | Tiemenguan above Korla |
  | Ferghana | the Farhad narrows at Bekabad |
  | Kapiśa | the Panjshir's lower gorge above the Kabul river |
  | Lampāka | the Alingar's mouth |
  | Nagarahāra | Dakka |
  | Kashmir | Baramulla |
  | Kulūta | Larji |
  | Brahmapura | Kalagarh on the Ramganga |
  | Kosala | the Mahanadi's exit from Chhattisgarh |

- **Finer grid:** the basins are computed on the 0.01° grid. A 0.08° cell counts as basin when half of it lies in the
  basin. Every channel passes within 0.6 of a 0.08° cell of its gorge.
- **Limits:** the basin stops at another country's capital, so a nested basin stays its own country's (Kapiśa's
  inside Nagarahāra's Kabul river). It is cut at the 1.6-radius cap.
- **Effect on growth:** the basin is closed to every neighbour. Outside the basin, the country may not climb high
  ground, but it may take low ground.

Each mountain border is checked too: high ground must actually be met. For mountains all round, the check counts how
many of 16 directions meet high ground. All eleven countries pass.

### 7. Outlines

The grid cells each country owns are traced into rings, simplified (Douglas–Peucker, 0.75 cell) and smoothed (three
rounds of Chaikin). Detached slivers under 400 km², or under 3% of the area, are dropped, and so are pinholes.

## Kapiśa (01.38)

### The text

> 迦畢試國，周四千餘里，北背雪山，三陲黑嶺。國大都城周十餘里。

"Kapiśa is over 4000 li in circuit. On the north it is backed by the Snow Mountains, and on its three other borders are
the Black Ranges. The great capital of the country is over 10 li round."

Xuanzang reached it from Bāmiyān by "entering the Snow Mountains and crossing the Black Range" (東行入雪山，踰越黑嶺).

### Identification

**The country.** All the authorities centre Kapiśa on the plain where the Panjshir and Ghorband rivers meet, north of
Kabul. They differ on its extent:
- **Mizutani:** the basin at the Panjshir–Ghorband confluence near Charikar, c. 72 km NE of Kabul.
- **Cunningham (pp. 21–24):** Kapisene = all Kafiristan plus the Ghorband and Panjshir valleys. Watters follows him.
- **Vivien de Saint-Martin (p. 298):** the Nijrao and Panjshir districts.
- **Kuwayama 1993 (p. 427):** separates two things. The country Xuanzang describes is the limited area round Begram,
  east of Charikar. The dominion of its Khingal king was far larger: it reached Kabul in the south, Gandhāra and the
  west bank of the Indus in the east, and Bannu in the south-east.
- **Kuwayama's thesis (1990):**
  - **Extent:** one long north–south basin from the Hindu Kush, including the Kabul basin (p. 927). This sits uneasily
    with his own southern border for it at the Khair Khana pass (pp. 1262–66).
  - **Dependencies in 629:** Lampāka, Nagarahāra, Gandhāra and Varṇu.
  - **Sui and Tang names:** the Sui's 漕國 was Kapiśa. Under the Tang it became the 修鮮都督府 (658/661).

How far south the country reached is therefore open. The study's point for the country is 35.00 N, 69.25 E, on the
Begram–Charikar plain. The study counts Kapiśa as **secure**.

**The capital (01.38a).** The capital is identified as Begram (Bāgh-i ʿĀlam), 35.00 N, 69.28 E, on the terrace south
of the Panjshir. Foucher identified it after his visit of 1923. The decisive point is the hostage monastery 3 li east
of the city (01.38.01, on Koh-i Pahlavān). Mizutani and Ji Xianlin follow him, and the French excavations (from
1927) found the Kushan city there.

The older authorities each chose a different site:
- Cunningham: Opian, at the north end of the Koh-daman (he put Begram's ruins at another of Xuanzang's places).
- Beal and Dey: Kushan.
- Vivien: round Nijrao or in the Tagao valley.

The one rival argued from excavation is Ghirshman's Gunde Paisa, c. 5 km south-east of Begram (1946). It rested on his
early end for the last level at Begram (Begram III). Kuwayama answers it in two ways:
- **From the text:** the 舊王伽藍 stands "north-west of the royal city, on the south bank of the great river", with no
  distance given. So the city stood close to the Panjshir's south bank, which fits Begram and not Gunde Paisa.
- **From the archaeology:** he dates Begram III by its round bastions and stamped pottery to the 7th century, so the
  city Xuanzang saw is Begram's top level.

When Ghirshman ended Begram III is still open: Kuwayama reports his date three different ways, and only Ghirshman 1946,
p. 41, can settle it.

### How the area is drawn

**The figures:**

| | |
|---|---|
| Circuit | 4000 li (餘 ignored) |
| Scale | 0.297 km per li (juan 1) |
| Perimeter | 1188 km |
| Target area | 84,233 km² |
| Radius of that area | 164 km |
| Cap (1.6 × radius) | 262 km |
| Capital's valley floor | 1456 m |
| High ground (+1200 m) | 2656 m and above |

**The borders used** (`data/country_borders.tsv`):
- **三陲黑嶺 is read as mountains all round.** The Snow Mountains close the north and the Black Ranges the other three
  sides. High ground is met in 15 of 16 directions.
- **北背雪山 is also entered as a range on the north.** It bars ground beyond the Hindu Kush crest, but not inside
  Kapiśa's own basin.

**The gorge.** The basin is taken above the Panjshir's lower gorge, at 34.68 N, 69.64 E, just above the Panjshir's
junction with the Kabul river near Naghlu. On the 0.01° grid the outlet lies at 34.685 N, 69.605 E, 0.4 of a 0.08°
cell from that point.

The basin includes:
- the Ghorband valley up to the Shibar pass, with Fondukistan;
- the Salang valley;
- the Panjshir up to its head below the Khawak and Anjuman passes;
- Nijrab;
- the Koh-daman (Istalif, Shakardara, Sarai Khwaja) south to the Khair Khana pass.

It stops at Vṛjisthāna's point at Kabul (12.02). Because Mizutani places that country at Kabul, the basin cannot
include the Kabul river above the city.

**The result.**

| | km² | Share of target |
|---|---|---|
| Basin (0.08° cells) | 12,598 | |
| Drawn | 12,728 | 15% |
| of which basin | 12,533 | |
| of which low ground just outside the basin | 195 | |

One basin cell was taken first by Vṛjisthāna. The country fills its basin and gets little more. Beyond the watershed
lies high ground, which it may not climb, or ground that its neighbours reached first or hold as closed basins.

**The neighbours:**
- **Andarāb (12.03):** the Salang pass and the north side of the Khawak.
- **Bāmiyān (01.37):** the Hajigak.
- **Vṛjisthāna (12.02):** Kabul, Paghman, Maidan Shahr and the Logar.
- **Lampāka (02.02):** Laghman.
- **No country:** the Tagab valley and Sarobi are drawn by none. They lie in Nagarahāra's closed basin above Dakka,
  but beyond the point where Nagarahāra had reached its own area.

**Why only 15%.** The circuit is 1.8 times the basin's perimeter, measured on the cell outline and corrected by π/4
for the stair-steps. Other mountain countries show the same gap, while countries in open basins fit:

| Country | Circuit ÷ basin perimeter |
|---|---|
| Kashmir | 2.4 |
| Kulūta | 2.6 |
| Brahmapura | 3.5 |
| Ferghana | 0.8 |
| Lampāka | 0.9 |
| Kosala | 1.2 |

So the shortfall is the common one of Himalayan and Hindu Kush circuits. Either the li ran long on mountain roads, as
the route legs show elsewhere, or the circuit took in hill country beyond the basin, which for Kapiśa would most
naturally be the Kabul basin (Kuwayama 1990, p. 927). Both readings are left open.

### A known fault: about 1,300 km² east of Kabul

On the 0.01° grid the Kabul river's gorge below the city (Tang-i Gharu) is closed: the narrow canyon is lost at that
resolution. As a result:
- **The modelled flow runs north:** in the model, the Kabul plain drains north over the low saddle at Khair Khana into
  the Koh-daman, and so into the Panjshir above Kapiśa's gorge.
- **What this adds to Kapiśa:** about 1,290 km² of ground that really drains east down the Kabul river: the river
  below the city (Pul-i Charkhi), Butkhak, Khurd Kabul and Deh Sabz, south to about 34.15 N.
- **Why it isn't larger:** Vṛjisthāna's point at Kabul cuts the modelled basin at the city, so everything upstream of
  Kabul (the Logar, Paghman, the upper Kabul river) is unaffected.

Kapiśa's true basin above the gorge is therefore nearer 11,300 km², 13% of the target, and its circuit about 1.9 times
the basin's perimeter. The fix is to burn the Natural Earth river courses into the fine grid before the drainage is
computed, so that gorges lost at that resolution stay open. That would have to be checked in all nine basins.
