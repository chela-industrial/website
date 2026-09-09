# -*- coding: utf-8 -*-
from common import L, lang_nodes, page_html, INK_950, INK_900, PAPER_50, SLATE_700, SLATE_600, SLATE_300, LINE

TITLE = L(
    'Über uns | CHELA Industrial',
    'About Us | CHELA Industrial',
    'Hakkımızda | CHELA Industrial',
)
DESCRIPTION = L(
    'CHELA Industrial: Handel &amp; Projektvermittlung für die Industrie — mit exklusiver EU-Vertretung von PERA Mühendislik.',
    'CHELA Industrial: trade &amp; project mediation for industry — with exclusive EU representation of PERA Mühendislik.',
    'CHELA Industrial: endüstri için ticaret ve proje arabuluculuğu — PERA Mühendislik\'in münhasır AB temsilciliğiyle.',
)
KEYWORDS = L(
    'Über CHELA Industrial, internationaler Industriehandel, schlanke Unternehmensstruktur',
    'about CHELA Industrial, international industrial trade, lean company structure',
    'CHELA Industrial hakkında, uluslararası endüstriyel ticaret, sade şirket yapısı',
)

EYEBROW = L('Über uns', 'About us', 'Hakkımızda')
H1 = L('Global Industrial Bridges', 'Global Industrial Bridges', 'Küresel Endüstriyel Köprüler')
HERO_SUB = L(
    'Der direkte Draht zwischen internationalen Industrieprojekten und den richtigen Partnern.',
    'The direct line between international industrial projects and the right partners.',
    'Uluslararası endüstriyel projeler ile doğru ortaklar arasındaki doğrudan hat.',
)

WHO_EYEBROW = L('Wer wir sind', 'Who we are', 'Biz kimiz')
WHO_P = L(
    'Bei <strong style="color:%s;">CHELA Industrial</strong> verfolgen wir einen klaren Auftrag: internationale Industrieprojekte mit den richtigen Herstellern, Ingenieuren und Technologiepartnern zusammenzubringen — schnell, direkt und ohne unnötige Zwischenstationen. Im Zentrum unseres Angebots steht die exklusive Vertretung von PERA Mühendislik, einem türkischen Spezialisten für Aufzugstechnik, für den gesamten EU-Raum. Darüber hinaus vermitteln wir Handelsbeziehungen und Projekte branchenübergreifend, mit Schwerpunkt auf Deutschland, der EU, dem Balkan und der Türkei.' % INK_950,
    'At <strong style="color:%s;">CHELA Industrial</strong>, we pursue a clear mandate: bringing international industrial projects together with the right manufacturers, engineers and technology partners — quickly, directly, and without unnecessary detours. At the center of what we do is our exclusive representation of PERA Mühendislik, a Turkish specialist in elevator technology, across the entire EU. Beyond that, we mediate trade relationships and projects across industries, with a focus on Germany, the EU, the Balkans and Turkey.' % INK_950,
    '<strong style="color:%s;">CHELA Industrial</strong> olarak net bir misyon izliyoruz: uluslararası endüstriyel projeleri doğru üretici, mühendis ve teknoloji ortaklarıyla hızlı, doğrudan ve gereksiz ara adımlar olmadan bir araya getirmek. Sunduğumuz hizmetlerin merkezinde, asansör teknolojisi alanında Türk uzman firma PERA Mühendislik\'in tüm AB genelindeki münhasır temsilciliği yer alır. Bunun ötesinde, Almanya, AB, Balkanlar ve Türkiye odaklı olarak sektörler arası ticaret ilişkileri ve projeler için de arabuluculuk yapıyoruz.' % INK_950,
)
KERNAUFTRAG_LABEL = L('Unser Kernauftrag', 'Our core mission', 'Temel misyonumuz')
KERNAUFTRAG_P = L(
    'Wir bauen Brücken, um Geschäftsbeziehungen im industriellen Sektor international zu festigen.',
    'We build bridges to strengthen business relationships in the industrial sector internationally.',
    'Endüstriyel sektördeki iş ilişkilerini uluslararası düzeyde güçlendirmek için köprüler kuruyoruz.',
)

