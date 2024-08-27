# Документация по запуску проекта FastAPI

## 1. Создание и активация виртуального окружения

Для изоляции зависимостей вашего проекта создайте виртуальное окружение. Это поможет избежать конфликтов между зависимостями разных проектов.

### Создание виртуального окружения

Откройте терминал и выполните следующие команды:

#### Для Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Для macOS и Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Установка зависимостей
После активации виртуального окружения установите зависимости проекта из файла `requirements.txt`. Если у вас ещё нет файла `requirements.txt`, создайте его в корне проекта с необходимыми зависимостями.

### Установка зависимостей

Выполните следующую команду для установки зависимостей:
```bash
pip install -r requirements.txt
```

## 4. Запуск приложения

Для запуска приложения FastAPI выполните следующую команду:
```bash
python3 main.py
```

## 5. Проверка работы приложения

После запуска команды вы должны увидеть вывод, аналогичный следующему:
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Вы также можете проверить автоматически сгенерированную документацию API по следующим адресам:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)
