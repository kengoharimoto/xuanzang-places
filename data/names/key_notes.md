# Xuanzang's transcription key (T2087): notes

Files: `align.tsv` (alignments; edit it and rerun `python3 build_key.py data/names`), `key.tsv` (one row per character), `key_charnotes.txt` (the per-character notes merged into `key.tsv`).

**Training set.** 262 Indic names are counted in the key:
- **Place names from `secure.tsv`:** 138 (116 sure, 22 probable).
- **Words glossed in the text:** 124 personal names and terms (ids `G.nnn`, 117 sure, 7 probable). Their Sanskrit is fixed by Xuanzang's own 唐言 gloss or by a 舊曰…訛 correction.

**Not counted.** 28 Iranian, Turkic, Tocharian and Tibetan names are aligned but kept out of the key (see the last section). Also left out: 2 "circular" forms that were reconstructed from the Chinese (04.01.x4, x5), 1 unsure form (11.23.02) and 1 duplicate.

**Secure entries without alignment.** The other secure.tsv entries are Chinese translations with no transcription (e.g. 戰主, 福地, the `x` sites), duplicates (11.15, 04.09.03, 08.05.01a, 09.02.17), or originals that are unknown or disputed (01.18, 01.38.03, 03.01.07, 03.01.14, 11.13, 12.22.06).

**Alignment convention.** The segments partition the Indic form.
- A consonant-only segment (`呾=t`, `室=ś`) means the character renders the first member of a cluster.
- `x(n)` means the character's nasal coda only anticipates the next onset (三=sa(m) 摩=ma = *sama*).
- `r(pre)` marks 曷 written before an initial r-.
- Counts below are tokens in the counted set.

## 1. Initials: one MC initial for each Indic consonant class

Onsets are almost entirely regular when they are checked against the Guangyun readings in `mc.tsv`:

| Indic | MC initial | regular | exceptions |
|---|---|---|---|
| k / kh / g, gh | 見 k / 溪 kʰ / 羣 g | 66/68, 2/3, 45/46 | 伽=ka (bhāviveka), 貨=khā (tukhāra, 曉 x-, Iranian style), 御=go (疑) |
| c / ch / j | 章 / 昌 / 常 | 13/13, 3/3*, 23/24 | *呫 is 透 in Guangyun but glossed 昌葉反 by XZ; 珠=jyo (章) |
| ṭ / ṭh / ḍ, ḍh / ṇ | 知 / 徹 / 澄 / 孃 | 12/12, 2/2, 5/6, 9/14 | ḍ→羅 l- (local Hidda); 那=ṇa ×3, 諾=ṇa, 穰=ṇya |
| t / th / d, dh / n | 端 / 透 / 定 / 泥 | 79/79, 8/8, 69/69, 47/52 | 尼, 你 (孃) and 若 (日) for n |
| p / b, bh / v / m | 幫 / 並 / 並 / 明 | 59/61, 31/32, 73/75, 62/62 | 婆=pa, 裒=pau; 弗 p- for v in vṛ- ×2; 彌 m- for -mb- |
| y / r / l / ṛ | 以 / 來 / 來 / 來 | 22/22, 126/126, 57/58, 5/5 | |
| ś / ṣ / s / h | 書 / 生 / 心 / 曉 | 49/49, 13/13, 49/49, 25/29 | 匣 for h in 怙 hu ×2 and 曷 |
| kṣ | 初 tʂʰ | 6/6 | 叉, 差, 刹, 芻 |

- **Retroflex vs dental.** He keeps them apart through the 知/徹/澄/孃 initials: 吒 胝 知 磔 for ṭ, 侘 for ṭh, 荼 擇 仗 for ḍ/ḍh, and 拏 痆 for ṇ. 拏 is ṇ 7 times out of 7. 那, however, also serves ṇ (3 of 39), so 那 does not prove a dental n.
- **Aspirates.** Voiceless aspirates are marked (他 菟 鐵 儻 th, 佉 kh, 侘 ṭh, 闡 ch). Voiced aspirates are not, because MC had only one voiced series: 陀 is da 11 and dha 6, 伽 is ga and gha, 婆 and 跋 are b, bh and v. A gh/dh/bh in a reconstruction therefore can never be confirmed or refuted from the initial.
- **Sibilants.** These are perfectly separated: ś is 書 (49/49), ṣ is 生 (13/13), s is 心 (49/49).
- **v and b.** These are not separated. v is 伐 (25), 婆 (16 as va), 縛, 毘 vi and 吠 ve/vai. b and bh use the same characters.
- **r and l.** These are not separated. 羅 is ra 60 : la 33, 邏 is ra 14 : lā 4, and 剌 is r/ra/la. 羅 and 邏 are interchangeable (補羅 and 補邏 both render -pura).

