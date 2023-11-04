from models import Author, Quote
import connect

# Функція для пошуку цитат за тегом або ім'ям автора
def search_quotes(query):
    if query.startswith('name:'):
        author_name = query[len('name: '):]
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            return [quote.quote for quote in quotes]
        else:
            return []

    elif query.startswith('tag:'):
        tag = query[len('tag: '):]
        quotes = Quote.objects(tags=tag)
        return [quote.quote for quote in quotes]

    elif query.startswith('tags:'):
        tags = query[len('tags: '):].split(',')
        quotes = Quote.objects(tags__in=tags)
        return [quote.quote for quote in quotes]

    elif query == 'exit':
        return "Дякую, що використовували наш скрипт. До побачення!"

    else:
        return "Невідома команда. Будь ласка, введіть правильну команду."

if __name__ == "__main__":

    while True:
        user_input = input("Введіть команду (наприклад, 'name: Steve Martin'): ")
        if user_input == 'exit':
            break
        
        result = search_quotes(user_input)
        if isinstance(result, list):
            for quote in result:
                print(quote)
        else:
            print(result)
