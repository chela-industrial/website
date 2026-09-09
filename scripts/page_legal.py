# -*- coding: utf-8 -*-
from common import L, lang_nodes, page_html, INK_950, INK_900, PAPER_50, SLATE_700, SLATE_600, SLATE_400, LINE

AUTHORITATIVE_NOTICE = L(
    '',
    'This page is a courtesy translation. The German version is legally authoritative.',
    'Bu sayfa bir nezaket çevirisidir. Almanca sürüm yasal olarak bağlayıcıdır.',
)

DRAFT_NOTICE = L(
    'Dieser Text ist ein allgemeiner Muster-Entwurf und ersetzt keine individuelle Rechtsberatung. Bitte vor Veröffentlichung von einem Rechtsanwalt oder Steuerberater prüfen lassen.',
    'This text is a general template and does not replace individual legal advice. Please have it reviewed by a lawyer or tax advisor before relying on it.',
    'Bu metin genel bir şablon taslağıdır ve bireysel hukuki danışmanlığın yerini tutmaz. Lütfen kullanmadan önce bir avukat veya mali müşavire kontrol ettirin.',
)


def _p(content_L):
    """Render a trilingual paragraph, pre-computed (no f-string backslash issues)."""
    return '<p class="m-0">' + lang_nodes(content_L, tag='span', display='block') + '</p>'


def _section(heading, body_html):
    heading_html = lang_nodes(heading)
    return (
        '\n      <div class="flex flex-col gap-2.5">'
        f'\n        <h2 class="font-display break-words text-lg font-semibold text-[{INK_950}]">{heading_html}</h2>'
        f'\n        <div class="text-[14.5px] leading-relaxed text-[{SLATE_700}]">{body_html}</div>'
        '\n      </div>'
    )


def _legal_page(active_nav, title, description, canonical, eyebrow, h1, sections):
    sections_html = ''.join(sections)
    eyebrow_html = lang_nodes(eyebrow)
    h1_html = lang_nodes(h1)
    notice_html = lang_nodes(AUTHORITATIVE_NOTICE, tag='span', display='block')
    draft_notice_html = lang_nodes(DRAFT_NOTICE, tag='span', display='block')
    body = f'''
    <header class="bg-[{INK_950}] text-white py-16 px-6 pb-12"
      style="background-image:linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size:46px 46px;">
        <div class="max-w-2xl mx-auto flex flex-col gap-3">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{eyebrow_html}</span>
            <h1 class="font-display break-words text-3xl font-bold leading-tight">{h1_html}</h1>
        </div>
    </header>

    <section class="bg-white py-16 px-6 pb-24">
        <div class="max-w-2xl mx-auto flex flex-col gap-9">
            <p class="text-[13px] text-[{SLATE_400}] italic">{notice_html}</p>
            {sections_html}
            <div class="p-5 bg-[{PAPER_50}] border border-[{LINE}] rounded-lg">
                <p class="text-[13px] text-[{SLATE_600}] m-0">{draft_notice_html}</p>
            </div>
        </div>
    </section>
'''
    return page_html(active_nav, title, description, canonical, body)


def _list(items_L):
    """items_L: list of L() dicts -> a <ul><li>...</li></ul> block."""
    lis = ''.join(f'<li>{lang_nodes(item)}</li>' for item in items_L)
    return f'<ul class="list-disc pl-5 flex flex-col gap-1 m-0">{lis}</ul>'


# ---------------------------------------------------------------- IMPRESSUM -
IMP_TITLE = L('Impressum | CHELA Industrial', 'Legal Notice | CHELA Industrial', 'Yasal Bilgiler | CHELA Industrial')
IMP_DESC = L(
    'Impressum von CHELA Industrial UG gemäß § 5 TMG.',
    'Legal notice of CHELA Industrial UG pursuant to Section 5 of the German Telemedia Act (TMG).',
    'CHELA Industrial UG kimlik bilgileri, Alman Telemedya Kanunu (TMG) Madde 5 uyarınca.',
)
IMP_EYEBROW = L('Rechtliches', 'Legal', 'Hukuki')
IMP_H1 = L('Impressum', 'Legal Notice', 'Yasal Bilgiler')

