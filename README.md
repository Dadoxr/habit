# Проект "Управление Привычками"
О проекте

Проект "Управление Привычками" представляет собой веб-приложение, разработанное для эффективного управления повседневными привычками. Проект включает в себя RESTful API для взаимодействия с привычками пользователей и управления учетными записями.
Установка и запуск

Для запуска проекта, выполните следующие шаги:

1)Клонирование репозитория:
```bash
git clone https://github.com/dadoxr/habit.git
cd habit
```

2)Установка зависимостей:
```bash
pip install -r requirements.txt
```

3)Настройка переменных окрения с файла `.env-sample`


4)Применение миграций:
```bash
python manage.py migrate
```

5)Запуск сервера разработки:
```bash
python manage.py runserver
```

ps) тестирование
```bash
coverage run --source='.' manage.py test
coverage report
```

# API Документация

Документация API доступна через Swagger и Redoc:

- Swagger: http://localhost:8000/docs/
- Redoc: http://localhost:8000/redoc/

## URL-пути

### Config
```python

urlpatterns = [
    # ... (URL-пути для документации, админки и статики)
    path('habit/', include('habit.urls', namespace='habit')),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Привычки
- Habit: http://localhost:8000/habit/...
```python
app_name = HabitConfig.name
urlpatterns = [
    path("", views.HabitPublicListAPIView.as_view(), name="list"),
    path("my/", views.HabitUserListAPIView.as_view(), name="my_list"),
    path("create/", views.HabitCreateAPIView.as_view(), name="create"),
    path("update/<int:pk>", views.HabitUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>", views.HabitDestroyAPIView.as_view(), name="delete"),
]
```

### Пользователи
- Users: http://localhost:8000/users/...
```python
app_name = UsersConfig.name
urlpatterns = [
    path("create/", u_v.UserCreateAPIView.as_view(), name="create"),
    path("token/", views.TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", views.TokenRefreshView.as_view(), name="refresh_token"),
]
```

# Модели
## Привычка

```python
class Habit(models.Model):
    # ... (поля модели привычки)
```
- **Пользователь** — создатель привычки.
- **Место** — место, в котором необходимо выполнять привычку.
- **Время** — время, когда необходимо выполнять привычку.
- **Действие** — действие, которое представляет из себя привычка.
- **Признак** приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
- **Связанная привычка** — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
- **Периодичность (по умолчанию ежедневная)** — периодичность выполнения привычки для напоминания в днях.
- **Вознаграждение** — чем пользователь должен себя вознаградить после выполнения.
- **Время на выполнение** — время, которое предположительно потратит пользователь на выполнение привычки.
- **Признак публичности** — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.


## Пользователь
```python
class User(AbstractUser):
    # ... (поля модели юзер)
```
- Username - отсутствует, переопределен на Email
- Email - почта пользователя
- Telegram Чат ID - ID чата переписки телеграм бота с пользователем

# Валидаторы
- Исключают одновременный выбор связанной привычки и указания вознаграждения.
- Проверяют время выполнения должно быть не больше MAX_TIME_REQUIRED(по-умолчанию 120) секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в MAX_FREQUENCY(по-умолчанию 7) дней.

# Пагинация
- Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.


# Права доступа
- Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
- Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.
