#!/usr/bin/env python3
"""Generate A5 couples notebook DOCX for Ilona & Lera (B&W print, 120 sheets)."""

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BLACK = RGBColor(0x00, 0x00, 0x00)
LINE_CHARS = 36  # fits A5 width with larger font


def set_a5(section):
    section.page_width = Cm(14.8)
    section.page_height = Cm(21.0)
    section.left_margin = Cm(1.5)
    section.right_margin = Cm(1.5)
    section.top_margin = Cm(1.2)
    section.bottom_margin = Cm(1.2)


def set_run_font(run, size=14, bold=False, italic=False, name="Georgia"):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = BLACK


def add_para(
    doc,
    text,
    *,
    size=14,
    bold=False,
    italic=False,
    align=WD_ALIGN_PARAGRAPH.LEFT,
    space_before=0,
    space_after=6,
):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold, italic=italic)
    return p


def add_divider(doc, char="* * *"):
    add_para(doc, char, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=6)


def add_lines(doc, n, size=14):
    """Writing lines that fill vertical space on A5."""
    for _ in range(n):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.45
        run = p.add_run("_" * LINE_CHARS)
        set_run_font(run, size=size)


def page_break(doc):
    doc.add_page_break()


def add_answer_block(doc, name, lines):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(f"{name}:")
    set_run_font(run, size=15, bold=True)
    add_lines(doc, lines, size=14)


def add_question_page(doc, part_label, number, question, note=None, lines_each=9):
    """One question per sheet; answer lines fill the rest of the page."""
    add_para(
        doc,
        part_label,
        size=11,
        bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=2,
    )
    add_para(
        doc,
        f"Вопрос {number}",
        size=12,
        bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=4,
    )
    add_para(
        doc,
        question,
        size=16,
        bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=2,
        space_after=4,
    )
    if note:
        add_para(
            doc,
            note,
            size=12,
            italic=True,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=4,
        )
    add_divider(doc)
    # ~9 lines each fills remaining A5 after larger question header
    add_answer_block(doc, "Илона", lines_each)
    add_answer_block(doc, "Лера", lines_each)
    page_break(doc)


