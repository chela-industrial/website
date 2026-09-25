# -*- coding: utf-8 -*-
from common import L, lang_nodes, page_html, INK_950, INK_900, PAPER_50, SLATE_700, SLATE_600, SLATE_300, LINE

TITLE = L(
    'Leistungen | CHELA Industrial',
    'Services | CHELA Industrial',
    'Hizmetler | CHELA Industrial',
)
DESCRIPTION = L(
    'Internationaler Handel, Projektvermittlung und Aufzugssysteme — Leistungen von CHELA Industrial für Hersteller, Lieferanten, Käufer und Projektträger.',
    'International trade, project mediation and elevator systems — CHELA Industrial\'s services for manufacturers, suppliers, buyers and project owners.',
    'Uluslararası ticaret, proje arabuluculuğu ve asansör sistemleri — üreticiler, tedarikçiler, alıcılar ve proje sahipleri için CHELA Industrial hizmetleri.',
)
KEYWORDS = L(
    'Beschaffung Industrieanlagen, Import Export Abwicklung, Aufzugstechnik Handel, Projektpartner Vermittlung',
    'industrial equipment sourcing, import/export handling, elevator technology trade, project partner matching',
    'endüstriyel ekipman tedariki, ithalat ihracat işlemleri, asansör teknolojisi ticareti, proje ortağı eşleştirme',
)

EYEBROW = L('Leistungen', 'Services', 'Hizmetler')
H1 = L(
    'Handel, Vermittlung und technische Brückenfunktion für die Industrie.',
    'Trade, mediation and a technical bridging role for industry.',
    'Endüstri için ticaret, arabuluculuk ve teknik köprü işlevi.',
)

ICONS = {
    'trade': '<rect x="7" y="8" width="10" height="9" rx="1"></rect><path d="M9 8V6a3 3 0 0 1 6 0v2"></path><path d="M3 12h2"></path><path d="M19 12h2"></path>',
    'network': '<circle cx="6" cy="7" r="2.2"></circle><circle cx="18" cy="7" r="2.2"></circle><circle cx="12" cy="18" r="2.2"></circle><path d="M7.8 8.6 10.4 16.2"></path><path d="M16.2 8.6 13.6 16.2"></path><path d="M8.2 7h7.6"></path>',
    'elevator': '<rect x="5" y="3" width="14" height="18" rx="1.5"></rect><polyline points="10 9 12 6.5 14 9"></polyline><polyline points="10 15 12 17.5 14 15"></polyline>',
}

SERVICE_BLOCKS = [
    (
        L('Internationaler Handel', 'International Trade', 'Uluslararası Ticaret'),
        L(
            'Wir übernehmen die strategische Beschaffung und Vermittlung von Industrieanlagen für globale Märkte — von der ersten Anfrage bis zur grenzüberschreitenden Lieferkoordination.',
            'We handle the strategic sourcing and mediation of industrial equipment for global markets — from the first inquiry to cross-border delivery coordination.',
            'Küresel pazarlar için endüstriyel tesislerin stratejik tedarik ve aracılığını üstleniyoruz — ilk talepten sınır ötesi teslimat koordinasyonuna kadar.',
        ),
        L('— Beschaffung industrieller Anlagen &amp; Komponenten', '— Sourcing of industrial equipment &amp; components', '— Endüstriyel tesis ve bileşenlerin tedariki'),
        L('— Grenzüberschreitende Import-/Exportabwicklung', '— Cross-border import/export handling', '— Sınır ötesi ithalat/ihracat işlemleri'),
        'trade',
    ),
    (
        L('Projektvermittlung', 'Project Mediation', 'Proje Arabuluculuğu'),
        L(
            'Wir vernetzen Hersteller, Ingenieurbüros, Lieferanten und Projektträger — branchenübergreifend und unabhängig vom Standort — und begleiten die Zusammenarbeit über Ländergrenzen hinweg.',
            'We connect manufacturers, engineering firms, suppliers and project owners — across industries and regardless of location — and support the collaboration across national borders.',
            'Üreticileri, mühendislik firmalarını, tedarikçileri ve proje sahiplerini — sektör ve konum fark etmeksizin — birbirine bağlıyor ve iş birliğini ülke sınırları ötesinde destekliyoruz.',
        ),
        L('— Zusammenführung relevanter Projektpartner', '— Bringing together the relevant project partners', '— İlgili proje ortaklarının bir araya getirilmesi'),
        L('— Begleitung über den gesamten Projektverlauf', '— Support throughout the entire project', '— Projenin tamamı boyunca destek'),
        'network',
    ),
    (
        L('Aufzugssysteme', 'Elevator Systems', 'Asansör Sistemleri'),
        L(
            'Spezialisierter Handel und Vermittlung im Bereich Aufzugstechnik — in Partnerschaft mit PERA Mühendislik, mit direktem Zugang zu Herstellern und technischen Partnern.',
            'Specialized trade and mediation in elevator technology — in partnership with PERA Mühendislik, with direct access to manufacturers and technical partners.',
            'Asansör teknolojisi alanında uzmanlaşmış ticaret ve aracılık — PERA Mühendislik iş birliğiyle, üreticilere ve teknik ortaklara doğrudan erişimle.',
        ),
        L('— Vermittlung zwischen Herstellern &amp; Käufern', '— Mediation between manufacturers &amp; buyers', '— Üreticiler ve alıcılar arasında aracılık'),
        L('— Technische Abstimmung mit Ingenieurpartnern', '— Technical coordination with engineering partners', '— Mühendislik ortaklarıyla teknik koordinasyon'),
        'elevator',
    ),
]

