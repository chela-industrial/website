# -*- coding: utf-8 -*-
from common import L, lang_nodes, page_html, FORMSPREE_ENDPOINT, SITE_URL, INK_950, INK_900, PAPER_50, SLATE_700, SLATE_600, SLATE_400, SLATE_300, LINE

# Both forms on this site (here and the contact page) submit to Formspree
# (see submitForm() in common.py's LANG_SCRIPT and FORMSPREE_ENDPOINT), which
# delivers to info@chela-industrial.de. Free tier, no card required.


# ---------------------------------------------------------------- LANDING ---
LANDING_TITLE = L('Partnerschaft | CHELA Industrial', 'Partnership | CHELA Industrial', 'Ortaklık | CHELA Industrial')
LANDING_DESC = L(
    'CHELA Industrial arbeitet mit sorgfältig ausgewählten Partnern zusammen — allen voran PERA Mühendislik, unser einziger offizieller EU-Partner für Aufzugstechnik.',
    'CHELA Industrial works with carefully selected partners — first and foremost PERA Mühendislik, our only official EU partner for elevator technology.',
    'CHELA Industrial, dikkatle seçilmiş ortaklarla çalışır — özellikle asansör teknolojisi için tek resmi AB ortağımız olan PERA Mühendislik.',
)
LANDING_KEYWORDS = L(
    'Partnerschaftsübersicht, PERA Mühendislik Partnerschaft, Partner werden, Handelspartner Netzwerk',
    'partnership overview, PERA Mühendislik partnership, become a partner, trade partner network',
    'ortaklık genel bakışı, PERA Mühendislik ortaklığı, partner olun, ticaret ortağı ağı',
)
LANDING_EYEBROW = L('Partnerschaft', 'Partnership', 'Ortaklık')
LANDING_H1 = L(
    'Ausgewählte Partnerschaften statt großer Verwaltung.',
    'Selected partnerships instead of heavy administration.',
    'Büyük bir idari yapı yerine seçilmiş ortaklıklar.',
)
LANDING_SUB = L(
    'CHELA Industrial arbeitet mit sorgfältig ausgewählten Partnern zusammen, um technisches Know-how und Marktzugang über Ländergrenzen hinweg zu verbinden.',
    'CHELA Industrial works with carefully selected partners to connect technical expertise and market access across national borders.',
    'CHELA Industrial, teknik uzmanlığı ve pazar erişimini ülke sınırları ötesinde birleştirmek için dikkatle seçilmiş ortaklarla çalışır.',
)
LANDING_OVERVIEW_EYEBROW = L('Überblick', 'Overview', 'Genel Bakış')
LANDING_OVERVIEW_H2 = L('Wie wir zusammenarbeiten', 'How we work together', 'Nasıl birlikte çalışıyoruz')

CARD_PERA_TITLE = L('PERA Mühendislik — Aufzugstechnik', 'PERA Mühendislik — Elevator Technology', 'PERA Mühendislik — Asansör Teknolojisi')
CARD_PERA_DESC = L(
    'Unser einziger offizieller EU-Partner für Aufzugstechnik — mit unterzeichneter Kooperationsvereinbarung.',
    'Our only official EU partner for elevator technology — under a signed cooperation agreement.',
    'Asansör teknolojisi için tek resmi AB ortağımız — imzalı bir iş birliği anlaşması kapsamında.',
)
CARD_IND_TITLE = L('Andere Branchen', 'Other Industries', 'Diğer Sektörler')
CARD_IND_DESC = L(
    'Handel und Projektvermittlung für Hersteller, Lieferanten, Käufer und Verkäufer über alle Industriezweige hinweg — weltweit, mit Schwerpunkt auf Deutschland, der EU, dem Balkan und der Türkei.',
    'Trade and project mediation for manufacturers, suppliers, buyers and sellers across every branch of industry — worldwide, with a focus on Germany, the EU, the Balkans and Turkey.',
    'Tüm sektörlerdeki üreticiler, tedarikçiler, alıcılar ve satıcılar için ticaret ve proje arabuluculuğu — dünya çapında, Almanya, AB, Balkanlar ve Türkiye odaklı.',
)
CARD_PARTNER_TITLE = L('Partner werden', 'Become a Partner', 'Partner Olun')
CARD_PARTNER_DESC = L(
    'Sie sind Hersteller, Ingenieurbüro oder Handelsunternehmen und möchten mit uns zusammenarbeiten? Erfahren Sie, wie eine offizielle Partnerschaft entsteht.',
    'Are you a manufacturer, engineering firm or trading company interested in working with us? Find out how an official partnership comes about.',
    'Bir üretici, mühendislik firması veya ticaret şirketi misiniz ve bizimle çalışmak mı istiyorsunuz? Resmi bir ortaklığın nasıl kurulduğunu öğrenin.',
)
LEARN_MORE = L('Mehr erfahren', 'Learn more', 'Daha fazla bilgi')
APPLY = L('Anfrage stellen', 'Submit an inquiry', 'Talep gönderin')

LANDING_CTA_H2 = L(
    'Haben Sie ein Projekt mit internationalem Bezug?',
    'Do you have a project with an international dimension?',
    'Uluslararası boyutu olan bir projeniz mi var?',
)
CTA_BTN = L('Kontakt aufnehmen', 'Get in touch', 'İletişime geçin')


def _icon(paths, size=22):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{INK_900}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{paths}</svg>'


def render_landing():
    cards = [
        ('/partnership/pera', f'<img src="/assets/pera-logo.png" alt="PERA Mühendislik" style="height:22px; width:auto; max-width:100%; object-fit:contain; align-self:flex-start; flex-shrink:0; display:block;">', CARD_PERA_TITLE, CARD_PERA_DESC, LEARN_MORE),
        ('/partnership/industries', _icon('<circle cx="6" cy="7" r="2.2"></circle><circle cx="18" cy="7" r="2.2"></circle><circle cx="12" cy="18" r="2.2"></circle><path d="M7.8 8.6 10.4 16.2"></path><path d="M16.2 8.6 13.6 16.2"></path><path d="M8.2 7h7.6"></path>'), CARD_IND_TITLE, CARD_IND_DESC, LEARN_MORE),
        ('/partnership/partner', _icon('<path d="M12 5v14"></path><path d="M5 12h14"></path>'), CARD_PARTNER_TITLE, CARD_PARTNER_DESC, APPLY),
    ]
    cards_html = ''
    for href, icon_html, title, desc, cta in cards:
        cards_html += f'''
      <a href="{href}" class="flex flex-col gap-3.5 p-7 border border-[{LINE}] rounded-xl bg-white hover:border-[{INK_900}] transition-colors">
        <div class="w-11 h-11 rounded-lg bg-[{PAPER_50}] flex items-center justify-center">{icon_html}</div>
        <div class="flex flex-col gap-2">
          <h3 class="font-display break-words text-[17px] font-semibold text-[{INK_950}]">{lang_nodes(title, tag="span", display="block")}</h3>
          <p class="text-[13.5px] leading-relaxed text-[{SLATE_600}]">{lang_nodes(desc, tag="span", display="block")}</p>
        </div>
        <span class="mt-auto inline-flex items-center gap-1.5 text-[13px] font-semibold text-[{INK_950}]">{lang_nodes(cta)}
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg>
        </span>
      </a>'''

    body = f'''
    <header class="bg-[{INK_950}] text-white py-20 px-6"
      style="background-image:linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size:46px 46px;">
        <div class="max-w-3xl mx-auto flex flex-col gap-4">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(LANDING_EYEBROW)}</span>
            <h1 class="font-display break-words text-3xl md:text-4xl font-bold leading-tight">{lang_nodes(LANDING_H1, tag="span", display="block")}</h1>
            <p class="text-base text-[{SLATE_300}] leading-relaxed max-w-xl">{lang_nodes(LANDING_SUB, tag="span", display="block")}</p>
        </div>
    </header>

    <section class="bg-white py-20 px-6">
        <div class="max-w-6xl mx-auto">
            <div class="max-w-2xl flex flex-col gap-2.5 mb-11">
                <span class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_600}]">{lang_nodes(LANDING_OVERVIEW_EYEBROW)}</span>
                <h2 class="font-display break-words text-2xl font-semibold text-[{INK_950}]">{lang_nodes(LANDING_OVERVIEW_H2)}</h2>
            </div>
            <div class="grid md:grid-cols-3 gap-6">{cards_html}
            </div>
        </div>
    </section>

    <section class="bg-[{INK_900}] py-[76px] px-6 text-center">
        <div class="max-w-xl mx-auto flex flex-col items-center gap-5 py-1">
            <h2 class="font-display break-words text-3xl font-semibold text-white">{lang_nodes(LANDING_CTA_H2, tag="span", display="block")}</h2>
            <a href="/contact" class="mt-1 px-8 py-3.5 rounded-md bg-white text-[{INK_900}] font-bold text-sm">{lang_nodes(CTA_BTN)}</a>
        </div>
    </section>
'''
    return page_html('partnership', LANDING_TITLE, LANDING_DESC, '/partnership', body, keywords=LANDING_KEYWORDS)


# -------------------------------------------------------------- PERA PAGE ---
# Title/description updated 2026-09-25 to add the KfW-159 retrofit-financing
# keyword cluster (brief: "CHELA Website — KfW-159 / PERAGREEN Content & SEO
# Brief for Dev") — only the 'de' copy actually renders in <title>/<meta
# description> (see page_html(): search engines see the German version as
# canonical for this single-URL trilingual page), so that's the version that
# matters for ranking; en/tr kept in sync for hygiene.
PERA_TITLE = L(
    'PERA Aufzugstechnik &amp; KfW-159-Förderung | CHELA Industrial',
    'PERA Elevator Technology &amp; KfW-159 Funding | CHELA Industrial',
    'PERA Asansör Teknolojisi &amp; KfW-159 Finansmanı | CHELA Industrial',
)
PERA_DESC = L(
    'CHELA Industrial: exklusiver EU-Partner von PERA Mühendislik für Aufzugstechnik — inkl. Aufzug-Nachrüstung im Bestandsgebäude mit KfW-159-Förderung.',
    'CHELA Industrial is the exclusive EU partner of PERA Mühendislik for elevator technology — including KfW-159-funded elevator retrofits for existing buildings.',
    'CHELA Industrial, asansör teknolojisi için PERA Mühendislik\'in tek resmi AB ortağıdır — mevcut binalarda KfW-159 destekli asansör sonradan montajı dahil.',
)
# Full DE/EN/TR elevator-vocabulary coverage, matching PERA Mühendislik's own
# product range (https://peramuhendislik.com/) — passenger, freight, panoramic,
# hydraulic, vehicle and helicopter-landing-pad elevators, plus modernization
# and maintenance — so this page surfaces for the same searches PERA does,
# in all three languages. DE/EN block also carries the KfW-159 retrofit-
# financing target keywords from the 2026-09-25 SEO brief.
PERA_KEYWORDS = L(
    'PERA Mühendislik Deutschland, Personenaufzüge, Lastenaufzüge, Panoramaaufzüge, Hydraulikaufzüge, '
    'Fahrzeugaufzüge, Hubschrauberlandeplatz-Aufzüge, Monşarj-Systeme, Aufzugsmodernisierung, Aufzugswartung, '
    'Aufzugsplanung und -konstruktion, Aufzugsherstellung und -montage, Aufzugslösungen nach Maß, '
    'europäischer Vertreter PERA, seit 1992, Aufzug Nachrüstung Mehrfamilienhaus, KfW 159 Aufzug, '
    'Aufzug altes Gebäude nachrüsten, Aufzug nachträglich einbauen, KfW Förderung Aufzug, '
    'Barrierefreier Umbau Aufzug Bestandsgebäude',
    'PERA Mühendislik Europe, passenger elevators, freight elevators, load elevators, panoramic elevators, '
    'hydraulic elevators, vehicle elevators, helicopter landing pad elevators, moncharge systems, '
    'elevator modernization, elevator maintenance, elevator design and engineering, elevator manufacturing '
    'and installation, custom-design elevator solutions, PERA European representative, since 1992, '
    'elevator retrofit existing building, KfW 159 elevator funding, barrier-free elevator conversion',
    'PERA Mühendislik Avrupa temsilcisi, yolcu asansörleri, yük asansörleri, panoramik asansörler, '
    'hidrolik asansörler, araç asansörleri, helikopter pist asansörleri, monşarj sistemleri, asansör modernizasyonu, '
    'asansör bakımı, asansör tasarım ve mühendislik, asansör üretim ve montaj, özel tasarım asansör çözümleri, '
    '1992\'den beri asansör, KfW 159 asansör finansmanı, mevcut binaya asansör montajı',
)
PERA_EYEBROW = L('Partnerschaft — PERA Mühendislik', 'Partnership — PERA Mühendislik', 'Ortaklık — PERA Mühendislik')
PERA_H1 = L('Europäische Vertretung für PERA Mühendislik', 'European representation for PERA Mühendislik', 'PERA Mühendislik için Avrupa temsilciliği')
PERA_BADGE = L(
    'Einziger offizieller Partner in der EU — unterzeichnete Kooperationsvereinbarung',
    'Only official partner in the EU — signed cooperation agreement',
    'AB\'deki tek resmi ortak — imzalı iş birliği anlaşması',
)
PERA_SUB = L(
    'Eine direkte Verbindung zwischen europäischen Industrieprojekten und türkischer Ingenieurskompetenz im Bereich Aufzugstechnik.',
    'A direct connection between European industrial projects and Turkish engineering expertise in elevator technology.',
    'Avrupa endüstriyel projeleri ile asansör teknolojisi alanındaki Türk mühendislik uzmanlığı arasında doğrudan bir bağlantı.',
)
PERA_BODY_P = L(
    '<strong style="color:%s;">PERA Mühendislik</strong> ist ein türkisches Ingenieurunternehmen für Aufzugstechnik. CHELA Industrial ist deren benannter, einziger offizieller Vertreter in der Europäischen Union — beide Unternehmen arbeiten eng zusammen, um Projekte über Ländergrenzen hinweg zu realisieren.' % INK_950,
    '<strong style="color:%s;">PERA Mühendislik</strong> is a Turkish elevator engineering company. CHELA Industrial is their named, sole official representative in the European Union — both companies work closely together to realize projects across national borders.' % INK_950,
    '<strong style="color:%s;">PERA Mühendislik</strong>, bir Türk asansör mühendislik şirketidir. CHELA Industrial, Avrupa Birliği\'ndeki belirlenen, tek resmi temsilcileridir — her iki şirket de ülke sınırları ötesinde projeleri hayata geçirmek için yakın iş birliği içinde çalışır.' % INK_950,
)
ABOUT_PERA_EYEBROW = L('Der Partner', 'The partner', 'Ortak')
ABOUT_PERA_H2 = L('Über PERA Mühendislik', 'About PERA Mühendislik', 'PERA Mühendislik Hakkında')
PERA_TAGLINE1 = L('Aufzugslösungen nach Maß', 'Custom-Design Elevator Solutions', 'Özel Tasarım Asansör Çözümleri')
PERA_TAGLINE2 = L('Türkisches Ingenieurunternehmen für Aufzugstechnik — seit 1992', 'Turkish elevator engineering company — since 1992', 'Türk asansör mühendislik şirketi — 1992\'den beri')
PERA_TAGS = L(
    ['Hubschrauberlandeplatz-Aufzüge', 'Fahrzeugaufzüge', 'Monşarj-Systeme', 'Panoramaaufzüge', 'Personenaufzüge', 'Lastenaufzüge &amp; Plattformen', 'Hydraulikaufzüge', 'Modernisierung'],
    ['Helicopter landing pad elevators', 'Vehicle elevators', 'Moncharge systems', 'Panoramic elevators', 'Passenger elevators', 'Freight elevators &amp; platforms', 'Hydraulic elevators', 'Modernization'],
    ['Helikopter pist asansörleri', 'Araç asansörleri', 'Monşarj', 'Panoramik asansörler', 'Yolcu asansörleri', 'Yük asansörleri / platformları', 'Hidrolik asansörler', 'Modernizasyon'],
)
PERA_QUOTE = L(
    '„Ein Aufzug muss bei der ersten Errichtung perfekt sein — Perfektion lässt sich nicht nachträglich hinzufügen.“',
    '"An elevator must be perfect the first time it\'s built — perfection cannot be added afterward."',
    '"Bir asansör ilk kurulumunda mükemmel olmalıdır — mükemmellik sonradan eklenemez."',
)
PERA_QUOTE_SRC = L('Unternehmensphilosophie, PERA Mühendislik', 'Company philosophy, PERA Mühendislik', 'Şirket felsefesi, PERA Mühendislik')

