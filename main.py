import flet as ft
import threading

from api_func import initial_client, generate_quiz
from dotenv_func import get_api_key

# ============================================
# КОНСПЕКТ
# ============================================
DEFAULT_TEXT = """1. Механическое движение
Механическое движение — изменение положения тела относительно других тел с течением времени.

Траектория — линия, по которой движется тело.

Путь — длина траектории. Измеряется в метрах (м).

Скорость — физическая величина, показывающая, какой путь проходит тело за единицу времени. Формула: v = S / t, где S — путь, t — время. Единица измерения: м/с.

Равномерное движение — движение, при котором скорость тела не меняется.

Неравномерное движение — движение, при котором скорость меняется.

2. Сила и масса
Сила — причина изменения скорости тела. Измеряется в ньютонах (Н).

Масса — мера инертности тела. Измеряется в килограммах (кг).

Закон всемирного тяготения (Ньютон): все тела притягиваются друг к другу с силой, прямо пропорциональной произведению их масс и обратно пропорциональной квадрату расстояния между ними.

Сила тяжести — сила, с которой Земля притягивает тело. Формула: F = mg, где g ≈ 9,8 Н/кг (ускорение свободного падения).

Вес тела — сила, с которой тело давит на опору или подвес.

3. Давление
Давление — физическая величина, равная отношению силы к площади поверхности. Формула: p = F / S. Единица измерения: паскаль (Па).

Закон Паскаля: давление, производимое на жидкость или газ, передаётся во все стороны без изменения.

Атмосферное давление — давление воздуха на поверхность Земли. У поверхности оно равно примерно 101 300 Па.

Закон Архимеда: на тело, погружённое в жидкость (или газ), действует выталкивающая сила, равная весу вытесненной жидкости (или газа).

4. Тепловые явления
Температура — мера средней кинетической энергии молекул. Измеряется в градусах Цельсия (°C) или Кельвинах (K).

Теплопередача — процесс передачи энергии от более нагретого тела к менее нагретому.

Теплопроводность — вид теплопередачи, при котором энергия передаётся от одной частицы к другой.

Конвекция — теплопередача за счёт движения жидкости или газа.

Излучение — теплопередача с помощью электромагнитных волн.

Количество теплоты — энергия, которую получает или отдаёт тело. Формула: Q = cmΔT, где c — удельная теплоёмкость, m — масса, ΔT — изменение температуры.

5. Агрегатные состояния вещества
Твёрдое тело — молекулы расположены в строгом порядке и колеблются около положений равновесия.

Жидкость — молекулы совершают колебания и могут перескакивать с места на место.

Газ — молекулы движутся хаотично, почти не взаимодействуя друг с другом.

Плавление — переход из твёрдого состояния в жидкое.

Кристаллизация — переход из жидкого в твёрдое.

Парообразование — переход из жидкого в газообразное.

Конденсация — переход из газообразного в жидкое.

6. Электричество и магнетизм
Электрический ток — упорядоченное движение заряженных частиц.

Сила тока (I) — заряд, проходящий через поперечное сечение проводника за единицу времени. Единица измерения: ампер (А).

Напряжение (U) — работа по перемещению заряда. Единица измерения: вольт (В).

Сопротивление (R) — способность проводника препятствовать току. Единица измерения: ом (Ом).

Закон Ома: I = U / R.

Магнитное поле — создаётся движущимися зарядами (электрическим током).

Электромагнит — катушка с током, усиливающая магнитное поле.

7. Оптика
Свет — электромагнитное излучение, воспринимаемое глазом.

Отражение света — изменение направления луча при встрече с поверхностью. Угол падения равен углу отражения.

Преломление света — изменение направления луча при переходе из одной среды в другую.

Линза — прозрачное тело, преломляющее свет. Бывают собирающие и рассеивающие.

Фокус — точка, в которой собираются лучи после прохождения через линзу.

8. Энергия и работа
Работа (A) — мера действия силы. Формула: A = F × S. Единица измерения: джоуль (Дж).

Мощность (N) — скорость выполнения работы. Формула: N = A / t. Единица измерения: ватт (Вт).

Кинетическая энергия — энергия движения. Формула: E = mv² / 2.

Потенциальная энергия — энергия взаимодействия. Формула: E = mgh (для тела, поднятого над землёй).

Закон сохранения энергии: энергия не исчезает и не создаётся, а только переходит из одной формы в другую."""


