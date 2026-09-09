# -*- coding: utf-8 -*-
from common import L, lang_nodes, page_html, INK_950, INK_900, PAPER_50, SLATE_700, SLATE_600, SLATE_300, LINE

TITLE = L(
    'CHELA Industrial | Handel & Projektvermittlung für die Industrie',
    'CHELA Industrial | Trade & Project Mediation for Industry',
    'CHELA Industrial | Endüstri için Ticaret ve Proje Arabuluculuğu',
)
DESCRIPTION = L(
    'CHELA Industrial verbindet globale Märkte mit deutschem Know-how: internationaler Handel, Projektvermittlung und B2B-Beschaffung über alle Industriezweige hinweg.',
    'CHELA Industrial connects global markets with German expertise: international trade, project mediation and B2B sourcing across all industries.',
    'CHELA Industrial, küresel pazarları Alman uzmanlığıyla buluşturur: tüm sektörlerde uluslararası ticaret, proje arabuluculuğu ve B2B tedarik.',
)
KEYWORDS = L(
    'CHELA Industrial Startseite, Handel und Projektvermittlung, Industriepartner Deutschland, Aufzugstechnik Partner',
    'CHELA Industrial homepage, trade and project mediation, industrial partner Germany, elevator technology partner',
    'CHELA Industrial ana sayfa, ticaret ve proje arabuluculuğu, Almanya endüstri ortağı, asansör teknolojisi ortağı',
)

EYEBROW = L('Internationaler Handel &amp; Projektvermittlung', 'International Trade &amp; Project Mediation', 'Uluslararası Ticaret ve Proje Arabuluculuğu')
H1 = L('Handel &amp; Projektvermittlung für die Industrie.', 'Trade &amp; project mediation for industry.', 'Endüstri için ticaret ve proje arabuluculuğu.')
HERO_SUB = L(
    'Ihr strategischer Partner im globalen Industriesektor — wir verbinden Hersteller, Ingenieure und Projektträger über Grenzen hinweg.',
    'Your strategic partner in the global industrial sector — we connect manufacturers, engineers and project owners across borders.',
    'Küresel endüstriyel sektörde stratejik ortağınız — üreticileri, mühendisleri ve proje sahiplerini sınırların ötesinde buluşturuyoruz.',
)
BTN_SERVICES = L('Leistungen entdecken', 'Discover our services', 'Hizmetlerimizi keşfedin')
BTN_CONTACT = L('Kontakt aufnehmen', 'Get in touch', 'İletişime geçin')

SERVICES_EYEBROW = L('Leistungen', 'Services', 'Hizmetler')
SERVICES_H2 = L(
    'Handel, Vermittlung und B2B-Beschaffung — über alle Industriezweige hinweg.',
    'Trade, mediation and B2B sourcing — across every branch of industry.',
    'Tüm sektörlerde ticaret, arabuluculuk ve B2B tedarik.',
)

SERVICE_CARDS = [
    (
        L('Internationaler Handel', 'International Trade', 'Uluslararası Ticaret'),
        L(
            'Strategische Beschaffung und Vermittlung von Industrieanlagen und -komponenten für globale Märkte.',
            'Strategic sourcing and mediation of industrial equipment and components for global markets.',
            'Küresel pazarlar için endüstriyel tesis ve bileşenlerin stratejik tedariki ve aracılığı.',
        ),
        'trade',
    ),
    (
        L('Projektvermittlung', 'Project Mediation', 'Proje Arabuluculuğu'),
        L(
            'Wir verbinden Hersteller, Lieferanten und Abnehmer über Branchen und Ländergrenzen hinweg.',
            'We connect manufacturers, suppliers and buyers across industries and national borders.',
            'Üreticileri, tedarikçileri ve alıcıları sektörler ve ülke sınırları ötesinde buluşturuyoruz.',
        ),
        'network',
    ),
    (
        L('Aufzugssysteme', 'Elevator Systems', 'Asansör Sistemleri'),
        L(
            'Spezialisierter Handel mit Aufzugstechnik — in Partnerschaft mit PERA Mühendislik.',
            'Specialized trade in elevator technology — in partnership with PERA Mühendislik.',
            'Asansör teknolojisinde uzmanlaşmış ticaret — PERA Mühendislik iş birliğiyle.',
        ),
        'elevator',
    ),
]

ICONS = {
    'trade': '<rect x="7" y="8" width="10" height="9" rx="1"></rect><path d="M9 8V6a3 3 0 0 1 6 0v2"></path><path d="M3 12h2"></path><path d="M19 12h2"></path>',
    'network': '<circle cx="6" cy="7" r="2.2"></circle><circle cx="18" cy="7" r="2.2"></circle><circle cx="12" cy="18" r="2.2"></circle><path d="M7.8 8.6 10.4 16.2"></path><path d="M16.2 8.6 13.6 16.2"></path><path d="M8.2 7h7.6"></path>',
    'elevator': '<rect x="5" y="3" width="14" height="18" rx="1.5"></rect><polyline points="10 9 12 6.5 14 9"></polyline><polyline points="10 15 12 17.5 14 15"></polyline>',
}

