# print ACSII code of charater
# print(ord('G'))


# print(chr(71))

# ascii_list = [104, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100]
# print(''.join(chr(i) for i in ascii_list))
# print(''.join(map(chr,ascii_list)))

words = 'hello world'
# str_list = demo_str.split()
# new_list = list()
# new_list.append(ord(str_list[i]) for i in str_list)
# print(new_list)

ascii = []
for word in words:
    for ch in word:
        ascii.append(ord(ch))
