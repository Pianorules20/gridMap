#main.py
import screen, data, os

os.system('clear')
print(f'\n\n    Welcome to OOP Screen! ')
user = input(f'\n\n    Press a key to begin')
On = True
while On:
    os.system('clear')
    screen.printScreen()
    user = input(f'\n\n    Continue?    \n\n    enter a letter to quit'   )
    print(user)
    if user in data.keys:
        os.system('clear')
        exit()
        
    else:
        pass
