#!/usr/bin/env python3
"""Generate A5 couples notebook DOCX for Ilona & Lera."""

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# Soft romantic palette (not purple-default AI look): dusty rose + warm ink
INK = RGBColor(0x3D, 0x2C, 0x2E)
ACCENT = RGBColor(0xB5, 0x6A, 0x6F)
SOFT = RGBColor(0x8A, 0x6B, 0x6E)
RULE = RGBColor(0xE8, 0xD0, 0xD2)


def set_a5(section):
    section.page_width = Cm(14.8)
    section.page_height = Cm(21.0)
    section.left_margin = Cm(1.4)
    section.right_margin = Cm(1.4)
    section.top_margin = Cm(1.3)
    section.bottom_margin = Cm(1.3)


def set_run_font(run, size=11, bold=False, italic=False, color=INK, name="Georgia"):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color


def add_para(
    doc,
    text,
    *,
    size=11,
    bold=False,
    italic=False,
    color=INK,
    align=WD_ALIGN_PARAGRAPH.LEFT,
    space_before=0,
    space_after=6,
    name="Georgia",
):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold, italic=italic, color=color, name=name)
    return p


def add_divider(doc, char="· · ·"):
    add_para(doc, char, size=12, color=ACCENT, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=8)


def add_lines(doc, n=3):
    for _ in range(n):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.35
        run = p.add_run("_" * 42)
        set_run_font(run, size=10, color=SOFT)


def page_break(doc):
    doc.add_page_break()


def set_cell_shading(cell, hex_color):
    tc = cell._tePr if hasattr(cell, "_tePr") else cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def add_answer_block(doc, name, lines=3):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(f"{name}:")
    set_run_font(run, size=10, bold=True, color=ACCENT)
    add_lines(doc, lines)


def add_question_page(doc, number, question, lines=3, note=None):
    add_para(
        doc,
        f"Вопрос {number}",
        size=9,
        bold=True,
        color=ACCENT,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=4,
    )
    add_para(
        doc,
        question,
        size=12,
        bold=True,
        color=INK,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=2,
        space_after=6,
    )
    if note:
        add_para(
            doc,
            note,
            size=9,
            italic=True,
            color=SOFT,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=8,
        )
    add_divider(doc)
    add_answer_block(doc, "Илона", lines)
    add_para(doc, "", space_after=2)
    add_answer_block(doc, "Лера", lines)
    page_break(doc)