def main(page: ft.Page):
    # ============================================
    # НАСТРОЙКА ОКНА — СРАЗУ НА ВЕСЬ ЭКРАН
    # ============================================
    page.title = "QuizBot"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO

    # Разворачиваем окно на весь экран
    page.window.maximized = True
    page.window.width = 1200
    page.window.height = 800
    page.window.min_width = 360
    page.window.min_height = 600
    page.window.resizable = True

    is_mobile = page.width < 700

    # Цвета
    PRIMARY = ft.Colors.INDIGO_600
    PRIMARY_DARK = ft.Colors.INDIGO_800
    PRIMARY_LIGHT = ft.Colors.INDIGO_50
    BG = ft.Colors.GREY_100
    CARD_BG = ft.Colors.WHITE
    SUCCESS = ft.Colors.GREEN_600
    SUCCESS_BG = ft.Colors.GREEN_50
    ERROR = ft.Colors.RED_600
    ERROR_BG = ft.Colors.RED_50

    # ============================================
    # СОСТОЯНИЕ
    # ============================================
    questions = []
    current_q = 0
    answers = {}
    client = None
    answered = False

    # ============================================
    # ФУНКЦИИ
    # ============================================

    def set_count(n):
        txt_question_count.value = str(n)
        page.update()

    preset_row = ft.Row(
        [
            ft.Button("3", on_click=lambda e: set_count(3), width=60),
            ft.Button("5", on_click=lambda e: set_count(5), width=60),
            ft.Button("10", on_click=lambda e: set_count(10), width=70),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=8,
    )

    def show_loading(show: bool):
        """Показывает/скрывает оверлей загрузки на весь экран"""
        loading_overlay.visible = show
        page.update()

    def on_generate(e):
        nonlocal questions, current_q, answers, client, answered

        text = txt_input.value
        if not text or len(text.strip()) < 20:
            txt_status.value = "⚠️ Введите текст конспекта (минимум 20 символов)"
            txt_status.color = ft.Colors.ORANGE
            page.update()
            return
        try:
            count = int(txt_question_count.value)
            if count < 1 or count > 20:
                raise ValueError
        except ValueError:
            txt_status.value = "⚠️ Введите число от 1 до 20"
            txt_status.color = ft.Colors.ORANGE
            page.update()
            return

        show_loading(True)

        def worker():
            nonlocal questions, current_q, answers, client, answered
            try:
                if client is None:
                    client = initial_client(get_api_key('ODI_API'))
                result = generate_quiz(text, client, count)

                if result:
                    questions = result
                    current_q = 0
                    answers = {}
                    answered = False
                    show_question()
                else:
                    txt_status.visible = True
                    txt_status.value = "❌ Не удалось сгенерировать вопросы"
                    txt_status.color = ft.Colors.RED
            except Exception as err:
                txt_status.visible = True
                txt_status.value = f"❌ Ошибка: {err}"
                txt_status.color = ft.Colors.RED
            finally:
                show_loading(False)

        threading.Thread(target=worker, daemon=True).start()

    def show_question():
        nonlocal current_q, answered

        if current_q >= len(questions):
            show_results()
            return

        answered = False
        q = questions[current_q]

        intro_section.visible = False
        input_card.visible = False
        txt_status.visible = False
        feedback_box.visible = False

        txt_question.visible = True
        txt_question.value = q['question']
        progress_text.visible = True
        progress_text.value = f"Вопрос {current_q + 1} из {len(questions)}"

        progress_bar.value = current_q / len(questions)
        progress_bar.visible = True

        options_container.controls.clear()
        for idx, option in enumerate(q['options']):
            btn = ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                chr(65 + idx),
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=PRIMARY,
                            ),
                            width=36,
                            height=36,
                            bgcolor=PRIMARY_LIGHT,
                            border_radius=18,
                            alignment=ft.Alignment.CENTER,
                        ),
                        ft.Markdown(  # ← было ft.Text
                            option,
                            selectable=False,
                            extension_set="gitHubWeb",
                            latex_scale_factor=0.9,
                            latex_style=ft.TextStyle(color=ft.Colors.GREY_900),
                            expand=True,
                        ),
                    ],
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=CARD_BG,
                border=ft.Border.all(2, ft.Colors.GREY_200),
                border_radius=14,
                padding=ft.Padding.symmetric(vertical=14, horizontal=16),
                on_click=lambda e, i=idx: select_answer(i),
                ink=True,
                animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
                shadow=ft.BoxShadow(
                    blur_radius=4,
                    color=ft.Colors.with_opacity(0.05, ft.Colors.BLACK),
                    offset=ft.Offset(0, 2),
                ),
            )
            options_container.controls.append(btn)

        options_container.visible = True
        btn_next.visible = False
        page.update()

    def select_answer(index):
        nonlocal answers, answered

        if answered:
            return
        answered = True
        answers[current_q] = index
        q = questions[current_q]

        correct_letter = q['correct']
        correct_index = next(
            (i for i, opt in enumerate(q['options']) if opt.startswith(correct_letter)),
            -1,
        )

        for i, btn in enumerate(options_container.controls):
            row = btn.content
            letter_box = row.controls[0]
            md = row.controls[1]

            if i == correct_index:
                btn.bgcolor = SUCCESS_BG
                btn.border = ft.Border.all(2, SUCCESS)
                letter_box.bgcolor = SUCCESS
                letter_box.content.color = ft.Colors.WHITE
            elif i == index:
                btn.bgcolor = ERROR_BG
                btn.border = ft.Border.all(2, ERROR)
                letter_box.bgcolor = ERROR
                letter_box.content.color = ft.Colors.WHITE
            else:
                btn.bgcolor = CARD_BG
                btn.border = ft.Border.all(2, ft.Colors.GREY_200)

        is_correct = index == correct_index
        description = q.get('description') or q.get('explanation') or ""

        feedback_title.value = "✅ Верно!" if is_correct else "❌ Неверно"
        feedback_title.color = SUCCESS if is_correct else ERROR
        feedback_icon.name = ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL
        feedback_icon.color = SUCCESS if is_correct else ERROR

        feedback_text.value = description if description else (
            "Правильный ответ: " + q['options'][correct_index]
        )
        feedback_box.bgcolor = SUCCESS_BG if is_correct else ERROR_BG
        feedback_box.border = ft.Border.all(1, SUCCESS if is_correct else ERROR)
        feedback_box.visible = True

        btn_next.visible = True
        page.update()

    def on_next(e):
        nonlocal current_q
        current_q += 1
        show_question()

    def show_results():
        correct = 0
        total = len(questions)

        for i, q in enumerate(questions):
            if i in answers:
                correct_letter = q['correct']
                correct_index = next(
                    (idx for idx, opt in enumerate(q['options']) if opt.startswith(correct_letter)),
                    -1,
                )
                if answers[i] == correct_index:
                    correct += 1

        percent = round(correct / total * 100) if total > 0 else 0

        txt_question.visible = False
        progress_text.visible = False
        progress_bar.visible = False
        feedback_box.visible = False
        options_container.controls.clear()

        if percent >= 80:
            emoji, message, color = "🎉", "Отличный результат!", SUCCESS
        elif percent >= 50:
            emoji, message, color = "👍", "Хороший результат!", ft.Colors.ORANGE_600
        else:
            emoji, message, color = "📚", "Стоит повторить материал", ERROR

        result_card = ft.Container(
            content=ft.Column(
                [
                    ft.Text(emoji, size=60),
                    ft.Text("Результат", size=20, weight=ft.FontWeight.BOLD),
                    ft.Container(height=10),
                    ft.Text(f"{correct} из {total}", size=48, weight=ft.FontWeight.BOLD, color=PRIMARY),
                    ft.Text(f"{percent}% правильных ответов", size=16, color=ft.Colors.GREY_600),
                    ft.Container(height=10),
                    ft.Text(message, size=18, weight=ft.FontWeight.W_600, color=color, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=20),
                    ft.Button(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.REFRESH, size=20),
                                ft.Text("Пройти ещё раз", size=16),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=8,
                        ),
                        style=ft.ButtonStyle(
                            bgcolor=PRIMARY,
                            color=ft.Colors.WHITE,
                            shape=ft.RoundedRectangleBorder(radius=12),
                            padding=ft.Padding.symmetric(vertical=14, horizontal=24),
                        ),
                        on_click=lambda e: restart_quiz(),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor=CARD_BG,
            border_radius=20,
            padding=30,
            border=ft.Border.all(1, ft.Colors.GREY_200),
            shadow=ft.BoxShadow(
                blur_radius=15,
                color=ft.Colors.with_opacity(0.08, ft.Colors.BLACK),
                offset=ft.Offset(0, 4),
            ),
        )

        options_container.controls.append(result_card)
        options_container.visible = True
        btn_next.visible = False
        page.update()

    def restart_quiz():
        nonlocal questions, current_q, answers, answered
        questions = []
        current_q = 0
        answers = {}
        answered = False
        intro_section.visible = True
        input_card.visible = True
        txt_status.visible = True
        txt_status.value = ""
        options_container.controls.clear()
        options_container.visible = False
        txt_question.visible = False
        progress_text.visible = False
        progress_bar.visible = False
        feedback_box.visible = False
        page.update()

    # ============================================
    # КОМПОНЕНТЫ СТАРТОВОГО ЭКРАНА
    # ============================================

    # Верхний баннер с градиентом (имитация через Container)
    hero_section = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Icon(ft.Icons.AUTO_STORIES, size=56, color=ft.Colors.WHITE),
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
                    border_radius=50,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(height=16),
                ft.Text(
                    "QuizBot",
                    size=42,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=8),
                ft.Text(
                    "Преврати любой конспект в интерактивный квиз за секунды",
                    size=16,
                    color=ft.Colors.with_opacity(0.9, ft.Colors.WHITE),
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        ),
        bgcolor=PRIMARY,
        padding=ft.Padding.symmetric(vertical=40, horizontal=24),
        border_radius=ft.BorderRadius.only(bottom_left=24, bottom_right=24),
    )

    # Карточки с описанием возможностей
    features_row = ft.Row(
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.BOLT, size=32, color=PRIMARY),
                        ft.Container(height=8),
                        ft.Text("Быстро", size=15, weight=ft.FontWeight.W_600),
                        ft.Text("Лучшие параметры для скорости", size=12, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=2,
                ),
                bgcolor=CARD_BG,
                border_radius=14,
                padding=16,
                expand=True,
                border=ft.Border.all(1, ft.Colors.GREY_200),
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.PSYCHOLOGY, size=32, color=PRIMARY),
                        ft.Container(height=8),
                        ft.Text("Умно", size=15, weight=ft.FontWeight.W_600),
                        ft.Text("ИИ подберёт вопросы", size=12, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=2,
                ),
                bgcolor=CARD_BG,
                border_radius=14,
                padding=16,
                expand=True,
                border=ft.Border.all(1, ft.Colors.GREY_200),
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.SCHOOL, size=32, color=PRIMARY),
                        ft.Container(height=8),
                        ft.Text("Полезно", size=15, weight=ft.FontWeight.W_600),
                        ft.Text("Проверь свои знания", size=12, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=2,
                ),
                bgcolor=CARD_BG,
                border_radius=14,
                padding=16,
                expand=True,
                border=ft.Border.all(1, ft.Colors.GREY_200),
            ),
        ],
        spacing=12,
    )

    intro_section = ft.Container(
        content=ft.Column(
            [
                hero_section,
                ft.Container(
                    content=features_row,
                    padding=ft.Padding.symmetric(horizontal=16, vertical=16),
                ),
            ],
            spacing=0,
        ),
        visible=True,
    )

    # ============================================
    # КОМПОНЕНТЫ ВВОДА
    # ============================================

    txt_input = ft.TextField(
        value=DEFAULT_TEXT,
        multiline=True,
        min_lines=6,
        max_lines=12,
        hint_text="Вставьте ваш конспект сюда...",
        border_radius=12,
        border_color=ft.Colors.GREY_300,
        focused_border_color=PRIMARY,
        filled=True,
        fill_color=ft.Colors.GREY_50,
        text_size=14,
    )

    txt_question_count = ft.TextField(
        value="5",
        label="Количество вопросов",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=200,
        border_radius=12,
        border_color=ft.Colors.GREY_300,
        focused_border_color=PRIMARY,
        filled=True,
        fill_color=ft.Colors.GREY_50,
        text_size=14,
        text_align=ft.TextAlign.CENTER,
    )

    txt_status = ft.Text("", size=13, color=ft.Colors.GREY_600)

    btn_generate = ft.Button(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.AUTO_AWESOME, size=20),
                ft.Text("Создать квиз", size=16, weight=ft.FontWeight.W_500),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        style=ft.ButtonStyle(
            bgcolor=PRIMARY,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=ft.Padding.symmetric(vertical=18, horizontal=24),
        ),
        width=float("inf"),
        on_click=on_generate,
    )

    # ============================================
    # КОМПОНЕНТЫ КВИЗА
    # ============================================

    txt_question = ft.Markdown(
        "",
        selectable=True,
        extension_set="gitHubWeb",
        latex_scale_factor=1.1,
        latex_style=ft.TextStyle(color=ft.Colors.GREY_900),
        visible=False,
    )

    options_container = ft.Column(spacing=10, visible=False)

    progress_bar = ft.ProgressBar(
        value=0,
        color=PRIMARY,
        bgcolor=ft.Colors.GREY_200,
        visible=False,
        bar_height=6,
    )

    feedback_icon = ft.Icon(ft.Icons.CHECK_CIRCLE, color=SUCCESS, size=22)
    feedback_title = ft.Text("", size=16, weight=ft.FontWeight.BOLD, color=SUCCESS)
    feedback_text = ft.Markdown(
        "",
        selectable=True,
        extension_set="gitHubWeb",
        latex_scale_factor=0.9,
        latex_style=ft.TextStyle(color=ft.Colors.GREY_800),
    )

    feedback_box = ft.Container(
        content=ft.Column(
            [
                ft.Row([feedback_icon, feedback_title], spacing=8),
                ft.Container(height=4),
                feedback_text,
            ],
            spacing=0,
        ),
        bgcolor=SUCCESS_BG,
        border=ft.Border.all(1, SUCCESS),
        border_radius=12,
        padding=14,
        visible=False,
    )

    btn_next = ft.Button(
        content=ft.Row(
            [
                ft.Text("Далее", size=16),
                ft.Icon(ft.Icons.ARROW_FORWARD, size=20),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        style=ft.ButtonStyle(
            bgcolor=PRIMARY,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=ft.Padding.symmetric(vertical=14, horizontal=24),
        ),
        width=float("inf"),
        visible=False,
        on_click=on_next,
    )

    progress_text = ft.Text("", size=13, color=ft.Colors.GREY_600, visible=False)

    # ============================================
    # КАРТОЧКИ
    # ============================================

    input_card = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.EDIT_NOTE, size=22, color=PRIMARY),
                        ft.Text("Введите конспект", size=16, weight=ft.FontWeight.W_600, color=ft.Colors.GREY_800),
                    ],
                    spacing=8,
                ),
                ft.Container(height=12),
                txt_input,
                ft.Container(height=12),
                ft.Row(
                    [
                        txt_question_count,
                        preset_row
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(height=14),
                btn_generate,
                ft.Container(height=8),
                txt_status,
            ],
            spacing=0,
        ),
        bgcolor=CARD_BG,
        border_radius=16,
        padding=20,
        border=ft.Border.all(1, ft.Colors.GREY_200),
        shadow=ft.BoxShadow(
            blur_radius=12,
            color=ft.Colors.with_opacity(0.06, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        ),
        visible=True,
    )

    quiz_card = ft.Container(
        content=ft.Column(
            [
                progress_text,
                ft.Container(height=6),
                progress_bar,
                ft.Container(height=12),
                txt_question,
                ft.Container(height=16),
                options_container,
                ft.Container(height=12),
                feedback_box,
                ft.Container(height=12),
                btn_next,
            ],
            spacing=0,
        ),
        bgcolor=CARD_BG,
        border_radius=16,
        padding=20,
        border=ft.Border.all(1, ft.Colors.GREY_200),
        shadow=ft.BoxShadow(
            blur_radius=12,
            color=ft.Colors.with_opacity(0.06, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        ),
        visible=True,
    )

    # ============================================
    # ОВЕРЛЕЙ ЗАГРУЗКИ — ЧЕРЕЗ page.overlay
    # ============================================
    loading_overlay = ft.Container(
        content=ft.Column(
            [
                ft.ProgressRing(width=64, height=64, stroke_width=5, color=PRIMARY),
                ft.Container(height=24),
                ft.Text(
                    "Генерируем вопросы...",
                    size=22,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.WHITE,
                ),
                ft.Container(height=8),
                ft.Text(
                    "Это может занять 40 секунд до 3 минут",
                    size=14,
                    color=ft.Colors.GREY_300,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.with_opacity(0.92, ft.Colors.BLACK),
        alignment=ft.Alignment.CENTER,
        expand=True,
        visible=False,
    )

    # Добавляем оверлей в page.overlay — он будет поверх ВСЕГО, включая header
    page.overlay.append(loading_overlay)

    # ============================================
    # СБОРКА ИНТЕРФЕЙСА
    # ============================================
    content = ft.Column(
        [
            intro_section,
            ft.Container(
                content=ft.Column(
                    [
                        input_card,
                        ft.Container(height=16),
                        quiz_card,
                    ],
                    spacing=0,
                    scroll=ft.ScrollMode.AUTO,
                ),
                padding=ft.Padding.symmetric(horizontal=16),
            ),
        ],
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    main_container = ft.Container(
        content=content,
        width=720 if not is_mobile else None,
        expand=True,
    )

    layout = ft.Container(
        content=ft.Row(
            [main_container],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
        ),
        bgcolor=BG,
        expand=True,
    )

    page.add(
        ft.Column(
            [layout],
            spacing=0,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
        )
    )


if __name__ == '__main__':
    ft.run(main)
