# -*- coding: utf-8 -*-
from common import L, lang_nodes, page_html, FORMSPREE_ENDPOINT, INK_950, INK_900, PAPER_50, SLATE_700, SLATE_600, SLATE_400, SLATE_300, LINE

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
PERA_TITLE = L(
    'Partnerschaft — PERA Mühendislik | CHELA Industrial',
    'Partnership — PERA Mühendislik | CHELA Industrial',
    'Ortaklık — PERA Mühendislik | CHELA Industrial',
)
PERA_DESC = L(
    'CHELA Industrial ist der einzige offizielle EU-Partner von PERA Mühendislik für Aufzugstechnik, unter einer unterzeichneten Kooperationsvereinbarung.',
    'CHELA Industrial is the only official EU partner of PERA Mühendislik for elevator technology, under a signed cooperation agreement.',
    'CHELA Industrial, asansör teknolojisi için PERA Mühendislik\'in imzalı bir iş birliği anlaşması kapsamındaki tek resmi AB ortağıdır.',
)
# Full DE/EN/TR elevator-vocabulary coverage, matching PERA Mühendislik's own
# product range (https://peramuhendislik.com/) — passenger, freight, panoramic,
# hydraulic, vehicle and helicopter-landing-pad elevators, plus modernization
# and maintenance — so this page surfaces for the same searches PERA does,
# in all three languages.
PERA_KEYWORDS = L(
    'PERA Mühendislik Deutschland, Personenaufzüge, Lastenaufzüge, Panoramaaufzüge, Hydraulikaufzüge, '
    'Fahrzeugaufzüge, Hubschrauberlandeplatz-Aufzüge, Monşarj-Systeme, Aufzugsmodernisierung, Aufzugswartung, '
    'Aufzugsplanung und -konstruktion, Aufzugsherstellung und -montage, Aufzugslösungen nach Maß, '
    'europäischer Vertreter PERA, seit 1992',
    'PERA Mühendislik Europe, passenger elevators, freight elevators, load elevators, panoramic elevators, '
    'hydraulic elevators, vehicle elevators, helicopter landing pad elevators, moncharge systems, '
    'elevator modernization, elevator maintenance, elevator design and engineering, elevator manufacturing '
    'and installation, custom-design elevator solutions, PERA European representative, since 1992',
    'PERA Mühendislik Avrupa temsilcisi, yolcu asansörleri, yük asansörleri, panoramik asansörler, '
    'hidrolik asansörler, araç asansörleri, helikopter pist asansörleri, monşarj sistemleri, asansör modernizasyonu, '
    'asansör bakımı, asansör tasarım ve mühendislik, asansör üretim ve montaj, özel tasarım asansör çözümleri, '
    '1992\'den beri asansör',
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
QUOTE_LABEL = L('Technische Anfrage', 'Technical Inquiry', 'Teknik Talep')
QUOTE_TITLE = L('Aufzugs-Anfrage stellen', 'Request an Elevator Quote', 'Asansör Teklifi İsteyin')
QUOTE_DESC = L(
    'Geben Sie Ihre Eckdaten ein — wir erstellen Ihnen ein unverbindliches Angebot.',
    'Enter your key details — we\'ll prepare a non-binding quote for you.',
    'Temel bilgilerinizi girin — size bağlayıcı olmayan bir teklif hazırlayalım.',
)
QUOTE_BTN = L('Anfrage stellen', 'Request a quote', 'Teklif isteyin')

QUOTE_MODAL_TITLE = L('Aufzugs-Anfrage', 'Elevator Inquiry', 'Asansör Talebi')
QUOTE_MODAL_SUB = L(
    'Technisches Anfrageformular für PERA-Hydraulikaufzüge',
    'Technical inquiry form for PERA hydraulic elevators',
    'PERA hidrolik asansörleri için teknik talep formu',
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

    <section class="bg-white py-[76px] px-6">
        <div class="max-w-5xl mx-auto grid md:grid-cols-[1.2fr_0.8fr] gap-10 items-center">
            <p class="text-[16.5px] leading-relaxed text-[{SLATE_700}] max-w-xl">{lang_nodes(PERA_BODY_P, tag="span", display="block")}</p>
            <div class="flex justify-center">
                <svg viewBox="0 0 260 180" width="240" height="166" fill="none" stroke="{INK_900}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="40" cy="90" r="9"></circle><circle cx="220" cy="90" r="9"></circle><circle cx="130" cy="40" r="9" fill="{INK_900}"></circle>
                    <path d="M48 90 L212 90" stroke-dasharray="2 7"></path>
                    <path d="M46 85 L126 44"></path>
                    <path d="M214 85 L134 44"></path>
                    <text x="24" y="118" fill="{INK_900}" stroke="none" font-family="IBM Plex Sans" font-size="12" font-weight="600">Europa</text>
                    <text x="188" y="118" fill="{INK_900}" stroke="none" font-family="IBM Plex Sans" font-size="12" font-weight="600">Türkei</text>
                    <text x="130" y="24" text-anchor="middle" fill="{INK_900}" stroke="none" font-family="IBM Plex Sans" font-size="12" font-weight="700">CHELA</text>
                </svg>
            </div>
        </div>
    </section>

    <section class="bg-[{PAPER_50}] py-[76px] px-6">
        <div class="max-w-5xl mx-auto">
            <div class="max-w-xl flex flex-col gap-2 mb-9">
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

            <div class="mt-7 relative overflow-hidden rounded-xl flex flex-col sm:flex-row sm:items-center gap-5 sm:gap-6 p-6 sm:p-7"
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

    <section class="bg-white py-[76px] px-6">
        <div class="max-w-5xl mx-auto">
            <h2 class="font-display break-words text-2xl font-semibold text-[{INK_950}] mb-9">{lang_nodes(WHAT_IT_MEANS_H2)}</h2>
            <div class="grid md:grid-cols-3 gap-7">{means_html}
            </div>
        </div>
    </section>

    <section class="bg-[{INK_900}] py-[76px] px-6 text-center">
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
                    <div class="grid sm:grid-cols-2 gap-[14px]">
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

        function openQuoteForm() {{
            var modal = document.getElementById('quote-modal');
            modal.style.display = 'flex';
            document.body.classList.add('overflow-hidden');
            document.addEventListener('keydown', quoteKeyHandler);
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
    return page_html('pera', PERA_TITLE, PERA_DESC, '/partnership/pera', body, keywords=PERA_KEYWORDS)


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