IMP_S1_HEAD = L('Angaben gemäß § 5 TMG', 'Information pursuant to Section 5 TMG', 'TMG Madde 5 uyarınca bilgiler')
IMP_S2_HEAD = L('Vertreten durch', 'Represented by', 'Temsilci')
IMP_S2_BODY = L('Geschäftsführer: Durukan Kürüm', 'Managing Director: Durukan Kürüm', 'Genel Müdür: Durukan Kürüm')
IMP_S3_HEAD = L('Kontakt', 'Contact', 'İletişim')
IMP_S4_HEAD = L('Registereintrag', 'Register Entry', 'Sicil Kaydı')
IMP_S4_L1 = L('Eintragung im Handelsregister.', 'Entered in the Commercial Register.', 'Ticaret Siciline kayıtlıdır.')
IMP_S4_L2 = L('Registergericht: Amtsgericht Zweibrücken', 'Register court: Amtsgericht Zweibrücken (local court)', 'Sicil mahkemesi: Amtsgericht Zweibrücken')
IMP_S4_L3 = L('Registernummer: HRB 33566', 'Register number: HRB 33566', 'Sicil numarası: HRB 33566')
IMP_S5_HEAD = L('Umsatzsteuer-Identifikationsnummer', 'VAT Identification Number', 'KDV Kimlik Numarası')
IMP_S5_BODY = L(
    'Umsatzsteuer-Identifikationsnummer gemäß §27a Umsatzsteuergesetz: wird auf Anfrage mitgeteilt.',
    'VAT identification number pursuant to Section 27a of the German VAT Act: provided upon request.',
    'Alman KDV Kanunu Madde 27a uyarınca KDV kimlik numarası: talep üzerine bildirilir.',
)
IMP_S6_HEAD = L('Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV', 'Responsible for Content pursuant to Section 18(2) MStV', 'MStV Madde 18(2) uyarınca içerikten sorumlu')
IMP_S6_L2 = L('Anschrift wie oben', 'Address as above', 'Adres yukarıdaki gibidir')
IMP_S7_HEAD = L('EU-Streitschlichtung', 'EU Dispute Resolution', 'AB Uyuşmazlık Çözümü')
IMP_S7_L1 = L(
    'Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit:',
    'The European Commission provides a platform for online dispute resolution (ODR):',
    'Avrupa Komisyonu, çevrimiçi uyuşmazlık çözümü (ODR) için bir platform sunmaktadır:',
)
IMP_S7_L2 = L(
    'Unsere E-Mail-Adresse finden Sie oben im Impressum. Wir sind nicht verpflichtet und nicht bereit, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.',
    'Our email address can be found above in this legal notice. We are not obliged, nor willing, to participate in dispute resolution proceedings before a consumer arbitration board.',
    'E-posta adresimizi yukarıdaki yasal bilgiler bölümünde bulabilirsiniz. Bir tüketici hakem heyeti önünde uyuşmazlık çözümü süreçlerine katılma yükümlülüğümüz veya isteğimiz bulunmamaktadır.',
)
IMP_S8_HEAD = L('Haftung für Inhalte', 'Liability for Content', 'İçerik Sorumluluğu')
IMP_S8_BODY = L(
    'Als Diensteanbieter sind wir gemäß § 7 Abs. 1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.',
    'As a service provider, we are responsible for our own content on these pages under general law in accordance with Section 7(1) TMG. However, pursuant to Sections 8 to 10 TMG, we as a service provider are not obliged to monitor transmitted or stored third-party information or to investigate circumstances indicating unlawful activity.',
    'Bir hizmet sağlayıcı olarak, TMG Madde 7(1) uyarınca bu sayfalardaki kendi içeriğimizden genel hukuk çerçevesinde sorumluyuz. Ancak TMG Madde 8 ila 10 uyarınca, iletilen veya depolanan üçüncü taraf bilgilerini izlemek veya hukuka aykırı bir faaliyete işaret eden koşulları araştırmakla yükümlü değiliz.',
)
IMP_S9_HEAD = L('Haftung für Links', 'Liability for Links', 'Bağlantı Sorumluluğu')
IMP_S9_BODY = L(
    'Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich.',
    'Our website contains links to external third-party websites over whose content we have no influence. We therefore cannot assume any liability for this third-party content. The respective provider or operator of the linked pages is always responsible for their content.',
    'Web sitemiz, içeriği üzerinde herhangi bir etkimiz olmayan harici üçüncü taraf web sitelerine bağlantılar içermektedir. Bu nedenle bu üçüncü taraf içerikler için herhangi bir sorumluluk üstlenemeyiz. Bağlantılı sayfaların içeriği her zaman ilgili sağlayıcı veya işletmeci sorumludur.',
)
IMP_S10_HEAD = L('Urheberrecht', 'Copyright', 'Telif Hakkı')
IMP_S10_BODY = L(
    'Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Beiträge Dritter sind als solche gekennzeichnet. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.',
    'The content and works created by the site operators on these pages are subject to German copyright law. Third-party contributions are marked as such. Duplication, editing, distribution and any kind of use outside the limits of copyright law require the written consent of the respective author or creator.',
    'Bu sayfalardaki site işletmecileri tarafından oluşturulan içerik ve eserler Alman telif hakkı yasasına tabidir. Üçüncü taraf katkıları bu şekilde işaretlenmiştir. Telif hakkı yasasının sınırları dışındaki çoğaltma, düzenleme, dağıtım ve her türlü kullanım, ilgili yazarın veya oluşturucunun yazılı onayını gerektirir.',
)


