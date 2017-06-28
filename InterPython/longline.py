#long_line = ''
long_line_len = 0
f = open("Bigfile")

for line in f:
    if len(line) > long_line_len:
        long_line_len = len(line)
        long_line = line

print long_line
print len(long_line)
