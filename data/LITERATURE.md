# Recent scholarship (1985–2026)

The study's sources stop at Ji (1985) for the commentary and at *Indian Archaeology – A Review* 2000–01 for excavation.
This file tracks the later literature: what has been found, what has been read and coded, and what is still wanted.

- **Bibliography:** `data/literature.tsv`, one row per item (454 in all): key, group (A juan 1 and 12; B juan 2–3; C juan 4–7;
  D juan 8–9; E juan 10–11; X general), the place ids it bears on, citation, access, URL, the local text
  (`data/ref/lit/<group>/<key>.txt`, gitignored), relevance and status. Status: `have` (text in hand), `in study` (already
  used under another name), `oa, not fetched` (free online but blocked for scripts), `wanted` (book or paywall),
  `not sought` (low relevance). Built by agents searching in English, Japanese, Chinese and European languages in
  November 2026, with a second round for the gaps; the searches ran out of budget part way, so coverage is uneven (see "Gaps"). Rows whose citation says
  "to verify" or "from memory" were not checked against a catalogue.
- **Coding:** `data/LIT_INSTRUCTIONS.md`; coded rows in `data/coded/lit_batch*.tsv` (1 A, 2 C, 3 D, 4 E, 5 B), quotes
  checked with `scripts/check_quotes_asr.py`. They appear in `places.tsv` (`lit`, `lit_n`, `lit_evidence`) and on the map
  ("Recent scholarship (since 1985)"), and are folded into the notes as **Recent scholarship.** paragraphs.
- **IAR 2007–14:** six later volumes of *Indian Archaeology – A Review* (2007–08, 2009–10 to 2013–14, from the ASI
  Aurangabad Circle's site) were added to the IAR index (`data/iar_hits.tsv` passages 729–790) and coded in
  `data/coded/iar_batch11.tsv`. 2001–02 to 2006–07, 2008–09 and 2014– are not online.
- **Not yet published:** Max Deeg's annotated English translation of the Xiyu ji (one volume per juan; juan 1–3 in
  editing, 4, 8, 9 finished as of his Language Log note). The Cardiff–Bihar "Xuanzang Trail" project (2020–24) has
  published no list of its sites yet; its Telhara excavation report (Choudhary et al.) is listed below.
- **Funayama Tōru:** no map or place project by him was found (Kyoto Zinbun joint research, KAKEN, the web). The
  closest Kyoto resource is the 西域行記データベース (text search). Other maps found: Hou Yangfang's Silk Road GIS (the
  return route), a GIS paper from FIU (2019) and hobby maps; none tests identifications.

## Gaps

What the searches could not reach, for a later pass (or a library):
- **Chinese journals (CNKI):** web search does not index them. Only titles found through footnotes and OpenAlex are
  listed; Karashahr (Shikchin, Boghda-qin), Aksu, Karghalik, the 公主堡 fort, Kashgar's Mor temple and the Tashkurgan
  Stone City have no formal reports in the list.
- **Russian, Uzbek and Tajik excavation literature:** Chach/Tashkent, Nujkath, Ispijab, Kesh, Chaghāniyān, Shumān,
  Kobadian, Kumādh; Badakhshan (Rāgh, Kishm, Yamgān, Kurān) and the Wakhan forts.
- **India:** nothing new was found for Kuśinagara, Kannauj, Kulūta/Jālandhara/Lakhanpur, Viśoka, Vṛji, Mahārāṣṭra's
  capital, Jejākabhukti, Bhramaragiri, Cōḷa, Bharukaccha, or Rajbadidanga after S. R. Das; no Japanese or Chinese work
  on Magadha or South India beyond what is listed.
- **IAR:** 2001–02 to 2006–07, 2008–09 and 2014– are not online. 1990–91 and 1993–94, missing from the study's own
  scans, were added from the ASI Aurangabad Circle PDFs (`data/ref/iar/`).

## Wanted

Please put the files in `data/ref/lit/<group>/` named `<key>.pdf` (the key is the one given here); the text is made with
`pdftotext`, or OCR'd if it is a scan.

### Free online, but blocked for scripts: please download in a browser

On 2026-11-12 every `oa, not fetched` item was tried again with curl from the Mac. Fifteen came through and are now
`have`; three more turned out to be on disk already. What still fails is mostly a block on the site (bot checks,
403/406), not a dead link, so a browser should get most of them. Direct links found on the landing pages:
- **Heidelberg (Anubis bot check):** ANP 1 `https://digi.hadw-bw.de/view/anp1text/download.pdf`; ANP 2, 3 and 5 the
  same with `anp2`, `anp3`, `anp5`; Härtel's *Sonkh* at `https://hasp.ub.uni-heidelberg.de/catalog/book/934`.
- **Persée (403):** Bernard et al. 2006 `https://www.persee.fr/docAsPDF/crai_0065-0536_2006_num_150_2_87126.pdf`.
  (Tarzi 2007 and Sims-Williams 2002 were downloaded in a browser on 2026-11-12, with Jokura et al. 2017.)
- **Brill (403):** Deeg 2025 is chapter BP000009 of *Early Āndhradeśa* II:
  `https://brill.com/downloadpdf/edcollchap-oa/book/9789004744097/BP000009.pdf`; the whole volume is
  `https://brill.com/downloadpdf/edcollbook-oa/title/73131.pdf`.
- **Refused or timing out:** the NII-hosted Japanese repositories (Teikyo, Waseda, Rissho: 406), Durham's Worktribe
  and DRO (all the Coningham papers: 403), UNESCO's unesdoc, CORE, figshare, J-STAGE and CiNii (202 holding pages),
  SOAS ePrints and aisixiang.com (no answer, from waffle either).
- **Partly:** the ICOMOS record for *Bamiyan II* (2016) offers only the cover and contents (8 pp.); the full volume is
  still wanted. Digital Himalaya's *Ancient Nepal* index page no longer lists its issues.

**Central Asia, Xinjiang, Afghanistan (juan 1, 12)**