# ---- KfW-159 retrofit-financing section (added 2026-09-25 per "CHELA
# Website — KfW-159 / PERAGREEN Content & SEO Brief for Dev"). Sits right
# after "Über PERA Mühendislik" and before the catalog/quote-request cards —
# read the partnership pitch, get the financing angle, then act via the
# existing Aufzugs-Anfrage form immediately below. Deliberately no PERAGREEN
# space-saving figures yet (v1 decision, 2026-09-25) — those go in only once
# Durukan supplies the confirmed real numbers; do not invent/approximate them
# (see business plan Section 1 note on UWG "green"-claim rules tightening
# 27.09.2026). Anchor id lets this be deep-linked from elsewhere (emails,
# other pages, ads) as /partnership/pera#kfw-159.
KFW_ANCHOR_ID = 'kfw-159'
KFW_EYEBROW = L('Förderung', 'Funding', 'Finansman')
KFW_BADGE = L(
    'Fördermöglichkeit für Bestandsgebäude',
    'Funding for existing buildings',
    'Mevcut binalar için finansman imkanı',
)
KFW_H2 = L(
    'Aufzug-Nachrüstung mit KfW-159-Förderung',
    'Elevator Retrofit with KfW-159 Funding',
    'KfW-159 Finansman Desteğiyle Asansör Sonradan Montajı',
)
KFW_LEAD = L(
    'PERA entwickelt individuelle Aufzugslösungen für Bestandsgebäude, die Standardanbieter ablehnen — '
    'nicht-normgerechte Schächte, Altbaustrukturen, ungünstige Grundrisse. CHELA übernimmt parallel die '
    'KfW-159-Antragsunterlagen, damit die Förderung nicht auf der Strecke bleibt.',
    'PERA designs custom elevator solutions for existing buildings that standard providers won\'t take on — '
    'non-standard shafts, older building structures, awkward floor plans. CHELA handles the KfW-159 '
    'financing paperwork alongside the sale, so it doesn\'t fall through the cracks.',
    'PERA, standart sağlayıcıların üstlenmediği mevcut binalar için özel asansör çözümleri geliştirir — '
    'standart dışı asansör boşlukları, eski bina yapıları, elverişsiz kat planları. CHELA, satışla birlikte '
    'KfW-159 finansman başvuru evraklarını da üstlenir, böylece destek imkanı gözden kaçmaz.',
)
KFW_STEPS_H3 = L('So funktioniert die Förderung', 'How the funding process works', 'Finansman süreci nasıl işliyor')
KFW_STEPS = [
    (L('Förderfähigkeit prüfen', 'Check eligibility', 'Uygunluk kontrolü'),
     L('Bestehendes Wohngebäude, bis zu 50.000 &euro; Darlehen je Wohneinheit.',
       'Existing residential building, up to &euro;50,000 loan per residential unit.',
       'Mevcut konut binası, bağımsız bölüm başına 50.000 &euro;\'ya kadar kredi.')),
    (L('Technisches Konzept &amp; Kostenvoranschlag', 'Technical concept &amp; cost estimate', 'Teknik konsept ve maliyet teklifi'),
     L('PERA plant die Aufzugslösung passend zu Ihrem Gebäude.',
       'PERA designs the elevator solution to fit your building.',
       'PERA, binanıza uygun asansör çözümünü tasarlar.')),
    (L('Antragsunterlagen &amp; Hausbank', 'Application &amp; your bank', 'Başvuru evrakları ve banka'),
     L('CHELA bereitet die Unterlagen vor — Sie reichen über Ihre eigene Hausbank ein.',
       'CHELA prepares the documents — you submit through your own bank.',
       'CHELA evrakları hazırlar — başvuruyu kendi bankanız üzerinden siz yaparsınız.')),
]
KFW_WHO_LABEL = L('Für wen:', 'Who this is for:', 'Kimler için:')
KFW_WHO_TEXT = L(
    'Eigentümer bestehender Gebäude — private Eigentümer, Vermieter und kleinere Hausverwaltungen. '
    'Nicht für Neubauten, nicht für Eigentümergemeinschaften (WEG).',
    'Owners of existing buildings — private homeowners, landlords, and small property management companies. '
    'Not for new construction, not for multi-owner (WEG) buildings.',
    'Mevcut bina sahipleri — özel mülk sahipleri, kiraya verenler ve küçük ölçekli yönetim şirketleri. '
    'Yeni inşaatlar için değil, çok ortaklı mülkiyet birlikleri (WEG) için değil.',
)
# The KfW-159 section deliberately carries no CTA of its own (2026-09-26 dev
# note) — it used to end in its own "Anfrage stellen" bar, which sat right on
# top of the near-identical quote card two sections down and read as two
# separate asks. There is now exactly one request CTA on the page (the quote
# card below, whose copy — QUOTE_LABEL / QUOTE_TITLE / QUOTE_DESC — was
# rewritten to cover both a plain elevator inquiry and a KfW-159 one) so a
# reader who just finished the funding section flows straight into it.

# ---- Page-specific JSON-LD for the PERA page (added 2026-09-25, SEO
# follow-up). page_html() already supported an extra `json_ld` param but no
# page used it. Content below is a direct restatement — same facts, plain
# text instead of the HTML-entity-encoded copy above (a <script> tag's
# content isn't HTML-entity-decoded, so &euro;/&amp; would render literally)
# — of the already-reviewed, already-live KFW_LEAD / KFW_WHO_TEXT / KFW_STEPS
# copy immediately above. No new facts, nothing invented: Service schema
# describes the KfW-159 retrofit offering, FAQPage mirrors the three points a
# reader of that section already sees (eligibility, funding amount, process).
# DE only, matching the DE-canonical pattern page_html() already uses for
# <title>/<meta description> (search engines/AI crawlers see the German
# version; the client-side language toggle is a UX layer on top).
PERA_JSON_LD = f'''<script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "Service",
          "serviceType": "Aufzug-Nachrüstung mit KfW-159-Förderung",
          "name": "Aufzug-Nachrüstung mit KfW-159-Förderung",
          "description": "PERA entwickelt individuelle Aufzugslösungen für Bestandsgebäude, die Standardanbieter ablehnen — nicht-normgerechte Schächte, Altbaustrukturen, ungünstige Grundrisse. CHELA übernimmt parallel die KfW-159-Antragsunterlagen, damit die Förderung nicht auf der Strecke bleibt.",
          "provider": {{
            "@type": "Organization",
            "name": "CHELA Industrial UG (haftungsbeschränkt)",
            "url": "{SITE_URL}"
          }},
          "areaServed": "DE",
          "audience": {{
            "@type": "Audience",
            "audienceType": "Eigentümer bestehender Wohngebäude"
          }},
          "url": "{SITE_URL}/partnership/pera#kfw-159"
        }},
        {{
          "@type": "FAQPage",
          "mainEntity": [
            {{
              "@type": "Question",
              "name": "Wer kann die KfW-159-Förderung für eine Aufzug-Nachrüstung nutzen?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Eigentümer bestehender Gebäude — private Eigentümer, Vermieter und kleinere Hausverwaltungen. Nicht für Neubauten, nicht für Eigentümergemeinschaften (WEG)."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Wie hoch ist die KfW-159-Förderung pro Wohneinheit?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Bis zu 50.000 Euro Darlehen je Wohneinheit für ein bestehendes Wohngebäude."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Wie läuft der Förderprozess ab?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Drei Schritte: zuerst die Förderfähigkeit prüfen, dann erstellt PERA das technische Konzept und den Kostenvoranschlag, anschließend bereitet CHELA die Antragsunterlagen vor, die Sie über Ihre eigene Hausbank einreichen."
              }}
            }}
          ]
        }}
      ]
    }}
    </script>'''

# ---- E-Katalog: in-page PDF.js viewer for PERA's product catalog (single
# English-language PDF, shown identically across all three site languages
# until PERA provides other language versions — see CATALOG_LANG_NOTE) ----
CATALOG_URL = '/assets/pera-catalog.pdf'
CATALOG_PAGES = 36
CATALOG_LABEL = L('PDF &middot; 36 Seiten', 'PDF &middot; 36 pages', 'PDF &middot; 36 sayfa')
CATALOG_TITLE = L('PERA Produktkatalog', 'PERA Product Catalog', 'PERA Ürün Kataloğu')
CATALOG_DESC = L(
    'Alle Aufzugslösungen im Überblick — direkt auf dieser Seite durchblättern.',
    'All elevator solutions at a glance — browse it right here on this page.',
    'Tüm asansör çözümlerine genel bakış — doğrudan bu sayfada göz atın.',
)
CATALOG_VIEW_BTN = L('Katalog ansehen', 'View catalog', 'Kataloğu görüntüle')
CATALOG_DOWNLOAD = L('PDF herunterladen', 'Download PDF', 'PDF indir')
CATALOG_LOADING = L('Katalog wird geladen …', 'Loading catalog …', 'Katalog yükleniyor …')
CATALOG_PREV_ARIA = L('Vorherige Seite', 'Previous page', 'Önceki sayfa')
CATALOG_NEXT_ARIA = L('Nächste Seite', 'Next page', 'Sonraki sayfa')
CATALOG_CLOSE_ARIA = L('Schließen', 'Close', 'Kapat')

