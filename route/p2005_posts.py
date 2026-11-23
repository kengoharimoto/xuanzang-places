#!/usr/bin/env python3
"""The posts of the "Fifth Road" (第五道) from Guazhou to Yizhou in P.2005 (沙州都督府圖經), against the road surveyed by
Stein and against the Life's beacons.

Usage (from xuanzang-places/): python3 -I route/p2005_posts.py  -> route/p2005_posts.tsv
Text: Sun Yingying, "Manuscripts, Texts and Geographical Writings: A Study of Dunhuang Manuscript P.2005" (PhD,
University of Washington, 2017), ch. 5, pp. 140-143, her transcription with the manuscript's column numbers
(data/ref/lit/A/sun2017_p2005.txt, gitignored). Distances are from Shazhou (Dunhuang), in li and bu; 1 li = 300 bu.
Each post also gives the distance to its neighbours, so the figures check one another.
Checked on the manuscript (Gallica, Pelliot chinois 2005, btv1b8301563c, PDF pp. 10-11; data/ref/p2005/, gitignored):
Sun's text is right except Shuangquan's bu (MS 一百六十步, Sun 二百六十步), the Fifth post <-> Lengquan bu (MS 卌步 in
both entries, Sun 卅步) and Hutong's bu (MS 一百七十步, Sun 七十步). The editions are compared in route/p2005_editions.tsv. The figures below are the manuscript's; MS_ONLY marks where it differs from Sun.
"""
import csv, math, re
SUN = "data/ref/lit/A/sun2017_p2005.txt"
T = re.sub(r"\s+", "", open(SUN, encoding="utf-8").read())
def li(l, b=0): return l + b / 300
# post, distance from Shazhou as transcribed (li, bu), the manuscript's own neighbour figures, quote checked in Sun
POSTS = [
    ("階亭驛 Jieting", li(170), "在州東一百七十里，東去瓜州常樂驛/3卅里"),
    ("常樂驛 Changle (Guazhou)", li(200), "(from Jieting: 170 + 30)"),
    ("新井驛 Xinjing", li(227, 200), "在州東北二百卄七里二百步。瓜州常樂界"),
    ("廣顯驛 Guangxian", None, "新井驛廣顯驛烏山驛已上驛瓜州提 (no separate distance)"),
    ("烏山驛 Wushan", None, "南去瓜州常樂/5縣界烏山驛六十九里二百六十步 (from Shuangquan)"),
    ("雙泉驛 Shuangquan", li(477, 160), "在州東北四百七十七里 (MS_ONLY: 一百六十步; Sun 二百六十步)"),
    ("第五驛 Diwu (the Fifth post)", li(511, 40), "在州東北五百一十一里卌步"),
    ("冷泉驛 Lengquan", li(579, 170), "在州東北五百七十九里一百七十步"),
    ("胡桐驛 Hutong", li(663, 170), "在州東北六百六十三里 (MS_ONLY: 一百七十步, as Li Zhengyu; Sun 七十步)"),
    ("赤崖驛 Chiya (Yizhou, Rouyuan county border)", None, "北去伊州柔遠縣界赤崖驛八十里 (from Hutong)"),
]
NEIGH = [   # (from, to, li as the manuscript states it, quote)
    ("雙泉驛 Shuangquan", "烏山驛 Wushan", li(69, 260), "南去瓜州常樂/5縣界烏山驛六十九里二百六十步"),
    ("雙泉驛 Shuangquan", "第五驛 Diwu (the Fifth post)", li(60, 80), "北去/6第五驛六十里八十步"),
    ("第五驛 Diwu (the Fifth post)", "雙泉驛 Shuangquan", li(64, 80), "南去雙泉/10驛六十四里八十步"),
    ("第五驛 Diwu (the Fifth post)", "冷泉驛 Lengquan", li(68, 40), "北去冷泉驛六十八里 (MS_ONLY: 卌步; Sun 卅步)"),
    ("冷泉驛 Lengquan", "第五驛 Diwu (the Fifth post)", li(68, 40), "南去第/15五驛六十八里 (MS_ONLY: 卌步; Sun 卅步)"),
    ("冷泉驛 Lengquan", "胡桐驛 Hutong", li(84), "北去胡桐驛八十四里"),
    ("胡桐驛 Hutong", "赤崖驛 Chiya (Yizhou, Rouyuan county border)", li(80), "北去伊州柔遠縣界赤崖驛八十里"),
]
for q in [p[2] for p in POSTS if not p[2].startswith("(")] + [n[3] for n in NEIGH]:
    qq = re.sub(r"\s*\(.*\)$", "", q).replace("/", "")   # the bracketed MS_ONLY readings are checked on the scan, not in Sun
    qq = re.sub(r"\d+", "", qq)
    assert re.sub(r"\s+", "", qq) in T.replace("/", "").translate(str.maketrans("", "", "0123456789")), q