PARTNERSHIP_EYEBROW = L('Partnerschaft', 'Partnership', 'Ortaklık')
PARTNERSHIP_H2 = L('Europäische Vertretung für PERA Mühendislik', 'European representation for PERA Mühendislik', 'PERA Mühendislik için Avrupa temsilciliği')
PARTNERSHIP_P = L(
    'CHELA Industrial arbeitet eng mit PERA Mühendislik zusammen — einem türkischen Ingenieurunternehmen für Aufzugstechnik. Als benannter europäischer Vertreter schaffen wir den direkten Zugang zwischen europäischen Projekten und türkischer Aufzugs-Ingenieurskompetenz.',
    'CHELA Industrial works closely with PERA Mühendislik — a Turkish elevator engineering company. As their named European representative, we create direct access between European projects and Turkish elevator engineering expertise.',
    'CHELA Industrial, bir Türk asansör mühendislik şirketi olan PERA Mühendislik ile yakın iş birliği içinde çalışır. Belirlenen Avrupa temsilcisi olarak, Avrupa projeleri ile Türk asansör mühendislik uzmanlığı arasında doğrudan bir bağlantı kuruyoruz.',
)
PARTNERSHIP_LINK = L('Mehr über die Partnerschaft', 'More about the partnership', 'Ortaklık hakkında daha fazla bilgi')

WHY_H2 = L('Warum CHELA Industrial', 'Why CHELA Industrial', 'Neden CHELA Industrial')
WHY_CARDS = [
    (L('International vernetzt', 'Globally connected', 'Küresel bağlantılar'),
     L('Handelsbrücken zwischen Herstellern, Lieferanten und Abnehmern weltweit — mit Schwerpunkt auf Deutschland, der EU, dem Balkan und der Türkei.',
       'Trade bridges between manufacturers, suppliers and buyers worldwide — with a focus on Germany, the EU, the Balkans and Turkey.',
       'Dünya çapında üreticiler, tedarikçiler ve alıcılar arasında ticaret köprüleri — Almanya, AB, Balkanlar ve Türkiye odaklı.')),
    (L('Ingenieursnah', 'Engineering-grounded', 'Mühendislik odaklı'),
     L('Getragen von einer echten Ingenieurpartnerschaft — nicht nur vom Handel.',
       'Backed by a genuine engineering partnership — not trade alone.',
       'Sadece ticaretle değil, gerçek bir mühendislik ortaklığıyla destekleniyor.')),
    (L('Lokale Sprachen', 'Local languages', 'Yerel diller'),
     L('Kommunikation in den jeweiligen lokalen Sprachen — ohne Reibungsverluste.',
       'Communication in local languages — without friction.',
       'İlgili yerel dillerde iletişim — sorunsuz bir şekilde.')),
    (L('Schlank &amp; direkt', 'Lean &amp; direct', 'Yalın ve doğrudan'),
     L('Kurze Wege und ein direkter Draht zum Entscheider.',
       'Short paths and a direct line to the decision-maker.',
       'Kısa yollar ve karar vericiyle doğrudan bağlantı.')),
]

CTA_H2 = L('Bereit für den nächsten Schritt?', 'Ready for the next step?', 'Bir sonraki adıma hazır mısınız?')
CTA_P = L(
    'Sprechen Sie direkt mit uns über Ihr Anliegen — vom internationalen Handel bis zur Projektvermittlung, gleich welche Branche.',
    'Talk to us directly about your project — from international trade to project mediation, whatever your industry.',
    'Projenizi doğrudan bizimle konuşun — uluslararası ticaretten proje arabuluculuğuna, hangi sektörde olursanız olun.',
)


