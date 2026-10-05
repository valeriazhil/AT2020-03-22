#!/usr/bin/env python3
"""Generate A5 couples notebook DOCX for Ilona & Lera (black & white print)."""

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BLACK = RGBColor(0x00, 0x00, 0x00)
FONT = "Georgia"

PAGE_W_CM = 14.8
PAGE_H_CM = 21.0
MARGIN_X_CM = 1.5
TEXT_W_CM = PAGE_W_CM - 2 * MARGIN_X_CM

QUESTION_LINES = 7
QUESTION_LINE_H_CM = 0.9
NOTES_LINES = 16
NOTES_LINE_H_CM = 0.9


def set_a5(section):
    section.page_width = Cm(PAGE_W_CM)
    section.page_height = Cm(PAGE_H_CM)
    section.left_margin = Cm(MARGIN_X_CM)
    section.right_margin = Cm(MARGIN_X_CM)
    section.top_margin = Cm(1.3)
    section.bottom_margin = Cm(1.3)


def set_run_font(run, size=14, bold=False, italic=False):
    run.font.name = FONT
    run._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
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
    new_page=False,
    keep_next=False,
):
    p = doc.add_paragraph()
    p.alignment = align
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    pf.page_break_before = new_page
    pf.keep_with_next = keep_next
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold, italic=italic)
    return p


def add_divider(doc, char="* * *", keep_next=False):
    return add_para(
        doc,
        char,
        size=12,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=2,
        space_after=4,
        keep_next=keep_next,
    )


def _set_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        if edge in ("bottom", "insideH"):
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "8")
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), "000000")
        else:
            el.set(qn("w:val"), "nil")
        borders.append(el)
    tblPr.append(borders)


def _set_cell_margins_zero(table):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), "0")
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)


def add_lines_table(doc, n, row_cm):
    """n writing lines; each row is a fixed-height row with its own bottom rule."""
    table = doc.add_table(rows=n, cols=1)
    table.autofit = False
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    _set_table_borders(table)
    _set_cell_margins_zero(table)

    twips = int(row_cm * 567)
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        h = OxmlElement("w:trHeight")
        h.set(qn("w:val"), str(twips))
        h.set(qn("w:hRule"), "exact")
        trPr.append(h)
        cant = OxmlElement("w:cantSplit")
        trPr.append(cant)
        cell = row.cells[0]
        cell.width = Cm(TEXT_W_CM)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.keep_with_next = True
        r = p.add_run("")
        set_run_font(r, size=2)
    return table


def add_answer_block(doc, name, lines, row_cm):
    add_para(
        doc,
        f"{name}:",
        size=14,
        bold=True,
        space_before=6,
        space_after=0,
        keep_next=True,
    )
    add_lines_table(doc, lines, row_cm)


def add_question_page(doc, number, question, note=None):
    """One question per sheet; Ilona and Lera each get their own set of lines."""
    add_para(
        doc,
        f"Вопрос {number}",
        size=12,
        bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=2,
        new_page=True,
        keep_next=True,
    )
    add_para(
        doc,
        question,
        size=14,
        bold=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_before=2,
        space_after=2,
        keep_next=True,
    )
    if note:
        add_para(
            doc,
            note,
            size=11,
            italic=True,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=2,
            keep_next=True,
        )
    add_divider(doc, keep_next=True)
    add_answer_block(doc, "Илона", QUESTION_LINES, QUESTION_LINE_H_CM)
    add_answer_block(doc, "Лера", QUESTION_LINES, QUESTION_LINE_H_CM)


def cover_page(doc):
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
        "Каждая отвечает отдельно.\nПотом можно читать вслух —\nкак на самом милом реалити-шоу.",
        size=13,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=12,
    )
    add_para(
        doc,
        "Пишите честно и бережно.\nНет правильных ответов — есть ваши.",
        size=12,
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=10,
    )
    add_para(doc, "*  *  *", size=16, align=WD_ALIGN_PARAGRAPH.CENTER)


def part_rules(doc, part_no, title, subtitle, rules):
    add_para(doc, "", space_after=10, new_page=True)
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


