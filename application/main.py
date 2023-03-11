from datetime import datetime
from .logger import logging
from .user_interface import main_menu, select_id_ui, ask_for_title, ask_about_data, note_added_ui, \
    data_saved, ask_about_data_edit, edit_title_note_ui, \
    edit_data_note_ui, data_deleted
from .file_worker import write_to_file, load_from_file
from .data_checker_and_filler import check_data_storage, DEFAULT_SRC, fill_new_note, update_note, \
    note_deletion
from .print import print_all, print_filter_date, print_id_date, \
    print_id_selection

# Вызов главного меню пока не выбран выход из приложения
def entrance_point() -> None:
    logging.info('Start program.')
    check_data_storage()
    operation_type, operation_code = main_menu()
    logging.info(f'Operation chosen = {operation_type}, operation code = {operation_code}')
    main_handler(operation_code)
    logging.info('Session finish')
    if operation_type != 0:
        entrance_point()

# Обработка главного меню
def main_handler(operation_code: int) -> None:
    if str(operation_code)[0] in ('1'):
        handler_for_read(operation_code)
    elif str(operation_code)[0] in ('2'):
        handler_for_add()
    elif str(operation_code)[0] in ('3'):
        handler_for_edit()
    elif str(operation_code)[0] in ('4'):
        handler_for_save()
    elif str(operation_code)[0] in ('5'):
        handler_for_delete()