def cover_page(doc):
    for _ in range(1):
        add_para(doc, "", space_after=6)
    add_para(doc, "*  *  *", size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_para(
        doc,
        "Блокнот нашей пары",
        size=26,
        bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=10,
    )
    add_para(
        doc,
        "Илона  &  Лера",
        size=20,
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=12,
    )
    add_divider(doc, "<3")
    add_para(
        doc,
        "Вопросы, которые сближают.\nОтветы, которые хочется хранить.",
        size=14,
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=8,
        space_after=12,
    )
    add_para(
        doc,
        "100 листов вопросов + по 10 листов заметок каждой.\nКаждая отвечает отдельно.\nПотом можно читать вслух —\nкак на самом милом реалити-шоу.",
        size=13,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=12,
    )
    add_para(
        doc,
        "Пишите честно и бережно. Нет правильных ответов — есть ваши.",
        size=12,
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=10,
    )
    add_para(doc, "*  *  *", size=16, align=WD_ALIGN_PARAGRAPH.CENTER)
    page_break(doc)


def how_to_use(doc):
    add_para(doc, "Как пользоваться", size=20, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_divider(doc)
    tips = [
        "Отвечайте честно, но бережно — к себе и к друг другу.",
        "Нет «правильных» ответов. Есть ваши.",
        "Пишите столько, сколько хочется: линии на весь лист.",
        "Если вопрос трогает — сделайте паузу и вернитесь позже.",
        "После заполнения можно устроить вечер чтения вслух.",
        "Этот блокнот — не экзамен. Это свидание на бумаге.",
    ]
    for t in tips:
        add_para(doc, f"-  {t}", size=14, space_before=4, space_after=8)
    add_para(
        doc,
        "\nС любовью к вашей паре",
        size=13,
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=16,
    )
    page_break(doc)


def part_rules(doc, part_no, title, subtitle, rules):
    add_para(doc, "", space_after=10)
    add_para(doc, f"ЧАСТЬ {part_no}", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    add_para(doc, title, size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
    add_para(doc, subtitle, size=13, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    add_divider(doc)
    add_para(doc, "Милые правила этой части", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
    for i, r in enumerate(rules, 1):
        add_para(doc, f"{i}.  {r}", size=13, space_before=4, space_after=6)
    add_para(
        doc,
        "\nГотовы? Переворачивайте страницу",
        size=13,
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=14,
    )
    page_break(doc)


def notes_section(doc, who, pages=10):
    for i in range(1, pages + 1):
        add_para(doc, "Заметки", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
        add_para(
            doc,
            f"Страница {who}  ·  {i} из {pages}",
            size=18,
            bold=True,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=4,
        )
        add_divider(doc)
        add_para(
            doc,
            "Мысли после вопросов, благодарности, мечты, списки свиданий...",
            size=12,
            italic=True,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=6,
        )
        add_lines(doc, 18, size=14)
        if not (who == "Леры" and i == pages):
            page_break(doc)


# --- 50 + 50 = 100 question sheets ---
PART1 = [
    "Какой у тебя любимый цвет — и почему именно он?",
    "Любимый фильм. Какая сцена цепляет сильнее всего?",
    "Любимый сериал или книга, к которым хочется возвращаться.",
    "Любимая еда. А если совсем честно — любимый «стыдный» перекус?",
    "Любимый напиток: горячий, холодный или «для души»?",
    "Любимое время года и запах, который с ним связан.",
    "Любимая песня. Что в ней отзывается?",
    "Любимый исполнитель или группа.",
    "Любимое место на земле (реальное или мечта).",
    "Море или горы? Утро или ночь? Сладкое или солёное?",
    "Идеальный выходной, если никого не нужно никуда вести.",
    "Хобби или занятие, которое тебя по-настоящему заряжает.",
    "Смешная привычка, которую ты в себе замечаешь.",
    "Суперсила, которую ты хотела бы иметь на один день.",
    "Твоё тотемное животное — и почему.",
    "Любимый запах. А любимый звук?",
    "Любимый праздник и маленькая традиция к нему.",
    "Что всегда поднимает тебе настроение за пять минут?",
    "Комплимент, который тебе особенно приятен.",
    "В детстве я мечтала стать… А сейчас мне важно…",
    "Три вещи, которые делают обычный день хорошим.",
    "Любимый способ провести вечер дома.",
    "Что ты коллекционируешь — вещи, моменты, плейлисты?",
    "Какой жанр тебе ближе: комедия, драма, фантастика, ужасы?",
    "Если бы день был только твоим — как бы ты его прожила?",
    # important self / relationship
    ("Как со мной можно поступать в отношениях? (что поддерживает и радует)", "Важно и честно."),
    ("Как со мной нельзя поступать в отношениях? (что ранит или отдаляет)", "Это про заботу о границах."),
    "Что для меня важно в партнёрше?",
    "Что для меня важно в отношениях в целом?",
    "Как я обычно проявляю любовь?",
    "Как я хочу, чтобы мне проявляли любовь?",
    "Что помогает мне чувствовать себя в безопасности рядом с человеком?",
    "Что меня успокаивает, когда я расстроена или тревожусь?",
    "Мои важные границы, которые нужно уважать.",
    "Как я обычно веду себя в конфликте — и чего мне тогда особенно нужно?",
    "Как понять, что мне сейчас нужна поддержка? Какие у меня сигналы?",
    "Когда мне нужно личное пространство — как это выглядит и как об этом сказать?",
    "Чего я боюсь в близких отношениях (даже если это неловко признавать)?",
    "О чём мне бывает сложно говорить, но это важно?",
    "Что для меня значит «быть услышанной»?",
    "Моя «батарейка»: что наполняет меня энергией и теплом?",
    "Три вещи, без которых мне эмоционально тяжело.",
    "Какой тип отдыха мне нужен после трудного дня?",
    "Что я ценю в близости: разговоры, прикосновения, дела вместе, тишину рядом?",
    "Если бы у меня был девиз в отношениях, он звучал бы так:",
    "Как я прошу о помощи — и что мне мешает это делать?",
    "Что для меня «романтика» в обычной жизни?",
    "Какие слова поддержки мне особенно нужны?",
    "Что я хочу чаще разрешать себе в любви и в жизни?",
    "Одно качество в себе, за которое я себе благодарна.",
]

PART2 = [
    "Как мы познакомились — моя версия этой истории.",
    "Первый момент, когда я подумала: «Ого, она особенная».",
    "Что я больше всего люблю в нашей паре?",
    "Наша самая смешная общая история.",
    "Маленький ритуал «только наш», который мне особенно дорог.",
    "Чем мы похожи? А чем красиво дополняем друг друга?",
    "Моё любимое воспоминание о нас.",
    "Место, песня или фильм, которые ассоциируются с «нами».",
    "Как я обычно чувствую себя рядом с тобой?",
    "Чему я научилась у тебя?",
    "Чему, как мне кажется, ты могла научиться у меня?",
    "Как мы справляемся с трудностями — что в этом работает хорошо?",
    "В чём нам как паре бывает непросто — и как можно бережнее?",
    "За что я особенно благодарна тебе прямо сейчас?",
    "Момент, когда я чувствовала нас особенно близкими.",
    "Как я узнаю, что нам хорошо и мы «в ресурсе» как пара?",
    "Что я хочу чаще делать вместе?",
    "Наше идеальное совместное утро.",
    "Наш идеальный совместный вечер.",
    "Путешествие (или просто выход), о котором я мечтаю с тобой.",
    "Традицию, которую я хочу завести именно для нас.",
    "О чём я мечтаю для нас через год?",
    "О чём я мечтаю для нас через пять лет?",
    "Как мы можем ещё лучше поддерживать друг друга?",
    "Что я хочу, чтобы ты всегда помнила обо мне?",
    "Если бы нашу пару позвали на реалити-шоу — какой у нас был бы «фирменный» ответ или шутка?",
    "Слоган нашей пары (серьёзный или абсолютно дурацкий).",
    "Мем, жест или фраза, которые понятны только нам.",
    "Чем я горжусь в нас как в команде?",
    ("Письмо нашей паре: что я желаю «Илоне и Лере» дальше.", "Можно от первого лица — как будто пишешь нам обеим."),
    "Какая наша ссора (если была) научила нас чему-то важному?",
    "Как я понимаю, что тебе сейчас нужна забота?",
    "Что в тебе неизменно восхищает меня?",
    "Наш «язык любви» как пары — какой он?",
    "Какое совместное дело делает нас ближе?",
    "О чём я мечтаю поговорить с тобой ещё глубже?",
    "Какой комплимент я хочу чаще говорить тебе?",
    "Какой комплимент я хочу чаще слышать от тебя?",
    "Если бы у нашей пары был саундтрек — что бы в него вошло?",
    "Дом / уют «по-нашему» — как он выглядит в моей голове?",
    "Что я хочу сохранить в нас всегда, даже когда жизнь штормит?",
    "Маленькая радость, которую я хочу дарить тебе чаще.",
    "Как мы отмечаем победы — и как хотелось бы отмечать?",
    "Что для меня значит «мы команда»?",
    "Одно обещание себе в наших отношениях (бережное, реальное).",
    "Одно тёплое пожелание тебе на ближайший месяц.",
    "История, которую я люблю рассказывать про нас другим.",
    "Что меня больше всего смешит в нас двоих?",
    "Как я хочу, чтобы мы заботились о «нас», а не только о делах?",
    "Три слова, которыми я бы описала нашу пару сегодня.",
]


def unpack(item):
    if isinstance(item, tuple):
        return item[0], item[1]
    return item, None


def build():
    assert len(PART1) == 50, len(PART1)
    assert len(PART2) == 50, len(PART2)

    doc = Document()
    set_a5(doc.sections[0])

    style = doc.styles["Normal"]
    style.font.name = "Georgia"
    style.font.size = Pt(14)
    style.font.color.rgb = BLACK

    # Exactly: 1 cover + 2 rule pages + 100 questions + 20 notes = 123 pages
    # Core asked by user: 100 question sheets + 20 note sheets (= 120).
    cover_page(doc)

    part_rules(
        doc,
        1,
        "«На случай участия в реалити-шоу»",
        "Каждая отвечает чисто за себя — про вкусы, привычки и то, как с ней быть в любви.",
        [
            "Представьте камеры и смешной диван — но пишите по-настоящему.",
            "Сначала лёгкие вопросы, потом важные про границы и близость.",
            "Можно не подглядывать в ответ, пока обе не закончите страницу.",
            "Вопросы «можно / нельзя» — про заботу, а не про контроль.",
            "Рисовать сердечки и звёздочки на полях официально можно.",
        ],
    )

    label1 = "Часть 1 · Реалити-шоу"
    for i, item in enumerate(PART1, 1):
        q, note = unpack(item)
        add_question_page(doc, label1, i, q, note=note, lines_each=9)

    part_rules(
        doc,
        2,
        "«Про нас»",
        "Вопросы о паре — но каждая отвечает отдельно. Две правды. Одна история.",
        [
            "Нет соревнования «кто романтичнее» — есть две точки зрения на «мы».",
            "Если воспоминания чуть разные — это нормально. Запишите обе версии.",
            "Можно смеяться, обниматься и делать паузы между страницами.",
            "Трудные вопросы — приглашение к мягкости, не к разбору полётов.",
            "В конце устройте мини-шоу: читайте ответы и хлопайте друг другу.",
        ],
    )

    label2 = "Часть 2 · Про нас"
    for i, item in enumerate(PART2, 1):
        q, note = unpack(item)
        add_question_page(doc, label2, i, q, note=note, lines_each=9)

    notes_section(doc, "Илоны", 10)
    notes_section(doc, "Леры", 10)

    out = "/workspace/couple_notebook/Bloknot_Ilona_i_Lera.docx"
    doc.save(out)

    # cover + 2 rules + 100 questions + 20 notes
    front = 3
    questions = len(PART1) + len(PART2)
    notes = 20
    print(f"Saved: {out}")
    print(f"Part 1 questions: {len(PART1)}")
    print(f"Part 2 questions: {len(PART2)}")
    print(f"Question sheets: {questions}")
    print(f"Note sheets: {notes}")
    print(f"Front sheets (cover+rules): {front}")
    print(f"Core (questions+notes): {questions + notes}")
    print(f"Total pages (approx): {front + questions + notes}")


if __name__ == "__main__":
    build()