## 2. Vowels

- **Vowel length is never marked.** The same characters render a and ā (歌 rhyme, e.g. 那 na 31 / nā 5), i and ī (脂/支/之), and u and ū (模/虞).
- **Vowel quality is rendered.** He uses:
  - 齊 for e: 提 de, 泥 ne, 醯 he, 犀 se, 鞮 te, 迷 me, 稽 ke, 第 de, 低 te.
  - 模/虞 for o: 瞿 go, 拘 ko, 布 po, 盧 ro, 踰 yo.
  - 祭/廢/灰 for ai: 勢 śai, 吠 vai, 梅 mai.
  - u-diphthong rhymes for au: 喬 gau, 憍 kau, 裒 pau.
  - However, e and ai overlap: 吠 is ve 3 / vai 2, and the 齊 characters also give i (醯 hi, 泥 ni).
- **ṛ** is written 栗 or 利 (ri/li) or 𩜁 (ṛṅ).
- **Final vowels and syllables are sometimes dropped:** nagarahār(a), nārāyaṇ(a) (延), lampa(-ka), kalanda(-ka), sātavāha(-na), and -varma(n) as 伐摩.

## 3. Clusters and codas (entering tones)

- **Closed characters for clusters.** 90 tokens render a bare consonant, and 72 of them use entering-tone (-p/-t/-k) characters. The usual pattern is a closed character for C1 followed by an open character for C2+V:
  - 呾 t-r ×13, 濕 ś ×9, 剌 r ×8, 室 ś ×7, 鉢 p-r ×6.
  - 窣, 悉, 薩 for s-; 色, 瑟, 澁 for ṣ-; 姞 and 訖 for g-/k- before r.
- **ś-clusters.** 室 is used only before r/ṛ (7/7: 室羅, 室利, 室縷, 室𩜁). 濕 is used only before v/m (9/9: 濕伐, 濕吠, 濕縛, 濕婆, 濕彌).
- **The cluster character takes the next vowel.** For s- and stop+r clusters, the vowel of the C1 character copies the vowel that follows:
  - 窣 (u) before u: 窣堵 stū, 伐窣堵 vastu, 窣祿 sru.
  - 悉 (i) before i: 悉底 stī, 悉鐵 sthi.
  - 薩 (a) before a: 薩他 sthā, 薩儻 sthā, 薩旦 stan.
  - Similarly 咄路 tru, 杜魯 dhru, 圖盧 dru, 姞栗 gṛ and 訖利 krī.
  - The rule fails for ś: 室 is used before rā, and 濕 before va.
- **Codas that render a real consonant.** The -t coda renders r before a consonant (伐 var, 達 dhar, 薩 sar, 鉢 par, 弗 pūr, 曷 hār), as well as d/t/ṭ (遏 ad, 佛 bud, 達 dat, 剌 raṭ). The -k coda renders k (屈 kuk, 磔 ṭak, 絡 rak, 僕 bhuk), and -k also appears before bj (鞠 kub). Closed C1 characters also take a pre-labial -p (答 tap-ta, 吸 h-m, 澁 ṣ-p, 葉 śya-p).
- **Codas that render nothing.** A coda that only anticipates the next onset adds no sound: 劫比 is *kapi*, 納縛 *nava*, 卑鉢羅 *pippala*.
- **Gemination is usually not marked** (蘇達多 *sudatta*, 鄔闍衍那 *ujjayana*), but a closed character can show it (屈屈吒 *kukkuṭa*, 鉢呾羅 *pattra*).
- **Final -t is written in full** with 多 (鉢邏犀那恃多 *prasenajit*), but is dropped in 阿濕婆恃 *aśvajit*.
- **Initial r-** takes the prefix 曷 in 5 cases (曷邏怙羅, 曷邏闍補羅, 曷羅闍姞利呬, 曷邏闍伐彈那; Iranian 曷邏胡). The prefix is absent in 羅怙羅 (the personal name), 盧醯呾迦, 絡多末知 and 藍摩. 曷 also renders ha(r) and a(r), so 曷 counts as **r** only at the start of a word before 邏/羅/剌.

## 4. Nasals and anusvāra

- **The nasal coda follows Chinese place of articulation:**
  - -ŋ before velars and h: 殑 gaṅ, 恭 koṅ, 𩜁 liṅ, 浪 laṅ, 賞 śāṅ, 僧 siṃ/saṃ before h/gh, 亘 haṃ, 鴦 aṅ/aṃ.
  - -n before dentals and ś: 信, 健, 案, 難, 蘭, 鄰, 畔, 戰, 爛 laṃdh, 頻 viṃś.
  - -m before labials: 濫 lamp, 瞻 camp, 贍 jamb.