def render_impressum():
    email_link = f'<a href="mailto:info@chela-industrial.de" class="text-[{INK_900}] font-semibold">info@chela-industrial.de</a>'
    odr_link = f'<a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener" class="text-[{INK_900}] font-semibold">ec.europa.eu/consumers/odr</a>'

    s1_body = '<p class="m-0">CHELA Industrial UG (haftungsbeschränkt)<br>Erfweiler Straße 12<br>66994 Dahn, Deutschland</p>'
    s3_body = '<p class="m-0">' + lang_nodes(L('E-Mail', 'Email', 'E-posta')) + ': ' + email_link + '</p>'
    s4_body = (
        '<p class="m-0">' + lang_nodes(IMP_S4_L1, tag='span', display='block')
        + '<br>' + lang_nodes(IMP_S4_L2, tag='span', display='block')
        + '<br>' + lang_nodes(IMP_S4_L3, tag='span', display='block') + '</p>'
    )
    s6_body = '<p class="m-0">Durukan Kürüm<br>' + lang_nodes(IMP_S6_L2, tag='span', display='block') + '</p>'
    s7_body = (
        '<p class="m-0">' + lang_nodes(IMP_S7_L1, tag='span', display='block') + ' ' + odr_link + '. '
        + lang_nodes(IMP_S7_L2, tag='span', display='block') + '</p>'
    )

    sections = [
        _section(IMP_S1_HEAD, s1_body),
        _section(IMP_S2_HEAD, _p(IMP_S2_BODY)),
        _section(IMP_S3_HEAD, s3_body),
        _section(IMP_S4_HEAD, s4_body),
        _section(IMP_S5_HEAD, _p(IMP_S5_BODY)),
        _section(IMP_S6_HEAD, s6_body),
        _section(IMP_S7_HEAD, s7_body),
        _section(IMP_S8_HEAD, _p(IMP_S8_BODY)),
        _section(IMP_S9_HEAD, _p(IMP_S9_BODY)),
        _section(IMP_S10_HEAD, _p(IMP_S10_BODY)),
    ]
    return _legal_page('legal', IMP_TITLE, IMP_DESC, '/impressum', IMP_EYEBROW, IMP_H1, sections)


# ---------------------------------------------------------------- DATENSCHUTZ
DS_TITLE = L('Datenschutzerklärung | CHELA Industrial', 'Privacy Policy | CHELA Industrial', 'Gizlilik Politikası | CHELA Industrial')
DS_DESC = L(
    'Datenschutzerklärung von CHELA Industrial UG gemäß DSGVO.',
    'Privacy policy of CHELA Industrial UG pursuant to the GDPR.',
    'CHELA Industrial UG GDPR uyarınca gizlilik politikası.',
)
DS_EYEBROW = L('Rechtliches', 'Legal', 'Hukuki')
DS_H1 = L('Datenschutzerklärung', 'Privacy Policy', 'Gizlilik Politikası')

DS_S1_HEAD = L('1. Verantwortlicher', '1. Controller', '1. Veri Sorumlusu')
DS_S1_INTRO = L('Verantwortlich für die Datenverarbeitung auf dieser Website ist:', 'Responsible for data processing on this website is:', 'Bu web sitesindeki veri işlemeden sorumlu taraf:')
DS_S1_MD = L('Geschäftsführer: Durukan Kürüm', 'Managing Director: Durukan Kürüm', 'Genel Müdür: Durukan Kürüm')

