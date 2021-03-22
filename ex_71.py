edittxt = input('Enter Text File: ')

try:
    fhand = open(edittxt)
except:
    print('Not a valid input')
    exit()

for line in fhand:
    strU = str(line)
    strUpper = strU.upper()

    print(strUpper)