def render():
    cards_html = ''
    for title, desc, icon in SERVICE_CARDS:
        cards_html += f'''
        <div class="bg-white p-8 rounded-xl border border-[{LINE}] flex flex-col gap-4">
            <div class="w-14 h-14 rounded-xl bg-[#eef0f1] text-[{INK_900}] flex items-center justify-center">
                <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</svg>
            </div>
            <h3 class="font-display break-words text-lg font-semibold text-[{INK_950}]">{lang_nodes(title, tag="span", display="block")}</h3>
            <p class="text-[{SLATE_600}] text-sm leading-relaxed">{lang_nodes(desc, tag="span", display="block")}</p>
        </div>'''

    why_html = ''
    for i, (title, desc) in enumerate(WHY_CARDS, start=1):
        why_html += f'''
            <div class="flex flex-col gap-2.5">
                <span class="font-display break-words text-2xl font-bold text-[{INK_900}]">0{i}</span>
                <h3 class="text-base font-semibold text-[{INK_950}]">{lang_nodes(title, tag="span", display="block")}</h3>
                <p class="text-sm leading-relaxed text-[{SLATE_600}]">{lang_nodes(desc, tag="span", display="block")}</p>
            </div>'''

    body = f'''
    <header class="relative overflow-hidden bg-[{INK_950}] text-white py-24 px-6"
      style="background-image:linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size:46px 46px;">
        <div class="relative max-w-6xl mx-auto flex flex-col gap-6">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(EYEBROW)}</span>
            <h1 class="font-display break-words text-4xl md:text-5xl font-bold leading-tight max-w-2xl">{lang_nodes(H1, tag="span", display="block")}</h1>
            <p class="text-lg text-[{SLATE_300}] max-w-xl leading-relaxed">{lang_nodes(HERO_SUB, tag="span", display="block")}</p>
            <div class="flex flex-wrap gap-4 mt-2">
                <a href="/services" class="px-7 py-3.5 rounded-md bg-[{INK_900}] hover:bg-[#3a4a5c] transition-colors font-semibold text-sm">{lang_nodes(BTN_SERVICES)}</a>
                <a href="/contact" class="px-7 py-3.5 rounded-md border border-white/40 hover:border-white/70 transition-colors font-semibold text-sm">{lang_nodes(BTN_CONTACT)}</a>
            </div>
        </div>
    </header>

    <section class="bg-white py-20 px-6">
        <div class="max-w-6xl mx-auto">
            <div class="max-w-2xl flex flex-col gap-3 mb-12">
                <span class="text-xs font-semibold tracking-widest uppercase text-[{INK_900}]">{lang_nodes(SERVICES_EYEBROW)}</span>
                <h2 class="font-display break-words text-3xl font-semibold text-[{INK_950}]">{lang_nodes(SERVICES_H2, tag="span", display="block")}</h2>
            </div>
            <div class="grid md:grid-cols-3 gap-7">{cards_html}
            </div>
        </div>
    </section>

    <section class="bg-[{INK_900}] py-20 px-6">
        <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-10 items-center">
            <div class="flex flex-col gap-4 max-w-lg">
                <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(PARTNERSHIP_EYEBROW)}</span>
                <h2 class="font-display break-words text-2xl font-semibold text-white leading-snug">{lang_nodes(PARTNERSHIP_H2, tag="span", display="block")}</h2>
                <p class="text-[15px] leading-relaxed text-[{SLATE_300}]">{lang_nodes(PARTNERSHIP_P, tag="span", display="block")}</p>
                <a href="/partnership/pera" class="inline-flex items-center gap-2 text-white font-semibold text-sm mt-1">{lang_nodes(PARTNERSHIP_LINK)}
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg>
                </a>
            </div>
            <div class="flex justify-center">
                <svg viewBox="0 0 260 180" width="260" height="180" fill="none" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" opacity="0.85">
                    <circle cx="40" cy="90" r="8"></circle>
                    <circle cx="220" cy="90" r="8"></circle>
                    <path d="M48 90 L212 90" stroke-dasharray="2 7"></path>
                    <text x="24" y="122" fill="#ffffff" stroke="none" font-family="IBM Plex Sans" font-size="12" font-weight="600">EU</text>
                    <text x="206" y="122" fill="#ffffff" stroke="none" font-family="IBM Plex Sans" font-size="12" font-weight="600">TR</text>
                </svg>
            </div>
        </div>
    </section>

    <section class="bg-[{PAPER_50}] py-20 px-6">
        <div class="max-w-6xl mx-auto">
            <h2 class="font-display break-words text-2xl font-semibold text-[{INK_950}] mb-11">{lang_nodes(WHY_H2)}</h2>
            <div class="grid md:grid-cols-4 gap-8">{why_html}
            </div>
        </div>
    </section>

    <section class="bg-[{INK_900}] py-20 px-6 text-center">
        <div class="max-w-xl mx-auto flex flex-col items-center gap-5">
            <h2 class="font-display break-words text-3xl font-semibold text-white">{lang_nodes(CTA_H2)}</h2>
            <p class="text-[15px] text-[#c7ccd1] leading-relaxed">{lang_nodes(CTA_P, tag="span", display="block")}</p>
            <a href="/contact" class="mt-2 px-8 py-3.5 rounded-md bg-white text-[{INK_900}] font-bold text-sm">{lang_nodes(BTN_CONTACT)}</a>
        </div>
    </section>
'''
    return page_html('home', TITLE, DESCRIPTION, '/', body, keywords=KEYWORDS)