# ---- Aufzugs-Anfrage: technical elevator price-request form, adapted from
# the PDF intake form (FS.01.01.A) used by PERA/CHELA today. Rearranged for
# the web (own pop-up, own CTA card next to the catalog) — kept close to the
# PDF's actual fields, especially the Section 3 technical specs, but dropped
# the print-only fields (Datum, Fax) and the shaft-section diagram, which a
# tip note replaces. Submits through the same Formspree inbox as the other
# site forms (see FORMSPREE_ENDPOINT / submitForm() in common.py). ----
QUOTE_LABEL = L('Unverbindlich &amp; kostenlos', 'No cost, no obligation', 'Ücretsiz ve taahhütsüz')
QUOTE_TITLE = L(
    'Aufzugsanfrage stellen — mit oder ohne KfW-159-Förderung',
    'Request an elevator quote — with or without KfW-159 funding',
    'Asansör teklifi isteyin — KfW-159 finansmanlı veya finansmansız',
)
QUOTE_DESC = L(
    'Ein Formular für Ihre technische Anfrage und, falls gewünscht, die KfW-159-Fördermittel-Angaben.',
    'One form for your technical inquiry and, if relevant, the KfW-159 funding details.',
    'Teknik talebiniz ve isterseniz KfW-159 finansman bilgileriniz için tek bir form.',
)
QUOTE_BTN = L('Anfrage stellen', 'Request a quote', 'Teklif isteyin')

QUOTE_MODAL_TITLE = L('Aufzugs-Anfrage', 'Elevator Inquiry', 'Asansör Talebi')
QUOTE_MODAL_SUB = L(
    'Technisches Anfrageformular für PERA-Hydraulikaufzüge — auch für KfW-159-Förderanfragen',
    'Technical inquiry form for PERA hydraulic elevators — also covers KfW-159 funding requests',
    'PERA hidrolik asansörleri için teknik talep formu — KfW-159 finansman talepleri için de kullanılabilir',
)
QUOTE_CLOSE_ARIA = CATALOG_CLOSE_ARIA

QUOTE_NAV = [
    L('Kontakt', 'Contact', 'İletişim'),
    L('Gebäude', 'Building', 'Bina'),
    L('Technik', 'Specifications', 'Teknik'),
    L('Notizen', 'Notes', 'Notlar'),
    L('Quelle', 'Source', 'Kaynak'),
]

Q_OPTIONAL = L('optional', 'optional', 'opsiyonel')

Q_S1_H = L('Kontakt &amp; Anfrage', 'Contact &amp; Inquiry', 'İletişim ve Talep')
Q_F_COMPANY = L('Firma', 'Company', 'Firma')
Q_F_COMPANY_PH = L('Musterfirma GmbH', 'Musterfirma GmbH', 'Musterfirma GmbH')
Q_F_CONTACT = L('Ansprechpartner', 'Contact person', 'Yetkili Kişi')
Q_F_EMAIL = L('E-Mail', 'Email', 'E-posta')
Q_F_PHONE = L('Telefon', 'Phone', 'Telefon')
Q_F_REF = L('Referenz', 'Reference', 'Referans')

Q_S2_H = L('Gebäude &amp; Verwendungszweck', 'Building &amp; Intended Use', 'Bina ve Kullanım Amacı')
Q_F_BTYPE = L('Gebäudetyp', 'Type of building', 'Bina Tipi')
Q_F_BCOND = L('Gebäudezustand', 'Condition of building', 'Bina Durumu')
Q_F_USE = L('Verwendungszweck', 'Intended use', 'Kullanım Amacı')
Q_MULTI = L('Mehrfachauswahl', 'select all that apply', 'birden fazla seçilebilir')
Q_F_LOCATION = L('Einbauort', 'Place of installation', 'Kurulum Yeri')
Q_F_LOCATION_PH = L('Stadt, Land', 'City, country', 'Şehir, ülke')
Q_F_DEADLINE = L('Gewünschter Termin', 'Required deadline', 'İstenen Teslim Tarihi')
Q_F_DEADLINE_PH = L('z. B. Q1 2027', 'e.g. Q1 2027', 'örn. 2027 1. Çeyrek')
# Added 2026-09-25 alongside the KfW-159 section (SEO/content brief, point C:
# "consider adding an optional field like building type or how many units so
# an inbound KfW-159 inquiry arrives pre-qualified") — both optional, so the
# form stays usable for every other inquiry too, not just KfW-159 leads.
Q_F_UNITS = L('Anzahl Wohneinheiten', 'Number of residential units', 'Bağımsız Bölüm Sayısı')
Q_F_KFW_INTEREST = L(
    'Ich interessiere mich für eine KfW-159-Förderung',
    'I\'m interested in KfW-159 funding',
    'KfW-159 finansman desteğiyle ilgileniyorum',
)
# Small helper line under the toggle above, and the toggle's own onward-reveal
# field — together these fold the KfW-159 funding request into this one form
# (rather than a bolted-on checkbox) per the 2026-09-25 dev brief: checking it
# reveals Q_F_UNITS inline (toggleKfwUnits() in the page script) and, when the
# quote form is opened from the KfW-159 CTA, is pre-checked automatically
# (openQuoteForm(true)).
Q_F_KFW_HINT = L(
    'Wir ergänzen Ihre Anfrage um die relevanten Förderangaben.',
    'We\'ll add the relevant funding details to your inquiry.',
    'Talebinize ilgili finansman bilgilerini ekleyeceğiz.',
)

BUILDING_TYPE_OPTS = [
    ('Business', L('Gewerbe', 'Business', 'Ticari')),
    ('Factory', L('Fabrik', 'Factory', 'Fabrika')),
    ('Residence', L('Wohngebäude', 'Residence', 'Konut')),
    ('School', L('Schule', 'School', 'Okul')),
    ('Hospital', L('Krankenhaus', 'Hospital', 'Hastane')),
    ('Other', L('Sonstiges', 'Other', 'Diğer')),
]
BUILDING_COND_OPTS = [
    ('Existing', L('Bestehend', 'Existing', 'Mevcut')),
    ('Under construction', L('Im Bau', 'Under construction', 'İnşaat Halinde')),
    ('Design stage', L('In Planung', 'Design stage', 'Planlama Aşamasında')),
]
INTENDED_USE_OPTS = [
    ('Passenger', L('Personenaufzug', 'Passenger', 'Yolcu')),
    ('Load', L('Lastenaufzug', 'Load', 'Yük')),
    ('Load cabin', L('Lastenkabine', 'Load cabin', 'Yük Kabini')),
    ('Vehicle platform', L('Fahrzeugplattform', 'Vehicle platform', 'Araç Platformu')),
    ('Fire elevator', L('Feuerwehraufzug', 'Fire elevator', 'İtfaiye Asansörü')),
    ('Disabled access', L('Barrierefrei', 'Disabled access', 'Engelli Erişimi')),
    ('Other', L('Sonstiges', 'Other', 'Diğer')),
]
SOURCE_OPTS = [
    ('Trade fair', L('Messe', 'Trade fair', 'Fuar')),
    ('Referral', L('Empfehlung', 'Referral', 'Tavsiye')),
    ('Website', L('Website', 'Website', 'Web Sitesi')),
    ('LinkedIn', L('LinkedIn', 'LinkedIn', 'LinkedIn')),
    ('Other', L('Sonstiges', 'Other', 'Diğer')),
]

Q_S3_H = L('Technische Spezifikationen', 'Elevator Specifications', 'Teknik Özellikler')
Q_S3_SUB = L(
    'Die wichtigsten Angaben für Ihr Angebot',
    'The key figures we need to prepare your quote',
    'Teklifiniz için gereken temel bilgiler',
)
Q_F_QTY = L('Anzahl Aufzüge', 'No. of elevators', 'Asansör Sayısı')
Q_F_LANDINGS = L('Anzahl Haltestellen', 'No. of landings', 'Durak Sayısı')
Q_F_SPEED = L('Geschwindigkeit', 'Speed', 'Hız')
Q_F_CAPACITY = L('Tragfähigkeit', 'Capacity', 'Kapasite')
Q_F_TRAVEL = L('Förderhöhe', 'Travel height', 'Yükseklik')
Q_F_PIT = L('Schachtgrube', 'Pit depth', 'Kuyu Çukuru')
Q_F_HEADROOM = L('Schachtkopfhöhe', 'Headroom', 'Üst Boşluk')
Q_F_WIDTH = L('Schachtbreite', 'Shaft width', 'Kuyu Genişliği')
Q_F_DEPTH = L('Schachttiefe', 'Shaft depth', 'Kuyu Derinliği')
Q_TIP = L(
    'Tipp: Bei Bestandsgebäuden Maße vor Ort durch einen Fachbetrieb aufnehmen lassen; bei Neubauten/Planung genügen die Rohbau- bzw. Planmaße.',
    'Tip: For existing buildings, have a specialist measure on-site; for new builds or projects still in planning, shell/architectural drawing dimensions are sufficient.',
    'İpucu: Mevcut binalarda ölçümlerin yerinde bir uzman tarafından alınmasını sağlayın; yeni yapılarda/planlama aşamasında kaba inşaat veya proje ölçüleri yeterlidir.',
)

Q_S4_H = L('Anmerkungen', 'Notes', 'Notlar')
Q_F_NOTES = L(
    'Weitere Angaben zu Ihrem Projekt',
    'Anything else we should know about your project',
    'Projeniz hakkında eklemek istediğiniz bilgiler',
)

Q_S5_H = L('Wie haben Sie von uns erfahren?', 'How did you hear about us?', 'Bizi nereden duydunuz?')
Q_SOURCE_PLACEHOLDER = L('Bitte wählen', 'Please select', 'Lütfen seçin')

Q_PRIVACY = L(
    'Mit dem Absenden stimmen Sie zu, dass wir Sie zu Ihrer Anfrage kontaktieren.',
    'By submitting, you agree that we may contact you regarding your inquiry.',
    'Gönder\'e tıklayarak, talebinizle ilgili sizinle iletişime geçmemizi kabul edersiniz.',
)
Q_SUBMIT = L('Anfrage senden', 'Send inquiry', 'Talebi gönder')

WHAT_IT_MEANS_H2 = L('Was das für Sie bedeutet', 'What this means for you', 'Bunun sizin için anlamı')
WHAT_IT_MEANS_CARDS = [
    (L('Ein Ansprechpartner', 'A single point of contact', 'Tek bir irtibat noktası'),
     L('Eine zentrale Kontaktstelle für Anfragen aus beiden Märkten — ohne Umwege.',
       'One central contact point for inquiries from both markets — no detours.',
       'Her iki pazardan gelen talepler için tek bir merkezi irtibat noktası — dolambaçsız.')),
    (L('Ingenieurskompetenz', 'Engineering expertise', 'Mühendislik uzmanlığı'),
     L('Zugang zu technischem Know-how für europäische Projekte, direkt aus der Partnerschaft mit PERA Mühendislik.',
       'Access to technical know-how for European projects, direct from the partnership with PERA Mühendislik.',
       'PERA Mühendislik ortaklığından doğrudan, Avrupa projeleri için teknik bilgi birikimine erişim.')),
    (L('Marktzugang', 'Market access', 'Pazar erişimi'),
     L('Unterstützung beim Einstieg in den jeweils anderen Markt — für Projektträger auf beiden Seiten.',
       'Support entering the other market — for project owners on both sides.',
       'Diğer pazara giriş konusunda destek — her iki taraftaki proje sahipleri için.')),
]
PERA_CTA_H2 = L(
    'Steht bei Ihrem Projekt Aufzugstechnik an?',
    'Does your project involve elevator technology?',
    'Projenizde asansör teknolojisi mi gerekiyor?',
)


