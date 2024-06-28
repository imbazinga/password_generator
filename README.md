# password_generator
This password generator tool generates strong and random passwords for online protection and also allows you to create custom passwords based on your preferences for the number of letters, symbols, and numbers included.
# Installation:
* clone this repository:
```bash
git clone https://github.com/imbazinga/password_generator
```
* run the python script:
```bash
python generate.py
```
# Customization
In the *save_passwords* function, replace the following path with the actual path where you want to store the passwords:
```bash
def save_passwords(self):
      with open(r"path/to/your/directory", "w") as file:
         file.write("\n".join(self.history))
```
