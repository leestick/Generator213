__author__ = 'dmitryh'
import os


def filenames_collect():
    """Определение БИК из имени файла"""
    path = 'SYS\\'
    dict_of_param = {}
    # чтение записей
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            if entry.is_file():
                if entry.name[0:3] == 'GOZ':
                    dict_of_param[entry.name[0:5]]=entry.name
                elif entry.name[0:3] == 'SKO':
                    dict_of_param[entry.name[0:9]]=entry.name
    return dict_of_param


