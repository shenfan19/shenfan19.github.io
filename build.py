"""Build index.html from template.html and papers.bib.

Run `python build.py` after editing template.html or papers.bib, then commit
index.html. Every entry in papers.bib is listed, one line each, newest
first.
"""
import html
import re
import datetime
from pathlib import Path


def entries(text):
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,]+),', text):
        kind = m.group(1).lower()
        if kind == 'string':
            continue
        # walk to the matching closing brace of this entry
        depth, i = 1, m.end()
        while depth and i < len(text):
            depth += {'{': 1, '}': -1}.get(text[i], 0)
            i += 1
        body = text[m.end():i - 1]
        fields = {}
        for f in re.finditer(r'(\w+)\s*=\s*\{', body):
            depth, j = 1, f.end()
            while depth and j < len(body):
                depth += {'{': 1, '}': -1}.get(body[j], 0)
                j += 1
            fields[f.group(1).lower()] = re.sub(r'\s+', ' ', body[f.end():j - 1]).strip()
        yield kind, m.group(2), fields


def clean(s):
    s = s.replace(r'\&', '&').replace('{', '').replace('}', '').replace('--', '–')
    return html.escape(s)


def authors(raw):
    names = [a.strip() for a in raw.split(' and ')]
    out = []
    for n in names:
        if n.lower() == 'others':
            out.append('et al.')
            continue
        last, _, first = n.partition(',')
        first = first.strip()
        initials = ' '.join(p[0] + '.' for p in re.split(r'[\s.]+', first) if p)
        name = clean(f'{initials} {last.strip()}'.strip())
        if (last.strip().lower() == 'shen' and first[:1].upper() == 'F') or n.replace(' ', '') == '沈凡':
            name = f'<b>{name}</b>'
        out.append(name)
    return ', '.join(out)


def publications(path):
    items = []
    text = path.read_text(encoding='utf-8')
    for kind, key, f in entries(text):
        venue = f.get('journal') or f.get('booktitle') or ''
        details = ', '.join(x for x in [
            f"{f['volume']}({f['number']})" if f.get('volume') and f.get('number') else f.get('volume', ''),
            f.get('pages', ''),
        ] if x)
        title = clean(f.get('title', ''))
        if f.get('url'):
            title = f'<a href="{html.escape(f["url"])}">{title}</a>'
        line = f'{authors(f.get("author", ""))}. {title}. <i>{clean(venue)}</i>'
        if details:
            line += f', {clean(details)}'
        line += f', {f.get("year", "")}.'
        items.append((int(f.get('year', 0) or 0), line))
    items.sort(key=lambda x: -x[0])
    return '\n'.join(f'  <li>{line}</li>' for _, line in items)


def main():
    here = Path(__file__).parent
    page = (here / 'template.html').read_text(encoding='utf-8')
    page = page.replace('{{PUBS}}', publications(here / 'papers.bib'))
    page = page.replace('{{UPDATED}}', datetime.date.today().strftime('%B %Y'))
    (here / 'index.html').write_text(page, encoding='utf-8')


main()
