# Что будем создавать?
# Консольный менеджер задач (To-Do List).

# Пользователь вводит команды: add (добавить), list (показать), done (выполнить), delete (удалить), exit (выход).

# Программа хранит задачи и управляет ими.

# Архитектура проекта:

# main.py — «Дирижер». Отвечает за общение с пользователем (input/print) и главный цикл.

# tasks.py — «Мозг». Хранит список задач и содержит функции для их изменения.



def add(task_list,task):
    if not task in task_list:
        task_list[task] = {}
        task_list[task]['status'] = False
    return task_list

def showlist(task_list):
    s = ''
    for k,v in task_list.items():
        s += f'{k}:\n'
        for i,j in v.items():
            s += f"\t{i}:{j}\n"
    return s

def delete_task(task_list,task):
    if task in task_list:
        del task_list[task]
    return task_list

def change_con_st(task_list,task,con):
    task_list[task][con] = not task_list[task][con] 

def del_con(task_list,task,con):
    if con in task_list[task]:
        del task_list[task][con]
    return task_list

def add_con(task_list,task,new_con):
    task_list[task][new_con] = False
    return task_list