def render_pera():
    tags_html = ''.join(
        f'<span class="px-3.5 py-1.5 border border-[{LINE}] rounded-full text-[12.5px] font-medium text-[{SLATE_700}] bg-white">{lang_nodes({l: PERA_TAGS[l][i] for l in ["de","en","tr"]})}</span>'
        for i in range(len(PERA_TAGS['de']))
    )
    means_html = ''
    for title, desc in WHAT_IT_MEANS_CARDS:
        means_html += f'''
        <div class="bg-[{PAPER_50}] border border-[{LINE}] rounded-xl p-6 flex flex-col gap-2">
            <h3 class="text-[15.5px] font-semibold text-[{INK_950}]">{lang_nodes(title)}</h3>
            <p class="text-[13.5px] leading-relaxed text-[{SLATE_600}]">{lang_nodes(desc, tag="span", display="block")}</p>
        </div>'''

    kfw_steps_html = ''
    for i, (title, desc) in enumerate(KFW_STEPS, start=1):
        kfw_steps_html += f'''
                <div class="flex gap-3 items-start">
                    <span class="w-[26px] h-[26px] rounded-full bg-[{INK_950}] text-white text-[12px] font-bold flex items-center justify-center flex-shrink-0">{i}</span>
                    <span class="text-[13.5px] leading-relaxed text-[{SLATE_700}]"><strong class="text-[{INK_950}]">{lang_nodes(title)}.</strong> {lang_nodes(desc)}</span>
                </div>'''

    # ---- Aufzugs-Anfrage form pieces ----
    def pill_group(name, opts, input_type='radio'):
        html = ''
        for val, label in opts:
            html += f'''<label class="inline-flex items-center px-3.5 py-1.5 border border-[{LINE}] rounded-full text-[12.5px] font-medium text-[{SLATE_700}] bg-white cursor-pointer select-none has-[:checked]:bg-[{INK_950}] has-[:checked]:text-white has-[:checked]:border-[{INK_950}] transition-colors">
                <input type="{input_type}" name="{name}" value="{val}" class="sr-only">{lang_nodes(label)}
            </label>'''
        return html

    def spec_field(name, label_html, unit, placeholder=''):
        return f'''<label class="flex flex-col gap-2">
                <span class="text-[13px] font-semibold text-[{INK_900}]">{label_html}</span>
                <div class="relative">
                    <input type="number" name="{name}" step="any" placeholder="{placeholder}" class="w-full border border-[{LINE}] rounded-md pl-3.5 pr-12 py-3 text-[14.5px] text-[{INK_900}]">
                    <span class="absolute right-3.5 top-1/2 -translate-y-1/2 text-[11.5px] font-bold text-[{SLATE_400}] pointer-events-none">{unit}</span>
                </div>
            </label>'''

    quote_nav_html = ''.join(
        f'<a href="#q-s{i+1}" class="flex-shrink-0 text-[11.5px] font-semibold text-[{SLATE_700}] bg-white border border-[{LINE}] px-2.5 py-1.5 rounded-full whitespace-nowrap"><b class="text-[{INK_900}] mr-1">{i+1}</b>{lang_nodes(label)}</a>'
        for i, label in enumerate(QUOTE_NAV)
    )

    btype_html = pill_group('building_type', BUILDING_TYPE_OPTS)
    bcond_html = pill_group('building_condition', BUILDING_COND_OPTS)
    use_html = pill_group('intended_use', INTENDED_USE_OPTS, input_type='checkbox')
    # A native <select>'s options can't use the lang_nodes() show/hide
    # technique, so each option shows all three languages at once (this
    # field is the lowest-priority one on the form — "how did you hear
    # about us", optional).
    def tri(label_dict):
        return ' / '.join(dict.fromkeys([label_dict['de'], label_dict['en'], label_dict['tr']]))

    source_opts_html = f'<option value="">{tri(Q_SOURCE_PLACEHOLDER)}</option>' + ''.join(
        f'<option value="{val}">{tri(label)}</option>' for val, label in SOURCE_OPTS
    )

    spec_fields_html = ''.join([
        spec_field('elevator_qty', lang_nodes(Q_F_QTY), '', placeholder='1'),
        spec_field('landings', lang_nodes(Q_F_LANDINGS), ''),
        spec_field('speed', lang_nodes(Q_F_SPEED), 'm/s'),
        spec_field('capacity_q', f'Q &mdash; {lang_nodes(Q_F_CAPACITY)}', 'kg'),
        spec_field('travel_height_fh', f'FH &mdash; {lang_nodes(Q_F_TRAVEL)}', 'mm'),
        spec_field('pit_sg', f'SG &mdash; {lang_nodes(Q_F_PIT)}', 'mm'),
        spec_field('headroom_sk', f'SK &mdash; {lang_nodes(Q_F_HEADROOM)}', 'mm'),
        spec_field('width_sb', f'SB &mdash; {lang_nodes(Q_F_WIDTH)}', 'mm'),
        spec_field('depth_st', f'ST &mdash; {lang_nodes(Q_F_DEPTH)}', 'mm'),
    ])

    body = f'''
    <header class="bg-[{INK_950}] text-white py-20 px-6"
      style="background-image:linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size:46px 46px;">
        <div class="max-w-3xl mx-auto flex flex-col gap-[18px]">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(PERA_EYEBROW)}</span>
            <h1 class="font-display break-words text-3xl md:text-4xl font-bold leading-tight">{lang_nodes(PERA_H1)}</h1>
            <div class="inline-flex self-start items-center gap-2 px-4 py-2 border border-white/30 rounded-full bg-white/[0.06]">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M8.5 12.5l2.5 2.5 5-5"></path></svg>
                <span class="text-xs font-semibold text-white">{lang_nodes(PERA_BADGE)}</span>
            </div>
            <p class="text-base text-[{SLATE_300}] leading-relaxed max-w-xl">{lang_nodes(PERA_SUB, tag="span", display="block")}</p>
        </div>
    </header>

    <section class="bg-white py-[56px] px-6">
        <div class="max-w-5xl mx-auto grid md:grid-cols-[1.2fr_0.8fr] gap-10 items-center">
            <p class="text-[16.5px] leading-relaxed text-[{SLATE_700}] max-w-xl">{lang_nodes(PERA_BODY_P, tag="span", display="block")}</p>
            <div class="flex justify-center">
                <!-- Isometric hydraulic-elevator cutaway (v2, 2026-09-26): replaces
                     the flat 2D line-art schematic, which read as too plain and
                     left too much empty space in this column. Built as a proper
                     axonometric technical illustration — shaft wireframe (2
                     floors) with the cabin as a shaded solid, a side-mounted
                     hydraulic ram running from the pit to the cabin underside,
                     and a compact ground-level power unit (oil tank + motor)
                     with the pressure line drawn in PERA red, per real hydraulic-
                     schematic convention — since PERA's own product line is
                     predominantly hydraulic elevators. Every coordinate below is
                     the output of a small isometric-projection generator (dev
                     scratch, not checked in); colors are hand-picked shades of
                     the site's ink/slate palette plus the one red accent, kept
                     literal here since this is a single fixed illustration. -->
                <svg viewBox="0 0 309 383" width="280" height="347" font-family="IBM Plex Sans">
                    <ellipse cx="186.9" cy="358.2" rx="89.8" ry="28.7" fill="#0d1720" opacity="0.10"></ellipse>
                    <line x1="94.4" y1="205.2" x2="181.7" y2="255.6" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="181.7" y1="255.6" x2="119.3" y2="291.6" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="119.3" y1="291.6" x2="32.0" y2="241.2" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="32.0" y1="241.2" x2="94.4" y2="205.2" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="94.4" y1="30.0" x2="181.7" y2="80.4" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="181.7" y1="80.4" x2="119.3" y2="116.4" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="119.3" y1="116.4" x2="32.0" y2="66.0" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="32.0" y1="66.0" x2="94.4" y2="30.0" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="94.4" y1="205.2" x2="94.4" y2="30.0" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="181.7" y1="255.6" x2="181.7" y2="80.4" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="119.3" y1="291.6" x2="119.3" y2="116.4" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <line x1="32.0" y1="241.2" x2="32.0" y2="66.0" stroke="#c7c9cb" stroke-width="1.1"></line>
                    <polygon points="94.4,117.6 181.7,168.0 119.3,204.0 32.0,153.6" fill="none" stroke="#c7c9cb" stroke-width="0.9" stroke-dasharray="2 4"></polygon>
                    <line x1="94.4" y1="260.4" x2="181.7" y2="310.8" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="181.7" y1="310.8" x2="119.3" y2="346.8" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="119.3" y1="346.8" x2="32.0" y2="296.4" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="32.0" y1="296.4" x2="94.4" y2="260.4" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="94.4" y1="205.2" x2="181.7" y2="255.6" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="181.7" y1="255.6" x2="119.3" y2="291.6" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="119.3" y1="291.6" x2="32.0" y2="241.2" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="32.0" y1="241.2" x2="94.4" y2="205.2" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="94.4" y1="260.4" x2="94.4" y2="205.2" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="181.7" y1="310.8" x2="181.7" y2="255.6" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="119.3" y1="346.8" x2="119.3" y2="291.6" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <line x1="32.0" y1="296.4" x2="32.0" y2="241.2" stroke="#999da2" stroke-width="0.9" stroke-dasharray="2 4"></line>
                    <polygon points="94.4,30.0 181.7,80.4 119.3,116.4 32.0,66.0" fill="#e3e4e5" fill-opacity="0.4" stroke="#c7c9cb" stroke-width="1"></polygon>
                    <polygon points="94.4,54.0 163.0,93.6 119.3,118.8 50.8,79.2" fill="#979da3" stroke="#101820" stroke-width="1.2"></polygon>
                    <polygon points="163.0,159.6 119.3,184.8 119.3,118.8 163.0,93.6" fill="#343f4b" stroke="#101820" stroke-width="1.2"></polygon>
                    <polygon points="50.8,145.2 119.3,184.8 119.3,118.8 50.8,79.2" fill="#111a24" stroke="#101820" stroke-width="1.2"></polygon>
                    <line x1="141.2" y1="168.6" x2="141.2" y2="109.8" stroke="#69717a" stroke-width="1.1"></line>
                    <line x1="159.9" y1="120.5" x2="122.5" y2="142.1" stroke="#525c66" stroke-width="0.8" stroke-dasharray="1 3"></line>
                    <line x1="94.4" y1="208.1" x2="94.4" y2="32.9" stroke="#999da2" stroke-width="0.8" stroke-dasharray="1 4"></line>
                    <line x1="176.7" y1="255.6" x2="176.7" y2="80.4" stroke="#999da2" stroke-width="0.8" stroke-dasharray="1 4"></line>
                    <polygon points="176.3,194.9 175.0,195.5 173.6,196.1 172.1,196.5 170.5,196.8 168.8,197.0 167.1,197.1 165.5,197.0 163.8,196.8 162.2,196.5 160.7,196.1 159.3,195.5 158.0,194.9 156.9,194.1 155.9,193.3 155.2,192.5 154.7,191.5 154.3,190.6 154.2,189.6 154.3,188.6 154.7,187.7 155.2,186.7 155.9,185.9 156.9,185.1 158.0,184.3 159.3,183.7 160.7,183.1 162.2,182.7 163.8,182.4 165.5,182.2 167.1,182.1 168.8,182.2 170.5,182.4 172.1,182.7 173.6,183.1 175.0,183.7 176.3,184.3 177.4,185.1 178.3,185.9 179.1,186.7 179.6,187.7 180.0,188.6 180.1,189.6 180.0,190.6 179.6,191.5 179.1,192.5 178.3,193.3 177.4,194.1" fill="#9b9fa4" stroke="#101820" stroke-width="1.1"></polygon>
                    <polygon points="180.1,332.4 180.0,333.2 179.8,334.0 179.4,334.7 179.0,335.4 178.3,336.1 177.6,336.8 176.8,337.4 175.8,337.9 174.7,338.4 173.6,338.9 172.4,339.2 171.1,339.5 169.8,339.7 168.5,339.8 167.1,339.9 165.8,339.8 164.5,339.7 163.1,339.5 161.9,339.2 160.7,338.9 159.5,338.4 158.5,337.9 157.5,337.4 156.7,336.8 155.9,336.1 155.3,335.4 154.8,334.7 154.5,334.0 154.3,333.2 154.2,332.4 154.2,189.6 154.3,190.4 154.5,191.2 154.8,191.9 155.3,192.6 155.9,193.3 156.7,194.0 157.5,194.6 158.5,195.1 159.5,195.6 160.7,196.1 161.9,196.4 163.1,196.7 164.5,196.9 165.8,197.0 167.1,197.1 168.5,197.0 169.8,196.9 171.1,196.7 172.4,196.4 173.6,196.1 174.7,195.6 175.8,195.1 176.8,194.6 177.6,194.0 178.3,193.3 179.0,192.6 179.4,191.9 179.8,191.2 180.0,190.4 180.1,189.6" fill="#525a61" stroke="#101820" stroke-width="1.1"></polygon>
                    <polygon points="171.9,192.3 171.2,192.7 170.5,193.0 169.7,193.2 168.9,193.4 168.0,193.4 167.1,193.5 166.3,193.4 165.4,193.4 164.6,193.2 163.8,193.0 163.1,192.7 162.4,192.3 161.8,192.0 161.3,191.5 160.9,191.1 160.6,190.6 160.5,190.1 160.4,189.6 160.5,189.1 160.6,188.6 160.9,188.1 161.3,187.7 161.8,187.2 162.4,186.9 163.1,186.5 163.8,186.2 164.6,186.0 165.4,185.8 166.3,185.8 167.1,185.7 168.0,185.8 168.9,185.8 169.7,186.0 170.5,186.2 171.2,186.5 171.9,186.9 172.5,187.2 173.0,187.7 173.4,188.1 173.6,188.6 173.8,189.1 173.9,189.6 173.8,190.1 173.6,190.6 173.4,191.1 173.0,191.5 172.5,192.0" fill="#e0e1e2" stroke="#101820" stroke-width="0.9"></polygon>
                    <polygon points="173.9,250.8 173.8,251.2 173.7,251.6 173.5,252.0 173.3,252.4 173.0,252.7 172.6,253.1 172.1,253.4 171.6,253.7 171.1,253.9 170.5,254.2 169.9,254.3 169.2,254.5 168.5,254.6 167.8,254.7 167.1,254.7 166.4,254.7 165.7,254.6 165.1,254.5 164.4,254.3 163.8,254.2 163.2,253.9 162.6,253.7 162.1,253.4 161.7,253.1 161.3,252.7 161.0,252.4 160.7,252.0 160.6,251.6 160.5,251.2 160.4,250.8 160.4,189.6 160.5,190.0 160.6,190.4 160.7,190.8 161.0,191.2 161.3,191.5 161.7,191.9 162.1,192.2 162.6,192.5 163.2,192.7 163.8,193.0 164.4,193.1 165.1,193.3 165.7,193.4 166.4,193.5 167.1,193.5 167.8,193.5 168.5,193.4 169.2,193.3 169.9,193.1 170.5,193.0 171.1,192.7 171.6,192.5 172.1,192.2 172.6,191.9 173.0,191.5 173.3,191.2 173.5,190.8 173.7,190.4 173.8,190.0 173.9,189.6" fill="#caccce" stroke="#101820" stroke-width="0.9"></polygon>
                    <line x1="169.0" y1="185.4" x2="151.6" y2="166.2" stroke="#101820" stroke-width="1.6"></line>
                    <polygon points="223.3,223.2 279.4,255.6 230.5,283.8 174.4,251.4" fill="#a3acb5" stroke="#101820" stroke-width="1.2"></polygon>
                    <polygon points="279.4,312.0 230.5,340.2 230.5,283.8 279.4,255.6" fill="#4b5d6e" stroke="#101820" stroke-width="1.2"></polygon>
                    <polygon points="174.4,307.8 230.5,340.2 230.5,283.8 174.4,251.4" fill="#24323f" stroke="#101820" stroke-width="1.2"></polygon>
                    <polygon points="232.8,222.7 231.5,223.4 230.0,224.0 228.4,224.4 226.8,224.7 225.0,224.9 223.3,225.0 221.5,224.9 219.8,224.7 218.1,224.4 216.5,224.0 215.0,223.4 213.7,222.7 212.5,222.0 211.6,221.1 210.8,220.2 210.2,219.2 209.9,218.2 209.7,217.2 209.9,216.2 210.2,215.2 210.8,214.2 211.6,213.3 212.5,212.4 213.7,211.7 215.0,211.0 216.5,210.4 218.1,210.0 219.8,209.7 221.5,209.5 223.3,209.4 225.0,209.5 226.8,209.7 228.4,210.0 230.0,210.4 231.5,211.0 232.8,211.7 234.0,212.4 235.0,213.3 235.8,214.2 236.3,215.2 236.7,216.2 236.8,217.2 236.7,218.2 236.3,219.2 235.8,220.2 235.0,221.1 234.0,222.0" fill="#9b9fa4" stroke="#101820" stroke-width="1"></polygon>
                    <polygon points="236.8,240.0 236.7,240.8 236.5,241.6 236.1,242.4 235.6,243.2 235.0,243.9 234.2,244.6 233.3,245.2 232.3,245.8 231.2,246.3 230.0,246.8 228.8,247.1 227.4,247.4 226.1,247.6 224.7,247.8 223.3,247.8 221.9,247.8 220.5,247.6 219.1,247.4 217.8,247.1 216.5,246.8 215.3,246.3 214.2,245.8 213.2,245.2 212.3,244.6 211.6,243.9 210.9,243.2 210.4,242.4 210.0,241.6 209.8,240.8 209.7,240.0 209.7,217.2 209.8,218.0 210.0,218.8 210.4,219.6 210.9,220.4 211.6,221.1 212.3,221.8 213.2,222.4 214.2,223.0 215.3,223.5 216.5,224.0 217.8,224.3 219.1,224.6 220.5,224.8 221.9,225.0 223.3,225.0 224.7,225.0 226.1,224.8 227.4,224.6 228.8,224.3 230.0,224.0 231.2,223.5 232.3,223.0 233.3,222.4 234.2,221.8 235.0,221.1 235.6,220.4 236.1,219.6 236.5,218.8 236.7,218.0 236.8,217.2" fill="#525a61" stroke="#101820" stroke-width="1"></polygon>
                    <polygon points="240.9,230.5 260.7,241.9 240.9,253.3 221.2,241.9" fill="#d1d3d5" stroke="#101820" stroke-width="1"></polygon>
                    <polygon points="260.7,256.8 240.9,268.2 240.9,253.3 260.7,241.9" fill="#a5a9ad" stroke="#101820" stroke-width="1"></polygon>
                    <polygon points="221.2,256.8 240.9,268.2 240.9,253.3 221.2,241.9" fill="#6b6e71" stroke="#101820" stroke-width="1"></polygon>
                    <line x1="212.9" y1="278.4" x2="205.4" y2="274.1" stroke="#c62828" stroke-width="1.8"></line>
                    <line x1="205.4" y1="274.1" x2="184.6" y2="335.3" stroke="#c62828" stroke-width="1.8"></line>
                    <line x1="184.6" y1="335.3" x2="171.5" y2="333.7" stroke="#c62828" stroke-width="1.8"></line>
                    <circle cx="212.9" cy="278.4" r="2" fill="#c62828"></circle>
                    <circle cx="205.4" cy="274.1" r="2" fill="#c62828"></circle>
                    <text x="30.0" y="196.8" text-anchor="end" fill="#101820" stroke="none" font-family="IBM Plex Sans" font-size="13" font-weight="700">EG</text>
                    <text x="30.0" y="99.6" text-anchor="end" fill="#101820" stroke="none" font-family="IBM Plex Sans" font-size="13" font-weight="700">1</text>
                    <line x1="125.6" y1="295.2" x2="130.8" y2="298.2" stroke="#999da2" stroke-width="0.8"></line>
                    <line x1="125.6" y1="350.4" x2="130.8" y2="353.4" stroke="#999da2" stroke-width="0.8"></line>
                    <line x1="128.7" y1="297.0" x2="128.7" y2="352.2" stroke="#999da2" stroke-width="0.8"></line>
                    <text x="132.9" y="325.8" text-anchor="start" fill="#999da2" stroke="none" font-family="IBM Plex Sans" font-size="10" font-weight="600">SG</text>
                </svg>
            </div>
        </div>
    </section>

    <section class="bg-[{PAPER_50}] py-[56px] px-6">
        <div class="max-w-5xl mx-auto">
            <div class="max-w-xl flex flex-col gap-2 mb-7">
                <span class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_600}]">{lang_nodes(ABOUT_PERA_EYEBROW)}</span>
                <h2 class="font-display break-words text-2xl font-semibold text-[{INK_950}]">{lang_nodes(ABOUT_PERA_H2)}</h2>
            </div>
            <div class="grid md:grid-cols-[0.85fr_1.15fr] gap-7 items-stretch">
                <div class="bg-white border border-[{LINE}] rounded-xl p-7 flex flex-col justify-center gap-4">
                    <img src="/assets/pera-logo.png" alt="PERA Mühendislik" style="height:56px; width:auto; max-width:100%; object-fit:contain; align-self:flex-start; flex-shrink:0; display:block;">
                    <div class="flex flex-col gap-1">
                        <span class="text-sm font-semibold text-[{INK_950}]">{lang_nodes(PERA_TAGLINE1)}</span>
                        <span class="text-[13px] text-[{SLATE_600}]">{lang_nodes(PERA_TAGLINE2)}</span>
                    </div>
                    <a href="https://peramuhendislik.com" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 text-[12.5px] font-semibold text-[{INK_900}]">peramuhendislik.com
                        <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7"></path><path d="M9 7h8v8"></path></svg>
                    </a>
                </div>
                <div class="flex flex-col gap-5">
                    <div class="flex flex-wrap gap-2.5">{tags_html}</div>
                    <div class="bg-white border-l-[3px] border-[{INK_900}] rounded-r-lg py-5 px-6">
                        <p class="text-[14.5px] leading-relaxed text-[{SLATE_700}] italic">{lang_nodes(PERA_QUOTE, tag="span", display="block")}</p>
                        <span class="block mt-2 text-[12.5px] text-[{SLATE_400}] not-italic">{lang_nodes(PERA_QUOTE_SRC)}</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="{KFW_ANCHOR_ID}" class="bg-white py-[56px] px-6">
        <div class="max-w-5xl mx-auto">
            <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[{PAPER_50}] border mb-5" style="border-color:#cfe4dd;">
                <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="#2f5347" stroke-width="2"><circle cx="12" cy="12" r="9"></circle><path d="M8.5 12.5l2.5 2.5 5-5"></path></svg>
                <span class="text-[11.5px] font-bold" style="color:#2f5347;">{lang_nodes(KFW_BADGE)}</span>
            </span>
            <div class="max-w-xl flex flex-col gap-2 mb-5">
                <span class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_600}]">{lang_nodes(KFW_EYEBROW)}</span>
                <h2 class="font-display break-words text-2xl font-semibold text-[{INK_950}]">{lang_nodes(KFW_H2)}</h2>
            </div>
            <p class="text-[15px] leading-relaxed text-[{SLATE_700}] max-w-2xl">{lang_nodes(KFW_LEAD, tag="span", display="block")}</p>

            <div class="grid md:grid-cols-[1.2fr_0.8fr] gap-7 items-start mt-6">
                <div>
                    <h3 class="text-[13px] font-bold uppercase tracking-wide text-[{INK_950}] mb-4">{lang_nodes(KFW_STEPS_H3)}</h3>
                    <div class="flex flex-col gap-4">{kfw_steps_html}
                    </div>
                </div>
                <div class="bg-[{PAPER_50}] border-l-[3px] rounded-r-lg py-5 px-6" style="border-color:#2f5347;">
                    <span class="block text-[12px] font-bold uppercase tracking-wide mb-1.5" style="color:#2f5347;">{lang_nodes(KFW_WHO_LABEL)}</span>
                    <p class="text-[13.5px] leading-relaxed text-[{SLATE_700}]">{lang_nodes(KFW_WHO_TEXT, tag="span", display="block")}</p>
                </div>
            </div>
        </div>
    </section>

    <section class="bg-[{PAPER_50}] py-[56px] px-6">
        <div class="max-w-5xl mx-auto">
            <div class="relative overflow-hidden rounded-xl flex flex-col sm:flex-row sm:items-center gap-5 sm:gap-6 p-6 sm:p-7"
                 style="background:linear-gradient(100deg, #0d1922 0%, {INK_900} 55%, #1c2c3c 100%);">
                <div class="absolute pointer-events-none" style="right:-40px; top:-60px; width:220px; height:220px; opacity:.35; transform:rotate(12deg); background:conic-gradient(from 45deg, #c62828 0deg 60deg, transparent 60deg 120deg, #a01f1f 120deg 180deg, transparent 180deg 240deg, #c62828 240deg 300deg, transparent 300deg 360deg);"></div>
                <div class="flex-shrink-0 relative z-10 w-[70px] h-[96px] rounded-md shadow-lg overflow-hidden" style="background:#1c2c3c;">
                    <div class="absolute" style="right:-14px; top:-10px; width:60px; height:60px; background:#c62828; clip-path:polygon(100% 0, 0 0, 100% 100%); opacity:.9;"></div>
                    <div class="absolute inset-0 flex flex-col justify-between p-[6px]">
                        <span class="relative z-10 text-white font-bold leading-tight" style="font-size:6px;">ELEVATOR<br>SOLUTIONS</span>
                        <span class="relative z-10 bg-white rounded-sm px-1 py-[3px] self-start"><img src="/assets/pera-logo.png" alt="" style="width:28px; display:block;"></span>
                    </div>
                </div>
                <div class="flex-1 relative z-10 text-white min-w-0">
                    <span class="block text-[10.5px] font-bold tracking-widest uppercase" style="color:#e8a9a4;">{lang_nodes(CATALOG_LABEL)}</span>
                    <h3 class="font-display text-[16.5px] font-semibold mt-1">{lang_nodes(CATALOG_TITLE)}</h3>
                    <p class="text-[12.5px] leading-relaxed mt-1" style="color:#c7cdd3;">{lang_nodes(CATALOG_DESC, tag="span", display="block")}</p>
                </div>
                <div class="relative z-10 flex gap-2.5 flex-shrink-0">
                    <button type="button" onclick="openCatalog()" class="px-5 py-3 rounded-md bg-white text-[{INK_950}] font-bold text-[13px] inline-flex items-center gap-2 whitespace-nowrap">
                        <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                        {lang_nodes(CATALOG_VIEW_BTN)}
                    </button>
                    <a href="{CATALOG_URL}" download class="px-3.5 py-3 rounded-md border border-white/30 text-white font-semibold text-[13px] inline-flex items-center gap-2 whitespace-nowrap" style="background:rgba(255,255,255,.08);">
                        <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v13"></path><path d="M7 11l5 5 5-5"></path><path d="M4 20h16"></path></svg>
                        <span class="hidden sm:inline">{lang_nodes(CATALOG_DOWNLOAD)}</span>
                    </a>
                </div>
            </div>

            <div class="mt-4 relative overflow-hidden rounded-xl flex flex-col sm:flex-row sm:items-center gap-5 sm:gap-6 p-6 sm:p-7"
                 style="background:linear-gradient(100deg, #0d1922 0%, {INK_900} 55%, #223247 100%); border:1px dashed rgba(255,255,255,.28);">
                <div class="flex-shrink-0 relative z-10 w-[54px] h-[54px] rounded-lg flex items-center justify-center" style="background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.18);">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="1.5"></rect><path d="M8 8h8M8 12h8M8 16h4"></path></svg>
                </div>
                <div class="flex-1 relative z-10 text-white min-w-0">
                    <span class="block text-[10.5px] font-bold tracking-widest uppercase" style="color:#9ad0c2;">{lang_nodes(QUOTE_LABEL)}</span>
                    <h3 class="font-display text-[16.5px] font-semibold mt-1">{lang_nodes(QUOTE_TITLE)}</h3>
                    <p class="text-[12.5px] leading-relaxed mt-1" style="color:#c7cdd3;">{lang_nodes(QUOTE_DESC, tag="span", display="block")}</p>
                </div>
                <div class="relative z-10 flex-shrink-0">
                    <button type="button" onclick="openQuoteForm()" class="px-5 py-3 rounded-md bg-white text-[{INK_950}] font-bold text-[13px] inline-flex items-center gap-2 whitespace-nowrap">
                        {lang_nodes(QUOTE_BTN)}
                        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg>
                    </button>
                </div>
            </div>
        </div>
    </section>

    <section class="bg-white py-[56px] px-6">
        <div class="max-w-5xl mx-auto">
            <h2 class="font-display break-words text-2xl font-semibold text-[{INK_950}] mb-7">{lang_nodes(WHAT_IT_MEANS_H2)}</h2>
            <div class="grid md:grid-cols-3 gap-7">{means_html}
            </div>
        </div>
    </section>

    <section class="bg-[{INK_900}] py-[56px] px-6 text-center">
        <div class="max-w-xl mx-auto flex flex-col items-center gap-5 py-1">
            <h2 class="font-display break-words text-3xl font-semibold text-white">{lang_nodes(PERA_CTA_H2, tag="span", display="block")}</h2>
            <a href="/contact" class="mt-1 px-8 py-3.5 rounded-md bg-white text-[{INK_900}] font-bold text-sm">{lang_nodes(CTA_BTN)}</a>
        </div>
    </section>

    <div id="catalog-modal" class="fixed inset-0 z-[100] items-center justify-center p-4" style="display:none; background:rgba(16,24,32,0.75);" onclick="if(event.target===this) closeCatalog();">
        <div class="w-full rounded-xl overflow-hidden shadow-2xl flex flex-col" style="max-width:760px; max-height:88vh; background:{PAPER_50};">
            <div class="flex items-center justify-between gap-3 px-4 py-3 text-white flex-shrink-0" style="background:{INK_950};">
                <div class="min-w-0">
                    <div class="text-[13.5px] font-bold truncate">{lang_nodes(CATALOG_TITLE)}</div>
                    <div class="text-[10.5px]" style="color:{SLATE_300};">peramuhendislik.com</div>
                </div>
                <div class="flex items-center gap-1.5 flex-shrink-0">
                    <button type="button" onclick="catalogPrevPage()" aria-label="{CATALOG_PREV_ARIA['de']}" class="w-8 h-8 rounded-md flex items-center justify-center text-white" style="background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.18);">
                        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"></path></svg>
                    </button>
                    <span id="catalog-page-indicator" class="text-[11.5px] px-2.5 py-1.5 rounded whitespace-nowrap" style="background:rgba(255,255,255,.08); color:#e7e9eb;">1 / {CATALOG_PAGES}</span>
                    <button type="button" onclick="catalogNextPage()" aria-label="{CATALOG_NEXT_ARIA['de']}" class="w-8 h-8 rounded-md flex items-center justify-center text-white" style="background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.18);">
                        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"></path></svg>
                    </button>
                    <button type="button" onclick="closeCatalog()" aria-label="{CATALOG_CLOSE_ARIA['de']}" class="w-8 h-8 rounded-md flex items-center justify-center text-white ml-1" style="background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.18);">
                        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 6l12 12"></path><path d="M18 6L6 18"></path></svg>
                    </button>
                </div>
            </div>
            <div class="relative flex-1 overflow-auto flex items-center justify-center" style="background:#dfe2e5; min-height:320px;">
                <button type="button" onclick="catalogPrevPage()" aria-label="{CATALOG_PREV_ARIA['de']}" class="hidden md:flex absolute left-3 top-1/2 -translate-y-1/2 w-9 h-9 rounded-full items-center justify-center z-10" style="background:rgba(16,24,32,.55); color:#fff;">
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"></path></svg>
                </button>
                <div id="catalog-loading" class="text-[13px] px-6 text-center" style="color:{SLATE_600};">{lang_nodes(CATALOG_LOADING)}</div>
                <canvas id="catalog-canvas" class="hidden shadow-lg" style="max-width:100%; height:auto;"></canvas>
                <button type="button" onclick="catalogNextPage()" aria-label="{CATALOG_NEXT_ARIA['de']}" class="hidden md:flex absolute right-3 top-1/2 -translate-y-1/2 w-9 h-9 rounded-full items-center justify-center z-10" style="background:rgba(16,24,32,.55); color:#fff;">
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"></path></svg>
                </button>
            </div>
            <div class="flex items-center justify-between gap-3 px-4 py-2.5 border-t flex-shrink-0" style="border-color:{LINE}; background:{PAPER_50};">
                <a href="{CATALOG_URL}" download class="text-[12px] font-semibold inline-flex items-center gap-1.5" style="color:{INK_900};">
                    <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v13"></path><path d="M7 11l5 5 5-5"></path><path d="M4 20h16"></path></svg>
                    {lang_nodes(CATALOG_DOWNLOAD)}
                </a>
                <div class="flex items-center gap-2">
                    <button type="button" onclick="catalogZoom(-1)" class="w-[26px] h-[26px] rounded border text-[13px] font-bold flex items-center justify-center" style="border-color:{LINE}; color:{SLATE_700};">&minus;</button>
                    <span id="catalog-zoom-indicator" class="text-[11.5px] w-9 text-center" style="color:{SLATE_600};">100%</span>
                    <button type="button" onclick="catalogZoom(1)" class="w-[26px] h-[26px] rounded border text-[13px] font-bold flex items-center justify-center" style="border-color:{LINE}; color:{SLATE_700};">+</button>
                </div>
            </div>
        </div>
    </div>

    <div id="quote-modal" class="fixed inset-0 z-[100] items-center justify-center p-4" style="display:none; background:rgba(16,24,32,0.75);" onclick="if(event.target===this) closeQuoteForm();">
        <div class="w-full rounded-xl overflow-hidden shadow-2xl flex flex-col" style="max-width:720px; max-height:90vh; background:{PAPER_50};">
            <div class="flex items-center justify-between gap-3 px-4 py-3 text-white flex-shrink-0" style="background:{INK_950};">
                <div class="min-w-0">
                    <div class="text-[13.5px] font-bold truncate">{lang_nodes(QUOTE_MODAL_TITLE)}</div>
                    <div class="text-[10.5px] truncate" style="color:{SLATE_300};">{lang_nodes(QUOTE_MODAL_SUB)}</div>
                </div>
                <button type="button" onclick="closeQuoteForm()" aria-label="{QUOTE_CLOSE_ARIA['de']}" class="w-8 h-8 rounded-md flex items-center justify-center text-white flex-shrink-0" style="background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.18);">
                    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 6l12 12"></path><path d="M18 6L6 18"></path></svg>
                </button>
            </div>

            <div class="flex items-center gap-1.5 px-4 py-2.5" style="background:#eceeef; border-bottom:1px solid {LINE}; overflow-x:auto;">{quote_nav_html}
            </div>

            <form id="quote-form" onsubmit="return submitForm(event, '{FORMSPREE_ENDPOINT}')" class="flex-1 overflow-y-auto px-5 sm:px-6 pt-5 pb-2">

                <div id="q-s1" class="bg-white border border-[{LINE}] rounded-xl p-5 sm:p-6 mb-4">
                    <div class="flex items-center gap-2.5 mb-4">
                        <span class="w-[22px] h-[22px] rounded-full bg-[{INK_950}] text-white text-[11px] font-bold flex items-center justify-center flex-shrink-0">1</span>
                        <h4 class="font-display text-[15px] font-semibold text-[{INK_950}]">{lang_nodes(Q_S1_H)}</h4>
                    </div>
                    <div class="grid sm:grid-cols-2 gap-[14px] mb-[14px]">
                        <label class="flex flex-col gap-2">
                            <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_COMPANY)} <span style="color:#c62828;">*</span></span>
                            <input type="text" name="company" required placeholder="{Q_F_COMPANY_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                        </label>
                        <label class="flex flex-col gap-2">
                            <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_CONTACT)} <span style="color:#c62828;">*</span></span>
                            <input type="text" name="contact_person" required class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                        </label>
                    </div>
                    <div class="grid sm:grid-cols-2 gap-[14px] mb-[14px]">
                        <label class="flex flex-col gap-2">
                            <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_EMAIL)} <span style="color:#c62828;">*</span></span>
                            <input type="email" name="email" required class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                        </label>
                        <label class="flex flex-col gap-2">
                            <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_PHONE)}</span>
                            <input type="tel" name="phone" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                        </label>
                    </div>
                    <label class="flex flex-col gap-2">
                        <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_REF)} <span class="font-medium text-[{SLATE_400}]">({lang_nodes(Q_OPTIONAL)})</span></span>
                        <input type="text" name="reference" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                    </label>
                </div>

                <div id="q-s2" class="bg-white border border-[{LINE}] rounded-xl p-5 sm:p-6 mb-4">
                    <div class="flex items-center gap-2.5 mb-4">
                        <span class="w-[22px] h-[22px] rounded-full bg-[{INK_950}] text-white text-[11px] font-bold flex items-center justify-center flex-shrink-0">2</span>
                        <h4 class="font-display text-[15px] font-semibold text-[{INK_950}]">{lang_nodes(Q_S2_H)}</h4>
                    </div>
                    <label class="flex items-center gap-3 rounded-lg px-4 py-3.5 mb-[14px] cursor-pointer select-none border" style="background:#eef4f2; border-color:#cfe4dd;">
                        <input type="checkbox" id="kfw-toggle" name="kfw_159_interest" value="Yes" onchange="toggleKfwUnits(this)" class="w-[18px] h-[18px] flex-shrink-0" style="accent-color:#2f5347;">
                        <span class="flex flex-col gap-0.5">
                            <span class="text-[13.5px] font-bold" style="color:#2f5347;">{lang_nodes(Q_F_KFW_INTEREST)}</span>
                            <span class="text-[11.5px] leading-snug" style="color:#2f5347; opacity:.85;">{lang_nodes(Q_F_KFW_HINT)}</span>
                        </span>
                    </label>
                    <div id="kfw-units-wrap" class="hidden flex-col gap-2 mb-[14px]">
                        <label class="flex flex-col gap-2">
                            <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_UNITS)} <span class="font-medium text-[{SLATE_400}]">({lang_nodes(Q_OPTIONAL)})</span></span>
                            <input type="number" name="unit_count" min="1" step="1" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                        </label>
                    </div>
                    <div class="flex flex-col gap-2 mb-[14px]">
                        <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_BTYPE)}</span>
                        <div class="flex flex-wrap gap-2">{btype_html}</div>
                    </div>
                    <div class="flex flex-col gap-2 mb-[14px]">
                        <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_BCOND)}</span>
                        <div class="flex flex-wrap gap-2">{bcond_html}</div>
                    </div>
                    <div class="flex flex-col gap-2 mb-[14px]">
                        <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_USE)} <span class="font-medium text-[{SLATE_400}]">({lang_nodes(Q_MULTI)})</span></span>
                        <div class="flex flex-wrap gap-2">{use_html}</div>
                    </div>
                    <div class="grid sm:grid-cols-2 gap-[14px] mb-[14px]">
                        <label class="flex flex-col gap-2">
                            <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_LOCATION)}</span>
                            <input type="text" name="location" placeholder="{Q_F_LOCATION_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                        </label>
                        <label class="flex flex-col gap-2">
                            <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_DEADLINE)}</span>
                            <input type="text" name="deadline" placeholder="{Q_F_DEADLINE_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                        </label>
                    </div>
                </div>

                <div id="q-s3" class="rounded-xl p-5 sm:p-6 mb-4" style="background:linear-gradient(180deg,#fff 0%, #fafbfb 100%); border:1.5px solid {INK_900};">
                    <div class="flex items-center gap-2.5 mb-1">
                        <span class="w-[22px] h-[22px] rounded-full text-white text-[11px] font-bold flex items-center justify-center flex-shrink-0" style="background:#c62828;">3</span>
                        <h4 class="font-display text-[15px] font-semibold text-[{INK_950}]">{lang_nodes(Q_S3_H)}</h4>
                    </div>
                    <p class="text-[12px] text-[{SLATE_600}] mb-4 ml-[30px]">{lang_nodes(Q_S3_SUB)}</p>
                    <div class="grid sm:grid-cols-3 gap-[14px]">{spec_fields_html}
                    </div>
                    <div class="flex gap-2.5 mt-4 rounded-lg p-3" style="background:#eef4f2; border:1px solid #cfe4dd;">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#2f5347" stroke-width="2" class="flex-shrink-0 mt-[1px]"><circle cx="12" cy="12" r="9"></circle><path d="M12 8v.01M11 12h1v5h1"></path></svg>
                        <p class="text-[12px] leading-relaxed" style="color:#2f5347;">{lang_nodes(Q_TIP, tag="span", display="block")}</p>
                    </div>
                </div>

                <div id="q-s4" class="bg-white border border-[{LINE}] rounded-xl p-5 sm:p-6 mb-4">
                    <div class="flex items-center gap-2.5 mb-4">
                        <span class="w-[22px] h-[22px] rounded-full bg-[{INK_950}] text-white text-[11px] font-bold flex items-center justify-center flex-shrink-0">4</span>
                        <h4 class="font-display text-[15px] font-semibold text-[{INK_950}]">{lang_nodes(Q_S4_H)}</h4>
                    </div>
                    <label class="flex flex-col gap-2">
                        <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(Q_F_NOTES)} <span class="font-medium text-[{SLATE_400}]">({lang_nodes(Q_OPTIONAL)})</span></span>
                        <textarea name="notes" rows="3" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]"></textarea>
                    </label>
                </div>

                <div id="q-s5" class="bg-white border border-[{LINE}] rounded-xl p-5 sm:p-6 mb-4">
                    <div class="flex items-center gap-2.5 mb-4">
                        <span class="w-[22px] h-[22px] rounded-full bg-[{INK_950}] text-white text-[11px] font-bold flex items-center justify-center flex-shrink-0">5</span>
                        <h4 class="font-display text-[15px] font-semibold text-[{INK_950}]">{lang_nodes(Q_S5_H)}</h4>
                    </div>
                    <select name="source" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}] bg-white w-full sm:w-auto">{source_opts_html}
                    </select>
                </div>

                <p class="submit-note-ok text-[13px] text-[{SLATE_600}] leading-relaxed mb-3" hidden>{lang_nodes(SUBMIT_NOTE_OK, tag="span", display="block")}</p>
                <p class="submit-note-error text-[13px] leading-relaxed mb-3" style="color:#b3261e;" hidden>{lang_nodes(SUBMIT_NOTE_ERROR, tag="span", display="block")}</p>
            </form>

            <div class="flex items-center justify-between gap-3 px-5 sm:px-6 py-3.5 border-t flex-shrink-0 flex-wrap" style="border-color:{LINE}; background:{PAPER_50};">
                <p class="text-[11px] text-[{SLATE_400}] leading-relaxed max-w-[260px]">{lang_nodes(Q_PRIVACY, tag="span", display="block")}</p>
                <button type="submit" form="quote-form" class="px-7 py-3 rounded-md text-white font-bold text-[13.5px] whitespace-nowrap" style="background:{INK_900};">{lang_nodes(Q_SUBMIT)}</button>
            </div>
        </div>
    </div>

    <script>
        var catalogState = {{ pdfDoc: null, pageNum: 1, numPages: {CATALOG_PAGES}, scale: 1.0, rendering: false, pending: null, loading: false }};
        var CATALOG_URL = '{CATALOG_URL}';
        var CATALOG_PDFJS_BASE = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/';

        function openCatalog() {{
            var modal = document.getElementById('catalog-modal');
            modal.style.display = 'flex';
            document.body.classList.add('overflow-hidden');
            document.addEventListener('keydown', catalogKeyHandler);
            if (!catalogState.pdfDoc && !catalogState.loading) {{
                catalogState.loading = true;
                loadCatalogPdfJs(function () {{
                    window.pdfjsLib.GlobalWorkerOptions.workerSrc = CATALOG_PDFJS_BASE + 'pdf.worker.min.js';
                    window.pdfjsLib.getDocument(CATALOG_URL).promise.then(function (pdf) {{
                        catalogState.pdfDoc = pdf;
                        catalogState.numPages = pdf.numPages;
                        renderCatalogPage(1);
                    }}).catch(function (err) {{
                        var loadingEl = document.getElementById('catalog-loading');
                        if (loadingEl) loadingEl.textContent = 'Error loading PDF.';
                        console.error('PERA catalog: PDF load error', err);
                    }});
                }});
            }}
        }}

        function closeCatalog() {{
            var modal = document.getElementById('catalog-modal');
            modal.style.display = 'none';
            document.body.classList.remove('overflow-hidden');
            document.removeEventListener('keydown', catalogKeyHandler);
        }}

        function catalogKeyHandler(e) {{
            if (e.key === 'Escape') closeCatalog();
            else if (e.key === 'ArrowLeft') catalogPrevPage();
            else if (e.key === 'ArrowRight') catalogNextPage();
        }}

        function openQuoteForm(kfw) {{
            var modal = document.getElementById('quote-modal');
            modal.style.display = 'flex';
            document.body.classList.add('overflow-hidden');
            document.addEventListener('keydown', quoteKeyHandler);
            if (kfw) {{
                var cb = document.getElementById('kfw-toggle');
                if (cb && !cb.checked) {{
                    cb.checked = true;
                    toggleKfwUnits(cb);
                }}
            }}
        }}

        function toggleKfwUnits(checkbox) {{
            var wrap = document.getElementById('kfw-units-wrap');
            if (!wrap) return;
            if (checkbox.checked) {{
                wrap.classList.remove('hidden');
                wrap.classList.add('flex');
            }} else {{
                wrap.classList.add('hidden');
                wrap.classList.remove('flex');
            }}
        }}

        function closeQuoteForm() {{
            var modal = document.getElementById('quote-modal');
            modal.style.display = 'none';
            document.body.classList.remove('overflow-hidden');
            document.removeEventListener('keydown', quoteKeyHandler);
        }}

        function quoteKeyHandler(e) {{
            if (e.key === 'Escape') closeQuoteForm();
        }}

        function loadCatalogPdfJs(cb) {{
            if (window.pdfjsLib) {{ cb(); return; }}
            var s = document.createElement('script');
            s.src = CATALOG_PDFJS_BASE + 'pdf.min.js';
            s.onload = cb;
            s.onerror = function () {{
                var loadingEl = document.getElementById('catalog-loading');
                if (loadingEl) loadingEl.textContent = 'Error loading viewer.';
            }};
            document.head.appendChild(s);
        }}

        function renderCatalogPage(num) {{
            if (!catalogState.pdfDoc) return;
            catalogState.rendering = true;
            var loadingEl = document.getElementById('catalog-loading');
            var canvas = document.getElementById('catalog-canvas');
            if (loadingEl) loadingEl.classList.remove('hidden');
            catalogState.pdfDoc.getPage(num).then(function (page) {{
                var container = canvas.parentElement;
                var containerWidth = Math.max(240, Math.min(container.clientWidth - 32, 900));
                var containerHeight = Math.max(240, container.clientHeight - 32);
                var unscaledViewport = page.getViewport({{ scale: 1 }});
                var widthScale = containerWidth / unscaledViewport.width;
                var heightScale = containerHeight / unscaledViewport.height;
                var fitScale = Math.min(widthScale, heightScale);
                var viewport = page.getViewport({{ scale: fitScale * catalogState.scale }});
                var ctx = canvas.getContext('2d');
                canvas.width = viewport.width;
                canvas.height = viewport.height;
                page.render({{ canvasContext: ctx, viewport: viewport }}).promise.then(function () {{
                    catalogState.rendering = false;
                    if (loadingEl) loadingEl.classList.add('hidden');
                    canvas.classList.remove('hidden');
                    if (catalogState.pending !== null) {{
                        var p = catalogState.pending;
                        catalogState.pending = null;
                        renderCatalogPage(p);
                    }}
                }});
            }});
            catalogState.pageNum = num;
            var indicator = document.getElementById('catalog-page-indicator');
            if (indicator) indicator.textContent = num + ' / ' + catalogState.numPages;
        }}

        function queueCatalogPage(num) {{
            if (num < 1 || num > catalogState.numPages) return;
            if (catalogState.rendering) {{ catalogState.pending = num; return; }}
            renderCatalogPage(num);
        }}
        function catalogPrevPage() {{ queueCatalogPage(catalogState.pageNum - 1); }}
        function catalogNextPage() {{ queueCatalogPage(catalogState.pageNum + 1); }}
        function catalogZoom(dir) {{
            catalogState.scale = Math.max(0.6, Math.min(2.2, Math.round((catalogState.scale + dir * 0.2) * 10) / 10));
            var indicator = document.getElementById('catalog-zoom-indicator');
            if (indicator) indicator.textContent = Math.round(catalogState.scale * 100) + '%';
            queueCatalogPage(catalogState.pageNum);
        }}
    </script>
'''
    return page_html('pera', PERA_TITLE, PERA_DESC, '/partnership/pera', body, json_ld=PERA_JSON_LD, keywords=PERA_KEYWORDS)


