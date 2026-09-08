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
    prompt = f"""
    Твоя задача — создать РОВНО 5 (ПЯТЬ) вопросов с 4 вариантами ответов на основе текста.

    ТРЕБОВАНИЯ:
    1. Должно быть РОВНО 5 вопросов. Не больше и не меньше.
    2. Каждый вопрос должен иметь 4 варианта ответа (A, B, C, D).
    3. Ответ должен быть ТОЛЬКО JSON массивом из 5 объектов.
    4. НЕ ДОБАВЛЯЙ пояснения, вступления или заключения.

    ФОРМАТ:
    [
        {{"question": "вопрос 1", "options": ["A. ответ", "B. ответ", "C. ответ", "D. ответ"], "correct": "A"}},
        {{"question": "вопрос 2", "options": ["A. ответ", "B. ответ", "C. ответ", "D. ответ"], "correct": "B"}},
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

    except Exception as e:
        print('Ошибка:', e)
