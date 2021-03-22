fhand = input('Enter File Name: ')
count = 0
total = 0

try:
    fhand = open(fhand)
except:
    print('Not a valid input')
    exit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        sspos = line.find(':')
        conf = line[sspos+1:]
        confidence = float(conf)

        count = count + 1
        total = total + confidence

average = total / count

print ('Average Spam Confidence: ',average)