# ---------------------------------------------------------- INDUSTRIES PAGE---
IND_TITLE = L(
    'Partnerschaft — Andere Branchen | CHELA Industrial',
    'Partnership — Other Industries | CHELA Industrial',
    'Ortaklık — Diğer Sektörler | CHELA Industrial',
)
IND_DESC = L(
    'CHELA Industrial verbindet Hersteller, Lieferanten, Käufer und Verkäufer über alle Industriezweige hinweg — weltweit, mit Schwerpunkt auf Deutschland, der EU, dem Balkan und der Türkei.',
    'CHELA Industrial connects manufacturers, suppliers, buyers and sellers across every branch of industry — worldwide, with a focus on Germany, the EU, the Balkans and Turkey.',
    'CHELA Industrial, tüm sektörlerdeki üreticileri, tedarikçileri, alıcıları ve satıcıları birbirine bağlar — dünya çapında, Almanya, AB, Balkanlar ve Türkiye odaklı.',
)
IND_KEYWORDS = L(
    'Branchenübergreifender Handel, Industriehandel weltweit, Handelsvermittlung Deutschland EU Balkan Türkei',
    'cross-industry trade, worldwide industrial trade, trade mediation Germany EU Balkans Turkey',
    'sektörler arası ticaret, dünya çapında endüstriyel ticaret, Almanya AB Balkanlar Türkiye ticaret aracılığı',
)
IND_EYEBROW = L('Partnerschaft — Andere Branchen', 'Partnership — Other Industries', 'Ortaklık — Diğer Sektörler')
IND_H1 = L(
    'Handel und Vermittlung über alle Industriezweige hinweg.',
    'Trade and mediation across every branch of industry.',
    'Tüm sektörlerde ticaret ve arabuluculuk.',
)
IND_SUB = L(
    'Unsere Partnerschaft mit PERA Mühendislik ist unser sichtbarstes Beispiel — aber bei weitem nicht der einzige Bereich, in dem wir aktiv sind. CHELA Industrial verbindet Hersteller, Lieferanten, Käufer und Verkäufer weltweit, unabhängig von Branche oder Standort.',
    'Our partnership with PERA Mühendislik is our most visible example — but by far not the only area we\'re active in. CHELA Industrial connects manufacturers, suppliers, buyers and sellers worldwide, regardless of industry or location.',
    'PERA Mühendislik ile ortaklığımız en görünür örneğimizdir — ancak faaliyet gösterdiğimiz tek alan değildir. CHELA Industrial, sektör veya konum fark etmeksizin dünya çapında üreticileri, tedarikçileri, alıcıları ve satıcıları birbirine bağlar.',
)
SCOPE_EYEBROW = L('Reichweite', 'Reach', 'Kapsam')
SCOPE_H2 = L('Für wen wir arbeiten', 'Who we work for', 'Kimler için çalışıyoruz')
SCOPE_P = L(
    'Ob produzierendes Gewerbe, Zulieferer oder Projektträger — wir bringen die passenden Parteien zusammen und begleiten die Abwicklung, mit Schwerpunkt auf Deutschland, der EU, dem Balkan und der Türkei, grundsätzlich aber ohne geografische oder branchenspezifische Einschränkung.',
    'Whether manufacturing businesses, suppliers or project owners — we bring the right parties together and support the process, with a focus on Germany, the EU, the Balkans and Turkey, but fundamentally without geographic or industry restrictions.',
    'İster üretim işletmesi, ister tedarikçi veya proje sahibi olun — doğru tarafları bir araya getirir ve süreci destekleriz; odağımız Almanya, AB, Balkanlar ve Türkiye olsa da temelde coğrafi veya sektörel bir kısıtlama yoktur.',
)
IND_CARDS = [
    (L('Hersteller', 'Manufacturers', 'Üreticiler'),
     L('Neue Absatzmärkte und Vertriebspartner jenseits der eigenen Landesgrenzen.',
       'New sales markets and distribution partners beyond your own borders.',
       'Kendi sınırlarınızın ötesinde yeni satış pazarları ve dağıtım ortakları.'),
     '<rect x="3" y="7" width="18" height="13" rx="1.5"></rect><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>'),
    (L('Lieferanten', 'Suppliers', 'Tedarikçiler'),
     L('Verlässliche Abnehmer und langfristige Handelsbeziehungen.',
       'Reliable buyers and long-term trade relationships.',
       'Güvenilir alıcılar ve uzun vadeli ticari ilişkiler.'),
     '<path d="M3 12h18"></path><path d="M3 6h18"></path><path d="M3 18h12"></path>'),
    (L('Käufer', 'Buyers', 'Alıcılar'),
     L('Zugang zu geprüften Herstellern und Anlagen für internationale Beschaffung.',
       'Access to vetted manufacturers and equipment for international sourcing.',
       'Uluslararası tedarik için denetlenmiş üreticilere ve tesislere erişim.'),
     '<circle cx="9" cy="7" r="3.2"></circle><path d="M2.5 20c0-3.6 2.9-6.5 6.5-6.5"></path><path d="M16 9.5a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path><path d="M14.5 20c0.2-3 2.4-5.4 5.3-5.9"></path>'),
    (L('Verkäufer', 'Sellers', 'Satıcılar'),
     L('Vermittlung an passende Projektträger und Abnehmer im Zielmarkt.',
       'Mediation to suitable project owners and buyers in the target market.',
       'Hedef pazardaki uygun proje sahipleri ve alıcılarla eşleştirme.'),
     '<path d="M12 2v20"></path><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7H14a3.5 3.5 0 0 1 0 7H6"></path>'),
]
IND_CTA_H2 = L(
    'Welches Anliegen bringen Sie mit — gleich aus welcher Branche?',
    'What can we help you with — whatever your industry?',
    'Hangi sektörden olursanız olun, size nasıl yardımcı olabiliriz?',
)


