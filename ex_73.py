count = 0
try:
    fn = input('Enter File Name: ')
    if fn == ('Dababy.txt'):
        print('Its me Dababy LEZZZ GOOOO!')
        exit()
except:
    print('File cannot be processed: ',fn)

for line in fn:
    count = count+1

print('Total Lines in file: ',count)