def notes_section(doc, who, pages=10):
    for i in range(1, pages + 1):
        add_para(
            doc,
            "Заметки",
            size=12,
            bold=True,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=2,
            new_page=True,
            keep_next=True,
        )
        add_para(
            doc,
            f"Страница {who}  ·  {i} из {pages}",
            size=16,
            bold=True,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=4,
            keep_next=True,
        )
        add_divider(doc, keep_next=True)
        add_para(
            doc,
            "Мысли, благодарности, мечты, идеи для свиданий...",
            size=12,
            italic=True,
            align=WD_ALIGN_PARAGRAPH.CENTER,
            space_after=4,
            keep_next=True,
        )
        add_lines_table(doc, NOTES_LINES, NOTES_LINE_H_CM)


# Часть 1: каждая отвечает про себя. Формулировки подходят обеим.
PART1 = [
    # --- лёгкие, «для реалити-шоу» ---
    "Мой любимый цвет — и почему именно он?",
    "Мой любимый фильм. Какая сцена цепляет сильнее всего?",
    "Мой любимый сериал или книга, к которым хочется возвращаться.",
    "Моя любимая еда. А если честно — любимый «стыдный» перекус?",
    "Мой любимый напиток: горячий, холодный или «для души»?",
    "Моё любимое время года и запах, который с ним связан.",
    "Моя любимая песня. Что в ней отзывается?",
    "Мой любимый исполнитель или группа.",
    "Моё любимое место на земле (реальное или мечта).",
    "Море или горы? Утро или ночь? Сладкое или солёное? Мои выборы и почему.",
    "Мой идеальный выходной, если никуда не нужно спешить.",
    "Занятие, которое меня по-настоящему заряжает.",
    "Смешная привычка, которую я в себе замечаю.",
    "Суперсила, которую я хотела бы иметь на один день.",
    "Моё тотемное животное — и почему.",
    "Мой любимый запах. А любимый звук?",
    "Мой любимый праздник и маленькая традиция к нему.",
    "Что поднимает мне настроение за пять минут?",
    "Мой самый нелепый страх — тот, над которым можно посмеяться.",
    "Что я никогда не откажусь съесть, даже если «уже наелась»?",
    "Три вещи, которые я взяла бы с собой на необитаемый остров.",
    "Мой талант, о котором мало кто знает.",
    "Кем я мечтала стать в детстве? А что важно мне сейчас?",
    "Какой комплимент мне особенно приятен?",
    "Если бы про меня снимали фильм — какого он был бы жанра и кто сыграл бы меня?",
    # --- важное про себя и отношения ---
    ("Как со мной можно поступать в отношениях?", "Что поддерживает, радует, делает мне тепло."),
    ("Как со мной нельзя поступать в отношениях?", "Это про заботу о границах, а не про обвинения."),
    "Что для меня важно в партнёрше?",
    "Что для меня важно в отношениях в целом?",
    "Как я проявляю любовь?",
    "Как я хочу, чтобы мне проявляли любовь?",
    "Что помогает мне чувствовать себя в безопасности рядом с человеком?",
    "Что меня успокаивает, когда мне тревожно или плохо?",
    "Мои важные границы, которые нужно уважать.",
    "Как я веду себя в конфликте — и что мне тогда нужно?",
    "По каким сигналам понятно, что мне нужна поддержка?",
    "Когда мне нужно личное пространство — как об этом сказать и что не принимать на свой счёт?",
    "Чего я боюсь в близких отношениях?",
    "О чём мне сложно говорить, но это важно?",
    "Что для меня значит «быть услышанной»?",
    "Что наполняет меня энергией и теплом?",
    "Три вещи, без которых мне эмоционально тяжело.",
    "Какой отдых мне нужен после трудного дня?",
    "Что я больше всего ценю в близости: разговоры, прикосновения, дела вместе, тишину рядом?",
    "Как я прошу о помощи — и что мне мешает это делать?",
    "Что для меня «романтика» в обычной жизни?",
    "Какие слова поддержки мне нужны чаще всего?",
    "Что в отношениях для меня «красный флаг», а что — «зелёный»?",
    "Чему я хочу научиться в отношениях?",
    "Моё качество, за которое я себе благодарна.",
]

