# -*- coding: utf-8 -*-
"""
Shared building blocks for generating the CHELA Industrial site as flat,
build-step-free HTML files (Tailwind via CDN, trilingual DE/EN/TR content
rendered inline and toggled with the existing setLang() pattern) — matching
the existing repo's index.html / about/index.html style exactly, just
extended to the new pages/design.
"""

LANGS = ['de', 'en', 'tr']

SITE_URL = 'https://www.chela-industrial.de'
SITE_NAME = 'CHELA Industrial'
OG_IMAGE = f'{SITE_URL}/assets/logo-navy.png'

# Both site forms (contact + partnership) submit here. Configured on the
# Formspree side to deliver to info@chela-industrial.de. Free tier, no
# card required; see the "CHELA Website Forms" form in the Formspree
# dashboard (project "My First Project") if this ever needs to change.
FORMSPREE_ENDPOINT = 'https://formspree.io/f/xwlkqqkb'

INK_950 = '#101820'
INK_900 = '#182533'
PAPER_50 = '#f5f5f6'
SLATE_700 = '#495159'
SLATE_600 = '#63686d'
SLATE_400 = '#999da2'
SLATE_300 = '#c7c9cb'
LINE = '#e2e3e5'


def L(de, en, tr):
    """A trilingual content dict."""
    return {'de': de, 'en': en, 'tr': tr}


def lang_nodes(content, tag='span', cls='', display='inline'):
    """
    Render one element per language, all present in the DOM, toggled by the
    site's existing setLang() script. `display` picks which CSS hook makes
    the *active* one visible with the right box type: 'inline', 'block',
    'inline-flex', or 'flex'.
    """
    display_cls = {
        'inline': '',
        'block': 'lang-block',
        'inline-flex': 'lang-inline-flex',
        'flex': 'lang-flex',
    }[display]
    parts = []
    for lang in LANGS:
        active = ' lang-active' if lang == 'de' else ''
        classes = f'lang-content {lang}{active} {display_cls} {cls}'.split()
        class_attr = ' '.join(dict.fromkeys(classes))  # de-dupe, keep order
        parts.append(f'<{tag} class="{class_attr}">{content[lang]}</{tag}>')
    return '\n'.join(parts)


LANG_STYLE = """
        .lang-content { display: none; }
        .lang-content.lang-active { display: inline; }
        .lang-content.lang-block.lang-active { display: block; }
        .lang-content.lang-inline-flex.lang-active { display: inline-flex; }
        .lang-content.lang-flex.lang-active { display: flex; }
"""

LANG_SCRIPT = """
    <script>
        function setLang(lang) {
            document.querySelectorAll('.lang-content').forEach(el => el.classList.remove('lang-active'));
            document.querySelectorAll('.lang-content.' + lang).forEach(el => el.classList.add('lang-active'));
            document.documentElement.lang = lang;
            try { localStorage.setItem('chela-lang', lang); } catch (e) {}
        }
        (function () {
            try {
                var saved = localStorage.getItem('chela-lang');
                if (saved && saved !== 'de') { setLang(saved); }
            } catch (e) {}
        })();

        function toggleMobileMenu() {
            var menu = document.getElementById('mobile-menu');
            var btn = document.getElementById('mobile-menu-btn');
            var iconOpen = document.getElementById('menu-icon-open');
            var iconClose = document.getElementById('menu-icon-close');
            if (!menu || !btn) return;
            var isOpen = !menu.classList.contains('hidden');
            menu.classList.toggle('hidden');
            btn.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
            if (iconOpen) iconOpen.classList.toggle('hidden');
            if (iconClose) iconClose.classList.toggle('hidden');
            document.body.classList.toggle('overflow-hidden', !isOpen);
        }
        // Close the mobile menu automatically if the viewport is widened past
        // the mobile breakpoint (e.g. rotating a tablet, resizing a window).
        window.addEventListener('resize', function () {
            var menu = document.getElementById('mobile-menu');
            if (menu && window.innerWidth >= 1024 && !menu.classList.contains('hidden')) {
                toggleMobileMenu();
            }
        });

        // The contact and "become a partner" forms submit to Formspree
        // (https://formspree.io/f/...) via a background fetch() so the
        // visitor never leaves the page. On success we show an inline
        // confirmation; if the request fails for any reason, we show an
        // error note with a mailto: fallback so the message is never
        // silently lost.
        function submitForm(event, endpoint) {
            event.preventDefault();
            var form = event.target;
            var btn = form.querySelector('button[type="submit"]');
            var noteOk = form.querySelector('.submit-note-ok');
            var noteError = form.querySelector('.submit-note-error');
            if (noteOk) noteOk.hidden = true;
            if (noteError) noteError.hidden = true;
            if (btn) btn.disabled = true;
            var data = new FormData(form);
            fetch(endpoint, {
                method: 'POST',
                body: data,
                headers: { 'Accept': 'application/json' }
            }).then(function (response) {
                if (response.ok) {
                    if (noteOk) noteOk.hidden = false;
                    form.reset();
                } else {
                    if (noteError) noteError.hidden = false;
                }
            }).catch(function () {
                if (noteError) noteError.hidden = false;
            }).finally(function () {
                if (btn) btn.disabled = false;
            });
            return false;
        }
    </script>
"""

