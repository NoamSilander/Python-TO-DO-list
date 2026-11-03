def neat_message(message):
    print(f"{'-' * len(message)}\n{message}\n{'-' * len(message)}")

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
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            print('')
            neat_message('Your current tasks are:')
            for i, line in enumerate(f, 1):
                print(f'{i}. {line.strip()}')
        print('-' * 23)
    except FileNotFoundError:
        neat_message("You haven't written anything yet")
    user_finish = input ('Press enter to go back: ')

def add_task():
    try:
        with open('tasks.txt', 'a', encoding='utf-8') as f:
            while True:
                user_input = input('\nTask to add: ')
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

    except Exception:
        pass


menu() 