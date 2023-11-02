while True:
    user_input = input("Введіть команду (наприклад, 'name: Steve Martin', 'tag: life', 'tags: life,live', 'exit'): ").strip()
    command, value = user_input.split(': ', 1)

    if command == 'exit':
        break

    if command == 'name':
        quotes = Quote.objects(author__name=value)
    elif command == 'tag':
        quotes = Quote.objects(tags=value)
    elif command == 'tags':
        tags = value.split(',')
        quotes = Quote.objects(tags__in=tags)
    else:
        print("Невідома команда.")
        continue

    if quotes:
        for quote in quotes:
            print(f"{quote.author.name}: {quote.text}, Tags: {', '.join(quote.tags)}")
    else:
        print("Цитати не знайдено.")
