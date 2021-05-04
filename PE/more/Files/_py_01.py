import re

# Input username and password
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

# Make a list if there are more than 1 password
password_list = password_input.strip().split(',')
valid_pass_list = list()
for password in password_list:
    # Set validating parameters
    lower = False
    digit = False
    upper = False
    spec_char = False
    length = False
    # Validate each password, based on validating conditions
    password = password.strip()
    password_size = len(password)
    if re.search('.*[a-z]+.*', password):
        lower = True
    if re.search('.*[0-9]+.*', password):
        digit = True
    if re.search('.*[A-Z]+.*', password):
        upper = True
    if re.search('.*[$#@]+.*', password):
        spec_char = True
    if password_size >= 6 and password_size <= 12:
        length = True
    if lower and digit and upper and spec_char and length:
        valid_pass_list.append(password)

# Print valid passwords
if len(valid_pass_list) > 0:
    print("Valid passwords: ", end = '')
    for i in range(len(valid_pass_list) - 1):
        print(valid_pass_list[i], end = ', ')
    print(valid_pass_list[len(valid_pass_list) - 1]) # Print the last password in the list
else:
    print("All passwords are invalid.")