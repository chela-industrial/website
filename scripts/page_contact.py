# -*- coding: utf-8 -*-
from common import L, lang_nodes, page_html, FORMSPREE_ENDPOINT, INK_950, INK_900, PAPER_50, SLATE_700, SLATE_600, SLATE_400, SLATE_300, LINE

TITLE = L('Kontakt | CHELA Industrial', 'Contact | CHELA Industrial', 'İletişim | CHELA Industrial')
DESCRIPTION = L(
    'Sprechen Sie mit CHELA Industrial über Ihr Anliegen — internationaler Handel, Aufzugstechnik oder Projektvermittlung.',
    'Talk to CHELA Industrial about your project — international trade, elevator technology or project mediation.',
    'Projeniz hakkında CHELA Industrial ile konuşun — uluslararası ticaret, asansör teknolojisi veya proje arabuluculuğu.',
)
KEYWORDS = L(
    'Kontakt CHELA Industrial, Anfrage stellen, Ansprechpartner Industriehandel',
    'contact CHELA Industrial, submit an inquiry, industrial trade contact',
    'CHELA Industrial iletişim, talep gönder, endüstriyel ticaret irtibat kişisi',
)

EYEBROW = L('Kontakt', 'Contact', 'İletişim')
H1 = L('Sprechen Sie mit uns über Ihr Anliegen.', 'Talk to us about your project.', 'Projeniz hakkında bizimle konuşun.')

F_NAME = L('Name', 'Name', 'Ad Soyad')
F_NAME_PH = L('Ihr vollständiger Name', 'Your full name', 'Tam adınız')
F_COMPANY = L('Firma', 'Company', 'Şirket')
F_COMPANY_PH = L('Unternehmen', 'Company', 'Şirket')
F_EMAIL = L('E-Mail', 'Email', 'E-posta')
F_EMAIL_PH = L('name@unternehmen.de', 'name@company.com', 'ad@sirket.com')
F_MESSAGE = L('Nachricht', 'Message', 'Mesaj')
F_MESSAGE_PH = L(
    'Beschreiben Sie kurz Ihr Anliegen — Handel, Aufzugstechnik oder Projektvermittlung.',
    'Briefly describe your request — trade, elevator technology or project mediation.',
    'Talebinizi kısaca açıklayın — ticaret, asansör teknolojisi veya proje arabuluculuğu.',
)
F_SUBMIT = L('Nachricht senden', 'Send message', 'Mesajı gönder')
SUBMIT_NOTE_OK = L(
    'Danke — Ihre Nachricht ist bei uns eingegangen. Wir melden uns so schnell wie möglich bei Ihnen.',
    'Thank you — your message has been received. We\'ll get back to you as soon as possible.',
    'Teşekkürler — mesajınız bize ulaştı. En kısa sürede size geri döneceğiz.',
)
SUBMIT_NOTE_ERROR = L(
    'Da ist leider etwas schiefgelaufen. Bitte schreiben Sie uns direkt an info@chela-industrial.de.',
    'Something went wrong on our end. Please email us directly at info@chela-industrial.de.',
    'Maalesef bir sorun oluştu. Lütfen doğrudan info@chela-industrial.de adresine yazın.',
)

INFO_EMAIL_LABEL = L('E-Mail', 'Email', 'E-posta')
INFO_ADDRESS_LABEL = L('Adresse', 'Address', 'Adres')
INFO_MD_LABEL = L('Geschäftsführer', 'Managing Director', 'Genel Müdür')
MAP_CAPTION = L('66994 Dahn, Deutschland', '66994 Dahn, Germany', '66994 Dahn, Almanya')


def render():
    body = f'''
    <header class="bg-[{INK_950}] text-white py-16 px-6 pb-14"
      style="background-image:linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size:46px 46px;">
        <div class="max-w-2xl mx-auto flex flex-col gap-3.5">
            <span class="text-xs font-semibold tracking-widest uppercase text-[#9aa1a8]">{lang_nodes(EYEBROW)}</span>
            <h1 class="font-display break-words text-3xl font-bold leading-tight">{lang_nodes(H1, tag="span", display="block")}</h1>
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
                <label class="flex flex-col gap-2">
                    <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(F_EMAIL)} <span style="color:{INK_900};">*</span></span>
                    <input type="email" name="email" required placeholder="{F_EMAIL_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]">
                </label>
                <label class="flex flex-col gap-2">
                    <span class="text-[13px] font-semibold text-[{INK_900}]">{lang_nodes(F_MESSAGE)}</span>
                    <textarea name="message" rows="4" placeholder="{F_MESSAGE_PH['de']}" class="border border-[{LINE}] rounded-md px-3.5 py-3 text-[14.5px] text-[{INK_900}]"></textarea>
                </label>
                <button type="submit" class="self-start mt-1 px-8 py-3.5 rounded-md bg-[{INK_900}] text-white font-semibold text-sm hover:bg-[#3a4a5c] transition-colors">{lang_nodes(F_SUBMIT)}</button>
                <p class="submit-note-ok text-[13px] text-[{SLATE_600}] leading-relaxed" hidden>{lang_nodes(SUBMIT_NOTE_OK, tag="span", display="block")}</p>
                <p class="submit-note-error text-[13px] leading-relaxed" style="color:#b3261e;" hidden>{lang_nodes(SUBMIT_NOTE_ERROR, tag="span", display="block")}</p>
            </form>

            <div class="flex flex-col gap-6">
                <div class="flex flex-col gap-4 p-7 border border-[{LINE}] rounded-xl">
                    <div class="flex flex-col gap-1">
                        <span class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_400}]">{lang_nodes(INFO_EMAIL_LABEL)}</span>
                        <a href="mailto:info@chela-industrial.de" class="text-[15px] font-semibold text-[{INK_900}]">info@chela-industrial.de</a>
                    </div>
                    <div class="flex flex-col gap-1">
                        <span class="text-xs font-semibold tracking-widest uppercase text-[{SLATE_400}]">{lang_nodes(INFO_ADDRESS_LABEL)}</span>
                        <span class="text-[14.5px] text-[{INK_900}] leading-relaxed">Erfweiler Straße 12<br>66994 Dahn, Deutschland</span>
                    </div>
                </div>
                <div class="h-[180px] rounded-xl border border-[{LINE}] bg-[{PAPER_50}] flex flex-col items-center justify-center gap-2"
                  style="background-image:linear-gradient(rgba(14,18,48,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(14,18,48,0.06) 1px, transparent 1px); background-size:24px 24px;">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="{SLATE_600}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"></path><circle cx="12" cy="10" r="2.4"></circle>
                    </svg>
                    <span class="text-[12.5px] font-medium text-[{SLATE_600}]">{lang_nodes(MAP_CAPTION)}</span>
                </div>
            </div>

        </div>
    </section>
'''
    return page_html('contact', TITLE, DESCRIPTION, '/contact', body, keywords=KEYWORDS)
