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

with open('tasks.txt', 'w', encoding='utf-8') as f:
    pass
menu() 