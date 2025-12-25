import os

def check_if_file_exists(path):
    if os.path.exists(path):
        return f'Файл {path} существует'
    else:
        return f'Файл {path} не найден'