# Часть 2: про пару, но каждая отвечает отдельно.
PART2 = [
    "Как мы познакомились — моя версия этой истории.",
    "Первый момент, когда я подумала: «Ого, она особенная».",
    "Что я больше всего люблю в нашей паре?",
    "Наша самая смешная общая история.",
    "Маленький ритуал «только наш», который мне особенно дорог.",
    "Чем мы похожи? А чем красиво дополняем друг друга?",
    "Моё любимое воспоминание о нас.",
    "Место, песня или фильм, которые ассоциируются с «нами».",
    "Как я чувствую себя рядом с тобой?",
    "Чему я научилась у тебя?",
    "Чему, как мне кажется, ты могла научиться у меня?",
    "Как мы справляемся с трудностями — что в этом работает хорошо?",
    "В чём нам как паре бывает непросто — и как можно бережнее?",
    "За что я особенно благодарна тебе прямо сейчас?",
    "Момент, когда я чувствовала нас особенно близкими.",
    "Как я понимаю, что нам хорошо и мы «в ресурсе» как пара?",
    "Что я хочу чаще делать вместе?",
    "Наше идеальное совместное утро.",
    "Наш идеальный совместный вечер.",
    "Путешествие (или просто выход), о котором я мечтаю с тобой.",
    "Традиция, которую я хочу завести именно для нас.",
    "О чём я мечтаю для нас через год?",
    "О чём я мечтаю для нас через пять лет?",
    "Как мы можем ещё лучше поддерживать друг друга?",
    "Что я хочу, чтобы ты всегда помнила обо мне?",
    "Если бы нашу пару позвали на реалити-шоу — какой у нас был бы «фирменный» ответ или шутка?",
    "Слоган нашей пары (серьёзный или абсолютно дурацкий).",
    "Мем, жест или фраза, которые понятны только нам.",
    "Чем я горжусь в нас как в команде?",
    ("Письмо нашей паре: что я желаю «Илоне и Лере» дальше.", "Можно писать так, будто обращаешься к нам обеим."),
    "Какая наша ссора (если была) научила нас чему-то важному?",
    "Как я понимаю, что тебе сейчас нужна забота?",
    "Что в тебе неизменно меня восхищает?",
    "Какой у нас «язык любви» как у пары?",
    "Какое совместное дело делает нас ближе?",
    "О чём я мечтаю поговорить с тобой глубже?",
    "Какой комплимент я хочу чаще говорить тебе?",
    "Какой комплимент я хочу чаще слышать от тебя?",
    "Если бы у нашей пары был саундтрек — что бы в него вошло?",
    "Каким мне представляется наш уют — наш дом «по-нашему»?",
    "Что я хочу сохранить в нас всегда, даже когда жизнь штормит?",
    "Маленькая радость, которую я хочу дарить тебе чаще.",
    "Как мы отмечаем победы — и как хотелось бы отмечать?",
    "Что для меня значит «мы — команда»?",
    "Одно бережное и реальное обещание себе в наших отношениях.",
    "Одно тёплое пожелание тебе на ближайший месяц.",
    "История про нас, которую я люблю рассказывать другим.",
    "Что меня больше всего смешит в нас двоих?",
    "Как я хочу, чтобы мы заботились о «нас», а не только о делах?",
    "Три слова, которыми я бы описала нашу пару сегодня.",
]


def unpack(item):
    if isinstance(item, tuple):
        return item[0], item[1]
    return item, None


def build(out="/workspace/couple_notebook/Bloknot_Ilona_i_Lera.docx"):
    assert len(PART1) == 50, len(PART1)
    assert len(PART2) == 50, len(PART2)

    doc = Document()
    set_a5(doc.sections[0])

    style = doc.styles["Normal"]
    style.font.name = FONT
    style.font.size = Pt(14)
    style.font.color.rgb = BLACK

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

    for i, item in enumerate(PART1, 1):
        q, note = unpack(item)
        add_question_page(doc, i, q, note=note)

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

    for i, item in enumerate(PART2, 51):
        q, note = unpack(item)
        add_question_page(doc, i, q, note=note)

    notes_section(doc, "Илоны", 10)
    notes_section(doc, "Леры", 10)

    tail = doc.add_paragraph()
    tail.paragraph_format.space_before = Pt(0)
    tail.paragraph_format.space_after = Pt(0)
    set_run_font(tail.add_run(""), size=1)

    doc.save(out)
    total = 1 + 1 + 50 + 1 + 50 + 20
    print(f"Saved: {out}")
    print(f"Question sheets: {len(PART1) + len(PART2)}, note sheets: 20, expected pages: {total}")


if __name__ == "__main__":
    build()
