import random
import string
import sys

class generatepassword:
    def __init__(self):
        self.history = []
        self.load_passwords()

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.history.append(password)
        self.save_passwords()
        return password

    def get_password_history(self):
        return self.history
    
    def load_passwords(self):
        try:
            with open("password_history.txt", "r") as file:
                self.history = file.read().splitlines()
        except FileNotFoundError:
            pass

    def save_passwords(self):
        with open(r"C:\Users\salma\Downloads\New folder (2)\passwords.txt", "w") as file:
            file.write("\n".join(self.history))

generator = generatepassword()

while True:
    print('\nchoose ur choice:')
    print('-------------------')
    print('1.generate password')
    print('2.password history')
    print('3.exit')
    print('-------------------')
    a=int(input('choice:'))
    
    if a==1:
        print(generator.generate_password(16))
        
    elif a==2:
        for password in generator.get_password_history():
            print(password)
            
    elif a==3:
        sys.exit(1)