def render_industries():
    cards_html = ''
    for title, desc, icon in IND_CARDS:
        cards_html += f'''
        <div class="flex flex-col gap-3">
            <div class="w-[52px] h-[52px] rounded-lg bg-[#eef0f1] text-[{INK_900}] flex items-center justify-center" style="width:52px;height:52px;">
                <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{icon}</svg>
            </div>
            <h3 class="text-[15px] font-semibold text-[{INK_950}]">{lang_nodes(title)}</h3>
            <p class="text-[13px] leading-relaxed text-[{SLATE_600}]">{lang_nodes(desc, tag="span", display="block")}</p>
        </div>'''

    body = f'''
    <header class="bg-[{INK_950}] text-white py-20 px-6"
      style="background-image:linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size:46px 46px;">
        <div class="max-w-3xl mx-auto flex flex-col gap-4">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(IND_EYEBROW)}</span>
            <h1 class="font-display break-words text-3xl md:text-4xl font-bold leading-tight">{lang_nodes(IND_H1, tag="span", display="block")}</h1>
            <p class="text-base text-[{SLATE_300}] leading-relaxed max-w-xl">{lang_nodes(IND_SUB, tag="span", display="block")}</p>
        </div>
    </header>

    <section class="bg-white py-20 px-6">
        <div class="max-w-6xl mx-auto">
            <div class="max-w-2xl flex flex-col gap-3.5 mb-[52px]">
                <span class="text-xs font-semibold tracking-widest uppercase text-[{INK_900}]">{lang_nodes(SCOPE_EYEBROW)}</span>
                <h2 class="font-display break-words text-2xl font-semibold text-[{INK_950}]">{lang_nodes(SCOPE_H2)}</h2>
                <p class="text-[15px] leading-relaxed text-[{SLATE_600}]">{lang_nodes(SCOPE_P, tag="span", display="block")}</p>
            </div>
            <div class="grid md:grid-cols-4 gap-7">{cards_html}
            </div>
        </div>
    </section>

    <section class="bg-[{INK_900}] py-[76px] px-6 text-center">
        <div class="max-w-xl mx-auto flex flex-col items-center gap-5 py-1">
            <h2 class="font-display break-words text-3xl font-semibold text-white">{lang_nodes(IND_CTA_H2, tag="span", display="block")}</h2>
            <a href="/contact" class="mt-1 px-8 py-3.5 rounded-md bg-white text-[{INK_900}] font-bold text-sm">{lang_nodes(CTA_BTN)}</a>
        </div>
    </section>
'''
    return page_html('industries', IND_TITLE, IND_DESC, '/partnership/industries', body, keywords=IND_KEYWORDS)


