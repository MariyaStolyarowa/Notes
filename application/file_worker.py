import json
from .logger import logging


def write_to_file(data: dict, source: str) -> None:
    """ This function is for writing data to the file. """
    try:
        with open(source, 'w', encoding='utf-8') as file_json:
            json.dump(data, file_json, ensure_ascii=False)
        logging.info(f'Write data to {source}')
    except FileNotFoundError as err:
        print(f'Source {source} not found. Aborting')
        logging.exception(err)
        return -1
    except OSError as err:
        print(f'OS error occurred trying to open {source}')
        logging.exception(err)
        return -1
    except Exception as error:
        print(f'Unexpected error opening {source} is', repr(error))
        logging.exception(error)
        return -1


def load_from_file(source: str) -> dict:
    """ This function is for loading data from the file. """
    try:
        with open(source, encoding='utf-8') as file:
            data = json.load(file)
        logging.info(f'Read data from {source}')
        return data
    except json.decoder.JSONDecodeError as jsonerr:
        print(jsonerr)
        logging.exception(jsonerr)
        return -1
    except FileNotFoundError as err:
        print(f'Source {source} not found. Aborting')
        logging.exception(err)
        return -1
    except OSError as oserr:
        print(f'OS error occurred trying to open {source}')
        logging.exception(oserr)
        return -1
    except Exception as excerr:
        print(f'Unexpected error opening {source} is', repr(excerr))
        logging.exception(excerr)
        return -1
