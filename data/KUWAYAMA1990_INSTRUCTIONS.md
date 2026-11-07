# Reading Kuwayama 1990 (handwritten thesis) for the place notes

Kuwayama Shōshin 桑山正進, 『カーピシー＝ガンダーラ史研究』 (doctoral thesis, Kyoto University, 1986; Kyoto University
repository 2433/78265, 1990 deposit). It is a handwritten manuscript on genkō yōshi (vertical Japanese, read columns
right to left, the right-hand page of each spread first). Its OCR is unusable, so read the page images directly.

- Images: `data/ref/kyoto/k1990/view/v{1,2,3}_p-NNN.png` (greyscale, about 1720 × 1214 px; each is a two-page spread;
  the handwritten manuscript page numbers are at the foot of each page, the right-hand page has the lower number).
  If a word is hard to read, open the full-resolution image `data/ref/kyoto/k1990/png{1,2,3}/p-NNN.png` (crop it with
  python PIL into a file under /home/kengo/.claude/jobs/ae7893d7/tmp/k1990/ and Read that).
- Locating pages: vol. 2 spread 20 has pp. 703–704, vol. 3 spread 10 has pp. 1469–1470, vol. 1 spread 340 has pp.
  603–604; plates (figures) interrupt the sequence, so check the page numbers on the images.
- Contents (manuscript pages): ch. 3 「隋代のカーピシー」 665 (§1 「『隋書』漕國はザーブリスターンか」 665; §2 「隋代の
  カーピシー」 710); ch. 4 「カーピシー國大都城とベグラーム」 731 (§1 「迦畢試國大都城」 731; §2–6 fortifications and
  stamped pottery 752–919); ch. 5 「七、八世紀のカーピシー」 920–1126; ch. 6 「カーピシー＝ガンダーラにおける佛教と
  ヒンドゥー教」 1127 (§1 「カーピシーにおける聖迹の分布」 1130; §2 「佛教事情」 1165; §3 「葱嶺山と阿路猱山と
  稿那呬羅山」 1221; §4–5 marble Hindu images 1271, 1337; §6 「バーミヤーン大佛の成立」 1417); notes 1454–1613
  (by chapter); appendix (Tokharistan) 1614–.
- Much of the thesis was published in English in Kuwayama, *Across the Hindukush of the First Millennium* (2002),
  `data/ref/kyoto/kuwayama2002_across_hindukush_Kuwayama_S.txt` (clean text). Read the thesis for what the English
  collection lacks, and say when a point is also in the 2002 English.

## Output

`data/ref/kyoto/k1990/summary_<part>.md`: for each section you read, a summary of the argument as it bears on places
in Xuanzang's Da Tang Xiyu ji (ids in `data/places.tsv`; the relevant notes are in `data/notes/`, grep '^### <id> '),
then, for each place, the identification Kuwayama proposes, his evidence (Chinese texts with their wording, sites,
excavations, finds), and 1–3 short verbatim transcriptions of his own key sentences with the manuscript page, in
Japanese as written (mark uncertain characters with [?]). Note where he disagrees with Mizutani (data/places.tsv
mz_identification) or with the study's current note. Don't edit any other file.

Report: the places he treats, his identifications in one line each, and anything that would change a note.
