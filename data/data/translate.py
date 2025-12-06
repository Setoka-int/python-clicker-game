import asyncio
from googletrans import Translator, LANGUAGES

print("-" * 10, "Переводчик", "-" * 10)

async def translate_text_async(text_to_translate, target_lang):
    try:
        translator = Translator()
        translate_result = await translator.translate(text_to_translate, dest=target_lang)

        # Получаем названия языков
        source_lang_name = LANGUAGES.get(translate_result.src, translate_result.src).capitalize()
        target_lang_name = LANGUAGES.get(target_lang, target_lang).capitalize()

        print(f"  > Язык оригинала: {source_lang_name}")
        print(f"  > Перевод на {target_lang_name}: {translate_result.text}\n")

    except Exception as e:
        print(f"Ошибка перевода: {e}")
        print("Проверьте подключение к интернету.\n")

translate_text = lambda text_to_translate, target_lang: asyncio.run(translate_text_async(text_to_translate, target_lang))

# Основной цикл программы
target_language = 'en'

print("Команды:")
print("  /ru - переводить на русский")
print("  /en - переводить на английский")
print("  /код - переводить на другой язык (например: /es, /fr, /de)")
print("  /список - показать все доступные языки")
print("  стоп - выход\n")

while True:
    try:
        text = input("Введите текст или команду: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nРабота завершена.")
        break

    if not text:
        continue

    # Обработка команд
    if text.lower() == "стоп":
        print("Завершение работы...")
        break

    elif text.lower().startswith("/"):
        lang_code = text[1:].lower()

        if text.lower() == "/список":
            print("\nДоступные языки:")
            for code, name in sorted(LANGUAGES.items()):
                print(f"  {code:6} - {name.capitalize()}")
            print()
            continue

        elif lang_code in LANGUAGES:
            target_language = lang_code
            lang_name = LANGUAGES[lang_code].capitalize()
            print(f"✓ Теперь переводим на {lang_name}")
            continue
        else:
            print(f"Неизвестный код языка: {lang_code}")
            print(f"Используйте /список чтобы увидеть все коды")
            continue

    if text:
        translate_text(text, target_language)