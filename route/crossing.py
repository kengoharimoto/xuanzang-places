#!/usr/bin/env python3
"""The desert crossing, Guazhou to Yiwu (the Life only, T50:222c-224c): the Life's figures against Stein's surveyed
road (GJ 54, 1919; Serindia iii, 1921), straight lines between the proposed sites, and the Tang official figure.

Usage (from xuanzang-places/): python3 -I route/crossing.py  -> route/crossing_legs.tsv
Each leg: the Life's li (or days), the ground distance under each proposal, and km per li. Stein's miles are his road
(cyclometer) or map miles as he states them; straight lines are great-circle distances between the points below
(approximate where marked). The study's li elsewhere: about 0.24 km in a straight line, 0.29-0.32 by road (§1).
"""
import csv, math
MI = 1.609344
P = {   # lat, lon, source
    "kuachoucheng": (40.43, 95.82, "Stein's Kua-chou-ch'eng, S of An-hsi (approx.: 8 miles S of the road's Su-lo crossing, NW of it a 4-mile plain and An-hsi)"),
    "suoyang": (40.2463, 96.2051, "Suoyang cheng ruins (Wikipedia, WHC 1442)"),
    "shuangta": (40.55, 96.35, "Shuangta-bao, now under the Shuangta reservoir (approx., reservoir point)"),
    "anxi": (40.5176, 95.7812, "Guazhou (An-hsi) county town"),
    "hongliuyuan": (41.0646, 95.4211, "Hongliuyuan (Hung-liu-yüan), Stein's 2nd stage"),
    "malianjing": (41.56, 95.30, "Malianjing (Ma-lien-ching-tzu), Stein's 4th stage (approx., highway service area)"),
    "xingxingxia": (41.7957, 95.1316, "Xingxingxia (Hsing-hsing-hsia), Stein's 5th stage"),
    "yandun": (42.29, 94.0108, "Yandun (Yen-tun)"),
    "hami": (42.8174, 93.5142, "Hami"),
    "pichan": (42.8733, 90.2774, "Pichan (辟展), easternmost Turfan oasis"),
    "gaochang": (42.8551, 89.5284, "Gaochang ruins"),
}
def km(a, b):
    (la1, lo1, _), (la2, lo2, _) = P[a], P[b]
    p1, p2 = math.radians(la1), math.radians(la2); dl = math.radians(lo2 - lo1)
    return 6371 * math.acos(min(1, math.sin(p1) * math.sin(p2) + math.cos(p1) * math.cos(p2) * math.cos(dl)))
L = []
def leg(name, li, li_note, proposal, ground_km, kind, source):
    L.append({"leg": name, "li": li, "li_text": li_note, "proposal": proposal, "km": round(ground_km, 1), "kind": kind,
              "km_per_li": round(ground_km / li, 3) if li else "", "source": source})
# 1. Guazhou -> Hulu river (北行五十餘里)
leg("Guazhou -> Hulu river", 50, "從此北行五十餘里有瓠蘆河 (reported at Guazhou)", "Stein: Kua-chou-ch'eng -> old Su-lo bed",
    10 * MI, "map miles (8 to the present ford + 2)", "Stein 1919 p. 271")
leg("Guazhou -> Hulu river", 50, "same", "Suoyang cheng -> Shuangta-bao (pass on the Shule)", km("suoyang", "shuangta"),
    "straight line", "points above; Seng 2017 p. 1172 has c. 30 km")
leg("Guazhou -> Hulu river", 50, "same", "Suoyang cheng -> Shuangta-bao", 30, "as stated", "Seng 2017 p. 1172 (after Li Bingcheng)")
# 2. river -> first beacon (經八十餘里，見第一烽)
leg("crossing -> first beacon", 80, "經八十餘里，見第一烽", "Stein: old Su-lo bed -> Pei-tan-tzu", 16 * MI, "map miles", "Stein 1919 p. 271")
# 3. river -> fifth beacon (80 + 4 x 100: 各相去百里)
leg("river -> fifth beacon", 480, "80 + 4 × 100 (五烽…各相去百里)", "Stein: Su-lo -> Hsing-hsing-hsia", 96 * MI,
    "cyclometer, road", "Stein 1919 p. 275")
leg("river -> fifth beacon", 480, "same", "An-hsi -> Xingxingxia", km("anxi", "xingxingxia"), "straight line", "points above")
# 4. fourth beacon -> Wild Horse Spring (可於此去百里許，有野馬泉)
leg("fourth beacon -> Wild Horse Spring", 100, "去百里許，有野馬泉 (reported)", "Stein: a water stage c. 30 miles WNW of Ma-lien-ching-tzu",
    30 * MI, "map miles, straight", "Stein 1919 pp. 275-276")
# 5. the Moheyan, 800 li (長八百餘里)
leg("Moheyan desert", 800, "莫賀延磧，長八百餘里 (reported)", "Stein: Hsing-hsing-hsia -> Hami (218 - 96 - c. 2 miles An-hsi -> river)",
    (218 - 96 - 2) * MI, "road miles, derived", "Stein 1919 pp. 267, 275")
leg("Moheyan desert", 800, "same", "Stein: Hsing-hsing-hsia -> Chang-liu-shui (first verdure; c. 35 miles short of Hami)",
    (218 - 96 - 2 - 35) * MI, "road miles, derived", "Stein 1919 pp. 267, 275, 277")
leg("Moheyan desert", 800, "same", "Xingxingxia -> Hami", km("xingxingxia", "hami"), "straight line", "points above")
# 6. the whole crossing: the Life's sum against the Tang official figure
life_sum = 50 + 80 + 400 + 800
leg("Guazhou -> Yiwu (whole)", life_sum, "50 + 80 + 4 × 100 + 800 (the Life's reported and travelled figures summed)",
    "Stein: Kua-chou-ch'eng -> Hami by road (218 + c. 8)", 226 * MI, "road miles", "Stein 1919 pp. 267, 271")
leg("Guazhou -> Yiwu (whole)", 900, "伊州…東南取莫賀磧路至瓜州九百里 (Yuanhe junxian tuzhi 40, Tang official)",
    "Stein: Kua-chou-ch'eng -> Hami by road", 226 * MI, "road miles", "Yuanhe zhi (Siku ed., Wikisource); Stein 1919")
leg("Guazhou -> Yiwu (whole)", 900, "same", "Suoyang cheng -> Hami", km("suoyang", "hami"), "straight line", "points above")
leg("Guazhou -> Yiwu (whole)", life_sum, "the Life's sum", "Suoyang cheng -> Hami", km("suoyang", "hami"), "straight line", "points above")
# 7. days, not li
leg("Yiwu -> Baili (6 days, 涉南磧，經六日)", 0, "six days", "Hami -> Pichan", km("hami", "pichan"), "straight line; km per day = km/6",
    "points above")
leg("Baili -> Gaochang royal city (one night, with relays of horses)", 0, "sunset to cockcrow", "Pichan -> Gaochang",
    km("pichan", "gaochang"), "straight line", "points above")
w = csv.DictWriter(open("route/crossing_legs.tsv", "w", encoding="utf-8", newline=""), list(L[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(L)
for r in L: print(f'{r["leg"][:38]:38} {r["li"]:>5} li  {r["km"]:>6} km  {str(r["km_per_li"]):>6}  {r["proposal"][:60]}')
