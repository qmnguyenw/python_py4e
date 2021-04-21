import re
strEmail = input('enter:')

if re.match('[a-zA-Z0-9]+@[a-zA-Z]+\.[.a-zA-Z]', strEmail):
    print('correct')
else:
    print('error')