- **Anusvāra is not distinguished from a homorganic nasal.**
- **Echo codas.** A nasal coda in front of a nasal onset only echoes it:
  - 三摩, 藍摩, 閻摩, 耽摩 render single m.
  - 衍那, 繕那, 旦那, 愼那, 彈那, 商諾, 奔穰 render single n/ṇ.
  - Do not reconstruct -mm-/-nn- from such pairs (cf. targets 奔那伐彈那, 屈浪拏).

## 5. Recurring elements (stock spellings)

| Element | Spelling (count) |
|---|---|
| -pura | 補羅 ×8 / 補邏 ×1 / 布邏 ×1 |
| -nagara | 那揭羅 ×2 |
| -giri | 祇釐 ×2 / 耆釐 ×1 |
| -vatī | 伐底 ×2 (-pati 鉢底 ×2) |
| -śaila | 勢羅 ×4 |
| -vana | 伐那 ×3 |
| -deva | 提婆 ×8 |
| -sena | 犀那 ×5 (incl. prasena-) |
| -gupta | 毱多 ×4 |
| -putra | 弗呾羅 ×3 |
| -bhadra | 跋陀羅 ×4 |
| -varman | 伐摩 ×3 |
| -mitra | 蜜呾羅 / 蜜多羅 |
| mahā- | 摩訶 (8; 莫訶 once) |
| mahe- | 摩醯 |

- **Compounds are transcribed member by member, with vowel sandhi undone:**
  - 婆羅·阿迭多 *bāla-āditya*, 尸羅·阿迭多, 毘訖羅摩·阿迭多.
  - 薩婆·曷剌他·悉陀 *sarva-artha-siddha*, 那伽·閼剌樹那 *nāga-arjuna*.
  - 摩醯·因陀羅 *mahe-indra*, 屈屈吒·阿濫摩 *kukkuṭa-ārāma*.
  - Therefore 阿, 因, 閼 or 曷 in the middle of a name signals a vowel-initial member.

## 6. Sanskrit vs Prakrit

- **Sanskritic in the great majority.** Examples include takṣaśilā (not takkasilā), śrāvastī, kapilavastu, mathurā, kanyakubja, puṣkalāvatī, kaśmīra, śākala, nepāla, vipula, gṛdhrakūṭa, prasenajit, ajātaśatru and kātyāyana.
- **Vernacular forms are kept in a minority, mostly western, southern and eastern regional names:**
  - Assimilated clusters: 屈屈吒 kukkuṭa ×2, 摩訶剌侘 / 蘇剌侘 -raṭṭha, 耽摩栗底 tāmalitti (not tāmralipti), 絡多末知 rakta-maṭṭi.
  - gh for h: 僧伽羅 siṃghala.
  - ḍḍ: 烏仗那 uḍḍiyāna, 烏荼 oḍḍa.
  - The targets list shows more of the same: 奔那伐彈那 puṇṇa-, 瞿折羅 gujjara.
- **Loss of intervocalic consonants is not reproduced** in the secure set; the only hint is 伽 = k in 婆毘吠伽 bhāvive(k/g)a.
- **The -o < -aḥ ending is not attested.**

## 7. The 舊曰…訛 corrections show what his ear attended to

The text has about 90 舊曰/舊云 notes. Among those on Indic words, the corrections fall into four groups:

1. **Prakrit/old-dialect form → Sanskrit (≈27).**
   - 優填 *udena* → 鄔陀衍那; 波斯匿 *pasenadi* → 鉢邏犀那恃多.
   - 耆闍崛 *gijjha-* → 姞栗陀羅矩吒; 舍衛 → 室羅伐悉底.
   - 阿耨達 *anotatta* → 阿那婆答多; 瞿耶尼 *goyānī* → 瞿陀尼 (intervocalic d restored).
   - 彌勒 → 梅呾麗耶; 阿那律 → 阿泥𢫫陀; 樹提伽 → 珠底色迦.
   - 浮圖/塔婆 *thūpa* → 窣堵波; 刹利 → 刹帝利; 闍維 → 涅疊般那.
2. **Truncation (訛略/略).** Restored examples: 恆 → 殑伽, 須達 → 蘇達多, 偈 → 伽他, 尸毘 → 尸毘迦, 末田地 → 末田底迦 and 迦葉 → 迦葉波 ("洎諸迦葉例無波字略也").
3. **Vowel quality.**
   - 毘 vi → 吠 ve/vai (吠陀, 吠奢, 吠舍釐).
   - 優 → 鄔 for u- (3×).
   - 須 → 蘇 for su- (須彌, 須達, 須跋陀羅, 須扶提 all rejected; 蘇 is su 10 times out of 10 in the key).
   - 拘睒彌 → 憍賞彌 (kau-).