# Internal link to the PERA page's KfW-159 section, shown only under the
# "Elevator Systems" block (added 2026-09-25, SEO follow-up: a same-site
# relevance signal was previously missing entirely).
KFW_MENTION = L(
    'Inkl. Aufzug-Nachrüstung mit KfW-159-Förderung — mehr erfahren',
    'Incl. elevator retrofits with KfW-159 funding — learn more',
    'KfW-159 destekli asansör sonradan montajı dahil — daha fazla bilgi',
)

PROCESS_H2 = L('So arbeiten wir', 'How we work', 'Nasıl çalışıyoruz')
PROCESS_INTRO = L(
    'Gleich ob Hersteller, Lieferant, Käufer oder Projektträger, gleich in welcher Branche oder an welchem Standort — unser Ablauf bleibt derselbe, mit Schwerpunkt auf Deutschland, der EU, dem Balkan und der Türkei.',
    'Whether you\'re a manufacturer, supplier, buyer or project owner, in any industry or location — our process stays the same, with a focus on Germany, the EU, the Balkans and Turkey.',
    'İster üretici, tedarikçi, alıcı veya proje sahibi olun, hangi sektörde veya konumda olursanız olun — sürecimiz aynı kalır; odak noktamız Almanya, AB, Balkanlar ve Türkiye\'dir.',
)
PROCESS_STEPS = [
    (L('Anfrage', 'Inquiry', 'Talep'),
     L('Sie schildern Ihren Bedarf — als Käufer, Verkäufer oder Projektpartner.',
       'You describe your need — as a buyer, seller or project partner.',
       'İhtiyacınızı bize anlatırsınız — alıcı, satıcı veya proje ortağı olarak.')),
    (L('Abstimmung &amp; Sourcing', 'Alignment &amp; Sourcing', 'Uyumlaştırma ve Tedarik'),
     L('Wir gleichen Anforderungen mit unserem Netzwerk aus Herstellern und Ingenieurpartnern ab.',
       'We match requirements against our network of manufacturers and engineering partners.',
       'Gereksinimleri, üretici ve mühendislik ortaklarından oluşan ağımızla eşleştiririz.')),
    (L('Koordination', 'Coordination', 'Koordinasyon'),
     L('Wir begleiten Verhandlung, Dokumentation und grenzüberschreitende Abwicklung.',
       'We support negotiation, documentation and cross-border handling.',
       'Müzakere, belgelendirme ve sınır ötesi işlemlerde destek sağlarız.')),
    (L('Umsetzung', 'Execution', 'Uygulama'),
     L('Von der Bestellung bis zur Lieferung — mit direktem Ansprechpartner.',
       'From order to delivery — with a direct point of contact.',
       'Siparişten teslimata — doğrudan bir irtibat kişisiyle.')),
]