# ---------------------------------------------------------- PARTNER-FORM PAGE
PF_TITLE = L(
    'Partnerschaft — Partner werden | CHELA Industrial',
    'Partnership — Become a Partner | CHELA Industrial',
    'Ortaklık — Partner Olun | CHELA Industrial',
)
PF_DESC = L(
    'Werden Sie offizieller Partner von CHELA Industrial — eine Partnerschaft entsteht immer über eine unterzeichnete Kooperationsvereinbarung.',
    'Become an official partner of CHELA Industrial — a partnership always comes about through a signed cooperation agreement.',
    'CHELA Industrial\'in resmi ortağı olun — bir ortaklık her zaman imzalı bir iş birliği anlaşmasıyla kurulur.',
)
PF_KEYWORDS = L(
    'Partner werden, Kooperationsanfrage, Hersteller Handelsunternehmen Partnerschaft',
    'become a partner, cooperation inquiry, manufacturer trading company partnership',
    'partner olun, iş birliği talebi, üretici ticaret şirketi ortaklığı',
)
PF_EYEBROW = L('Partnerschaft — Partner werden', 'Partnership — Become a Partner', 'Ortaklık — Partner Olun')
PF_H1 = L('Mit CHELA Industrial zusammenarbeiten.', 'Work with CHELA Industrial.', 'CHELA Industrial ile çalışın.')
PF_SUB = L(
    'Eine offizielle Partnerschaft entsteht bei uns immer über eine unterzeichnete Kooperationsvereinbarung — so wie mit PERA Mühendislik. Schildern Sie uns kurz Ihr Anliegen, und wir melden uns direkt bei Ihnen.',
    'An official partnership with us always comes about through a signed cooperation agreement — just as with PERA Mühendislik. Tell us briefly about your interest, and we\'ll get back to you directly.',
    'Bizimle resmi bir ortaklık her zaman imzalı bir iş birliği anlaşmasıyla kurulur — tıpkı PERA Mühendislik ile olduğu gibi. İlginizi bize kısaca anlatın, size doğrudan geri döneceğiz.',
)

