from .logger import logging

AVAILABLE_MODES_MAIN_MENU = 6
MUST_BE_INTEGER = 'Некорректный ввод! Это должно быт целое число.'
INCORRECT_DATE = 'Дата введена в неверном формате или не существует!'
INCORRECT_INPUT = 'Некорректный ввод! Выберите доступный.'
NO_VALID_FILE = 'Корректный файл отсутствует.'

# Проверка пользовательского ввода в главном меню 
def validation_mode() -> int:
    while True:
        try:
            main_menu_mode = int(input('Мне нужно: '))
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        if main_menu_mode in range(AVAILABLE_MODES_MAIN_MENU):
            if main_menu_mode == 0:
                logging.info('Finished work from main menu.')
            else:
                logging.info(f'Main mode of interface = {main_menu_mode}')
            return main_menu_mode
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)

# Проверка пользовательского ввода для режима работы
def validation_operation(main_menu_mode: int) -> int:
    match main_menu_mode:
        case 1:
            return validate_read()
        case 2:
            return 21
        case 3:
            return 31
        case 4:
            return 41
        case 5:
            return 51
        case _:
            logging.INFO(INCORRECT_INPUT)

# Проверка пользовательского ввода типа операции чтения данных
def validate_read() -> int:
    number_of_available_modes = 4
    while True:
        try:
            operation_type = int(input('Мне нужно: '))
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        if operation_type in range(number_of_available_modes):
            logging.info(f'Operation code for read = {operation_type + 10}')
            return operation_type + 10
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)
# Проверка корректности даты и наличия по данной дате заметок 
def validation_date(data: dict)-> str:
    print("Введите дату в формате: дд-мм-гггг")
    while True:
        try:
            available_date = [data['notes'][i]['date'] for i in range(len(data['notes']))]
            selected_date = str(input('Введите дату: '))
            if selected_date in available_date:
                logging.info(f'{selected_date = }')
                return selected_date
            else: selected_date = str(input('Заметок на данную дату нет или дата введена в неверном формате.Нажмите любую клавишу, чтобы повторить ввод'))
        except ValueError as err:
            print(INCORRECT_DATE)
            logging.exception(err)
            continue
        except TypeError as error:
            print('Файл с данными поврежден.')
            logging.exception(error)
            return -1
        except KeyError as error:
            print(NO_VALID_FILE)
            logging.exception(error)
            break;

# Проверка id заметки, введенного пользователем
def validation_id(data: dict) -> int:
    while True:
        try:
            available_ids = [data['notes'][i]['id'] for i in range(len(data['notes']))]
            selected_id = int(input('id заметки: '))
            if selected_id in available_ids:
                logging.info(f'{selected_id = }')
                return selected_id
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        except TypeError as error:
            print('Файл с данными поврежден.')
            logging.exception(error)
            return -1
        except KeyError as error:
            print(NO_VALID_FILE)
            logging.exception(error)
            break;
        print('Неверный ID!')
        logging.exception('Incorrect ID!')

# Проверка данных введенных пользователем для заполнения заметки
def validation_data(max_symbols: int) -> str:
    while True:
        try:
            fill_data = input(f'Допустимо максимум {max_symbols} символов: ')
        except Exception as err:
            print('Что-то не так. Попробуй еще раз')
            logging.exception(err)
            continue
        if len(fill_data) in range(max_symbols + 1):
            logging.info(f'Entered data for note {fill_data = } with length = {len(fill_data)}.')
            return fill_data
        print(f'Должно быть максимум {max_symbols} символов.')
        logging.info(f'Entered data for note {fill_data = } with length = {len(fill_data)}.')

# Проверка пользовательского ввода для выбора типа операции редактирования
def validate_edit() -> int:
    number_of_available_modes = 3
    while True:
        try:
            operation_type = int(input('Мне нужно: '))
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        if operation_type in range(number_of_available_modes):
            logging.info(f'Operation code for read = {operation_type + 30}')
            return operation_type + 30
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)