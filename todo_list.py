def menu():
    while True:
        user_choice = input('--- TO-DO list ---\n 1. View tasks\n 2. Add a task\n 3. Complete a task\n 4. Quit\n Choose: ').strip()
        if user_choice == '1':
            view_task()
        elif user_choice == '2':
            add_task()
        elif user_choice == '3':
            complete_task()
        elif user_choice == '4':
            print('Quitting...')
            return user_choice
        else:
            print('\nPlease choose an option.\n')

def view_task():
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            print('Your current tasks are:')
            for i, line in enumerate(f, 1):
                print(f'{i}. {line}').st
    except FileNotFoundError:
        message = "You haven't written anything yet!"
        print(f"{'-' * len(message)}\n{message}\n{'-' * len(message)}")


menu() 