'''Write a loop that reads each line of a file. It should count the number of characters in each line and keep track of the total number of characters read. Once you have a total of 1,000 or more characters, break from the loop. (You can use a break statement to do this.)
'''
filename = 'abc.txt'
try:
    f = open(filename,'r')
except IOError:
    print("Couldn't open %s" %  filename)
charc = 0
line = f.readline()
for line in f:
    if line.startswith('#') == True:
        break
    charc = charc + len(line)
    if charc > 1000 :
        print charc
        break
    else:
        print charc
