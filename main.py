import AsciiArts
import os , sys
import time , datetime
from prettytable import PrettyTable , from_csv
import csv


task_table = PrettyTable(["Row","Task Name", "Status", "Deadline"])

all_task = []
status = 'undone'


def adding_task():
    os.system('cls')
    print('| print b to get back |')
    print('-----------------------')

    print("current tasks: ",all_task)

    addt = input(("Enter your task: "))
    deadline = input(("When's the deadline: "))

    if addt =='b':
        return
    else:
        lenn = len(all_task) + 1

        all_task.append(addt)
        task_table.add_row([str(lenn),addt, status, deadline])

        with open('catcoach/CatCoachProject/usr_tasks.csv', 'w',newline='',encoding='UTF8') as f:
        # writer = csv.writer(f)
            f.write(task_table.get_csv_string())
            f.close()
    os.system('cls')
    

def removing_task():
    os.system('cls')

    print('| print b to get back |')
    print('-----------------------')

    lenn = len(all_task)
    print(task_table)

    remt = int(input(('Enter the task number to remove it: ')))

    if int(remt) > lenn:
        remt = input(('Enter a row number to remove: '))
    if remt == 'b':
        return
    else:
        task_table.del_row(int(remt-1))
        with open('catcoach/CatCoachProject/usr_tasks.csv', 'w',newline='',encoding='UTF8') as f_r:
            f_r.write(task_table.get_csv_string())
        os.system('cls')


def showing_task():
    os.system('cls')

    with open("catcoach/CatCoachProject/usr_tasks.csv", "r") as f_output:
        x = from_csv(f_output)
        print(x)

    print('| Enter any key to get back |')
    sht = input()
    return


def exit_project():
    os.system('cls')

    AsciiArts.menu_exit()
    exu = input('>> ' )
    if exu == 'y':
        sys.exit()
    elif exu == 'n':
        return
    else:
        print("Hmmm??")
        exu = input('>> ' )



while True:

    AsciiArts.title()
    AsciiArts.cat1()
    AsciiArts.menu_index()

    dir_i = input((">> "))

    if dir_i == '1':
        adding_task()
    elif dir_i =='2':
        removing_task()
    elif dir_i == '3':
        showing_task()
    elif dir_i == '4':
        exit_project()



