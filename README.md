# Jarvis-COS Minimal
Минимальная версия Jarvis COS для CPU + 8GB RAM.
## ?? Quick Start

```bash
# 1. Клонирование репозитория
git clone https://github.com/username/Jarvis-COS-Minimal.git
cd Jarvis-COS-Minimal

# 2. Установка зависимостей
pip install -r requirements.txt

# 3. Запуск основной программы
python src/main.py

# 4. Пример команд в консоли
Jarvis-COS> chat
Jarvis-COS> schedule
Jarvis-COS> think
Jarvis-COS> status
Jarvis-COS> exit
## ?? Основные файлы и назначение

| Путь / Файл | Назначение |
|--------------|-------------|
| `src/main.py` | Точка входа. Управляет модулями Dialog, Scheduler, Logic. |
| `src/core/memory_engine.py` | Хранилище и обработка данных памяти. |
| `src/core/process_core.py` | Управление процессами и потоками системы. |
| `src/core/command_parser.py` | Разбор пользовательских команд. |
| `src/core/scheduler.py` | Базовый планировщик задач. |
| `src/core/security_shell.py` | Безопасность и контроль исполнения. |
| `src/core/system_log.py` | Логирование действий и ошибок. |
| `src/modules/dialog/dialog.py` | Модуль диалога и взаимодействия с пользователем. |
| `src/modules/logic/logic.py` | Модуль логического мышления (I1/I2). |
| `src/modules/magic_field.py` | Интуитивный модуль "Magic Field" (7D-практики). |
| `src/modules/vision/vision_adapter.py` | Визуальная подсистема / адаптер восприятия. |
| `src/modules/scheduler/scheduler.py` | Планировщик задач верхнего уровня. |
| `src/modules/intuition/intuition_layer.py` | Модуль интуитивного слоя. |
| `tests/test_core.py` | Набор тестов для проверки ядра и логики. |
```bash
# Запуск тестов
pytest
Ожидаемый результат:
в консоли появятся строки с успешным прохождением тестов (test passed), что подтверждает корректность работы ядра и модулей.
```markdown
## ? FAQ

**Как добавить новый модуль?**  
Создайте папку в `src/modules/`, добавьте свой файл `new_module.py` с классом `NewModule`, зарегистрируйте его в `src/main.py` в словаре `modules`.

**Как сделать pull-request?**  
1. Сделайте форк репозитория.  
2. Создайте ветку: `git checkout -b feature/my-feature`.  
3. Внесите изменения и выполните коммит.  
4. Отправьте Pull Request с описанием изменений.

**Куда писать баги и предложения?**  
Используйте вкладку **Issues** на GitHub-странице проекта или отправьте письмо на адрес, указанный в разделе "Contacts" README.md.
