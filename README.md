# **Парсер PEP на базе фреймворка Scrapy**
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=013220)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=013220)](https://scrapy.org/)

Парсер, собирающий информацию с сайта [https://peps.python.org/](https://peps.python.org/)<br/>
Вся собранная информация сохраняется в файлы с расширением **.csv** в директории **results**:
- pep_<date.time>.csv - список всех PEP: номер, название, статус;
- status_summary_<date.time>.csv - сводка по статусам PEP: количество документов в каждом статусе на сайте, а также общее количество всех документов.

## Автор проекта:
Валерий Шанкоренко<br/>
Github: [Valera Shankorenko](https://github.com/valerashankorenko)<br/>
Telegram: [@valeron007](https://t.me/valeron007)<br/>
E-mail: valerashankorenko@yandex.by<br/>

## Стек технологий
- [Python](https://www.python.org/)
- [Scrapy](https://scrapy.org/)

## Как запустить проект:
1. Клонировать репозиторий и перейти в его директорию в командной строке:
```shell
git clone git@github.com:valerashankorenko/scrapy_parser_pep.git
```
```shell
cd scrapy_parser_pep
```
2. Cоздать и активировать виртуальное окружение:
 - для Linux/MacOS
```shell
python3 -m venv venv
source venv/bin/activate
```
- для Windows
```shell
python -m venv venv
source venv/Scripts/activate
```
3. Обновить пакетный менеджер pip
```shell
python3 -m pip install --upgrade pip
```
4. Установить зависимости из файла requirements.txt:
```shell
pip install -r requirements.txt
```
5. Запускаем парсер pep.
```shell
scrapy crawl pep
```
