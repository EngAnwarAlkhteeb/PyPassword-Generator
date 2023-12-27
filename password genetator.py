print('''
______                                   _                                   _             
| ___ \                                 | |                                 | |            
| |_/ /_ _ ___ _____      _____  _ __ __| |   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| | | (_| \__ \__ \\ V  V / (_) | | | (_| | | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                              __/ |                                        
                                             |___/                                         
''')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


import random
print("Welcome to the PyPassword Generator!")
length_char = int(input("How many characters would you like your password to have? "))
n_symbols = int(input("how many symbols would you like your password to have? "))
n_numbers = int(input("How many numbers would you like your password to have? "))

# password = ""
# for char in range(1, length_char + 1):
#     password = random.choice(letters)

# for char in range(1, n_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, n_numbers + 1):
#     password += random.choice(numbers)

# print(password)




password_list = []
for char in range(1, length_char + 1):
    password_list.append(random.choice(letters))

for char in range(1, n_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, n_numbers + 1):
    password_list += random.choice(numbers)
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")