FONT_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com">\n' \
    '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n' \
    '    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">'

BASE_FONT_STYLE = """
        body { font-family: 'IBM Plex Sans', system-ui, sans-serif; }
        .font-display { font-family: 'Space Grotesk', system-ui, sans-serif; }
"""

# NAV_ITEMS: key -> label L() ; 'partnership' also carries the dropdown children
NAV_LABELS = {
    'home': L('Home', 'Home', 'Anasayfa'),
    'about': L('Über uns', 'About', 'Hakkımızda'),
    'services': L('Leistungen', 'Services', 'Hizmetler'),
    'partnership': L('Partnerschaft', 'Partnership', 'Ortaklık'),
    'contact': L('Kontakt aufnehmen', 'Contact', 'İletişim'),
}

PARTNERSHIP_SUB = [
    ('/partnership/pera', L('PERA Mühendislik — Aufzugstechnik', 'PERA Mühendislik — Elevator Technology', 'PERA Mühendislik — Asansör Teknolojisi')),
    ('/partnership/industries', L('Andere Branchen', 'Other Industries', 'Diğer Sektörler')),
    ('/partnership/partner', L('Partner werden', 'Become a Partner', 'Partner Olun')),
]

PARTNERSHIP_GROUP = {'partnership', 'pera', 'industries', 'partner-form'}


def nav_html(active):
    """active: one of home/about/services/partnership/pera/industries/partner-form/contact/legal"""
    is_partnership_active = active in PARTNERSHIP_GROUP

    def link_classes(key, is_active):
        base = 'text-sm font-bold uppercase tracking-widest pb-1 border-b-2 transition-colors'
        if is_active:
            return f'{base} text-[{INK_900}] border-[{INK_900}]'
        return f'{base} text-[{SLATE_700}] border-transparent hover:text-[{INK_900}]'

    links = []
    for key in ['home', 'about', 'services']:
        href = '/' if key == 'home' else f'/{key}'
        is_active = (active == key)
        links.append(
            f'<a href="{href}" class="{link_classes(key, is_active)}">'
            f'{lang_nodes(NAV_LABELS[key])}</a>'
        )

    # Partnership: a plain link to the landing page (which itself links on to
    # the PERA / industries / partner-form subpages) — no hover dropdown.
    links.append(
        f'<a href="/partnership" class="{link_classes("partnership", is_partnership_active)}">'
        f'{lang_nodes(NAV_LABELS["partnership"])}</a>'
    )

    nav_links_html = '\n'.join(links)

    # Mobile menu gets its own stacked, full-width copy of the same links
    # (block display, larger tap targets) plus the contact CTA — everything
    # that's hidden on small screens in the desktop bar above.
    mobile_links = []
    for key in ['home', 'about', 'services']:
        href = '/' if key == 'home' else f'/{key}'
        is_active = (active == key)
        mobile_links.append(
            f'<a href="{href}" class="{link_classes(key, is_active)} block py-3 border-b border-[{LINE}]">'
            f'{lang_nodes(NAV_LABELS[key])}</a>'
        )
    mobile_links.append(
        f'<a href="/partnership" class="{link_classes("partnership", is_partnership_active)} block py-3 border-b border-[{LINE}]">'
        f'{lang_nodes(NAV_LABELS["partnership"])}</a>'
    )
    mobile_links_html = '\n'.join(mobile_links)

    return f'''
    <nav class="bg-white shadow-md sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="/" class="flex items-center shrink-0">
                <img src="/assets/logo-navy.png" alt="CHELA Industrial UG" width="121" height="32" style="height:32px; width:auto;">
            </a>
            <div class="flex items-center gap-4 lg:gap-8">
                <div class="hidden lg:flex items-center gap-7">
                    {nav_links_html}
                </div>
                <div class="flex gap-2 text-xs font-black lg:border-l pl-0 lg:pl-6">
                    <button onclick="setLang('de')" class="hover:text-[{INK_900}] px-1 py-1">DE</button>
                    <button onclick="setLang('en')" class="hover:text-[{INK_900}] px-1 py-1">EN</button>
                    <button onclick="setLang('tr')" class="hover:text-[{INK_900}] px-1 py-1">TR</button>
                </div>
                <a href="/contact" class="hidden lg:inline-block px-5 py-2.5 rounded-md bg-[{INK_950}] text-white font-semibold text-sm hover:bg-[{INK_900}] transition-colors">{lang_nodes(NAV_LABELS['contact'])}</a>
                <button type="button" id="mobile-menu-btn" onclick="toggleMobileMenu()" aria-label="Menu" aria-controls="mobile-menu" aria-expanded="false"
                    class="lg:hidden inline-flex items-center justify-center w-10 h-10 rounded-md border border-[{LINE}] text-[{INK_900}] shrink-0">
                    <svg id="menu-icon-open" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                    <svg id="menu-icon-close" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="hidden"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
            </div>
        </div>
        <div id="mobile-menu" class="hidden lg:hidden border-t border-[{LINE}] bg-white max-h-[calc(100vh-64px)] overflow-y-auto">
            <div class="max-w-6xl mx-auto px-6 py-2 flex flex-col">
                {mobile_links_html}
                <a href="/contact" class="mt-4 mb-2 px-5 py-3 rounded-md bg-[{INK_950}] text-white font-semibold text-sm text-center hover:bg-[{INK_900}] transition-colors">{lang_nodes(NAV_LABELS['contact'])}</a>
            </div>
        </div>
    </nav>
'''


