from datetime import datetime
from prettytable import PrettyTable

from application.validator import validation_date
from .logger import logging

FILTERED_PRINT_TIP = 'Filtered by date notes printed as table in console.'
SORTED_PRINT_TIP = 'Sorted by date notes printed as table in console.'
NO_VALID_FILE = 'No valid file for reading.'

# Печать всех заметок
def print_all(data_notes: dict) -> None:
    try:
        table = PrettyTable()
        table.field_names = list(data_notes['notes'][0].keys())
        for item in data_notes['notes']:
            table.add_row([item[i] for i in table.field_names])
        print(table)
        logging.info('Notes printed as table in console.')
    except TypeError as error:
        print(error)
        logging.exception(error)
    except KeyError as err:
        print(NO_VALID_FILE)
        logging.exception(err)

# Печать заметок по выбранной дате
def print_filter_date(data_notes: dict) -> None:
    date = validation_date(data_notes)
    filtered_notes = []
    for item in data_notes['notes']:
        if item['date'] == date:
            filtered_notes.append(item)
       
    try:
        table = PrettyTable()
        table.field_names = list(filtered_notes[0].keys())
        
        for item in filtered_notes:
            table.add_row([item[i] for i in table.field_names])
        print(table)
        logging.info(FILTERED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
    except KeyError as error:
        print(NO_VALID_FILE)
        logging.exception(error)

# Вывод id заметки и Заголовка в консоль, отсортированных по дате
def print_id_date(data_notes: dict) -> None:
    
    try:
        sorted_notes = sorted(data_notes['notes'], key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'), reverse=True)
        table = PrettyTable()
        all_fields = list(sorted_notes[0].keys())
        table.field_names = [_ for _ in all_fields if _ in ['id', 'title']]
        for item in sorted_notes:
            table.add_row([item[i] for i in table.field_names])

        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
    except KeyError as error:
        print(NO_VALID_FILE)
        logging.exception(error)
    except IndexError as index_err:
        print('Nothing to delete!')
        logging.exception(index_err)
        return -1

# Печать заметки по id
def print_id_selection(data_notes: dict, idx: int) -> None:
    
    try:
        table = PrettyTable()
        table.field_names = list(data_notes['notes'][0].keys())

        for item in data_notes['notes']:
            if item.get('id') == idx:
                table.add_row([item[i] for i in table.field_names])

        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
    except KeyError as error:
        print(NO_VALID_FILE)
        logging.exception(error)
