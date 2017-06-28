import re
file = open('short_file.txt')
fileread = file.read()
#for line in file :
#print fileread

search = re.findall('.[0-9]+',fileread)
print search

for searc in search :
 searchi = int(search[0:])
 
#print searchi

#searchi = int(search)
#print search
#sum = sum(search)
#print sum

