# Xuanzang's places: plan (not yet started)

The question: where are the countries and sites of the *Da Tang Xiyu ji* (大唐西域記)? Collect the identifications that
scholars have proposed, mark which are agreed and which disputed, and test the disputed ones against the British
Indian gazetteers. Update the identifications where the gazetteers add something. Agreed with the user on
2026-11-05. Work happens in its own session and folder (`xuanzang-places/`).

## Sources

**Text**
- Taishō 2087: `/mnt2/kengo/E-texts/6_other_languages/xuanzang_datang-xiyuji_t2087.txt` and `大唐西域記.txt`
  (also `xiyuji.html`).
- Huili's *Life* (慈恩伝): `/mnt2/kengo/E-texts/6_other_languages/大唐大慈恩寺三藏法師傳.txt`. Use it for the route and
  for which places he actually visited.

**Main reference: Mizutani Shinjō's translation, "大唐西域記. 水谷真成訳.pdf"** (Heibonsha, 中国古典文学大系 22, 1971;
reissued in 東洋文庫). It was not found on `/`, `/mnt` or `/mnt2` on 2026-11-05 (full file index). Ask the user for
the path; it may be on iCloud or the NAS (`/qnap`). The user cancelled a full `find /qnap`, so don't repeat that
search without asking. Check whether the PDF has a text layer; if it does not, it needs Japanese OCR.

**Other translations and identifications already on the machine**
- Beal, *Si-yu-ki*, vols 1–2: `/mnt/staging/data/secondary-literature/Xuanzang Buddhist Records of the Western World
  (Si-Yu-Ki)  Vol.{1,2}_Beal, tr.txt`; also `/mnt2/kengo/dox-text/txt/Books_and_Articles_on_iCloud/Beal Si Yu Ki
  siyukibuddhistr00bealgoog.pdf.txt`.
- Beal, *Life of Hiuen-Tsiang* (1911): `/mnt/staging/data/secondary-literature/Life of Hiuen-Tsiang (Xuanzang) by
  Shaman Hwui Li_Samuel Beal, 1911.txt`.
- Watters, *On Yuan Chwang's Travels*, **vol. 2 only**: `/mnt2/kengo/dox-text/txt/Books_and_Articles_on_iCloud/383-Travels
  in India by Thomas Watters M.r.a.s Vol 2_text.pdf.txt`. Vol. 1 is needed (it is on the Internet Archive).
- Cunningham, *Ancient Geography of India* (1871): `/mnt2/kengo/dox-text/txt/Books_and_Articles_on_iCloud/2015.32009.Cunninghams-Ancient-Geography-Of-India_text.pdf.txt`.
- Kuwayama 1972 and 2000 (Kāpiśī, Kābul) and Kuwayama, *Across the Hindukush* (2002): in the same iCloud folder and
  `/mnt/staging/data/secondary-literature/`.
- Deeg, "Legend and cult" (stūpas, parts 1–2) in `/mnt/staging/data/secondary-literature/`. Also Legge's and Beal's
  *Faxian*, for cross-checks.
- 山口周子 2015 (Siṃhala legend) in `/mnt/staging/data/secondary-literature/japanese-modern/pickles/`.

**To obtain** (from the Internet Archive or the user)
- Julien, *Mémoires sur les contrées occidentales* (1857–58), with Vivien de Saint-Martin's geographical memoir;
- Watters vol. 1;
- Cunningham's ASI *Reports* (vols I–XXIII);
- 季羨林 et al., 大唐西域記校注 (1985) and Li Rongxi's translation (1996);
- N. L. Dey, *Geographical Dictionary of Ancient and Mediaeval India* (1927);
- Nayanjot Lahiri, *Finding Forgotten Cities* (2005), on how Cunningham made his identifications;
- recent site literature as needed (Kapilavastu: Piprahwa or Tilaurakot; Kuśinagara; Kauśāmbī; Karṇasuvarṇa/
  Rajbadidanga; Dhānyakaṭaka; and others).

**Gazetteers:** the gazetteer study's local OCR (about 800 volumes, gitignored, under `gazetteer-vedanta/*/` and
re-fetchable from the `selection*.tsv` tables with `gazetteer-vedanta/scripts/fetch_ia_ocr.py`). On 2026-11-05, 325
volumes matched Xuanzang's name in its old spellings: `hiuen|hwen|thsang|yuan chwang|hiouen` (also try `Hiuen Thsang`,
`Hiouen-Thsang`, `Huen Tsang`, `Yuan Chuang`). Downloads from the Internet Archive must be **sequential**, and only
one session at a time should fetch.

## Steps

1. **Master table** (`data/places.tsv`), one row per country (about 138) and per major named site. Columns:
   - Chinese name, juan, Mizutani's reading and Sanskrit reconstruction;
   - the distance and direction Xuanzang gives from the previous place;
   - 親践 or 伝聞: whether he visited it or reports it from hearsay (Mizutani marks this; cross-check with the *Life*);
   - an identification column with page number for each authority: Julien/Saint-Martin, Cunningham, Beal, Watters,
     Mizutani, 季羨林, and modern work;
   - status: agreed, disputed or unknown.

   Mizutani's notes are the backbone; extract them first.
2. **Gazetteer pass.** Grep every Xuanzang spelling, the reconstructed Sanskrit names and the candidate modern place
   names. Code each passage using the gazetteer study's method: written coding instructions, a verbatim quote with
   page number, quotes checked by script (`gazetteer-vedanta/mathas/scripts/check_quotes.py`). Collect:
   - what the gazetteer says about the identification;
   - local evidence: mounds, ruins, old names, changed river courses, finds, excavations in the revised series;
   - local identifications that the standard authorities don't record.
3. **Disputed cases first.** Write a short note for each disputed site: the competing identifications, then what the
   gazetteers add. Say plainly when they add nothing.
4. **Output.** A report (`README.md`, kept as one current account), the TSV, and a map or places page adapted from
   `gazetteer-vedanta/map/` (`places_data.py`, `build_page.py`).