DS_S2_HEAD = L('2. Allgemeines zur Datenverarbeitung', '2. General Information on Data Processing', '2. Veri İşleme Hakkında Genel Bilgiler')
DS_S2_BODY = L(
    'Wir verarbeiten personenbezogene Daten unserer Nutzer grundsätzlich nur, soweit dies zur Bereitstellung einer funktionsfähigen Website sowie unserer Inhalte und Leistungen erforderlich ist, oder soweit Nutzer in eine weitergehende Verarbeitung eingewilligt haben. Rechtsgrundlage hierfür sind Art. 6 Abs. 1 lit. a (Einwilligung), lit. b (Vertragserfüllung) und lit. f (berechtigtes Interesse) der Datenschutz-Grundverordnung (DSGVO).',
    'We generally process our users\' personal data only to the extent necessary to provide a functional website and our content and services, or to the extent users have consented to further processing. The legal basis for this is Art. 6(1)(a) (consent), (b) (contract performance) and (f) (legitimate interest) GDPR.',
    'Kullanıcılarımızın kişisel verilerini genel olarak yalnızca işlevsel bir web sitesi ile içerik ve hizmetlerimizi sunmak için gerekli olduğu ölçüde, veya kullanıcıların daha ileri işlemeye onay verdiği ölçüde işleriz. Bunun yasal dayanağı GDPR Madde 6(1)(a) (onay), (b) (sözleşmenin ifası) ve (f) (meşru menfaat) hükümleridir.',
)

DS_S3_HEAD = L('3. Bereitstellung der Website / Server-Logfiles', '3. Provision of the Website / Server Log Files', '3. Web Sitesinin Sağlanması / Sunucu Günlük Dosyaları')
DS_S3_BODY = L(
    'Beim Aufruf dieser Website erhebt der Hosting-Anbieter automatisch Informationen in sogenannten Server-Logfiles, die Ihr Browser automatisch übermittelt. Dies sind: Browsertyp und -version, verwendetes Betriebssystem, Referrer-URL, Hostname des zugreifenden Rechners, Uhrzeit der Serveranfrage und IP-Adresse. Diese Daten werden nicht mit anderen Datenquellen zusammengeführt und nach spätestens 14 Tagen gelöscht. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der technisch fehlerfreien Bereitstellung der Website).',
    'When you access this website, our hosting provider automatically collects information in server log files that your browser transmits. These are: browser type and version, operating system, referrer URL, host name of the accessing computer, time of the server request, and IP address. This data is not merged with other data sources and is deleted after 14 days at the latest. The legal basis is Art. 6(1)(f) GDPR (legitimate interest in the technically error-free provision of the website).',
    'Bu web sitesine eriştiğinizde, barındırma sağlayıcımız tarayıcınızın ilettiği bilgileri sunucu günlük dosyalarında otomatik olarak toplar. Bunlar: tarayıcı türü ve sürümü, işletim sistemi, yönlendiren URL, erişen bilgisayarın ana bilgisayar adı, sunucu talebinin saati ve IP adresidir. Bu veriler başka veri kaynaklarıyla birleştirilmez ve en geç 14 gün sonra silinir. Yasal dayanak GDPR Madde 6(1)(f)\'dir (web sitesinin teknik olarak hatasız sağlanmasında meşru menfaat).',
)

DS_S4_HEAD = L('4. Kontaktaufnahme', '4. Contacting Us', '4. Bizimle İletişime Geçme')
DS_S4_BODY = L(
    'Wenn Sie uns per Kontaktformular oder E-Mail Anfragen zukommen lassen, werden Ihre Angaben aus dem Anfrageformular inklusive der von Ihnen dort angegebenen Kontaktdaten zwecks Bearbeitung der Anfrage und für den Fall von Anschlussfragen bei uns gespeichert. Diese Daten geben wir nicht ohne Ihre Einwilligung weiter. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, soweit die Anfrage der Anbahnung eines Vertrags dient, andernfalls Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der Beantwortung von Anfragen).',
    'If you send us inquiries via the contact form or email, your details from the inquiry, including the contact data you provide, are stored by us to process the inquiry and for any follow-up questions. We do not share this data without your consent. The legal basis is Art. 6(1)(b) GDPR where the inquiry serves to initiate a contract, otherwise Art. 6(1)(f) GDPR (legitimate interest in responding to inquiries).',
    'Bize iletişim formu veya e-posta yoluyla talep gönderdiğinizde, talebinizdeki bilgileriniz, verdiğiniz iletişim verileri de dahil olmak üzere, talebin işlenmesi ve olası takip soruları için tarafımızca saklanır. Bu verileri onayınız olmadan paylaşmayız. Yasal dayanak, talebin bir sözleşmenin başlatılmasına hizmet ettiği ölçüde GDPR Madde 6(1)(b), aksi takdirde GDPR Madde 6(1)(f)\'dir (taleplere yanıt vermede meşru menfaat).',
)

