from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

promt = """
Always answer in Russian. Вы - преподаватель программирования. Анализируйте код по критериям:
1. Корректность выполнения задачи
2. Наличие ошибок выполнения/безопасности
3. Качество кода и читаемость
4. Орфография/форматирование

Формат ответа:
- Всегда указывайте номер строки в поле 'line' (начиная с 0) или null если комментарий ко всему коду
- Не включайте номер строки в текст комментария
- Для критических ошибок обязательно добавляйте example_code
"""

task_response_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "task_response_schema",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "comments": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string",
                                "description": "Текст комментария",
                                "maxLength": 150
                            },
                            "type": {
                                "type": "string",
                                "enum": ["comment", "improvement", "typo", "critical"],
                                "description": "Уровень важности комментария"
                            },
                            "line": {
                                "type": ["integer", "null"],
                                "nullable": True,
                                "description": "Номер строки (начиная с 0), null если неприменимо"
                            },
                            "example_code": {
                                "type": "string",
                                "description": "Пример исправления (опционально)",
                                "maxLength": 100
                            }
                        },
                        "required": ["text", "type", "line"]
                    }
                }
            },
            "required": ["comments"]
        }
    }
}