def cover_page(doc):
    for _ in range(3):
        add_para(doc, "", space_after=6)
    add_para(doc, "✦  ✦  ✦", size=14, color=ACCENT, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_para(
        doc,
        "Блокнот нашей пары",
        size=22,
        bold=True,
        color=INK,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=8,
        space_after=8,
    )
    add_para(
        doc,
        "Илона  &  Лера",
        size=16,
        italic=True,
        color=ACCENT,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=16,
    )
    add_divider(doc, "♡")
    add_para(
        doc,
        "Вопросы, которые сближают.\nОтветы, которые хочется хранить.",
        size=11,
        italic=True,
        color=SOFT,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=10,
        space_after=20,
    )
    add_para(
        doc,
        "Каждая отвечает отдельно.\nПотом можно читать вслух —\nкак на самом милом реалити-шоу в мире.",
        size=10,
        color=INK,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=24,
    )
    add_para(doc, "✦  ✦  ✦", size=14, color=ACCENT, align=WD_ALIGN_PARAGRAPH.CENTER)
    page_break(doc)


def how_to_use(doc):
    add_para(doc, "Как пользоваться", size=16, bold=True, color=INK, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_divider(doc, "♡")
    tips = [
        "Отвечайте честно, но бережно — к себе и к друг другу.",
        "Нет «правильных» ответов. Есть ваши.",
        "Можно писать коротко, можно целыми историями.",
        "Если вопрос трогает — сделайте паузу. Вернётесь позже.",
        "После заполнения можно устроить вечер чтения вслух и какао.",
        "Этот блокнот — не экзамен. Это свидание на бумаге.",
    ]
    for t in tips:
        add_para(doc, f"•  {t}", size=11, color=INK, space_before=4, space_after=6)
    add_para(
        doc,
        "\nС любовью к вашей паре ♡",
        size=10,
        italic=True,
        color=ACCENT,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=20,
    )
    page_break(doc)


def part_rules(doc, title, subtitle, rules):
    for _ in range(1):
        add_para(doc, "", space_after=8)
    add_para(doc, "ЧАСТЬ", size=10, bold=True, color=ACCENT, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_para(doc, title, size=15, bold=True, color=INK, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_para(doc, subtitle, size=10, italic=True, color=SOFT, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
    add_divider(doc, "· · ·")
    add_para(doc, "Милые правила этой части", size=12, bold=True, color=ACCENT, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
    for i, r in enumerate(rules, 1):
        add_para(doc, f"{i}.  {r}", size=10, color=INK, space_before=3, space_after=5)
    add_para(
        doc,
        "\nГотовы? Переворачивайте страницу ♡",
        size=10,
        italic=True,
        color=SOFT,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=16,
    )
    page_break(doc)


def notes_section(doc, who, pages=5):
    for i in range(1, pages + 1):
        add_para(doc, "Заметки", size=9, bold=True, color=ACCENT, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
        add_para(
            doc,
            f"Страница {who}  ·  {i} из {pages}",
            size=14,
            bold=True,
            color=INK,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=6,
        )
        add_divider(doc, "♡")
        add_para(
            doc,
            "Сюда можно писать мысли после вопросов, благодарности, мечты, списки свиданий…",
            size=9,
            italic=True,
            color=SOFT,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=10,
        )
        add_lines(doc, 14)
        if not (who == "Леры" and i == pages):
            page_break(doc)


PART1 = [
    ("Какой у тебя любимый цвет — и почему именно он?", 3),
    ("Любимый фильм. Какая сцена цепляет сильнее всего?", 3),
    ("Любимый сериал или книга, к которым хочется возвращаться.", 3),
    ("Любимая еда. А если совсем честно — любимый «стыдный» перекус?", 3),
    ("Любимый напиток (горячий / холодный / «для души»).", 2),
    ("Любимое время года и запах, который с ним связан.", 3),
    ("Любимая песня. Что в ней отзывается?", 3),
    ("Любимое место на земле (реальное или мечта).", 3),
    ("Море или горы? Утро или ночь? Сладкое или солёное?", 2),
    ("Идеальный выходной, если никого не нужно никуда вести.", 4),
    ("Хобби или занятие, которое тебя по-настоящему заряжает.", 3),
    ("Смешная привычка, которую ты в себе замечаешь.", 3),
    ("Суперсила, которую ты хотела бы иметь на один день.", 2),
    ("Твоё тотемное животное (и почему).", 2),
    ("Любимый запах. А любимый звук?", 2),
    ("Любимый праздник и маленькая традиция, без которой он не тот.", 3),
    ("Что всегда поднимает тебе настроение за пять минут?", 3),
    ("Комплимент, который тебе особенно приятен.", 3),
    ("В детстве я мечтала стать… А сейчас мне важно…", 3),
    ("Три вещи, которые делают обычный день хорошим.", 3),
    # important relationship self-knowledge
    ("Как со мной можно поступать в отношениях? (что поддерживает и радует)", 5, "Важно и честно."),
    ("Как со мной нельзя поступать в отношениях? (что ранит или отдаляет)", 5, "Без самокритики — только забота о границах."),
    ("Что для меня важно в партнёрше?", 4),
    ("Что для меня важно в отношениях в целом?", 4),
    ("Как я обычно проявляю любовь?", 3),
    ("Как я хочу, чтобы мне проявляли любовь?", 3),
    ("Что помогает мне чувствовать себя в безопасности рядом с человеком?", 4),
    ("Что меня успокаивает, когда я расстроена или тревожусь?", 3),
    ("Мои важные границы, которые нужно уважать.", 4),
    ("Как я обычно веду себя в конфликте — и чего мне тогда особенно нужно?", 4),
    ("Как понять, что мне сейчас нужна поддержка? Какие сигналы?", 3),
    ("Когда мне нужно личное пространство — как это выглядит и как об этом сказать?", 4),
    ("Чего я боюсь в близких отношениях (даже если это неловко признавать)?", 4),
    ("О чём мне бывает сложно говорить, но это важно?", 4),
    ("Что для меня значит «быть услышанной»?", 3),
    ("Моя «батарейка»: что наполняет меня энергией и теплом?", 3),
    ("Три вещи, без которых мне эмоционально тяжело.", 3),
    ("Какой тип отдыха мне нужен после трудного дня?", 3),
    ("Что я ценю в близости: разговоры, прикосновения, совместные дела, тишину рядом…?", 3),
    ("Если бы у меня был девиз в отношениях, он звучал бы так:", 3),
]

PART2 = [
    ("Как мы познакомились — моя версия этой истории.", 4),
    ("Первый момент, когда я подумала: «Ого, она особенная».", 4),
    ("Что я больше всего люблю в нашей паре?", 4),
    ("Наша самая смешная общая история.", 4),
    ("Маленький ритуал «только наш», который мне особенно дорог.", 3),
    ("Чем мы похожи? А чем красиво дополняем друг друга?", 4),
    ("Моё любимое воспоминание о нас.", 4),
    ("Место, песня или фильм, которые ассоциируются с «нами».", 3),
    ("Как я обычно чувствую себя рядом с тобой?", 3),
    ("Чему я научилась у тебя?", 3),
    ("Чему, как мне кажется, ты могла научиться у меня?", 3),
    ("Как мы справляемся с трудностями — что в этом работает хорошо?", 4),
    ("В чём нам как паре бывает непросто — и как можно бережнее?", 4),
    ("За что я особенно благодарна тебе прямо сейчас?", 4),
    ("Момент, когда я чувствовала нас особенно близкими.", 4),
    ("Как я узнаю, что нам хорошо и мы «в ресурсе» как пара?", 3),
    ("Что я хочу чаще делать вместе?", 3),
    ("Наше идеальное совместное утро.", 3),
    ("Наш идеальный совместный вечер.", 3),
    ("Путешествие (или просто выход), о котором я мечтаю с тобой.", 3),
    ("Традицию, которую я хочу завести именно для нас.", 3),
    ("О чём я мечтаю для нас через год?", 4),
    ("О чём я мечтаю для нас через пять лет?", 4),
    ("Как мы можем ещё лучше поддерживать друг друга?", 4),
    ("Что я хочу, чтобы ты всегда помнила обо мне?", 3),
    ("Если бы нашу пару позвали на реалити-шоу — какой у нас был бы «фирменный» ответ / шутка?", 3),
    ("Слоган нашей пары (серьёзный или абсолютно дурацкий).", 2),
    ("Мем, жест или фраза, которые понятны только нам.", 3),
    ("Чем я горжусь в нас как в команде?", 3),
    ("Письмо нашей паре (коротко): что я желаю «Илоне и Лере» дальше.", 5, "Можно от первого лица — как будто пишешь нам обеим."),
]


def normalize(items):
    out = []
    for item in items:
        if len(item) == 2:
            q, lines = item
            out.append((q, lines, None))
        else:
            out.append(item)
    return out


def build():
    doc = Document()
    set_a5(doc.sections[0])

    style = doc.styles["Normal"]
    style.font.name = "Georgia"
    style.font.size = Pt(11)
    style.font.color.rgb = INK

    cover_page(doc)
    how_to_use(doc)

    part_rules(
        doc,
        "«На случай участия в реалити-шоу»",
        "Каждая отвечает чисто за себя — про вкусы, привычки и то, как с ней быть в любви.",
        [
            "Представьте камеры, ведущего и смешной студийный диван — но пишите по-настоящему.",
            "Сначала лёгкие вопросы «любимый цвет / фильм», потом — важные про границы и близость.",
            "Не подглядывайте в ответ подруги, пока обе не закончите страницу (можно договориться иначе).",
            "Если вопрос про «нельзя» — это не про контроль, а про заботу: где мне больно, а где тепло.",
            "Можно рисовать сердечки, звёздочки и глупые смайлики на полях. Это официально разрешено.",
        ],
    )

    for i, (q, lines, note) in enumerate(normalize(PART1), 1):
        add_question_page(doc, i, q, lines=lines, note=note)

    part_rules(
        doc,
        "«Про нас»",
        "Вопросы о паре — но каждая всё равно отвечает отдельно. Две правды. Одна история.",
        [
            "Здесь нет соревнования «кто романтичнее». Есть две точки зрения на одно «мы».",
            "Если воспоминания чуть различаются — это нормально и даже мило. Запишите обе версии.",
            "Можно плакать, смеяться и делать перерыв на обнимашки между страницами.",
            "Трудные вопросы — приглашение к мягкости, а не к разбору полётов.",
            "В конце части устройте мини-шоу: читайте ответы по очереди и хлопайте друг другу.",
        ],
    )

    for i, (q, lines, note) in enumerate(normalize(PART2), 1):
        add_question_page(doc, i, q, lines=lines, note=note)

    # Notes divider
    add_para(doc, "", space_after=20)
    add_para(doc, "✦  ✦  ✦", size=14, color=ACCENT, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_para(doc, "Страницы заметок", size=18, bold=True, color=INK, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=8)
    add_para(
        doc,
        "5 листов для Илоны и 5 листов для Леры.\nПишите всё, что не влезло в ответы —\nили то, что родилось после разговора.",
        size=10,
        italic=True,
        color=SOFT,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=12,
    )
    add_para(doc, "♡", size=16, color=ACCENT, align=WD_ALIGN_PARAGRAPH.CENTER)
    page_break(doc)

    notes_section(doc, "Илоны", 5)
    notes_section(doc, "Леры", 5)

    out = "/workspace/couple_notebook/Bloknot_Ilona_i_Lera.docx"
    doc.save(out)
    print(f"Saved: {out}")
    print(f"Part 1 questions: {len(PART1)}")
    print(f"Part 2 questions: {len(PART2)}")
    # approximate pages: cover+howto+2 rules + q pages + notes divider + 10 notes
    approx = 1 + 1 + 1 + len(PART1) + 1 + len(PART2) + 1 + 10
    print(f"Approx pages: {approx}")


if __name__ == "__main__":
    build()