WHY_EYEBROW = L('Warum CHELA', 'Why CHELA', 'Neden CHELA')
WHY_H2 = L('Was uns unterscheidet', 'What sets us apart', 'Bizi farklı kılan ne')
WHY_CARDS = [
    (
        L('Direkter Zugang', 'Direct access', 'Doğrudan erişim'),
        L(
            'Kurze Entscheidungswege statt mehrstufiger Prozesse — Sie sprechen direkt mit uns, nicht mit einer Warteschlange.',
            'Short decision paths instead of multi-layered processes — you speak directly with us, not a queue.',
            'Çok katmanlı süreçler yerine kısa karar yolları — bir sırayla değil, doğrudan bizimle konuşursunuz.',
        ),
    ),
    (
        L('Brücke zwischen den Märkten', 'A bridge between markets', 'Pazarlar arasında köprü'),
        L(
            'Fließend in den jeweiligen lokalen Sprachen — wir verstehen beide Seiten eines Geschäfts, kulturell wie sprachlich.',
            'Fluent in the relevant local languages — we understand both sides of a deal, culturally as well as linguistically.',
            'İlgili yerel dillerde akıcı — bir anlaşmanın her iki tarafını da kültürel ve dilsel olarak anlıyoruz.',
        ),
    ),
    (
        L('Spezialisierte Technikpartnerschaft', 'A specialized technology partnership', 'Uzmanlaşmış teknoloji ortaklığı'),
        L(
            'Als einziger offizieller EU-Vertreter von PERA Mühendislik bringen wir echtes technisches Fachwissen in der Aufzugstechnik mit — kein austauschbarer Zwischenhändler.',
            'As the sole official EU representative of PERA Mühendislik, we bring genuine technical expertise in elevator technology — not an interchangeable middleman.',
            'PERA Mühendislik\'in tek resmi AB temsilcisi olarak, asansör teknolojisinde gerçek teknik uzmanlık sunuyoruz — sıradan bir aracı değil.',
        ),
    ),
]

WORKING_EYEBROW = L('Arbeitsweise', 'How we work', 'Çalışma şeklimiz')
WORKING_H2 = L('Schlank, direkt, persönlich', 'Lean, direct, personal', 'Sade, doğrudan, kişisel')
WORKING_P1 = L(
    'CHELA Industrial arbeitet bewusst schlank: keine mehrstufige Hierarchie, keine unnötige Bürokratie. Entscheidungen laufen direkt und ohne Umwege über mehrere Ebenen. Das hält uns schnell, reaktionsschnell und nah an jedem Projekt.',
    'CHELA Industrial operates deliberately lean: no multi-layered hierarchy, no unnecessary bureaucracy. Decisions run directly, without detours through multiple levels. That keeps us fast, responsive and close to every project.',
    'CHELA Industrial bilinçli olarak sade çalışır: çok katmanlı bir hiyerarşi ve gereksiz bürokrasi yoktur. Kararlar doğrudan alınır, birden fazla kademeden geçmeden. Bu da bizi hızlı, tepkisel ve her projeye yakın tutar.',
)
WORKING_P2 = L(
    'Der eingetragene Geschäftssitz von CHELA Industrial UG (haftungsbeschränkt) befindet sich in Dahn, eingetragen beim Amtsgericht Zweibrücken (HRB 33566). Operativ sind wir im Raum Bremen und Norddeutschland verankert.',
    'The registered seat of CHELA Industrial UG (haftungsbeschränkt) is in Dahn, entered at the Zweibrücken local court (HRB 33566). Operationally, we are based in the Bremen / Northern Germany region.',
    'CHELA Industrial UG\'nin (haftungsbeschränkt) tescilli merkezi Dahn\'dadır, Zweibrücken Sulh Hukuk Mahkemesi\'nde kayıtlıdır (HRB 33566). Operasyonel olarak Bremen ve Kuzey Almanya bölgesinde konumlanıyoruz.',
)
WORKING_P3 = L(
    'Die Zusammenarbeit mit PERA Mühendislik ist dabei projektbezogen: Sobald ein Vorhaben Aufzugstechnik betrifft, übernimmt CHELA Industrial als benannter europäischer Vertreter die technische und kaufmännische Koordination mit PERA — für alle anderen Anfragen sind wir Ihr direkter Ansprechpartner für Handel und Projektvermittlung.',
    'Our work with PERA Mühendislik is project-based: whenever a project involves elevator technology, CHELA Industrial coordinates directly with PERA as their named European representative — for every other inquiry, we\'re your direct contact for trade and project mediation.',
    'PERA Mühendislik ile çalışmamız proje bazlıdır: bir proje asansör teknolojisini içerdiğinde, CHELA Industrial belirlenen Avrupa temsilcisi olarak PERA ile doğrudan koordinasyonu üstlenir — diğer tüm talepler için ticaret ve proje arabuluculuğu konusunda doğrudan irtibat noktasıyız.',
)