CTA_H2 = L('Welche Anfrage haben Sie?', 'What can we help you with?', 'Size nasıl yardımcı olabiliriz?')
CTA_BTN = L('Kontakt aufnehmen', 'Get in touch', 'İletişime geçin')


def render():
    kfw_link_html = f'''
                <a href="/partnership/pera#kfw-159" class="inline-flex items-center gap-2 text-[13px] font-semibold text-[{INK_900}] mt-1">{lang_nodes(KFW_MENTION)}
                    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg>
                </a>'''

    blocks_html = ''
    for title, desc, bullet1, bullet2, icon in SERVICE_BLOCKS:
        blocks_html += f'''
        <div class="grid grid-cols-[64px_1fr] md:grid-cols-[120px_1fr] gap-8 py-9 border-b border-[{LINE}] last:border-none">
            <div class="w-16 h-16 rounded-xl bg-[#eef0f1] text-[{INK_900}] flex items-center justify-center">
                <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</svg>
            </div>
            <div class="flex flex-col gap-2.5 min-w-0">
                <h3 class="font-display break-words text-xl font-semibold text-[{INK_950}]">{lang_nodes(title, tag="span", display="block")}</h3>
                <p class="text-[15px] leading-relaxed text-[{SLATE_600}]">{lang_nodes(desc, tag="span", display="block")}</p>
                <div class="flex flex-wrap gap-6 mt-1">
                    <span class="text-[13px] font-medium text-[{SLATE_700}]">{lang_nodes(bullet1)}</span>
                    <span class="text-[13px] font-medium text-[{SLATE_700}]">{lang_nodes(bullet2)}</span>
                </div>{kfw_link_html if icon == "elevator" else ""}
            </div>
        </div>'''

    steps_html = ''
    for i, (title, desc) in enumerate(PROCESS_STEPS, start=1):
        steps_html += f'''
            <div class="flex flex-col gap-2.5">
                <div class="w-9 h-9 rounded-full bg-[{INK_950}] text-white flex items-center justify-center font-display text-sm font-bold">{i}</div>
                <h3 class="text-[15px] font-semibold text-[{INK_950}]">{lang_nodes(title)}</h3>
                <p class="text-[13.5px] leading-relaxed text-[{SLATE_600}]">{lang_nodes(desc, tag="span", display="block")}</p>
            </div>'''

    body = f'''
    <header class="bg-[{INK_950}] text-white py-20 px-6"
      style="background-image:linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size:46px 46px;">
        <div class="max-w-3xl mx-auto flex flex-col gap-4">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(EYEBROW)}</span>
            <h1 class="font-display break-words text-3xl md:text-4xl font-bold leading-tight">{lang_nodes(H1, tag="span", display="block")}</h1>
        </div>
    </header>

    <section class="bg-white py-20 px-6 pb-10">
        <div class="max-w-4xl mx-auto">{blocks_html}
        </div>
    </section>

    <section class="bg-[{PAPER_50}] py-20 px-6">
        <div class="max-w-6xl mx-auto">
            <h2 class="font-display break-words text-2xl font-semibold text-[{INK_950}] mb-3.5">{lang_nodes(PROCESS_H2)}</h2>
            <p class="text-[15px] leading-relaxed text-[{SLATE_600}] max-w-2xl mb-10">{lang_nodes(PROCESS_INTRO, tag="span", display="block")}</p>
            <div class="grid md:grid-cols-4 gap-7">{steps_html}
            </div>
        </div>
    </section>

    <section class="bg-[{INK_900}] py-[76px] px-6 text-center">
        <div class="max-w-xl mx-auto flex flex-col items-center gap-5 py-1">
            <h2 class="font-display break-words text-3xl font-semibold text-white">{lang_nodes(CTA_H2)}</h2>
            <a href="/contact" class="mt-1 px-8 py-3.5 rounded-md bg-white text-[{INK_900}] font-bold text-sm">{lang_nodes(CTA_BTN)}</a>
        </div>
    </section>
'''
    return page_html('services', TITLE, DESCRIPTION, '/services', body, keywords=KEYWORDS)
