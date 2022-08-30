import os, datetime
from pars import habr_info


def logger(old_func):
    def new_func(*args, **kwargs):
        filename = os.fspath("./LOG/INFO.log")
        pathtolog = os.path.abspath(filename)
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d время %H-%M-%S')
        result = old_func(*args, **kwargs)

        if not os.path.exists('LOG'):
            os.mkdir('LOG')

        with open(filename, 'a', encoding='utf-8') as file:

            text = f"\nТрям!!!\nПуть до файла:\n{pathtolog}"
            text += f"\n** [INFO] — {current_datetime}"
            text += f"\nВызвана функция {old_func.__name__} с аргументами: {args}, {kwargs}.\nРезультат: {result}"
            text += "\n" + "=" * 88 + "\n"

            file.write(text)

            print(f"Лог успешно записан:\n{pathtolog}")

    return new_func


@logger
def summa(a, b):
    return a + b


@logger
def new_post():
    post = habr_info()
    posts = []
    for date, post_info in post.items():
        posts.append(f"{date} - {' | '.join(post_info)}")

    return posts


if __name__ == '__main__':
    summa(78, 87)
    new_post()