FOOTER_TAGLINE = L(
    'Handel &amp; Projektvermittlung für die Industrie. Ihr strategischer Partner im globalen Industriesektor.',
    'Trade &amp; project mediation for industry. Your strategic partner in the global industrial sector.',
    'Endüstri için ticaret ve proje arabuluculuğu. Küresel endüstriyel sektördeki stratejik ortağınız.',
)
FOOTER_IMPRESSUM_LABEL = L('Impressum', 'Legal Notice', 'Yasal Bilgiler')
FOOTER_CONTACT_LABEL = L('Kontakt', 'Contact', 'İletişim')
FOOTER_LEGAL_LABEL = L('Rechtliches', 'Legal', 'Hukuki')
FOOTER_MANAGING_DIRECTOR = L('Geschäftsführer: Durukan Kürüm', 'Managing Director: Durukan Kürüm', 'Genel Müdür: Durukan Kürüm')
FOOTER_RIGHTS = L('© 2026 CHELA Industrial UG. Alle Rechte vorbehalten.', '© 2026 CHELA Industrial UG. All rights reserved.', '© 2026 CHELA Industrial UG. Tüm hakları saklıdır.')
FOOTER_PRIVACY_LABEL = L('Datenschutzerklärung', 'Privacy Policy', 'Gizlilik Politikası')
LINKEDIN_URL = 'https://www.linkedin.com/company/chela-industrial'
LINKEDIN_ICON = '''<svg viewBox="0 0 24 24" width="17" height="17" fill="currentColor" aria-hidden="true">
                            <path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.11 1 2.48 1s2.5 1.12 2.5 2.5zM.24 8.25h4.47V23H.24V8.25zM8.24 8.25h4.29v2.01h.06c.6-1.13 2.06-2.32 4.24-2.32 4.53 0 5.37 2.98 5.37 6.86V23h-4.47v-6.43c0-1.53-.03-3.5-2.13-3.5-2.14 0-2.47 1.67-2.47 3.39V23H8.24V8.25z"></path>
                        </svg>'''

