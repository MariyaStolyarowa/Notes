import sys
from .validator import validation_mode, validation_operation, validation_id, validation_data, \
    validate_edit, validation_date

MAX_SYMBOLS_TITLE = 30
MAX_SYMBOLS_DATA = 60

# Вывод главного меню
def main_menu() -> None | tuple[int, int]:
    print("""Привет!
Что хочешь сделать:
1 - Просмотреть заметки
2 - Добавить новую заметку
3 - Редактировать заметку
4 - Сохранить заметки
5 - Удалить заметку
0 - Выход. 
""")
# Завершает работу приложения
    mode = validation_mode()
    if mode == 0:
        print('Работа завершена')
        sys.exit()
    return choose_option(mode)

# Подменю "Просмотреть заметки"
def choose_option(main_mode: int) -> None | tuple[int, int]:
    if main_mode in [1]:
        print("""Здесь ты можешь:
1 - Напечатать все заметки в консоль
2 - Напечать все заметки отфильтровав их по дате
3 - Напечатать выбранную заметку в консоль
0 - Вернуться в предыдущее меню
""")
    operation = validation_operation(main_mode)
    if operation in [10]:
        return main_menu()
    return main_mode, operation

# Выбор id заметки
def select_id_ui(data: dict) -> int:
    """ This function is for id selection UI. """
    print("""Введи id заметки.""")
    return validation_id(data)

# Ввод заголовка заметки
def ask_for_title() -> str:
    """ This function is for title getting from user. """
    print(f"""Введи заголовок заметки""")
    return validation_data(MAX_SYMBOLS_TITLE)

# Ввод текста заметки
def ask_about_data() -> str:
    """ This function is for data getting from user. """
    print(f"""Введи заметку""")
    return validation_data(MAX_SYMBOLS_DATA)

# Выводит информацию, что заметка добалена
def note_added_ui() -> None:
    """ This function is for notification about adding a note. """
    print('Заметка добавлена!')

# Выводит информацию, что заметки сохранены
def data_saved(srs: str) -> None:
    """ This function is for UI for telling user that data is saved. """
    print(f"""Заметки сохранены.""")

# Подменю "Редактировать заметку"
def ask_about_data_edit() -> int:
    print("""Выбери,что хочешь отредактировать:
1 - Заголовок
2 - Текст заметки
0 - Вернуться в предыдущее меню
""")
    operation = validate_edit()
    if operation in [30]:
        return main_menu()
    return operation

# Предлагает ввести новый заголовок
def edit_title_note_ui() -> str:
    """ This function is for new title for note. """
    print("""Введи новый заголовок.""")
    return validation_data(MAX_SYMBOLS_TITLE)

# Предлагает ввести новый текст заметки
def edit_data_note_ui() -> str:
    """ This function is for new data for note. """
    print("""Введи новый текст заметки""")
    return validation_data(MAX_SYMBOLS_DATA)

# Выводит информацию, что заметка удалена
def data_deleted(srs: str) -> None:
    """ This function is for UI for telling user that data is deleted. """
    print("Заметка удалена")