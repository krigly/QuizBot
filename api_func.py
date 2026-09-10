from openai import OpenAI
import json

from dotenv_func import get_api_key


def initial_client(api_key):
    if not api_key:
        raise Exception('API ключ не найден!')

    client = OpenAI(
        api_key=api_key,
        base_url='https://api.odirouter.ai/v1'
    )

    return client

def generate_quiz(text, client):
    prompt = rf"""
    Твоя задача — создать РОВНО 5 (ПЯТЬ) вопросов с 4 вариантами ответов на основе текста.

    ТРЕБОВАНИЯ:
    1. Должно быть РОВНО 5 вопросов. Не больше и не меньше.
    2. Каждый вопрос должен иметь 4 варианта ответа (A, B, C, D).
    3. Ответ должен быть ТОЛЬКО JSON массивом из 5 объектов.
    4. НЕ ДОБАВЛЯЙ пояснения, вступления или заключения.
    5. Напиши для каждого варианта ответа краткое пояснение почему он верный или неверный
    6. ═══════════════════════════════════════
        ПРАВИЛА ЗАПИСИ ФОРМУЛ (LaTeX)
        ═══════════════════════════════════════
        
        ВСЕ математические формулы и физические величины записывай ТОЛЬКО в LaTeX.
        Формулы оборачивай в ОДИНАРНЫЕ знаки доллара: $формула$
        
        ❌ НЕПРАВИЛЬНО (обычный текст):
           "v = S/t"
           "Q = cm * ΔT"
           "F = m*g"
           "ΔT"
           "v²"
        
        ✅ ПРАВИЛЬНО (LaTeX):
           "$v = \frac{{S}}{{t}}$"
           "$Q = cm\Delta T$"
           "$F = mg$"
           "$\Delta T$"
           "$v^2$"
        
        ОБЯЗАТЕЛЬНЫЕ ПРАВИЛА LATEX:
        - Дроби пиши через \frac{{числитель}}{{знаменатель}}
        - Греческие буквы через \Delta, \alpha, \beta, \gamma, \pi и т.д.
        - Степени через ^, например: $v^2$, $m^3$
        - Индексы через _, например: $S_1$, $v_0$
        - Умножение просто подряд: $mg$, $cm$, не $m \cdot g$
        - НЕ ставь пробелы сразу после $ и перед $: пиши $v = mg$, а НЕ $ v = mg $\
    7. НЕ делай все вопросы про формулы! Вопросы должны быть РАЗНЫМИ по типу: определения, термины и другое. Разных типов вопросов должно быть примерно ОДИНАКОВОЕ количество.
    

    ФОРМАТ:
    [
        {{"question": "вопрос 1", "options": ["A. ответ", "B. ответ", "C. ответ", "D. ответ"], "correct": "A", "description": "Пояснение"}},
        {{"question": "вопрос 2", "options": ["A. ответ", "B. ответ", "C. ответ", "D. ответ"], "correct": "B", "description": "Пояснение"}},
        ...
    ]
    ТЕКСТ:
    {text}
    """

    try:
        resp = client.chat.completions.create(
            model='free-qwen3.5-flash',
            messages=[{'role': 'user', "content": prompt}],
            temperature=0.7,
            response_format={'type': 'json_object'}
        )

        content = resp.choices[0].message.content
        print(content)

        try:
            return json.loads(content)

        except json.JSONDecodeError as e:
            print('Ошибка парсинга: ', e)

    except Exception as e:
        print('Ошибка:', e)
