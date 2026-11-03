import os

def neat_message(message):
    print(f"{'-' * len(message)}\n{message}\n{'-' * len(message)}")

def print_list():
    amount = 0
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            print('')
            neat_message('Your current tasks are:')
            for i, line in enumerate(f, 1):
                print(f'{i}. {line.strip()}')
                amount += 1
            return amount
        print('-' * 23)
    except FileNotFoundError:
        neat_message("You haven't written anything yet")
        return 0

def menu():
    while True:
        user_choice = input('\n--- TO-DO list ---\n1. View tasks\n2. Add a task\n3. Complete a task\n4. Quit\n------------------\nChoose: ').strip()
        if user_choice == '1':
            view_task()
        elif user_choice == '2':
            add_task()
        elif user_choice == '3':
            complete_task()
        elif user_choice == '4':
            neat_message('Quitting...')
            return user_choice
        else:
            neat_message('Please choose an option')

def view_task():
    print_list()
    user_finish = input ('Press enter to go back: ')

def add_task():
    with open('tasks.txt', 'a', encoding='utf-8') as f:
        while True:
            user_input = input('\nTask to add: ').strip()
            if len(user_input) < 1:
                neat_message('Task must be atleast 1 character long')
            else:
                break
        while True:
            user_y_n = input(f"You're about to add '{user_input}' as a task. Are you sure? (y/n): ").lower()
            if user_y_n == 'y':
                f.write(user_input + '\n')
                neat_message('Task added!')
                break
            elif user_y_n == 'n':
                break

def complete_task():
    amount = print_list()
    if amount < 1:
        return
    while True:
        user_choice = input('Which task would you like to complete (1, 2, ...) (q to exit)? ').lower()
        try:
            if user_choice == 'q':
                return
            user_choice = int(user_choice)
        except ValueError:
            print('Must be a whole number')
            continue
        if user_choice > amount or user_choice < 1:
            print('Must be valid list number')
            print_list()
        else:
            break

    with open('tasks.txt', encoding='utf-8') as source, open('tasks_temp.txt', 'w', encoding='utf-8') as target:
        for i, line in enumerate(source, 1):
            if i != user_choice:
                target.write(line)
    os.replace('tasks_temp.txt', 'tasks.txt')
    neat_message('Tasks updated!')

if __name__ = '__main__':
    menu() 