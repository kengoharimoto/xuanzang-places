"""Join Mizutani's per-page Vision OCR into one text with page markers, and index running heads.

Usage: python3 mizutani_join.py <vision_dir> <out_txt> <out_heads_tsv>
Book page = printed page number from the running head when present; pdf page = scan index.
"""
import re, sys, pathlib
vis, out_txt, out_tsv = map(pathlib.Path, sys.argv[1:4])
KANJI = '〇一二三四五六七八九十'
heads, parts = [], []
for p in sorted(vis.glob('p*.txt')):
    pdf = int(p.stem[1:])
    lines = p.read_text().split('\n')
    top = ' '.join(lines[:3])
    m = re.search(r'巻([一二三四五六七八九十]+)\s*[・･.]?\s*([' + KANJI + r'・･\s=]+?)\s*([^\s\d]{1,20})', top)
    pg = re.search(r'(?:^|\s)(\d{1,3})(?:\s|$)', top)
    heads.append((pdf, pg.group(1) if pg else '', m.group(0) if m else ''))
    parts.append(f'\n<<pdf {pdf:03d} | p. {pg.group(1) if pg else "?"}>>\n' + '\n'.join(lines))
out_txt.write_text(''.join(parts))
out_tsv.write_text('pdf\tprinted\trunning_head\n' + ''.join(f'{a}\t{b}\t{c}\n' for a, b, c in heads))
