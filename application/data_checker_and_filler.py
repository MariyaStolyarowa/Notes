from os import path, makedirs
from typing import Any
from .logger import logging
from .file_worker import write_to_file

DEFAULT_DIRNAME = './Data_store/'
DEFAULT_FILENAME = 'notes.json'
DEFAULT_EXTENSION = '.json'
DEFAULT_SRC = DEFAULT_DIRNAME + DEFAULT_FILENAME
TEST_DATA_JSON = {"notes": [
    {"id": 1, "title": "Направить контракт", "data": "Направить проект контракта поставщику", "date": "07-03-2023"},
    {"id": 2, "title": "Составить претензию", "data": "Включить пени и штраф", "date": "10-03-2023"},
    {"id": 3, "title": "Позвонить в ЦОЗ", "data": "Обсудить протокол", "date": "10-03-2023"}]
    }

# Для хранения данных
def check_data_storage() -> None:
    logging.info('Checking data.')
    check_folder()
    check_notes_json()
    logging.info('Data checked.')

# Проверка существования папки для сохранения файла с заметками
def check_folder() -> None:
    try:
        if not path.exists(DEFAULT_DIRNAME):
            makedirs(DEFAULT_DIRNAME)
            logging.info(f'Folder {DEFAULT_DIRNAME} created for data storage.')
    except OSError as error:
        print(f'Дирректория {DEFAULT_DIRNAME} не может быть создана', error)
        logging.exception(f'cannot create {DEFAULT_DIRNAME} directory', error)

# Проверка существования файла для записи заметок
def check_notes_json() -> None:
    try:
        if not path.exists(DEFAULT_SRC):
            fill_notes()
            logging.info(f'Notes {DEFAULT_FILENAME} file created in data strage {DEFAULT_DIRNAME}.')
    except OSError as error:
        print(f'Файл {DEFAULT_FILENAME} не может быть создан', error)
        logging.exception(f'Cannot create {DEFAULT_FILENAME} file', error)

# Зполнение тестовыми данными
def fill_notes() -> None:
    try:
        write_to_file(TEST_DATA_JSON, DEFAULT_SRC)
    except Exception as fillerr:
        print(fillerr)
        logging.exception(fillerr)
    logging.info(f'Notes filled in file {DEFAULT_FILENAME}.')

# Заполнение новой заметки
def fill_new_note(data: dict, note_id: int,
                  note_title: str, note_data: str, date: str) -> dict:
    new_note = fill_dict(('id', note_id), ('title', note_title), ('data', note_data), ('date', date))
    data['notes'].append(new_note)
    return data

# Создание новой заметки
def fill_dict(*args: Any) -> dict:
    return {arg[0]: arg[1] for arg in args}

# Выбор что редактировать
def update_note(mode: int, data: str, notes: dict, id_note: int) -> dict:
    if mode in [31]:
        return update_title(data, notes, id_note)
    if mode in [32]:
        return update_data(data, notes, id_note)

# Изменение заголовка
def update_title(new_title: str, notes: dict, id_note: int) -> dict:
    for i in range(len(notes['notes'])):
        if notes['notes'][i].get('id') == id_note:
            notes['notes'][i]['title'] = new_title
            return notes

# Изменение текста заметки
def update_data(new_data: str, notes: dict, id_note: int) -> dict:
    for i in range(len(notes['notes'])):
        if notes['notes'][i].get('id') == id_note:
            notes['notes'][i]['data'] = new_data
            return notes

# Удаление заметки по id
def note_deletion(note_id: int, notes: dict) -> dict:
    for i in range(len(notes['notes'])):
        if notes['notes'][i].get('id') == note_id:
            new_notes = notes['notes'][:i] + notes['notes'][-1:i:-1]
    notes['notes'] = new_notes
    return notes