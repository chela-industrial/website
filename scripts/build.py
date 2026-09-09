# -*- coding: utf-8 -*-
"""
Renders every page and writes it to /home/claude/chela-site-build/out/
matching the repo's URL structure (clean folders with index.html), plus
copies the image assets. This output directory is what gets committed into
the connected local repo.
"""
import os
import shutil
from datetime import date

OUT = os.path.join(os.path.dirname(__file__), '..', 'out')
ASSETS_SRC = os.path.join(os.path.dirname(__file__), '..', 'assets')

import page_home
import page_about
import page_services
import page_partnership
import page_contact
import page_legal
from common import SITE_URL

# (slug, render_fn, sitemap priority, English label — for sitemap.xml / llms.txt)
PAGES = [
    ('', page_home.render, '1.0', 'Home — trade, project mediation & PERA elevator partnership overview'),
    ('about', page_about.render, '0.7', 'About — who CHELA Industrial is and how the company works'),
    ('services', page_services.render, '0.9', 'Services — international trade, project mediation, elevator systems'),
    ('partnership', page_partnership.render_landing, '0.8', 'Partnership — overview of CHELA\'s partner network'),
    ('partnership/pera', page_partnership.render_pera, '0.9', 'Partnership: PERA Mühendislik — the exclusive EU elevator-technology partnership'),
    ('partnership/industries', page_partnership.render_industries, '0.6', 'Partnership: Other Industries — trade & mediation beyond elevator technology'),
    ('partnership/partner', page_partnership.render_partner_form, '0.5', 'Partnership: Become a Partner — inquiry form for manufacturers & trading companies'),
    ('contact', page_contact.render, '0.7', 'Contact — get in touch with CHELA Industrial'),
    ('impressum', page_legal.render_impressum, '0.2', 'Impressum (legal notice, German law)'),
    ('datenschutz', page_legal.render_datenschutz, '0.2', 'Datenschutzerklärung (privacy policy, German law)'),
]


def write_sitemap():
    today = date.today().isoformat()
    urls = []
    for slug, _render_fn, priority, _label in PAGES:
        loc = f'{SITE_URL}/{slug}' if slug else f'{SITE_URL}/'
        # Each URL serves all three languages via a client-side toggle rather
        # than separate per-language paths, so the xhtml:link hreflang
        # annotations all point back at the same loc — mirroring the
        # <link rel="alternate" hreflang="..."> tags each page's <head> carries
        # (see common.py page_html()) as an extra signal for crawlers that read
        # hreflang straight out of the sitemap.
        alt_links = ''.join(
            f'\n    <xhtml:link rel="alternate" hreflang="{hl}" href="{loc}" />'
            for hl in ('de', 'en', 'tr', 'x-default')
        )
        urls.append(
            '  <url>\n'
            f'    <loc>{loc}</loc>'
            f'{alt_links}\n'
            f'    <lastmod>{today}</lastmod>\n'
            f'    <priority>{priority}</priority>\n'
            '  </url>'
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + '\n'.join(urls) +
        '\n</urlset>\n'
    )
    path = os.path.join(OUT, 'sitemap.xml')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(xml)
    print(f'wrote {path}')