D = {p[0]: p[1] for p in POSTS}
# the check: each post's distance from Shazhou against its neighbour's plus the stated interval
print("internal check (li from Shazhou):")
print(f"  Diwu - 64 li 80 bu = {D['第五驛 Diwu (the Fifth post)'] - li(64, 80):.2f}, Diwu - 60 li 80 bu = {D['第五驛 Diwu (the Fifth post)'] - li(60, 80):.2f};"
      f" the manuscript has Shuangquan at {D['雙泉驛 Shuangquan']:.2f} (四百七十七里一百六十步): its own absolute figure is c. 30 li out")
print(f"  Diwu + 68 li 40 bu = {D['第五驛 Diwu (the Fifth post)'] + li(68, 40):.2f}; Hutong - 84 li = {D['胡桐驛 Hutong'] - 84:.2f}"
      f" = Lengquan in the manuscript {D['冷泉驛 Lengquan']:.2f} exactly; the Fifth post is 90 bu off")
print("  Shuangquan's 'north to Diwu 60 li 80 bu' and Diwu's 'south to Shuangquan 64 li 80 bu' are both in the manuscript")
C = dict(D)
C["雙泉驛 Shuangquan"] = li(446, 260)   # from the Fifth post and its 64 li 80 bu (the 60 li 80 bu reading gives 450 li 260 bu)
# Lengquan and Hutong as the manuscript gives them (they agree exactly)
C["烏山驛 Wushan"] = C["雙泉驛 Shuangquan"] - li(69, 260)
C["赤崖驛 Chiya (Yizhou, Rouyuan county border)"] = C["胡桐驛 Hutong"] + 80
# the road (Stein's stages), points as in route/crossing.py; straight lines; the road runs nearly straight
P = {"anxi": (40.5176, 95.7812), "hongliuyuan": (41.0646, 95.4211), "daquan": (41.2886, 95.1844), "malianjing": (41.56, 95.30),
     "xingxingxia": (41.7957, 95.1316), "shaquanzi": (41.8854, 94.8054), "yandun": (42.29, 94.0108),
     "chiya_li": (42 + 10/60 + 1.27/3600, 94 + 23/60 + 53.10/3600),   # Chiya post as located by Li Zhengyu (2006/2011, n. [14])
     "xinjing_li": (40.5570, 95.5998),
     "baidunzi": (40.8043, 95.5998)}   # Guangxian post: Li's 55 huali (27.5 km) N of Xinjing; Stein's Pei-tan-tzu c. 40.80, 95.60   # Xinjing post, Li's grid X16720.2 Y4494.7 (n. [1]), Gauss-Krueger zone 16 converted (data/coords_added.tsv)
def km(a, b):
    (a1, o1), (a2, o2) = P[a], P[b]; p1, p2 = map(math.radians, (a1, a2)); dl = math.radians(o2 - o1)
    return 6371 * math.acos(min(1, math.sin(p1) * math.sin(p2) + math.cos(p1) * math.cos(p2) * math.cos(dl)))
MI = 1.609344
# Stein: river -> Pei-tan-tzu 16 miles, river -> Xingxingxia 96 miles (cyclometer); Daquan -> Xingxingxia straight
baidunzi_daquan = (96 - 16) * MI - km("daquan", "malianjing") - km("malianjing", "xingxingxia")
rows = []
def leg(scheme, a, b, li_, ground, how):
    rows.append({"scheme": scheme, "from": a, "to": b, "li": round(li_, 2), "km": round(ground, 1), "km_per_li": round(ground / li_, 3), "ground": how})
