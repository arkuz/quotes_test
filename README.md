### Тестовое задание
Вам предлагается развернуть на сервере или локально любую из выбранных вами БД (но предлагаю выбрать что-то более современное). При помощи браузера Google Chrome под управлением Selenium, собрать данные из таблицы, находящейся тут http://tereshkova.test.kavichki.com в вашу таблицу на сервере, распарсив данные. Далее заполнить некоторыми данными таблицу на сайте «Терешкова», сравнить ее результаты с вашей БД и с теми данными, которые вы на самом деле вводили и вывести результат об изменениях. + можно несколько функциональных UI тестов на ваше усмотрение по этой таблице на сайте. Код желательно написать на Python. Результат можно запаковать или выложить в ББ или в Гит. На ваше усмотрение.

### Описание
 - В качестве СУБД выбрана MySQL. Дамп в репозитории - [dump_tereshkova_table.sql](https://github.com/arkuz/quotes_test/blob/master/dump_tereshkova_table.sql).
 - Так же в репозитории есть драйвер для браузера Chrome - [chromedriver.exe](https://github.com/arkuz/quotes_test/blob/master/chromedriver.exe)
 - Отчет о прохождении тестов - [Test Results - Unittests_in_MainPageTests_py.html](https://github.com/arkuz/quotes_test/blob/master/Test%20Results%20-%20Unittests_in_MainPageTests_py.html)

### Установка
```bash
pip install virtualenv
git clone https://github.com/arkuz/quotes_test
cd quotes_test
virtualenv env
cd env/scripts
activate.bat
pip install -r requirements.txt
cd ../..
```

### Запуск
```bash
python MainPageTests.py
```
или
```bash
python -m unittest -v MainPageTests.py
```

### Набор тестов
1. `test_add_new_row` - проверяет добавление новой записи в таблицу
2. `test_delete_last_added_row` - проверяет удаление последней добавленной записи из таблицы
3. `test_delete_first_row` - проверяет удаление первой записи из таблицы
4. `test_reset_form` - проверяет очистку полей формы добавления записи
5. `test_compare_tables_data` - собирает данные из таблицы, в таблицу в БД, распарсив данные. Далее заполняет некоторыми данными таблицу на сайте «Терешкова», сравнивает ее результаты с таблицей в БД и в случае, если на сайте количество записей больше чем в БД выводит результат об изменениях

