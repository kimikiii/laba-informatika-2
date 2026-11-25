import os
from datetime import datetime
from PIL import Image, ImageFilter, ImageOps


def write_log(filename, filter_name, status):
    log_path = os.path.join('Lab2_Media', 'logs', 'history.txt')
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    log_line = f'[{now}] Файл: {filename} | Фильтр: {filter_name} | Статус: {status}\n'

    with open(log_path, 'a', encoding='UTF-8') as log_file:
        log_file.write(log_line)



filename = input('Введите имя файла для обработки (например, image1.jpg или image2.png): ').strip()
input_path = os.path.join('Lab2_Media', 'data', 'input', filename)
output_path = os.path.join('Lab2_Media', 'data', 'output', 'result.jpg')

filter_name = 'Фильтр Гаусса + Робастная коррекция'

try:
    with open(input_path, 'rb'):
        pass
    if not os.access(input_path, os.W_OK):
        raise PermissionError
    with Image.open(input_path) as img:
        img = img.convert('RGB')
        img = img.filter(ImageFilter.GaussianBlur(radius=2))
        img = ImageOps.autocontrast(img, cutoff=5)
        img.save(output_path)

    print(f'Готово! Результат сохранён в {output_path}')
    write_log(filename, filter_name, 'Успешно')

except PermissionError:
    print(f'Ошибка: Нет прав на чтение файла {filename}. Обратитесь к администратору')
    write_log(filename, filter_name, 'Ошибка доступа')

except FileNotFoundError:
    print('Ошибка: Файл не найден')
    write_log(filename, filter_name, 'Файл не найден')

except IOError:
    print(f'Ошибка: Нет прав на чтение файла {filename}. Обратитесь к администратору')
    write_log(filename, filter_name, 'Ошибка доступа')