# Sitewide keyword baseline (trilingual) — merged with any page-specific
# `keywords=` passed to page_html() into a single combined <meta
# name="keywords"> tag. Google itself ignores this tag, but plenty of other
# search engines, directories and AI/LLM crawlers still parse it, and it
# costs nothing to cover DE/EN/TR (and the PERA elevator-technology
# vocabulary) on every single page rather than only the pages that mention
# it explicitly.
SITE_KEYWORDS = L(
    'CHELA Industrial, Internationaler Handel, Projektvermittlung, B2B-Beschaffung, Industrieanlagen, '
    'Aufzugstechnik, Personenaufzüge, Lastenaufzüge, Panoramaaufzüge, Hydraulikaufzüge, '
    'Fahrzeugaufzüge, Aufzugsmodernisierung, Aufzugswartung, PERA Mühendislik, Deutschland Türkei Handel, '
    'Maschinenbau Handel, Industrievermittlung, Handelsvermittler Deutschland',
    'CHELA Industrial, international trade, project mediation, B2B sourcing, industrial equipment trade, '
    'elevator technology, passenger elevators, freight elevators, panoramic elevators, '
    'hydraulic elevators, vehicle elevators, elevator modernization, elevator maintenance, PERA Mühendislik, '
    'Germany Turkey trade, industrial machinery sourcing, trade intermediary Germany',
    'CHELA Industrial, uluslararası ticaret, proje aracılığı, B2B tedarik, endüstriyel ekipman ticareti, '
    'asansör teknolojisi, yolcu asansörleri, yük asansörleri, panoramik asansörler, '
    'hidrolik asansörler, araç asansörleri, asansör modernizasyonu, asansör bakımı, PERA Mühendislik, '
    'Almanya Türkiye ticareti, endüstriyel makine tedariki, Almanya ticaret aracısı',
)


def _keywords_content(page_keywords=None):
    langs = ['de', 'en', 'tr']
    parts = []
    for lang in langs:
        combined = SITE_KEYWORDS[lang]
        if page_keywords:
            combined = f'{page_keywords[lang]}, {combined}'
        # De-dupe terms within each language chunk (case-insensitive),
        # keeping the page-specific ones first — avoids the tag reading as
        # repetitive keyword-stuffing when a page's own terms overlap with
        # the sitewide baseline.
        seen = set()
        terms = []
        for term in combined.split(', '):
            key = term.strip().lower()
            if key and key not in seen:
                seen.add(key)
                terms.append(term.strip())
        parts.append(', '.join(terms))
    return ' | '.join(parts)


# Sitewide Organization structured data (JSON-LD) — included on every page via
# page_html() so search engines *and* AI/LLM crawlers get consistent,
# machine-readable facts about the company on every URL, not just the home
# page. `inLanguage` and `knowsAbout` spell out — for crawlers and AI models
# alike — that the site is trilingual and exactly which elevator
# and trade topics it covers (mirroring PERA Mühendislik's own product range:
# https://peramuhendislik.com/), not just in English.
ORG_JSON_LD = f'''<script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "{SITE_NAME}",
      "legalName": "CHELA Industrial UG (haftungsbeschränkt)",
      "url": "{SITE_URL}",
      "logo": "{OG_IMAGE}",
      "email": "info@chela-industrial.de",
      "description": "Strategic interface for international industrial trade and project mediation, and the exclusive EU sourcing partner of PERA Mühendislik for elevator technology.",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Erfweiler Straße 12",
        "addressLocality": "Dahn",
        "postalCode": "66994",
        "addressCountry": "DE"
      }},
      "areaServed": ["Germany", "Turkey", "Balkans", "European Union"],
      "knowsLanguage": ["de", "en", "tr"],
      "inLanguage": ["de", "en", "tr"],
      "knowsAbout": [
        "International industrial trade", "Project mediation", "B2B sourcing",
        "Elevator technology", "Conveying technology", "Passenger elevators",
        "Freight elevators", "Panoramic elevators", "Hydraulic elevators",
        "Vehicle elevators", "Elevator modernization", "Elevator maintenance",
        "PERA Mühendislik", "Aufzugstechnik", "Asansör teknolojisi"
      ],
      "sameAs": ["{LINKEDIN_URL}"]
    }}
    </script>'''