DS_S5_HEAD = L('5. Cookies', '5. Cookies', '5. Çerezler')
DS_S5_BODY = L(
    'Diese Website verwendet, sofern eingesetzt, nur technisch notwendige Cookies, die für den Betrieb der Website erforderlich sind. Sofern zusätzliche Cookies (z. B. für Statistik oder Marketing) eingesetzt werden, geschieht dies nur nach Ihrer ausdrücklichen Einwilligung über ein Cookie-Consent-Tool.',
    'If used at all, this website only uses technically necessary cookies required for its operation. Should additional cookies (e.g. for statistics or marketing) be used, this only happens with your express consent via a cookie consent tool.',
    'Bu web sitesi, kullanılıyorsa, yalnızca web sitesinin çalışması için gerekli olan teknik olarak gerekli çerezleri kullanır. Ek çerezler (örneğin istatistik veya pazarlama için) kullanılacaksa, bu yalnızca bir çerez onay aracı üzerinden açık onayınızla gerçekleşir.',
)

DS_S6_HEAD = L('6. Ihre Rechte', '6. Your Rights', '6. Haklarınız')
DS_S6_INTRO = L('Ihnen stehen als Betroffener folgende Rechte zu:', 'As a data subject, you have the following rights:', 'Veri sahibi olarak aşağıdaki haklara sahipsiniz:')
DS_S6_RIGHTS = [
    L('Recht auf Auskunft (Art. 15 DSGVO)', 'Right to access (Art. 15 GDPR)', 'Erişim hakkı (GDPR Madde 15)'),
    L('Recht auf Berichtigung (Art. 16 DSGVO)', 'Right to rectification (Art. 16 GDPR)', 'Düzeltme hakkı (GDPR Madde 16)'),
    L('Recht auf Löschung (Art. 17 DSGVO)', 'Right to erasure (Art. 17 GDPR)', 'Silme hakkı (GDPR Madde 17)'),
    L('Recht auf Einschränkung der Verarbeitung (Art. 18 DSGVO)', 'Right to restriction of processing (Art. 18 GDPR)', 'İşlemenin kısıtlanması hakkı (GDPR Madde 18)'),
    L('Recht auf Datenübertragbarkeit (Art. 20 DSGVO)', 'Right to data portability (Art. 20 GDPR)', 'Veri taşınabilirliği hakkı (GDPR Madde 20)'),
    L('Widerspruchsrecht gegen die Verarbeitung (Art. 21 DSGVO)', 'Right to object to processing (Art. 21 GDPR)', 'İşlemeye itiraz etme hakkı (GDPR Madde 21)'),
    L('Recht auf Beschwerde bei einer Aufsichtsbehörde (Art. 77 DSGVO)', 'Right to lodge a complaint with a supervisory authority (Art. 77 GDPR)', 'Bir denetim makamına şikayette bulunma hakkı (GDPR Madde 77)'),
]

DS_S7_HEAD = L('7. Speicherdauer', '7. Storage Period', '7. Saklama Süresi')
DS_S7_BODY = L(
    'Personenbezogene Daten werden nur so lange gespeichert, wie dies für den jeweiligen Zweck erforderlich ist, oder solange gesetzliche Aufbewahrungsfristen bestehen.',
    'Personal data is only stored for as long as necessary for the respective purpose, or for as long as statutory retention periods apply.',
    'Kişisel veriler yalnızca ilgili amaç için gerekli olduğu sürece veya yasal saklama süreleri geçerli olduğu sürece saklanır.',
)


def render_datenschutz():
    email_link = f'<a href="mailto:info@chela-industrial.de" class="text-[{INK_900}] font-semibold">info@chela-industrial.de</a>'
    s1_body = (
        '<p class="m-0">' + lang_nodes(DS_S1_INTRO, tag='span', display='block')
        + '<br><br>CHELA Industrial UG (haftungsbeschränkt)<br>Erfweiler Straße 12<br>66994 Dahn, Deutschland<br>'
        + lang_nodes(DS_S1_MD, tag='span', display='block')
        + '<br>E-Mail: ' + email_link + '</p>'
    )
    s6_body = (
        '<p class="mb-2">' + lang_nodes(DS_S6_INTRO, tag='span', display='block') + '</p>'
        + _list(DS_S6_RIGHTS)
    )

    sections = [
        _section(DS_S1_HEAD, s1_body),
        _section(DS_S2_HEAD, _p(DS_S2_BODY)),
        _section(DS_S3_HEAD, _p(DS_S3_BODY)),
        _section(DS_S4_HEAD, _p(DS_S4_BODY)),
        _section(DS_S5_HEAD, _p(DS_S5_BODY)),
        _section(DS_S6_HEAD, s6_body),
        _section(DS_S7_HEAD, _p(DS_S7_BODY)),
    ]
    return _legal_page('legal', DS_TITLE, DS_DESC, '/datenschutz', DS_EYEBROW, DS_H1, sections)