- [high] `amanbaeva2022_akbeshim2018`: Bakit Amanbaeva & Yamauchi Kazuya (eds.), Ak-Beshim (Suyab) 2018 (帝京大学シルクロード学術調査団調査研究報告). Teikyo University Research Institute of Cultural Properties & Institute of History and Cultural Heritage, NAS Kyrgyz Republic, 2022. 217 pp. — https://teikyo-u.repo.nii.ac.jp/record/2003929/files/2018s.pdf
- [high] `jokura2016_akbeshim_rabat`: Jokura Masayoshi, Yamafuji Masatoshi, Nawabi Yama, Yamauchi Kazuya & Bakit Amanbaeva, 「キルギス共和国アク・ベシム遺跡の発掘（2015年秋期）調査」, WASEDA RILAS JOURNAL 4 (2016): 43-71. — https://waseda.repo.nii.ac.jp/record/35967/files/RILAS_4_Jokura.pdf
- [high] `yamauchi2018_akbeshim2017`: Yamauchi Kazuya, Kushihara Kōichi & Mochizuki Hidekazu, 「2017年度アク・ベシム遺跡発掘調査報告」, 帝京大学文化財研究所研究報告 17 (2018): 121-168. — https://teikyo-u.repo.nii.ac.jp/
- [high] `yamauchi2022_akbeshim2016_2017`: Yamauchi Kazuya, Kushihara Kōichi, D. Sorokin, Nakayama Chieko & Mochizuki Hidekazu, アク・ベシム（スイヤブ）2016・2017 (帝京大学シルクロード学術調査団調査研究報告1). 帝京大学文化財研究所 / キルギス共和国国立科学アカデミー, 2022. 235 pp. (English/Russian ed.: Amanbaeva & Yamauchi (eds.), Ak-Beshim (Suyab) 2016-2017, 2023, 242 pp.) — https://teikyo-u.repo.nii.ac.jp/record/2003927/files/2016-2017s.pdf
- [high] `yamauchi2025_suiye_construction`: Yamauchi Kazuya, 「砕葉鎮城の建設とアク・ベシム遺跡シャフリスタン1の都市プランの変化」, 帝京大学文化財研究所研究報告 23 (2025): 255-296. — https://teikyo-u.repo.nii.ac.jp/
- [medium] `bernard2006_bactres`: Paul Bernard, Roland Besenval, Philippe Marquis, "Du « mirage bactrien » aux réalités archéologiques: nouvelles fouilles de la DAFA à Bactres (2004–2005)", CRAI 150(2) (2006): 1175–1248. — https://doi.org/10.3406/crai.2006.87126
- [medium] `jokura2018_akbeshim_part1`: Jokura Masayoshi et al., [Ak-Beshim (Suyab) archaeological study, Part 1], WASEDA RILAS JOURNAL 6 (2018): 205-257. [title not verified; file name 205-257_Masayoshi-JOKURA_Part1.pdf] — https://www.waseda.jp/flas/rilas/assets/uploads/2018/10/205-257_Masayoshi-JOKURA_Part1.pdf
- [medium] `kyzlasov2023_akbeshim_trans`: L. R. Kyzlasov, 「クズラソフによるアク・ベシム遺跡の発掘」, trans. Yamauchi Kazuya, 帝京大学文化財研究所研究報告 21 (2023): 157-252. (Japanese translation of Kyzlasov 1959.) — https://teikyo-u.repo.nii.ac.jp/
- [medium] `liu2025_xuanzang_route`: 刘屹《玄奘的西行与东归之路再考察》,《光明日报》2025年6月14日, 第10版 (repr. 爱思想 aisixiang.com/data/163842.html) — https://www.aisixiang.com/data/163842.html
- [medium] `morimoto2006_nara_bamiyan`: 森本晋「バーミヤーン谷における考古調査」『奈良文化財研究所紀要』2006: 6–7. — https://cir.nii.ac.jp/crid/1390853650400230400
- [medium] `petzet2016_bamiyan_icomos2`: Michael Petzet (ed.), The Giant Buddhas of Bamiyan II: Safeguarding the Remains 2010–2015. ICOMOS Monuments and Sites XXI. Berlin, 2016. — https://openarchive.icomos.org/id/eprint/3076/
- [medium] `rissho2020_karatepe_report`: Rissho University Uzbekistan Academic Research Group (Ikegami Satoru, Iwamoto Atsushi et al.), Kara Tepe - Buddhist Complex of Termez: Excavation of the Northern Hill 2014-2017. Tokyo: Rissho University, 2020 (English abstracts: Karatepe_abstracts_En.pdf). — https://rissho.repo.nii.ac.jp/record/11465/files/Karatepe_abstracts_En.pdf
- [medium] `rissho2021_buddhist_heritage_uz`: Rissho University, 『ウズベキスタンにおける仏教文化遺産の調査と保護』. Tokyo: Rissho University (Agency for Cultural Affairs project), 2021. — https://rissho.repo.nii.ac.jp/record/11464/files/
- [medium] `saito2022_suiye_texts`: Saitō Shigeo 齊藤茂雄, 「文献史料から見た砕葉城」, 帝京大学文化財研究所研究報告 21 (2022): 25-37. — https://teikyo-u.repo.nii.ac.jp/
- [medium] `stanco2022_irongate_hellenistic`: Ladislav Stančo et al., 'The Iron Gate and its environs in the Hellenistic period: preliminary report', Studia Hercynia 26.2 (2022): 91-114. — https://cejsh.icm.edu.pl/cejsh/element/bwmeta1.element.desklight-b795c538-bfcc-4c14-9bbb-2716e96682c4/c/Ladislav_Stanco_et_al_91-114.pdf
- [medium] `xiao2025_mor`: 肖小勇 (leader), 中央民族大学 & 新疆维吾尔自治区文物考古研究所, 'Kashgar Mor temple site (新疆喀什莫尔寺遗址)', 《中国文物报》2025年5月2日 (feature); also National Cultural Heritage Administration entry, 2024 (http://www.ncha.gov.cn/art/2024/3/25/art_2760_187828.html). No formal excavation report found — http://www.zhongguowenwubao.com/portal/DigitPager/paperDetail/publishdate/2025-05-02/paperId/21468/id/107842
- [medium] `xjicra2017_shitoucheng`: 新疆文物考古研究所, '2017年新疆考古新进展：葱岭传奇—塔什库尔干石头城遗址' (field-season summary; excavations 2015–2020, field staff 艾涛 et al.), silkroads.org.cn. No formal report found — https://www.silkroads.org.cn/portal.php?mod=view&aid=12458
- [medium] `yamauchi2019_shahristan1_plan`: Yamauchi Kazuya, 「アク・ベシム遺跡第1シャフリスタンの都市プランの変化」, 帝京大学文化財研究所研究報告 18 (2019): 1-17. — https://teikyo-u.repo.nii.ac.jp/
- [medium] `yamauchi2025_dayunsi`: Yamauchi Kazuya, 「砕葉鎮城の大雲寺の位置と伽藍配置に関する試論」, 帝京大学文化財研究所研究報告 23 (2025): 167-190. — https://teikyo-u.repo.nii.ac.jp/

**Gandhāra, Swat, Taxila, Kashmir (juan 2–3)**

- [high] `anp1_jettmar1989`: Jettmar, Karl (ed.). Antiquities of Northern Pakistan: Reports and Studies 1. Rock Inscriptions in the Indus Valley. Mainz: von Zabern, 1989 (Text and Plates; with Fussman, von Hinüber, Sander, Sims-Williams, Ma Yong) — https://digi.hadw-bw.de/view/anp1text
- [high] `anp2_jettmar1993`: Jettmar, Karl (ed.). Antiquities of Northern Pakistan 2. Mainz: von Zabern, 1993 (incl. Fussman, 'Chilas, Hatun et les bronzes bouddhiques du Cachemire'; Jettmar, 'The Paṭolas, their governors and their successors'; Höllmann on Chinese inscriptions) — https://digi.hadw-bw.de/view/anp2
- [high] `hakal_chartoi_maitreya`: Hakal, Mueezuddin. 'Faxian's and Xuanzang's wooden Maitreya and the Chartoi rock-cut niche at Gupis, Gilgit-Baltistan.' Journal of Asian Civilizations (Taxila Institute, Quaid-i-Azam University) [vol./year to verify, c. 2020s] — https://jac.qau.edu.pk/index.php/jac/article/view/80
- [high] `hinuber2004_palola`: Hinüber, Oskar von. Die Palola Ṣāhis: Ihre Steininschriften, Inschriften auf Bronzen, Handschriftenkolophone und Schutzzauber. Materialien zur Geschichte von Gilgit und Chilas. Antiquities of Northern Pakistan 5. Mainz: von Zabern, 2004 — https://digi.hadw-bw.de/view/anp5
- [high] `olivieri_orgyanpa`: Olivieri, Luca Maria. Paper on the itinerary of the Tibetan pilgrim O rgyan pa in Swat (1260s–80s, after Tucci 1940) and the 'Indrabhūti temple' near Manglawar [c. 2017; exact title and venue to verify; CORE output 287124416] — https://core.ac.uk/download/287124416.pdf
- [medium] `anp3_fussman1994`: Fussman, Gérard (ed.). Antiquities of Northern Pakistan 3. Mainz: von Zabern, 1994 (Shatial stupa triptych, Chilas-Thalpan and Tibetan art, Kuberavāhana stupas, Helor Das, Nokkono Ghwand in Swat) — https://digi.hadw-bw.de/view/anp3
- [medium] `baums_glass_cgt`: Baums, Stefan and Andrew Glass. Catalog of Gāndhārī Texts (online database). 2002– — https://gandhari.org/catalog
- [medium] `niklasson2025_palola`: Agneta Niklasson, The Buddhist Sculptures of the Palola Ṣāhi, PhD thesis, SOAS University of London, 2025, doi:10.25501/soas.00821294 — https://doi.org/10.25501/soas.00821294
- [medium] `olivieri_filigenzi2018_chronology`: Olivieri, Luca M. and Anna Filigenzi. 'On Gandhāran sculptural production from Swat: recent archaeological and chronological data.' In W. Rienjang and P. Stewart (eds), Problems of Chronology in Gandhāran Art. Oxford: Archaeopress, 2018, 71–92 — https://www.carc.ox.ac.uk/GandharaConnections/
- [medium] `rienjang_stewart2019_geography`: Rienjang, Wannaporn and Peter Stewart (eds). The Geography of Gandhāran Art. Proceedings of the Second International Workshop of the Gandhāra Connections Project, Oxford, 2018. Oxford: Archaeopress, 2019 — https://www.carc.ox.ac.uk/GandharaConnections/
- [medium] `yatoo2012_nwkashmir`: Mumtaz A. Yatoo, Characterising Material Culture to Determine Settlement Patterns in North West Kashmir, PhD thesis, University of Leicester, 2012 (institution from memory; verify) (Figshare) — https://figshare.com/articles/thesis/Characterising_Material_Culture_to_Determine_Settlement_Patterns_in_North_West_Kashmir/10107209

**North India, Kapilavastu, Nepal (juan 4–7)**

- [high] `coningham2013_sacred_garden`: Coningham, R.A.E. and K.P. Acharya, 'Re-discovering Lumbini: archaeology and site interpretation', in K. Weise (ed.), The Sacred Garden of Lumbini: Perceptions of Buddha's Birthplace (Paris: UNESCO), pp. 50-103 [chapter pages as given in Durham record] — https://unesdoc.unesco.org/ark:/48223/pf0000223986
- [high] `coningham2018_tilaurakot`: Coningham, R.A.E., K.P. Acharya, M.J. Manuel, C.E. Davis, R.B. Kunwar, I.A. Simpson, K.M. Strickland, E. Smaghur, J. Tremblay, A. Lafortune-Bernard, 'Archaeological investigations at Tilaurakot-Kapilavastu, 2014-2016', Prācīna Nepāla / Ancient Nepal 197-198, pp. 5-59 (Kathmandu: Department of Archaeology) — https://dro.dur.ac.uk/26943
- [high] `coningham2019_handigaon`: Coningham, R.A.E., K.P. Acharya, R.B. Kunwar, C.E. Davis, D. Hale, M.J. Manuel, R. Villis and L. Watson, 'Pilot Geophysical Survey in Handigaon, Kathmandu', Ancient Nepal 201 (2019): 19-37 — https://durham-repository.worktribe.com/output/1259738
- [high] `coningham2019_ramagrama`: Coningham, R.A.E., K.P. Acharya, et al., 'Geophysical investigations at Ramagrama, Nepal: results from new surveys undertaken in January 2018', Ancient Nepal 201, pp. 5-17 — https://durham-repository.worktribe.com/output/1295952
- [high] `coningham2020_ramagrama`: Coningham, R.A.E., K.P. Acharya, C.E. Davis, R.B. Kunwar, et al., 'Geophysical investigations at Ramagrama: results from new surveys undertaken in November 2019 and February 2020', Ancient Nepal (issue no. as listed in Durham record), pp. 5-28 — https://durham-repository.worktribe.com/output/1295952
- [medium] `coningham2016_bhandarkhal`: Coningham, R.A.E., K.P. Acharya, C.E. Davis, M.J. Manuel, R.B. Kunwar, D. Hale, J. Tremblay, D. Gautam and N. Mirnig, 'Exploring Ancient Pashupati: Preliminary Results of Archaeological Surveys and Excavations at Bhandarkhal, Kathmandu Valley UNESCO World Heritage Property (Nepal)', Ancient Nepal 191-192 (2016): 93-112 — https://durham-repository.worktribe.com/output/1375401
- [medium] `coningham2020_dohani_karma`: Coningham, R.A.E., K.P. Acharya, et al., 'Preliminary results of geophysical survey, mapping and auger coring at Dohani and Karma, two fortified enclosures in Kapilbastu District, Nepal', Ancient Nepal 204, pp. 25-57 — https://durham-repository.worktribe.com/output/1294406
- [medium] `coningham2020_lumbini_routeway`: Coningham, R.A.E., K.P. Acharya, et al., 'Lumbini's nursery well and the evidence for an ancient routeway through Rupandehi and Kapilbastu districts, Nepal', Ancient Nepal 204, pp. 5-24 — https://durham-repository.worktribe.com/output/1263529
- [medium] `coningham_satyanarayan_handigaon`: Coningham, R.A.E. et al., 'Geophysical Investigations at the Satya Narayan Temple, Handigaon, Kathmandu (Nepal)', Ancient Nepal 207 [year not seen; verify] — https://durham-repository.worktribe.com/output/1191349
- [medium] `digitalhimalaya_ancient_nepal`: Ancient Nepal (Prācīna Nepāla), journal of the Department of Archaeology, Nepal, 1967-: digitised back issues (Digital Himalaya; Nepal in Data) — https://digitalhimalaya.com/collections/journals/ancientnepal
- [medium] `hartel1993_sonkh`: Härtel, Herbert, Excavations at Sonkh: 2500 Years of a Town in Mathura District (Monographien zur indischen Archäologie, Kunst und Philologie 9; Berlin: Dietrich Reimer); open-access reissue CrossAsia-eBooks 2021, doi:10.11588/xabooks.934 — https://doi.org/10.11588/xabooks.934
- [medium] `kaken_maheth_1994_96`: Aboshi Yoshinori (PI), 'A study of Maheth (Sravasti) site in India', KAKEN Grant 06041110, final research report summary FY1994-1996 — https://kaken.nii.ac.jp/en/report/KAKENHI-PROJECT-06041110/060411101996kenkyu_seika_hokoku_gaiyo
- [medium] `murakami2016_tilaurakot`: 村上東俊 (Murakami Tōshun), 'ティラウラコットにおける近年の考古学調査について' [The recent archaeological survey of Tilaurakot], 印度學佛教學研究 (Journal of Indian and Buddhist Studies) 65(1) — https://cir.nii.ac.jp/crid/1390282680357686912
- [medium] `noritake2021_tilaurakot`: 則武海源 (Noritake Kaigen), 'ティラウラコットの現状を考える', 立正大学大学院紀要 37, p. 301ff. — https://rissho.repo.nii.ac.jp/record/7941/files/in_kiyo_37_301_noritake.pdf
- [medium] `strickland2016_tilaurakot_industrial`: Strickland, K.M., R.A.E. Coningham, K.P. Acharya, et al., 'Recent excavations at Tilaurakot's southern industrial mound (Lohasariya): a preliminary report', Ancient Nepal 190, pp. 47-58 — https://durham-repository.worktribe.com/output/1406984
- [medium] `unesco2019_rupandehi_catalogue`: UNESCO Kathmandu / Department of Archaeology Nepal, The Archaeological Site Catalogue - Rupandehi District — https://unesdoc.unesco.org/ark:/48223/pf0000372559

**Magadha (juan 8–9)**

- [high] `amar2009_bodhgaya_thesis`: Amar, Abhishek Singh, 'Contextualising the navel of the earth: the emergence, sustenance and religious transformation of Buddhism in the Bodhgaya region (circa 300 BCE-1200 CE)', PhD thesis, SOAS, University of London, 2009 (DOI 10.25501/SOAS.00029300) — https://eprints.soas.ac.uk/29300/
- [medium] `deeg2025_week_interview`: Deeg, Max (interviewed). "'Xuanzang's work has certain bias that calls for careful interpretation': Max Deeg". The Week, 18 July 2025 (cover story) — https://www.theweek.in/theweek/cover/2025/07/18/xuanzangs-work-has-certain-bias-that-calls-for-careful-interpretation-max-deeg.html
- [medium] `mani2012_rajgir_slides`: Mani, B. R. "Magadha and Mahabharata: Archaeological Indications from Rajgir Area" (conference presentation, uploaded to SlideShare c. 2012) — https://www.slideshare.net/slideshow/magadhaandmahabharataarchaeologicalindicationsfromrajgirareabybrmani/15597057
- [medium] `pti2024_mahabodhi_satellite`: PTI. "Satellite images suggest architectural wealth beneath Mahabodhi temple in Bodh Gaya: Officials". The Week (wire), 13 July 2024 (BHDS–Cardiff project "Archaeology on the footsteps of the Chinese traveller Xuanzang"; M. B. Rajni, NIAS) — https://www.theweek.in/wire-updates/national/2024/07/13/cal14-bh-mahabodhi-temple-study.html

**East, South and West India, Sindh (juan 10–11)**

- [high] `deeg2025_andhra`: Deeg, Max (with an appendix by Peter Zieme), 'Chinese Reports about Buddhism in Early Āndhra', in Griffiths, Tournier & Shimada (eds.), Early Āndhradeśa, vol. II. Leiden: Brill, 2025, pp. 565–591. DOI 10.1163/9789004744097_015. Open access (CC BY-NC). — https://orca.cardiff.ac.uk/id/eprint/182757/1/9789004744097-BP000009.pdf
- [high] `griffiths2025_earlyandhradesa`: Griffiths, Arlo, Vincent Tournier & Akira Shimada (eds.), Early Āndhradeśa: Historical Studies around the Epigraphic Corpus. 2 vols (I: Inventory; II: Studies). Gonda Indological Studies 25. Leiden: Brill, 2025. Open access. — https://brill.com/edcollbook-oa/title/73131

### Books and paywalled articles, high relevance

**Central Asia, Xinjiang, Afghanistan (juan 1, 12)**

- `ball2019_gazetteer` [book]: Warwick Ball, Archaeological Gazetteer of Afghanistan, revised edition. Oxford: Oxford University Press, 2019. — https://academic.oup.com/book/40301
- `delavaissiere2010_chronology` [paywall]: Étienne de la Vaissière, "Note sur la chronologie du voyage de Xuanzang", Journal asiatique 298(1) (2010): 157–168. — https://poj.peeters-leuven.be/content.php?url=journal&journal_code=JA
- `forte1994_chinese_monastery_kirgiziya` [paywall]: Antonino Forte, 'An Ancient Chinese Monastery Excavated in Kirgiziya', Central Asiatic Journal 38.1 (1994): 41-57. — https://www.jstor.org/journal/centasiaj
- `gardin1998_bactriane_orientale` [book]: Jean-Claude Gardin et al., Prospections archéologiques en Bactriane orientale (1974–1978). 3 vols. Paris: ERC (Mémoires de la Mission archéologique française en Asie centrale 9), 1989–1998 (vol. 2: B. Lyonnet, Céramique et peuplement, 1997; vol. 3: Description des sites et notes de synthèse, 1998). — https://zenon.dainst.org/Record/000203472
- `hou2021_pamir` [book]: 侯杨方《重返帕米尔：追寻玄奘与丝绸之路》, 上海: 上海译文出版社, 2021
- `iwamoto2016_rissho` [paywall]: 岩本篤志「トハリスタンの仏教遺跡と玄奘—立正隊による調査をふまえて」『唐代史研究』19 (2016): 256–264. — https://cir.nii.ac.jp/crid/1521980705281714048
- `kuwayama1992_huichao` [book]: 桑山正進 編『慧超往五天竺國傳研究』京都大学人文科学研究所, 1992 (repr. 臨川書店 1998). — https://ci.nii.ac.jp/ncid/BN08087915
- `kuwayama2023_bamiyan` [book]: 桑山正進『新興バーミヤーンの時代』(ヒンドゥークシュ南北歴史考古学樷攷 2) 臨川書店, 2023. — https://ci.nii.ac.jp/ncid/BD00522431
- `kuwayama2023_xuanzang` [book]: 桑山正進『玄奘三蔵の形而下』(ヒンドゥークシュ南北歴史考古学樷攷 3) 臨川書店, 2023. 494 pp. — https://ci.nii.ac.jp/ncid/BD02378008
- `li1998_kancheng` [book]: 李吟屏《古于阗坎城考》, 马大正、杨镰编《西域考察与研究续编》, 乌鲁木齐: 新疆人民出版社, 1998, 236–262
- `liu2017_talagan` [paywall]: 刘振玉《〈大唐西域记〉所记“呾剌健国”考》,《西域研究》2017年第3期: 82–96
- `niya_reports_1996_2007` [book]: 中日・日中共同尼雅遺跡学術調査隊『日中共同尼雅遺跡学術調査報告書』第1–3巻, 京都, 1996, 1999, 2007 (Chinese ed. 《中日日中共同尼雅遗迹学术调查报告书》) — https://kaken.nii.ac.jp/grant/KAKENHI-PROJECT-09041035
- `rapin2022_irongates_wall` [book]: Claude Rapin, Mutalib Khasanov & Shapulat Rakhmanov, 'The Iron Gates Wall near Derbent (Uzbekistan) from Alexander the Great to the 19th century', in Ch. Baumer, M. Novák & S. Rutishauser (eds.), Cultures in Contact: Central Asia as Focus of Trade, Cultural Exchange and Knowledge Transmission (Schriften zur Vorderasiatischen Archäologie). Wiesbaden: Harrassowitz, 2022, 57-85. ISBN 978-3-447-11880-4. — https://www.harrassowitz-verlag.de/
- `sakai2000_pamir` [book]: 酒井敏明 Sakai Toshiaki『旅人たちのパミール：玄奘、マルコ・ポーロはどの道を通ったか』, 東京: 春風社, 2000 (first published as 「旅人たちのパミール」, 帝塚山大学教養学部紀要 45 (1996): 1–82) — https://cir.nii.ac.jp/crid/1970023484858787246
- `semenov2002_suyab` [book]: G. L. Semenov (ed.), Суяб. Ак-Бешим [Suyab. Ak-Beshim] (Археологические экспедиции Государственного Эрмитажа). St Petersburg: State Hermitage & Institute of History NAS KR, 2002. 174 pp. (incl. E. I. Lubo-Lesnichenko, 'Сведения китайских письменных источников о Суябе', 115-127.) — https://www.old.archeo.ru/izdaniya-1/archaeological-news/annotations-of-issues/arheologicheskie-vesti-spb.-2002.-vypusk-10.-annotaciya
- `simswilliams2000_bd` [book]: Nicholas Sims-Williams, Bactrian Documents from Northern Afghanistan I: Legal and Economic Documents (Oxford 2000; rev. ed. London: Nour/Khalili 2012); II: Letters and Buddhist Texts (London 2007); III: Plates (2012). — https://www.khalilicollections.org/
- `song2025_songyun` [paywall]: 宋立州《〈宋云行纪〉与6–7世纪丝绸之路南道葱岭东段路线》,《史林》2025年第3期: 94–100 — https://search.napstic.cn/literature/periodical/010shilin202503009
- `xjicra2025_subashi` [paywall]: 新疆维吾尔自治区文物考古研究所、兰州大学考古与文化遗产研究院《新疆库车苏巴什佛寺遗址考古新发现》,《文物》2025年第2期 (2023–2024 excavation of the East Temple; authors and pages not captured) — https://www.aksxw.com/sy/rdxw/aks/202509/t20250909_30530466.html
- `xjicra2025_yotkan_survey` [book]: 新疆维吾尔自治区文物考古研究所等《新疆和田约特干遗址考古勘探报告(2022–2024年)》(launched at the Nov. 2025 symposium 约特干遗址与古于阗国都城研究; publisher not confirmed) — https://www.cssn.cn/lsx/slcz/202511/t20251121_5950773.shtml
- `xu2015_tang_silkroad` [book]: 许序雅《唐代丝绸之路与中亚史地丛考——以唐代文献为研究中心》 (publisher and year from memory: 北京: 商务印书馆, 2015; verify). Abstract read at https://appbook.qq.com/read/1024905837/4 (citation from memory; verify) — https://appbook.qq.com/read/1024905837/4
- `yamauchi2016_chu_heritage` [unknown]: Yamauchi Kazuya & Bakit Amanbaeva (eds.), キルギス共和国チュー川流域の文化遺産の保護と研究 アク・ベシム遺跡、ケン・ブルン遺跡 2011～2014年度. Bishkek/Tokyo: Institute of Cultural Heritage, NAS Kyrgyz Republic & Tokyo National Research Institute for Cultural Properties, 2016. 108 pp. — https://kaken.nii.ac.jp/en/grant/KAKENHI-PROJECT-15H05166/
- `yamauchi2020_akbeshim2019` [unknown]: Yamauchi Kazuya & Bakit Amanbaeva (eds.), Ak-Beshim (Suyab) 2019. Teikyo University Research Institute of Cultural Properties & National Academy of Sciences of the Kyrgyz Republic, 2020. — https://kaken.nii.ac.jp/en/grant/KAKENHI-PROJECT-21H04984/
- `yamauchi2024_akbeshim2022_2023` [unknown]: Yamauchi Kazuya, Yoshida Yutaka, Uetsuki M., Fujisawa A. et al., アク・べシム（スイヤブ）2022・2023 / Ak-Beshim (Suyab) 2022-2023 (帝京大学シルクロード学術調査団調査研究報告4). 帝京大学文化財研究所・キルギス共和国国立科学アカデミー, 2024. 381 pp. — https://kaken.nii.ac.jp/en/grant/KAKENHI-PROJECT-21H04984/
- `yoshida2023_xuanzang_sogdians` [book]: Yoshida Yutaka 吉田豊, 「玄奘とソグド人」, in Chikamoto Kensuke 近本謙介 & Kageyama Etsuko 影山悦子 (eds.), 玄奘三蔵がつなぐ中央アジアと日本. Kyoto: Rinsen, 2023, 33-66. — https://www.rinsen.com/
- `zhangping2015_ashliji` [paywall]: 张平《龟兹阿奢理贰伽蓝遗址新证》,《西域研究》2015年第1期 (cited in Zhang & Zhu 2019, n. 8; pages not captured)
- `zhu2012_prophecy` [paywall]: 朱丽双《〈于阗国授记〉译注》(上)(下),《中国藏学》2012年增刊1: 223–268; 2014年增刊1: 121–131 — https://www.cnki.net/

**Gandhāra, Swat, Taxila, Kashmir (juan 2–3)**

- `ali1999_hund` [book]: Ali, Ihsan. 'Excavations at Hund on the banks of the Indus: the last capital of Gandhara.' In A. Meadows and P.S. Meadows (eds), The Indus River: Biodiversity, Resources, Humankind. Karachi: Oxford University Press, 1999, 269–283 — https://www.worldcat.org/search?q=The+Indus+River+Biodiversity+Resources+Humankind
- `coningham_ali2007_charsadda` [book]: Coningham, Robin and Ihsan Ali (eds). Charsadda: The British-Pakistani Excavations at the Bala Hisar. BAR International Series 1709. Oxford: Archaeopress, 2007 — https://barpublishing.com/charsadda.-the-british-pakistani-excavations-at-the-bala-hisar.html
- `dani1986_taxila` [book]: Dani, Ahmad Hasan. The Historic City of Taxila. Paris: UNESCO; Tokyo: Centre for East Asian Cultural Studies, 1986 — https://www.worldcat.org/search?q=The+Historic+City+of+Taxila+Dani
- `deeg2005_faxian` [book]: Deeg, Max. Das Gaoseng-Faxian-zhuan als religionsgeschichtliche Quelle: Der älteste Bericht eines chinesischen buddhistischen Pilgermönchs über seine Reise nach Indien. Wiesbaden: Harrassowitz, 2005 — https://www.harrassowitz-verlag.de/
- `faccenna_spagnesi2014_swat_architecture` [book]: Faccenna, Domenico and Piero Spagnesi. Buddhist Architecture in the Swat Valley, Pakistan: Stupas, Viharas, a Dwelling Unit. Lahore: Sang-e-Meel, 2014 (ACT Field School Project Reports and Memoirs, Special Volume) — https://arca.unive.it/retrieve/e4239ddd-6dde-7180-e053-3705fe0a3322/Faccenna_2014_pre-print_light-grayscaleversion.pdf
- `kuwayama1992_huichao` [book]: 桑山正進 Kuwayama Shōshin (ed.). 『慧超往五天竺國傳研究』 Kyoto: Institute for Research in Humanities, Kyoto University, 1992 (repr. Rinsen 1998) — https://www.zinbun.kyoto-u.ac.jp/
- `kuwayama2006_pilgrimage` [book]: Kuwayama, Shōshin. 'Pilgrimage route changes and the decline of Gandhāra.' In P. Brancaccio and K. Behrendt (eds), Gandharan Buddhism: Archaeology, Art, Texts. Vancouver: UBC Press, 2006, 107–134 — https://www.ubcpress.ca/gandharan-buddhism
- `kuwayama2022_isou` [book]: 桑山正進 Kuwayama Shōshin. 『異相ガンダーラの仏教』（ヒンドゥークシュ南北歴史考古学叢攷 I）. Kyoto: Rinsen shoten 臨川書店, 2022 — https://www.rinsen.com/
- `olivieri_vidale2006_amsv` [paywall]: Olivieri, Luca M. and Massimo Vidale. 'Archaeology and art of Swat (Pakistan): fieldwork reports and studies — Archaeological Map of the Middle Swat Valley (AMSV)' East and West 56.1–3 (2006): 73–150 — https://www.jstor.org/journal/eastwest

**North India, Kapilavastu, Nepal (juan 4–7)**

- `aboshi1997_jetavana` [book]: Aboshi Yoshinori et al. (Kansai University Indo-Japanese joint team), Excavations at Jetavana (Saheth) / 『祇園精舎: サヘート遺跡発掘調査報告書』 (Tokyo: Dōhōsha Shuppan), 1642 pp. — https://kaken.nii.ac.jp/en/report/KAKENHI-PROJECT-06041110/060411101996kenkyu_seika_hokoku_gaiyo
- `asher2020_sarnath` [book]: Asher, Frederick M., Sarnath: A Critical History of the Place Where Buddhism Began (Los Angeles: Getty Research Institute) — https://shop.getty.edu/products/sarnath-a-critical-history-of-the-place-where-buddhism-began-978-1606066164
- `bakker1986_ayodhya` [book]: Bakker, Hans, Ayodhyā (Groningen Oriental Studies 1; Groningen: Egbert Forsten), 3 parts — https://relbib.de/Record/028861671/Details
- `coningham2013_lumbini_antiquity` [paywall]: Coningham, R.A.E., K.P. Acharya, K.M. Strickland, et al., 'The earliest Buddhist shrine: excavating the birthplace of the Buddha, Lumbini (Nepal)', Antiquity 87(338), pp. 1104-1123, doi:10.1017/S0003598X00049899 — https://doi.org/10.1017/S0003598X00049899
- `deeg2003_siddhartha_trod` [unknown]: Deeg, Max, The Places Where Siddhārtha Trod: Lumbinī and Kapilavastu (Lumbini International Research Institute, Occasional Papers 3; Lumbini: LIRI) — https://zenon.dainst.org/Record/000227538
- `deeg2005_faxian` [book]: Deeg, Max, Das Gaoseng-Faxian-zhuan als religionsgeschichtliche Quelle: der älteste Bericht eines chinesischen buddhistischen Pilgermönchs über seine Reise nach Indien mit Übersetzung des Textes (Studies in Oriental Religions 52; Wiesbaden: Harrassowitz) — https://www.harrassowitz-verlag.de/
- `jbf2005_lumbini_mayadevi` [book]: 全日本仏教会ルンビニー委員会 編, 『ルンビニー: マヤ堂の考古学的調査 1992-1995』 (東京: 全日本仏教会) — https://cir.nii.ac.jp/crid/1971430859825650221
- `kansai2000_maheth_prelim` [book]: 関西大学文学部考古学研究室, 『インド共和国ウッタル・プラデーシュ州シュラーヴァスティー県所在マヘート遺跡発掘調査概報』 (吹田: 関西大学) — https://cir.nii.ac.jp/crid/1970304959845779637
- `rissho2000_tilaurakot_text` [book]: 立正大学ネパール考古学調査団 / 中村瑞隆 編, 『ティラウラコット I 本文編』 (東京: 雄山閣出版) [plates vol. 1978] — https://cir.nii.ac.jp/crid/1970023484862363577
- `sakazume1993_kapilavastu` [unknown]: 坂詰秀一 (Sakazume Hideichi), 'カピラヴァストウはどこか' [Where is Kapilavastu?], 立正史学 73 — https://cir.nii.ac.jp/crid/1520853833376654976
- `sakazume2015_shaka_kokyo` [book]: 坂詰秀一 編著, 『釈迦の故郷を掘る: カピラ城比定地ティラウラコット発掘の記録』 (東京: 北隆館) — https://cir.nii.ac.jp/crid/1971149384795806218
- `schmidt2011_ramagrama` [unknown]: Schmidt, A., R.A.E. Coningham, K.M. Strickland, J.S. Shoebridge, 'A pilot geophysical evaluation of the site of Ramagrama, Nepal', Ancient Nepal 177, pp. 17-33 — https://pure.uhi.ac.uk/en/publications/a-pilot-geophysical-evaluation-of-the-site-of-ramagrama-nepal/
- `srivastava1986_discovery_kapilavastu` [book]: Srivastava, K.M., Discovery of Kapilavastu (New Delhi: Books & Books) — https://relbib.de/Record/1626395365
- `srivastava1996_piprahwa_ganwaria` [book]: Srivastava, K.M., Excavations at Piprahwa and Ganwaria (Memoirs of the Archaeological Survey of India 94; New Delhi: ASI) — https://vedamsbooks.com/books/excavations_at_piprahwa_and_ganwaria
- `takahashi2005_maheth_palace` [unknown]: 高橋隆博, 高橋誠一, 木庭元晴, 薮田貫, 中谷伸生, 米田文孝, 山岡泰造, 『インド共和国マヘート(舎衛城)遺跡の研究: 王宮地区の調査』 (KAKEN research report, Kansai University) — https://cir.nii.ac.jp/crid/1970867909840952262
- `verardi2002_gotihawa_survey` [book]: Verardi, Giovanni (with K.P. Acharya), Excavations at Gotihawa and a Territorial Survey in Kapilavastu District of Nepal: A Preliminary Report (LIRI Occasional Papers 2; Lumbini: Lumbini International Research Institute) — https://zenon.dainst.org/Record/000227532
- `verardi2007_gotihawa_pipri` [book]: Verardi, Giovanni, with F. Barba, Excavations at Gotihawa and Pipri, Kapilbastu District, Nepal (IsIAO Reports and Memoirs; Rome: IsIAO / Lumbini International Research Institute / Univ. of Naples 'L'Orientale') — https://zenon.dainst.org/Record/000789420

**Magadha (juan 8–9)**

- `asher1986_rajaona` [paywall]: Asher, Frederick M. "Sculptures from Rajaona, Valgudar and Jaynagar: Evidence for an Urban Center". East and West 36, no. 1–3 (1986): 227–246 — https://www.jstor.org/stable/29756765
- `asher2000_lakhiserai` [paywall]: Asher, Frederick M. "An Image at Lakhi Serai and Its Implications". Artibus Asiae 59, no. 3/4 (2000): 296–302. doi:10.2307/3249882 — https://doi.org/10.2307/3249882
- `choudhary2023_telhara` [book]: Choudhary, Bijoy Kumar; Arun Kumar; Oishi Roy; Amit Ranjan. Sri Prathamasivapura Mahavihara: Excavating an Early Medieval Buddhist Monastery at Telhara in Magadh (Eastern India) 2020–2022. Patna: Bihar Heritage Development Society, c. 2023. ISBN 978-81-961222-4-9 — https://en.wikipedia.org/wiki/Telhara_monastery
- `desimone_bodhgaya_excavations` [unknown]: De Simone, Daniela (with Abhishek Singh Amar and Vishi Upadhyay), Excavations at Bodhgaya, the Site of the Buddha's Enlightenment: The Mahabodhi Temple, Taradih Monastery and Bakraur Stupa (book project; Harvard White-Levy programme; status unverified) — https://whitelevy.fas.harvard.edu/excavations-bodhgaya-site-buddha%E2%80%99s-enlightenment-mahabodhi-temple-taradih-monastery-and
- `kumar2011_krimila` [paywall]: Kumar, Anil. "Kṛimilā: A Forgotten Adhiṣṭhāna of Early Medieval Eastern India". Indian Historical Review 38, no. 1 (2011): 23–50 — https://journals.sagepub.com/home/ihr
- `kumar2018_lalpahari` [book]: Kumar, Anil. "The Excavated Remains of a Buddhist Nunnery (Matha) at Lal Pahari (Jainagar), District Lakhisarai, Bihar: 2017–18". Bharati (Bulletin of the Dept. of AIHC & Archaeology, BHU) 42 (2018): 107–131 — https://bhu.ac.in/
- `kumar2019_lalpahari` [book]: Kumar, Anil. "Excavation at Lalpahari (Lakhisarai, Bihar) 2018–2019". In Interrogating Early India: Evolving Perspectives, 26–48. Kolkata, 2019 — https://www.visvabharati.ac.in/
- `prasad1988_sariputra` [paywall]: Prasad, Chandra Shekhar. "Nalanda vis-à-vis the Birthplace of Śāriputra". East and West 38, no. 1–4 (1988): 175–188 — https://www.jstor.org/journal/eastwest
- `sanyal2016_telhara` [unknown]: Sanyal, Rajat. "Discovery of a Buddhist Monastery at Telhara". Monthly Bulletin of the Asiatic Society (Kolkata), 2016 — https://www.academia.edu/43992861
- `saran2008_juafardih` [book]: Saran, S. C. "Excavation at Juafardih and its Identification with Kulika". Purātattva 38 (2008): 59–73
- `verma2010_telhara` [unknown]: Verma, Atul Kumar. "Telhara (Nalanda) Excavation – A Brief Report". Patna: Directorate of Archaeology, Department of Art, Culture and Youth, Government of Bihar (yac.bih.nic.in), c. 2010–13 — https://web.archive.org/web/20140628083818/http://yac.bih.nic.in/Documents/Telhara-(Nalanda)-Excavation-Report.pdf

**East, South and West India, Sindh (juan 10–11)**

- `alam2001_mahasthan` [book]: Alam, Md. Shafiqul & Jean-François Salles (eds.), France-Bangladesh Joint Venture Excavations at Mahasthangarh: First Interim Report 1993–1999. Dhaka: Department of Archaeology, Ministry of Cultural Affairs, 2001. 495 pp. — https://zenon.dainst.org/Record/000107148
- `chakrabarti2001_gangaplain` [book]: Chakrabarti, Dilip K., Archaeological Geography of the Ganga Plain: The Lower and the Middle Ganga. Delhi: Permanent Black, 2001. — https://search.worldcat.org/search?q=Archaeological%20Geography%20of%20the%20Ganga%20Plain%20Lower%20and%20Middle%20Ganga
- `cohen2006_ajantainscr` [paywall]: Cohen, Richard S., 'Appendix: Ajanta's Inscriptions', in Walter M. Spink, Ajanta: History and Development, vol. 2. Leiden: Brill, 2006, pp. 273–339. — https://brill.com/display/title/12396
- `hikosaka1989_tamilnadu` [book]: Hikosaka, Shu, Buddhism in Tamil Nadu: A New Perspective. Madras: Institute of Asian Studies, 1989. — https://search.worldcat.org/search?q=Buddhism%20in%20Tamil%20Nadu%3A%20A%20New%20Perspective%20Hikosaka
- `langudi_excavations` [unknown]: Pradhan, Debraj [and colleagues], reports on the Langudi hill excavations (Kayama/Deuli/Langudi, Jajpur), Orissa Institute of Maritime and South East Asian Studies / Odisha State Archaeology, c. 1996–2006 (incl. inscribed stupa fragments read as Aśokan). [exact titles to verify] (citation from memory; verify) — https://search.worldcat.org/search?q=Langudi%20excavation%20Pushpagiri%20Pradhan
- `pradeep2025_valabhi` [paywall]: Pradeep, A.S. and M.B. Rajani, 'Ancient Valabhi: A Remote Sensing Perspective', Journal of the Indian Society of Remote Sensing 53 (2025): 1765-1783, doi:10.1007/s12524-024-02087-7 — https://doi.org/10.1007/s12524-024-02087-7
- `prusty1993_langudi` [paywall]: Prusty, Harish Chandra & Pradeep Mohanty, 'Langudi: A Unique Rock-cut Buddhist Site in Orissa', Bulletin of the Deccan College Research Institute 53 (1993): 325–327. JSTOR 42936452. — https://www.jstor.org/stable/42936452
- `sharma_sirpur` [book]: Sharma, Arun Kumar, Excavations at Sirpur, Chhattisgarh 2000–2012: Antiquities (and associated reports on Sirpur). New Delhi: Aryan Books International, c. 2014. [year to verify] (citation from memory; verify) — https://www.exoticindiaart.com/book/details/excavations-at-sirpur-2000-2012-antiquities-uap796/
- `spink2005_ajanta` [paywall]: Spink, Walter M., Ajanta: History and Development. 7 vols. Handbook of Oriental Studies 2.18. Leiden: Brill, 2005–2017. — https://brill.com/display/serial/HO2-18
- `suvrathan2014_banavasi_sacred` [paywall]: Suvrathan, Uthara, 'Spoiled for Choice? The Sacred Landscapes of Ancient and Early Medieval Banavasi', South Asian Studies 30.2 (2014): 206-229, doi:10.1080/02666030.2014.962317 — https://doi.org/10.1080/02666030.2014.962317

Medium-relevance books and paywalled items (154) are listed in `data/literature.tsv` (status `wanted`); get them after these.

### From earlier passes (`FOLLOWUPS.md`, `PLAN.md`)

Kept by hand; `wanted_md.py` prints only the lists above. These come from the work before the recent-scholarship pass.

**Obtained 2026-11-12** (Internet Archive OCR, in `data/ref/ia/`, listed in its `SOURCES.tsv`; not yet coded):
- Burgess & Bhagwanlal Indraji, *Inscriptions from the Cave-Temples of Western India* (1881): the Ajanta Cave 26
  inscription naming the *sthavira* Acala (11.03.03), which the note cites from general knowledge.
- *Indian Antiquary* 19 (1890), with Fleet's Mahākūṭa pillar inscription of Maṅgaleśa: Ji's Coliya.
- *Gazetteer of the Hazara District* 1883–84 and 1907: none was in the gazetteer set; Hargreaves cites one for
  Mangali = Uraśā.
- Marquart, *Ērānšahr* (1901), another scan (IA `Eranshahr`) for Zumathān (鋭秣陀). Its OCR keeps more of the Arabic
  than the one judged unreadable, but is still rough.
- Kuwayama 1985, listed as not online in `FOLLOWUPS.md`, is on disk as `kuwayama1985_bamiyan_two_roads` (if that is
  the paper meant there). Li Rongxi's translation (`PLAN.md`) is `li1996_great_tang_record`.

**Still wanted**
- Bakker, *The Alkhan* (2020): not open access; only a 10-page excerpt is on disk.
- Bakker 2014 on Śaṅkukarṇa at Banbhore, cited in SP IV p. 55 n. 133 (probably *The World of the Skandapurāṇa*,
  Leiden: Brill, 2014; check).
- Marquis's identifications of 提謂城 and 波利城 near Balkh (01.32.02): known only from slides without names or
  coordinates; a publication is needed.
- Mirchandani 1967, *JIH* 45: pp. 312–313 and 348–349 are missing from the OCR (IA `dli.bengal.10689.12681`).
- Stein, MASI 37 (1929): the OCR used stops at about p. 64, before the Tor-dherai stūpa and Konow's appendix. The two
  other IA scans (`in.ernet.dli.2015.70429`, `in.gov.ignca.21977`) carry about as little text (c. 41 KB each), so
  they are probably no better; the page images may be.
- CII IV.2 (djvu only, no text); *Epigraphia Indica* vols 37 onwards (not online as text).
- Cited by Ji et al. (1985), not in these sources: Srivastava, "Kapilavastu and its precise location", *East and
  West* 29 (1979) 61–74 (JSTOR); N. Ahmed's Mahasthan report (Bhasu Vihar, 10.04.02); B. P. Sinha, *Archaeology and
  Art of India* (1979); Belenitskii et al., *Srednevekovyi gorod Srednei Azii* (1973), for Khanabad (01.08);
  Stavisky, *Kushanskaya Baktriya* (1977); 内田吟風 1972; 謝方, 南亞研究 1982/2; Tugusheva 1980 (Uighur *Life*);
  Huang Wenbi on Zanguya (12.22.06) and Shisbir (12.22a).
- For the original names: Yoshida's review of BD I (BAI XIV, 2000 [2003], pp. 154–9) and his reviews in BSOAS 76
  (2013) and IIJ 68 (2025) (paywalled; logins failed); Enoki 1951/1992 (not online); Bailey's Khotanese for
  Ditkabani (地迦婆縛那).
- Nayanjot Lahiri, *Finding Forgotten Cities* (2005), on how Cunningham made his identifications (`PLAN.md`).
- IAR 2001–02 to 2006–07, 2008–09 and 2014 onwards (see "Gaps").
