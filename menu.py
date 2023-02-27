import work_file
from Notes import *


def main_menu():
    json_list = work_file.file_read()
    #json_list = sorted(json_list['date'])
    notes_list = Notes()
    j = len(json_list) - 1
    while j >= 0:
        notes_list.notes_add(json_list[j]['titl'], json_list[j]['msg'])
        notes_list.get_note(notes_list.get_size() - 1).set_dat(json_list[j]['date'])
        j -= 1
    ex = True
    sort_date(notes_list)
    while ex:
        print(' Заметки \n'
          '1. Просмотр списка заметок \n'
          '2. Просмотр заметки \n'
          '3. Добавление новой заметки \n'
          '4. Редактирование заметки \n'
          '5. Удаление заметки\n'
          '6. Сохранение данных \n'
          '7. Выход')
        choice_action = str(input('Выберите действи, через ввод номера: '))
        if choice_action == '1':
            print_notes(notes_list)
        elif choice_action == '2':
            view_note(notes_list)
        elif choice_action == '3':
            new_add_note(notes_list)
        elif choice_action == '4':
            editing_notes(notes_list)
        elif choice_action == '5':
            rm_note(notes_list)
        elif choice_action == '6':
            work_file.file_writ(notes_list)
        elif choice_action == '7':
            work_file.file_writ(notes_list)
            ex = False
        else:
            print('Введено неверное значение, повторите ввод \n')

def print_notes(notes_list):
    i = 0
    while i < notes_list.get_size():
        print(f"{i+1} {notes_list.get_note(i).titl_info()}")
        i += 1

def new_add_note(notes_list):
    titl_name = str(input('Введите название заметки: '))
    new_msg = str(input('Введите заметку: '))
    notes_list.notes_add(titl_name, new_msg)

def rm_note(notes_list):
    print_notes(notes_list)
    number_note = int(input('Введите номер заметки или 0 для отмены: '))
    if number_note > 0:
        notes_list.notes_rm(number_note-1)
    else:
        return 0

def editing_notes(notes_list):
    print_notes(notes_list)
    number_note = int(input('Введите номер заметки или 0 для отмены: '))
    if number_note > 0:
        print(' Редактирование заметки\n'
              '1. Изменение имени заметки\n'
              '2. Изменение содержания заметки \n'
              '3. Отмена')
        choice_action = str(input('Выберите действи, через ввод номера: '))
        if choice_action == '1':
            new_titl = str(input('Введите новое имя: '))
            notes_list.get_note(number_note-1).set_titl(new_titl)
        elif choice_action == '2':
            new_msg = str(input('Введите новое содержание: '))
            notes_list.get_note(number_note - 1).set_msg(new_msg)
        elif choice_action == '3':
            return 0
    else:
        return 0

def view_note(notes_list):
    print_notes(notes_list)
    number_note = int(input('Введите номер заметки или 0 для отмены: '))
    if number_note > 0:
        notes_list.get_note(number_note-1).display_info()
    else:
        return 0

def sort_date(notes_list):
    for i in range(notes_list.get_size()):
        min_index = i
        j = i + 1
        for j in range(notes_list.get_size()):
            if notes_list.get_note(min_index).get_dat() > notes_list.get_note(j).get_dat():
                min_index = j
        if min_index != i:
            min_date = notes_list.get_note(min_index)
            notes_list.set_note(notes_list.get_note(i), min_index)
            notes_list.set_note(min_date, i)
