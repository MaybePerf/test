from tasks import *

tdlist = {}

while True:
    choice = input('Выберите действие: showlist, task, del_task, add_con, del_con, change_con_st, change_st, exit ')
    if choice == 'showlist':
        print(showlist(tdlist))
    elif choice == 'task':
        print(showlist(tdlist))
        newtask = input('Введите название задачи: ')
        tdlist = add(tdlist,newtask)
    elif choice == 'del':
        print(showlist(tdlist))
        deltask = input('Введите название задачи: ')
        tdlist = delete_task(tdlist,deltask)
    elif choice == 'add_con':
        print(showlist(tdlist))
        c_choice = input('Выберите задачу')
        condition = input('Введите условие:')
        tdlist = add_con(tdlist,c_choice,condition)
    elif choice == 'del_con':
        print(showlist(tdlist))
        task_ch = input('Выберите задачу:')
        if task_ch in tdlist:
            con_del = input('Выберите условие:')
            tdlist = del_con(tdlist,task_ch,con_del)
    elif choice == 'change_st':
        print(showlist(tdlist))
        ch = input('Выберите задачу')
        if ch in tdlist:
            con_ch = input('Выберите условие')
            if con_ch in tdlist[ch]:
                change_con_st(tdlist,ch,con_ch)
            else:
                print('Условие не найдено')
        else:
            print('Задача не найдена')
    elif choice == 'exit':
        break
    else:
        print('Команда не найдена')