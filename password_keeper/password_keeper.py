# simple password keeper

from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)        

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

# note that we need to create key to encrypt for the first time
# write_key()

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            url, user, passw = data.split('|')
            print('URL: ', url, '| User:', user, '| Password:', fer.decrypt(passw.encode()).decode())

def add():
    url = input('URL: ')
    acc = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(url + '|' + acc + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

if __name__ == "__main__":
    
    while True:
        mode = input(
            'Would you like to add a new password or view existing ones (view, add), press q to quit? ').lower()
        if mode == 'q':
            break
        if mode == 'view':
            view()
        elif mode == 'add':
            add()
        else:
            print('Invalid mode.')
            continue