CTA_H2 = L('Lernen wir uns kennen.', 'Let\'s get to know each other.', 'Tanışalım.')
CTA_SUB = L(
    'Erzählen Sie uns von Ihrem Projekt — wir melden uns direkt bei Ihnen.',
    'Tell us about your project — we\'ll get back to you directly.',
    'Projenizden bize bahsedin — doğrudan sizinle iletişime geçelim.',
)
CTA_BTN = L('Kontakt aufnehmen', 'Get in touch', 'İletişime geçin')


def render():
    why_html = ''
    for title, desc in WHY_CARDS:
        why_html += f'''
        <div class="bg-white border border-[{LINE}] rounded-xl p-7 flex flex-col gap-2.5">
            <h3 class="text-[15.5px] font-semibold text-[{INK_950}]">{lang_nodes(title, tag="span", display="block")}</h3>
            <p class="text-[13.5px] leading-relaxed text-[{SLATE_600}]">{lang_nodes(desc, tag="span", display="block")}</p>
        </div>'''

    body = f'''
    <header class="bg-[{INK_950}] text-white py-20 px-6"
      style="background-image:linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size:46px 46px;">
        <div class="max-w-4xl mx-auto flex flex-col gap-4">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(EYEBROW)}</span>
            <h1 class="font-display break-words text-4xl md:text-5xl font-bold">{lang_nodes(H1)}</h1>
            <p class="text-lg text-[{SLATE_300}]">{lang_nodes(HERO_SUB, tag="span", display="block")}</p>
        </div>
    </header>

    <section class="bg-white py-20 px-6">
        <div class="max-w-4xl mx-auto flex flex-col gap-8">
            <span class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_600}]">{lang_nodes(WHO_EYEBROW)}</span>
            <p class="text-[17px] leading-relaxed text-[{SLATE_700}] max-w-3xl -mt-4">{lang_nodes(WHO_P, tag="span", display="block")}</p>
            <div class="max-w-3xl bg-[{PAPER_50}] border-l-4 border-[{INK_900}] rounded-r-lg py-6 px-8 flex flex-col gap-2">
                <span class="text-sm font-bold text-[{INK_950}]">{lang_nodes(KERNAUFTRAG_LABEL)}</span>
                <p class="text-[15.5px] leading-relaxed text-[{SLATE_700}]">{lang_nodes(KERNAUFTRAG_P, tag="span", display="block")}</p>
            </div>
        </div>
    </section>

    <section class="bg-[{PAPER_50}] py-20 px-6">
        <div class="max-w-5xl mx-auto flex flex-col gap-9">
            <div class="max-w-xl flex flex-col gap-2">
                <span class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_600}]">{lang_nodes(WHY_EYEBROW)}</span>
                <h2 class="font-display break-words text-2xl font-semibold text-[{INK_950}]">{lang_nodes(WHY_H2)}</h2>
            </div>
            <div class="grid md:grid-cols-3 gap-6">{why_html}
            </div>
        </div>
    </section>

    <section class="bg-[{INK_900}] py-20 px-6">
        <div class="max-w-3xl mx-auto flex flex-col gap-4">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(WORKING_EYEBROW)}</span>
            <h2 class="font-display break-words text-2xl font-semibold text-white">{lang_nodes(WORKING_H2)}</h2>
            <p class="text-[15.5px] leading-relaxed text-[{SLATE_300}]">{lang_nodes(WORKING_P1, tag="span", display="block")}</p>
            <p class="text-[15.5px] leading-relaxed text-[{SLATE_300}]">{lang_nodes(WORKING_P2, tag="span", display="block")}</p>
            <p class="text-[15.5px] leading-relaxed text-[{SLATE_300}]">{lang_nodes(WORKING_P3, tag="span", display="block")}</p>
        </div>
    </section>

    <section class="bg-white py-[76px] px-6 text-center">
        <div class="max-w-xl mx-auto flex flex-col items-center gap-4 py-1">
            <h2 class="font-display break-words text-3xl font-semibold text-[{INK_950}]">{lang_nodes(CTA_H2, tag="span", display="block")}</h2>
            <p class="text-[15.5px] text-[{SLATE_600}]">{lang_nodes(CTA_SUB, tag="span", display="block")}</p>
            <a href="/contact" class="mt-1 px-8 py-3.5 rounded-md bg-[{INK_900}] text-white font-bold text-sm hover:bg-[{INK_950}] transition-colors">{lang_nodes(CTA_BTN)}</a>
        </div>
    </section>
'''
    return page_html('about', TITLE, DESCRIPTION, '/about', body, keywords=KEYWORDS)