def footer_html():
    return f'''
    <footer class="bg-[{INK_950}] text-[{SLATE_300}] py-16 px-6">
        <div class="max-w-6xl mx-auto flex flex-col gap-12">
            <div class="flex flex-col md:flex-row justify-between gap-10 pb-11 border-b border-white/10">
                <div class="max-w-xs flex flex-col gap-4">
                    <img src="/assets/logo-white.png" alt="CHELA Industrial UG" width="129" height="34" style="height:34px; width:129px; object-fit:contain; align-self:flex-start; flex-shrink:0; display:block;">
                    <p class="text-sm leading-relaxed">{lang_nodes(FOOTER_TAGLINE, tag='span', display='block')}</p>
                    <a href="{LINKEDIN_URL}" target="_blank" rel="noopener" aria-label="LinkedIn"
                       class="inline-flex items-center justify-center w-9 h-9 rounded-md border border-white/15 text-white hover:bg-white/10 hover:border-white/30 transition-colors">
                        {LINKEDIN_ICON}
                    </a>
                </div>
                <div class="flex flex-wrap gap-12">
                    <div class="flex flex-col gap-3.5">
                        <a href="/impressum" class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_400}] hover:text-white">{lang_nodes(FOOTER_IMPRESSUM_LABEL)}</a>
                        <div class="flex flex-col gap-1.5 text-sm leading-relaxed">
                            <span class="text-white font-semibold">CHELA Industrial UG</span>
                            <span>(haftungsbeschränkt)</span>
                            <span>Erfweiler Straße 12</span>
                            <span>66994 Dahn, Deutschland</span>
                        </div>
                    </div>
                    <div class="flex flex-col gap-3.5">
                        <div class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_400}]">{lang_nodes(FOOTER_CONTACT_LABEL)}</div>
                        <div class="flex flex-col gap-1.5 text-sm leading-relaxed">
                            <a href="mailto:info@chela-industrial.de" class="hover:text-white">info@chela-industrial.de</a>
                        </div>
                    </div>
                    <div class="flex flex-col gap-3.5">
                        <div class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_400}]">{lang_nodes(FOOTER_LEGAL_LABEL)}</div>
                        <div class="flex flex-col gap-1.5 text-sm leading-relaxed">
                            <span>{lang_nodes(FOOTER_MANAGING_DIRECTOR, display='block')}</span>
                            <span>Handelsregister Amtsgericht Zweibrücken</span>
                            <span>HRB 33566</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                <span class="text-xs text-[{SLATE_400}]">{lang_nodes(FOOTER_RIGHTS)}</span>
                <div class="flex gap-6">
                    <a href="/impressum" class="text-xs text-[{SLATE_400}] hover:text-white">{lang_nodes(FOOTER_IMPRESSUM_LABEL)}</a>
                    <a href="/datenschutz" class="text-xs text-[{SLATE_400}] hover:text-white">{lang_nodes(FOOTER_PRIVACY_LABEL)}</a>
                </div>
            </div>
        </div>
    </footer>
'''


def page_html(active_nav, title, description, canonical_path, body_html, extra_head='', json_ld='', keywords=None):
    """
    active_nav: nav-highlight key (see nav_html)
    title / description: trilingual L() dicts, rendered into <title> etc. using
      the DE copy for the actual <title>/<meta> tags (search engines see the
      German version as canonical; the on-page toggle is a UX layer on top).
    canonical_path: e.g. '/', '/about', '/partnership/pera'
    json_ld: OPTIONAL extra structured data for this page (e.g. a more
      specific schema), included in addition to the sitewide ORG_JSON_LD
      that every page already gets automatically.
    keywords: OPTIONAL trilingual L() dict of page-specific keywords, merged
      into the sitewide DE/EN/TR keyword baseline (SITE_KEYWORDS).
    """
    canonical = f'{SITE_URL}{canonical_path}'
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="{INK_950}">

    <title>{title['de']}</title>
    <meta name="description" content="{description['de']}">
    <meta name="keywords" content="{_keywords_content(keywords)}">
    <link rel="canonical" href="{canonical}" />

    <!-- The DE/EN/TR content all lives on this one URL (client-side toggle),
         so all three hreflang tags — plus x-default — point back at the same
         canonical address. That's the recognized pattern for telling search
         engines a single-URL, JS-toggled page serves multiple languages. -->
    <link rel="alternate" hreflang="de" href="{canonical}" />
    <link rel="alternate" hreflang="en" href="{canonical}" />
    <link rel="alternate" hreflang="tr" href="{canonical}" />
    <link rel="alternate" hreflang="x-default" href="{canonical}" />

    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{SITE_NAME}">
    <meta property="og:title" content="{title['de']}">
    <meta property="og:description" content="{description['de']}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{OG_IMAGE}">
    <meta property="og:locale" content="de_DE">
    <meta property="og:locale:alternate" content="en_US">
    <meta property="og:locale:alternate" content="tr_TR">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title['de']}">
    <meta name="twitter:description" content="{description['de']}">
    <meta name="twitter:image" content="{OG_IMAGE}">

    {ORG_JSON_LD}
    {json_ld}
    {FONT_LINK}
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
{LANG_STYLE}
{BASE_FONT_STYLE}
    </style>
    {extra_head}
</head>
<body class="bg-[{PAPER_50}] text-[{INK_900}]">
{nav_html(active_nav)}
{body_html}
{footer_html()}
{LANG_SCRIPT}
</body>
</html>
'''