4. **Consonant quality.** Retroflexes (僧祇梨 → 僧伽胝 ṭ; 波羅奈 → 婆羅痆斯 ṇ) and aspirates (毘琉離 → 毘盧擇迦 ḍh).

He also gives fanqie for rare or ambiguous characters: 殑 巨勝反, 屈 居勿反, 痆 女黠反, 呫 昌葉反, 洩 移結反, 𢫫 盧骨反, 亘 許贈切 and 奔 逋論反. These annotations override the dictionary readings.

## 8. Mizutani forms that conflict with the key

- **01.01c** "Ind. cakṣu": 縛 is v-; the form is vakṣu.
- **01.20.02** Tuṣāra: 貨 is x/kh, not ṣ; the form is Tukhāra.
- **03.01** udyāna: 仗 is retroflex (澄), so uḍḍiyāna/oḍḍiyāna, not udyāna.
- **03.05** urasā / uragā: 尸 is ś; uraśā only.
- **04.12** Govisana: 霜 is 生 (ṣ); Goviṣāṇa.
- **05.02** Ayodhyā: there is no character for -y-; XZ heard Ayodhā/Ayudhā.
- **07.03.12** licchavi: 婆 is never vi (毘 is); the form is licchava.
- **08.04.01** teladhaka: 擇 is retroflex; telāḍhaka.
- **10.06.02c** Dvāravatī: 鉢 never renders va; dvārapati.
- **10.07** tāmralipti: XZ writes Pkt. tāmalitti.
- **11.12** ujjayanī: 那 gives *ujjayana*.
- **11.21** pitaśaila: should be pīta- (length is not marked, so this is consistent with the key).
- **11.23.02** kokaṅkaṇa: four syllables for three characters, and 稽 is ke-; unresolved.
- **02.02** lampāka: only *lampa* is transcribed.
- **Mismatched objects.** In 04.07.03 and 06.03.04 the original_name belongs to a different object (Uruṇḍa, Pippalavana) than the transcribed name (鄔波毱多 upagupta, 尼拘盧陀 nyagrodha/nigrodha).

## 9. Characters the next stage must treat as ambiguous

- **r/l:** 羅, 邏, 剌, 利, 栗, 盧, 釐, 縷, 洛 and 路.
- **Voiced aspiration:** 陀 (d/dh/dd), 伽 (g/gh, once k), 婆 (va/ba/bha, once pa), 跋, 毘 (vi/bhi), 瞿 (go/gu/gho), 提 (de/dhi), 達, 度, 地 and 部.
- **Dental or retroflex n:** 那 (na/ṇa) and 諾.
- **e/i and e/ai:** 醯, 泥, 吠 and 提.
- **Length of every vowel.**
- **Closed characters whose coda may or may not be a real Indic consonant:**
  - 伐 (va/var), 鉢 (p/pa/par/pat), 薩 (s/sa/sar), 達 (d/dha/dhar/dat), 剌 (r/ra/raṭ), 呾 (t/ta).
  - 曷 (r- prefix / ha(r) / a(r)).
  - The nasal-coda characters before 摩/那 (x(m), x(n)).
- **Same syllable, several characters:**
  - va: 伐, 縛, 婆.
  - ra: 羅, 邏, 剌.
  - ka: 迦, 羯.
  - pu: 補, 布.
  - ś before r vs before v/m: 室 vs 濕, which is conditioned and not free.

## 10. Non-Indic names (excluded from the key)

These names show 28 Iranian, Turkic, Tocharian and Tibetan alignments, mostly from juan 1:
- **Indian practice carried over:**
  - -t coda for r: 秣 mar/mur (颯秣建 Samarkand, 弭秣賀 Maymurgh), 呾蜜 Tar-midh, 喝 khar/khār (喝捍, 捕喝).
  - The 曷 r- prefix: 曷邏胡 rāgh.
- **Iranian-specific values:**
  - x/kh → 曉 (喝, 貨, 忽): Indic kh is 溪 (佉), so 覩貨邏 follows the Bactrian pronunciation.
  - z → 習/寔.
  - Final -l/-lm → 羅/懍 (珂咄羅 Khuttal, 忽懍 Khulm).
  - b/w → 縛 (縛喝 Balkh, 縛伽浪 Baghlān).
  - Final clusters: -kand → 建, -gān → 健.
- **Tocharian:** Tocharian forms account for 屈支 *kuči* and 阿奢理貳 *aśari-* (< āścarya).

None of these should be used to test Sanskrit reconstructions.