W, S_, F, L, H, X = "烏山驛 Wushan", "雙泉驛 Shuangquan", "第五驛 Diwu (the Fifth post)", "冷泉驛 Lengquan", "胡桐驛 Hutong", "新井驛 Xinjing"
CH = "赤崖驛 Chiya (Yizhou, Rouyuan county border)"
# A: the posts on Stein's beacon stations (Li Zhengyu's equation of beacons and posts, on Stein's beacons)
leg("A: Xinjing = Pei-tan-tzu (Stein's first beacon)", X, W, C[W] - C[X], baidunzi_daquan, "Pei-tan-tzu -> Daquan: Stein's 80 cyclometer miles less the two straight stages after Daquan")
leg("A", W, S_, C[S_] - C[W], km("daquan", "malianjing"), "Daquan -> Malianjing")
leg("A", S_, F, C[F] - C[S_], km("malianjing", "xingxingxia"), "Malianjing -> Xingxingxia")
leg("A", F, L, C[L] - C[F], km("xingxingxia", "shaquanzi"), "Xingxingxia -> Shaquanzi")
leg("A", L, CH, C[CH] - C[L], km("shaquanzi", "yandun"), "Shaquanzi -> Yandun (if Chiya, the Yizhou border, is Yandun: a fit, not evidence)")
# B: the posts placed by P.2005's own distance from Shazhou: Xinjing 27.7 li beyond the Changle post, near the Shule;
#    this is Li Zhengyu's field identification (Xinjing N of Liugong, Wushan = Hongliuyuan, Shuangquan = Daquan,
#    the Fifth post = Malianjing, Lengquan = Xingxingxia, Hutong = Shaquanzi, Chiya at his coordinates)
leg("B: Xinjing near the Shule N of Changle (P.2005's own distances; Tosaki 2000)", X, W, C[W] - C[X], km("xinjing_li", "baidunzi") + km("baidunzi", "hongliuyuan"), "Xinjing as located by Li Zhengyu -> Baidunzi (Guangxian) -> Hongliuyuan")
leg("B", W, S_, C[S_] - C[W], km("hongliuyuan", "daquan"), "Hongliuyuan -> Daquan")
leg("B", S_, F, C[F] - C[S_], km("daquan", "malianjing"), "Daquan -> Malianjing")
leg("B", F, L, C[L] - C[F], km("malianjing", "xingxingxia"), "Malianjing -> Xingxingxia")
leg("B", L, CH, C[CH] - C[L], km("xingxingxia", "chiya_li"), "Xingxingxia -> Chiya as located by Li Zhengyu (94°23'53\"E, 42°10'01\"N)")
w = csv.DictWriter(open("route/p2005_posts.tsv", "w", encoding="utf-8", newline=""), list(rows[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(rows)
print("\ncorrected chain (li from Shazhou):", {k.split()[0]: round(v, 2) for k, v in C.items() if v})
for r in rows: print(f'{r["scheme"][:12]:12} {r["from"][:4]}->{r["to"][:4]} {r["li"]:>7} li {r["km"]:>6} km {r["km_per_li"]:>6}  {r["ground"]}')
for s in ("A", "B"):
    xs = [r for r in rows if r["scheme"].startswith(s)]
    print(s, "overall", round(sum(r["km"] for r in xs) / sum(r["li"] for r in xs), 3), "km per li; range",
          min(r["km_per_li"] for r in xs), "-", max(r["km_per_li"] for r in xs))
span = C[F] - C[X]
print(f"B: Chiya would lie {(C[CH] - C[L]) * 0.455:.0f} km beyond Xingxingxia (Kushui-Yandun stretch); Shazhou -> Xinjing {C[X]:.1f} li = {C[X] * 0.455:.0f} km at the posts' scale (Dunhuang -> An-hsi 104 km straight)")
print(f"\nXinjing -> Diwu (five posts) {span:.1f} official li; the Life's first -> fifth beacon 400 li: ratio {span/400:.2f}")
