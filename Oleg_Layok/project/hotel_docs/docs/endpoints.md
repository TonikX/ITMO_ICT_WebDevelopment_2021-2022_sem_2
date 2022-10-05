# HotelManager
### Get started

```python manage.py runserver```

```mkdocs serve```

## Available endpoints

###Authentication request
* `/auth/token/login/` - Авторизация
#####Пример POST:
```
{
    "password": "root",
    "username": "root"
}
```
#####Результат:

```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "auth_token": "41asdhu12h3jsadkh37721y38ashdjwadu23h4kjashd"
}
```

* `/auth/token/logout/` - Выход
#####Пример POST:
```
{}
```
#####Результат:
```
HTTP 204 No Content
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept
```

* `/auth/users` - Регистрация
#####Пример POST:
```
{
    "email": "example@gmail.com",
    "username": "example",
    "password": "exampleexample"
}
```
#####Результат:
```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "example@gmail.com",
    "username": "example",
    "id": 9
}
```

###Get request
* `/admins` - Получить информацию о всех администраторах
* `/admins/{pk}` - Получить информацию о конкретном администраторе

* `/guests` - Получить информацию о всех гостях
* `/guests/{pk}` - Получить информацию о конкретном госте
* `/guests?check_in_date_after={check_in_date}&check_in_date_before={check_in_date}` - Получить отфильтрованный список гостей в указанном диапазоне дат заезда
* `/guests?check_out_date_after={check_out_date}&check_out_date_before={check_out_date}` - Получить отфильтрованный список гостей в указанном диапазоне дат выезда
* `/guests?search={name, passport_number}` - Найти гостя с указанным именем или номером паспорта
* `/guests?ordering={check_in_date,check_out_date}` - Получить сортированный список гостей по дате заезда или дате выезда
* `/guests?page={page}` - Получить конкретную страницу списка гостей

* `/rooms` - Получить информацию о всех комнатах
* `/rooms/{pk}` - Получить информацию о конкретной комнате
* `rooms/type/<int:type>/` - Получить отфильтрованный список комнат по указанному типу
* `rooms/floor/<int:fl_g>/<int:fl_l>/` - Получить отфильтрованный список комнат в находящихся межу указанными этажами
* `rooms/floor-room-type/<int:floor>/<int:type>/` - Получить отфильтрованный список комнат с конкретным типом на конкретном этаже
* `/rooms?price_min={price}&price_max={price}` - Получить отфильтрованный список комнат в указанном диапазоне цен
* `/rooms?number_min={number}&number_max={number}` - Получить отфильтрованный список комнат в указанном диапазоне номеров
* `/rooms?type={type}` - Получить отфильтрованный список комнат c указанным типом
* `/rooms?search={number}` - Найти комнату с указанным номером
* `/rooms?ordering={number,price}` - Получить сортированный список комнат по номеру или цене
* `/rooms?page={page}` - Получить конкретную страницу списка комнат

* `/staff` - Получить информацию о всех членах персонала
* `/staff/{pk}` - Получить информацию о конкретном члене персонала

* `/cleaning` - Получить информацию о всех уборках
* `/cleaning/{pk}` - Получить информацию о конкретной уборке
* `/cleaning?room_number={room__number}` - Получить отфильтрованный список уборок в указанной комнате
* `/cleaning?staff_name={staff__name}` - Получить отфильтрованный список уборок сделаный указаным уборщиком
* `/cleaning?search={date_time,room__number,staff__name}` - Найти уборку по указанной дате, номеру комнаты или имени уборщика
* `/cleaning?ordering={date_time}` - Получить сортированный список уборок по дате уборки

###Post request
* `/upload-room-picture` - Загрузить фотографию конкретной комнаты
* `/upload-files` - Загрузить несколько фотографий комнат
* `/admins` - Добавить администратора
* `/rooms` - Добавить номер
* `/guests` - Добавить гостя
* `/staff` - Добавить члена персонала
* `/cleaning` - Добавить уборку

###Put/Patch request
* `/admins/{pk}` - Изменить информацию о конкретном администраторе
* `/guests/{pk}` - Изменить информацию о конкретном госте
* `/rooms/{pk}` - Изменить информацию о конкретной комнате
* `/staff/{pk}` - Изменить информацию о конкретном члене персонала
* `/cleaning/{pk}` - Изменить информацию о конкретной уборке


###Delete request
* `/admins/{pk}` - Удалить информацию о конкретном администраторе
* `/guests/{pk}` - Удалить информацию о конкретном госте
* `/rooms/{pk}` - Удалить информацию о конкретной комнате
* `/staff/{pk}` - Удалить информацию о конкретном члене персонала
* `/cleaning/{pk}` - Удалить информацию о конкретной уборке