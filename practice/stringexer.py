'''Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor '''
def str_exer(str) :
    if len(str) < 2:
        return ' '

    return str[:2] + str[-2:]

print (str_exer('google'))
print (str_exer('go'))
print (str_exer('o'))