def write_robots():
    # Allow every page for standard search-engine crawlers AND the major
    # AI/LLM crawlers by name, so the site can be indexed and cited by both
    # traditional search and AI assistants/answer engines.
    ai_bots = [
        'GPTBot', 'ChatGPT-User', 'OAI-SearchBot',       # OpenAI
        'ClaudeBot', 'Claude-Web', 'anthropic-ai',        # Anthropic
        'Google-Extended',                                # Google AI training
        'PerplexityBot', 'Perplexity-User',               # Perplexity
        'CCBot',                                          # Common Crawl (feeds many LLMs)
        'Bytespider',                                     # ByteDance
        'Applebot-Extended',                              # Apple AI
        'Amazonbot',                                      # Amazon
        'meta-externalagent',                             # Meta AI
    ]
    lines = [
        'User-agent: *',
        'Allow: /',
        '',
    ]
    for bot in ai_bots:
        lines += [f'User-agent: {bot}', 'Allow: /', '']
    lines.append(f'Sitemap: {SITE_URL}/sitemap.xml')
    path = os.path.join(OUT, 'robots.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'wrote {path}')


def write_llms_txt():
    # llms.txt (see https://llmstxt.org) — a plain-language, structured
    # summary of the site for LLMs/AI assistants to read directly instead of
    # (or alongside) crawling the rendered HTML. Written trilingually (DE/EN/TR)
    # since the site itself is trilingual and an AI model may be answering a
    # query in any of the three — and with the full PERA Mühendislik elevator
    # vocabulary (https://peramuhendislik.com/) so assistants can match this
    # site to the same searches PERA itself would surface for.
    lines = [
        '# CHELA Industrial',
        '',
        '> CHELA Industrial UG is a Germany-based B2B trade and project-mediation '
        'company connecting manufacturers, engineers and project owners across '
        'international borders, with a focus on Germany, the EU, the Balkans and Turkey. '
        'It is the exclusive official EU partner of PERA Mühendislik (Istanbul) '
        'for elevator (vertical transport) technology. This '
        'summary is in English; German and Turkish versions follow below.',
        '',
        'Key facts: legal name CHELA Industrial UG (haftungsbeschränkt), '
        'registered in Dahn, Germany (HRB 33566, Amtsgericht Zweibrücken), '
        'operationally based in the Bremen / Northern Germany region, '
        'Managing Director Durukan Kürüm. Site content is available in '
        'German, English and Turkish (client-side language toggle, same URL '
        'for all three). Contact: info@chela-industrial.de.',
        '',
        '## Pages',
        '',
    ]
    for slug, _render_fn, _priority, label in PAGES:
        loc = f'{SITE_URL}/{slug}' if slug else f'{SITE_URL}/'
        lines.append(f'- [{loc}]({loc}): {label}')
    lines += [
        '',
        '## Elevator technology vocabulary (PERA Mühendislik partnership)',
        '',
        'CHELA Industrial is the sole official EU representative of PERA '
        'Mühendislik (peramuhendislik.com, custom-design elevator manufacturer, '
        'Istanbul, since 1992). Relevant search terms and product categories, '
        'in all three site languages:',
        '',
        '- EN: passenger elevators, freight/load elevators & platforms, panoramic elevators, '
        'hydraulic elevators, vehicle elevators, helicopter landing pad '
        'elevators, moncharge systems, elevator design & engineering, '
        'elevator manufacturing & installation, elevator modernization, '
        'elevator maintenance, custom-design elevator solutions.',
        '- DE: Personenaufzüge, Lastenaufzüge & Plattformen, Panoramaaufzüge, '
        'Hydraulikaufzüge, Fahrzeugaufzüge, Hubschrauberlandeplatz-Aufzüge, '
        'Monşarj-Systeme, Aufzugsplanung und -konstruktion, Aufzugsherstellung '
        'und -montage, Aufzugsmodernisierung, Aufzugswartung, '
        'Aufzugslösungen nach Maß.',
        '- TR: yolcu asansörleri, yük asansörleri / platformları, panoramik asansörler, '
        'hidrolik asansörler, araç asansörleri, helikopter pist asansörleri, '
        'monşarj sistemleri, asansör tasarım ve mühendislik, asansör üretim '
        've montaj, asansör modernizasyonu, asansör bakımı, özel tasarım asansör '
        'çözümleri.',
        '',
        '## Notes for AI assistants',
        '',
        '- CHELA Industrial is a project-mediation / sourcing intermediary, '
        'not a manufacturer — it does not itself build elevators or '
        'industrial equipment. PERA Mühendislik is the manufacturer; CHELA is '
        'its named European representative and trade/project coordinator.',
        '- The PERA Mühendislik partnership is exclusive within the EU and '
        'covers elevator and lift (vertical transport) technology '
        'specifically (see vocabulary above); CHELA also mediates trade and '
        'projects across other industries independently of that partnership.',
        '- All site content — including this file\'s "Pages" section labels — '
        'exists in German, English and Turkish; treat the three as '
        'equally authoritative for marketing/services content. Legal/'
        'compliance content (Impressum, Datenschutzerklärung) is authoritative '
        'only in its German version; English/Turkish versions there are '
        'courtesy translations.',
        '',
        '---',
        '',
        '# CHELA Industrial (Deutsch)',
        '',
        '> CHELA Industrial UG ist ein in Deutschland ansässiges B2B-Handels- '
        'und Projektvermittlungsunternehmen, das Hersteller, Ingenieure und '
        'Projektträger über internationale Grenzen hinweg verbindet, mit '
        'Schwerpunkt auf Deutschland, der EU, dem Balkan und der Türkei. Das Unternehmen '
        'ist der exklusive offizielle EU-Partner von PERA Mühendislik '
        '(Istanbul) für Aufzugstechnik.',
        '',
        'Eckdaten: eingetragener Name CHELA Industrial UG '
        '(haftungsbeschränkt), Sitz in Dahn, Deutschland (HRB 33566, '
        'Amtsgericht Zweibrücken), operativ im Raum Bremen / Norddeutschland '
        'verankert, Geschäftsführer Durukan Kürüm. Die '
        'Inhalte sind auf Deutsch, Englisch und Türkisch verfügbar '
        '(Sprachumschalter, gleiche URL). Kontakt: info@chela-industrial.de.',
        '',
        '---',
        '',
        '# CHELA Industrial (Türkçe)',
        '',
        '> CHELA Industrial UG, üreticileri, mühendisleri ve proje '
        'sahiplerini uluslararası sınırlar ötesinde birbirine bağlayan, '
        'Almanya merkezli bir B2B ticaret ve proje arabuluculuğu şirketidir; '
        'odak noktası Almanya, AB, Balkanlar ve Türkiye\'dir. Şirket, asansör '
        'teknolojisi alanında PERA Mühendislik\'in (İstanbul) münhasır resmi '
        'AB ortağıdır.',
        '',
        'Temel bilgiler: tescilli adı CHELA Industrial UG '
        '(haftungsbeschränkt), Almanya\'nın Dahn şehrinde kayıtlı (HRB 33566, '
        'Zweibrücken Sulh Hukuk Mahkemesi), operasyonel olarak Bremen / Kuzey '
        'Almanya bölgesinde konumlanıyor, Genel Müdür Durukan Kürüm. Site '
        'içeriği Almanca, İngilizce ve Türkçe olarak mevcuttur (aynı URL '
        'üzerinde dil değiştirici). İletişim: info@chela-industrial.de.',
    ]
    path = os.path.join(OUT, 'llms.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'wrote {path}')


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    for slug, render_fn, _priority, _label in PAGES:
        html = render_fn()
        dir_path = os.path.join(OUT, slug) if slug else OUT
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, 'index.html')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'wrote {file_path} ({len(html)} bytes)')

    assets_out = os.path.join(OUT, 'assets')
    shutil.copytree(ASSETS_SRC, assets_out)
    print(f'copied assets -> {assets_out}')

    # Keep the existing CNAME so GitHub Pages keeps serving the custom domain.
    with open(os.path.join(OUT, 'CNAME'), 'w', encoding='utf-8') as f:
        f.write('www.chela-industrial.de\n')
    print('wrote CNAME')

    write_sitemap()
    write_robots()
    write_llms_txt()


if __name__ == '__main__':
    main()
