# Перспективное преобразование изображения
Утилита для быстрой обработки фотографии.
Основано на [статье](https://nuancesprog.ru/p/7590/), но сокращена часть по обработке изображения.
Возможно, будет что-то добавлено позже.
Зато есть gui с ручным поиском углов!
## Запуск
1. Установить [Python](https://www.python.org/downloads/), если его нет
2. Обновится и загрузить библиотеки

    pip install numpy

    pip install opencv-python

    pip install PyQt5

3. Перейти в папку проекта и запустить main.py

    python main.py

## Генерация exe для Windows (по желанию)
У меня получился exe файл размером 80Мб, который запускается несколько секунд. Учитывая функциональность приложения, оно того не стоит...

    pip install pyinstaller
    mkdir build
    cd build
    pyinstaller.exe --onefile --noconsole  ..\main.py

