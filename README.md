# TO-DO List
You might've clicked on this thinking it's my Python project TO-DO list or something, but alas it is a badly written terminal TO-DO list written in Python.

The script works by creating (or using) a file called `tasks.txt` in the same working directory as the `todo_list.py` script. If you see a file called `tasks_temp.txt` in the directory for a split second, do not be alarmed. I had to use some ripping and gluing magic to make task completions work.

THE PROGRAM IS FILE AGNOSTIC!! Meaning no matter what the file looks like, as long as it's called exactly `tasks.txt` and has one goal per line, it will work and be formatted correctly inside the script. So if you really wanted to, you could technically import an already made tasks.txt file into the same directory as the script.

The script has a UI, with 4 options:
1. **View tasks**
2. **Add a task**
3. **Complete a task**
4. **Quit**
It is pretty self-explanatory what each option does.

The script 'saves' automatically.

## How to Run
1. Import your existing `tasks.txt` (if you have one) INTO THE SAME DIRECTORY AS THE SCRIPT
2. Run `todo_list.py`

## Example
```
--- TO-DO list ---
1. View tasks
2. Add a task
3. Complete a task
4. Quit
------------------
Choose: 1

-----------------------
Your current tasks are:
-----------------------
1. Wash the dishes
2. Buy Groceries
3. Finish studies
Press enter to go back: 

--- TO-DO list ---
1. View tasks
2. Add a task
3. Complete a task
4. Quit
------------------
Choose: 2

Task to add: Watch TV
You're about to add 'Watch TV' as a task. Are you sure? (y/n): y
-----------
Task added!
-----------

--- TO-DO list ---
1. View tasks
2. Add a task
3. Complete a task
4. Quit
------------------
Choose: 1

-----------------------
Your current tasks are:
-----------------------
1. Wash the dishes
2. Buy Groceries
3. Finish studies
4. Watch TV
Press enter to go back: 

--- TO-DO list ---
1. View tasks
2. Add a task
3. Complete a task
4. Quit
------------------
Choose: 3

-----------------------
Your current tasks are:
-----------------------
1. Wash the dishes
2. Buy Groceries
3. Finish studies
4. Watch TV
Which task would you like to complete (1, 2, ...) (q to exit)? 2
--------------
Tasks updated!
--------------

--- TO-DO list ---
1. View tasks
2. Add a task
3. Complete a task
4. Quit
------------------
Choose: 1

-----------------------
Your current tasks are:
-----------------------
1. Wash the dishes
2. Finish studies
3. Watch TV
Press enter to go back: 

--- TO-DO list ---
1. View tasks
2. Add a task
3. Complete a task
4. Quit
------------------
Choose: 
```