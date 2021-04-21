# valid ip address

ip = input('Enter ip address:')

try:
    arr = ip.split('.')
    if len(arr) == 4:
        for item in arr:
            item = int(item)
            if (item < 0 and item > 255):
                print('Invalid')
                quit()
            else:
                print('Valid')
    else:
        print('Invalid')
        quit()
except:
    print('No valid')
    quit()