F_NAME = L('Name', 'Name', 'Ad Soyad')
F_NAME_PH = L('Ihr vollständiger Name', 'Your full name', 'Tam adınız')
F_COMPANY = L('Unternehmen', 'Company', 'Şirket')
F_COMPANY_PH = L('Firmenname', 'Company name', 'Şirket adı')
F_EMAIL = L('E-Mail', 'Email', 'E-posta')
F_EMAIL_PH = L('name@unternehmen.de', 'name@company.com', 'ad@sirket.com')
F_INDUSTRY = L('Branche', 'Industry', 'Sektör')
F_INDUSTRY_PH = L('z. B. Maschinenbau, Aufzugstechnik …', 'e.g. mechanical engineering, elevator technology …', 'örn. makine mühendisliği, asansör teknolojisi …')
F_MESSAGE = L('Worum geht es?', 'What\'s this about?', 'Konu nedir?')
F_MESSAGE_PH = L(
    'Beschreiben Sie kurz Ihr Unternehmen und Ihr Anliegen für eine mögliche Zusammenarbeit.',
    'Briefly describe your company and your interest in a possible collaboration.',
    'Şirketinizi ve olası bir iş birliğine olan ilginizi kısaca açıklayın.',
)
F_SUBMIT = L('Anfrage senden', 'Send inquiry', 'Talebi gönder')
SUBMIT_NOTE_OK = L(
    'Danke — Ihre Anfrage ist bei uns eingegangen. Wir melden uns so schnell wie möglich bei Ihnen.',
    'Thank you — your inquiry has been received. We\'ll get back to you as soon as possible.',
    'Teşekkürler — talebiniz bize ulaştı. En kısa sürede size geri döneceğiz.',
)
SUBMIT_NOTE_ERROR = L(
    'Da ist leider etwas schiefgelaufen. Bitte schreiben Sie uns direkt an info@chela-industrial.de.',
    'Something went wrong on our end. Please email us directly at info@chela-industrial.de.',
    'Maalesef bir sorun oluştu. Lütfen doğrudan info@chela-industrial.de adresine yazın.',
)

NEXT_STEPS_H3 = L('So geht es weiter', 'What happens next', 'Sırada ne var')
NEXT_STEPS = [
    L('Wir prüfen Ihre Anfrage und melden uns persönlich zurück.',
      'We review your inquiry and get back to you personally.',
      'Talebinizi inceler ve size şahsen geri döneriz.'),
    L('Gemeinsames Gespräch zu Umfang und Rahmen der Zusammenarbeit.',
      'A joint conversation about the scope and framework of the collaboration.',
      'İş birliğinin kapsamı ve çerçevesi hakkında ortak bir görüşme.'),
    L('Eine offizielle Partnerschaft wird erst mit einer unterzeichneten Kooperationsvereinbarung wirksam.',
      'An official partnership only takes effect once a cooperation agreement has been signed.',
      'Resmi bir ortaklık yalnızca bir iş birliği anlaşması imzalandığında yürürlüğe girer.'),
]
DIRECT_CONTACT = L('Direktkontakt', 'Direct contact', 'Doğrudan iletişim')


def render_partner_form():
    steps_html = ''
    for i, step in enumerate(NEXT_STEPS, start=1):
        steps_html += f'''
                    <div class="flex gap-3 items-start">
                        <span class="w-[22px] h-[22px] rounded-full bg-[{INK_950}] text-white text-[11px] font-bold flex items-center justify-center flex-shrink-0">{i}</span>
                        <span class="text-[13.5px] text-[{SLATE_700}] leading-relaxed">{lang_nodes(step, tag="span", display="block")}</span>
                    </div>'''

    body = f'''
    <header class="bg-[{INK_950}] text-white py-20 px-6 pb-14"
      style="background-image:linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size:46px 46px;">
        <div class="max-w-2xl mx-auto flex flex-col gap-3.5">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(PF_EYEBROW)}</span>
            <h1 class="font-display break-words text-3xl font-bold leading-tight">{lang_nodes(PF_H1)}</h1>
            <p class="text-[15.5px] text-[{SLATE_300}] leading-relaxed max-w-lg">{lang_nodes(PF_SUB, tag="span", display="block")}</p>
        </div>
    </header>

    <section class="bg-white py-20 px-6">
        <div class="max-w-5xl mx-auto grid md:grid-cols-[1.3fr_0.8fr] gap-14">

            <form onsubmit="return submitForm(event, '{FORMSPREE_ENDPOINT}')" class="flex flex-col gap-5 max-w-lg">
                <div class="grid sm:grid-cols-2 gap-[18px]">
                    <label class="flex flex-col gap-2">
                        <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(F_NAME)} <span style="color:{INK_900};">*</span></span>
                        <input type="text" name="name" required placeholder="{F_NAME_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                    </label>
                    <label class="flex flex-col gap-2">
                        <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(F_COMPANY)} <span style="color:{INK_900};">*</span></span>
                        <input type="text" name="company" required placeholder="{F_COMPANY_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                    </label>
                </div>
                <div class="grid sm:grid-cols-2 gap-[18px]">
                    <label class="flex flex-col gap-2">
                        <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(F_EMAIL)} <span style="color:{INK_900};">*</span></span>
                        <input type="email" name="email" required placeholder="{F_EMAIL_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                    </label>
                    <label class="flex flex-col gap-2">
                        <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(F_INDUSTRY)} <span style="color:{INK_900};">*</span></span>
                        <input type="text" name="industry" required placeholder="{F_INDUSTRY_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                    </label>
                </div>
                <label class="flex flex-col gap-2">
                    <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(F_MESSAGE)}</span>
                    <textarea name="message" rows="4" placeholder="{F_MESSAGE_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]"></textarea>
                </label>
                <button type="submit" class="self-start mt-1 px-8 py-3.5 rounded-md bg-[{INK_900}] text-white font-semibold text-sm hover:bg-[#3a4a5c] transition-colors">{lang_nodes(F_SUBMIT)}</button>
                <p class="submit-note-ok text-[13px] text-[{SLATE_600}] leading-relaxed" hidden>{lang_nodes(SUBMIT_NOTE_OK, tag="span", display="block")}</p>
                <p class="submit-note-error text-[13px] leading-relaxed" style="color:#b3261e;" hidden>{lang_nodes(SUBMIT_NOTE_ERROR, tag="span", display="block")}</p>
            </form>

            <div class="flex flex-col gap-6">
                <div class="flex flex-col gap-4 p-7 border border-[{LINE}] rounded-xl bg-[{PAPER_50}]">
                    <h3 class="text-[15px] font-semibold text-[{INK_950}]">{lang_nodes(NEXT_STEPS_H3)}</h3>
                    <div class="flex flex-col gap-3.5">{steps_html}
                    </div>
                </div>
                <div class="flex flex-col gap-1">
                    <span class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_400}]">{lang_nodes(DIRECT_CONTACT)}</span>
                    <a href="mailto:info@chela-industrial.de" class="text-[15px] font-semibold text-[{INK_900}]">info@chela-industrial.de</a>
                </div>
            </div>

        </div>
    </section>
'''
    return page_html('partner-form', PF_TITLE, PF_DESC, '/partnership/partner', body, keywords=PF_KEYWORDS)
