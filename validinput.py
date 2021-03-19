while True:
    demo = input('Enter number:')
    if demo.isdigit():
        print('digit')
    if demo.containsisalnum() or demo.isspace():
        print('word + num')
    
    try:        
        demo_parse = int(demo)
        print(demo_parse)
        break
    except:
        print('Wrong type input. Redo')

# def hasSpaceAndAlpha(string):
#     return any(char.isalpha() for char in string) and any(char.isspace() for char in string) and all(char.isalpha() or char.isspace() for char in string)

# import re
# alpha_regex = "^[a-z A-Z]+$"
# if re.match(alpha_regex, string):
#    print("Only alphabetical letters and spaces: yes")
# else:
#    print("Only alphabetical letters and spaces: no")

