'''As an alternative to the range function, some programmers like to increment a counter inside a while loop and stop the while loop when the counter is no longer less than the length of the array. Rewrite the following code using a while loop instead of a for loop.
'''
a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big = [ ] 
'''
for i in range ( len ( a ) ): 
    big.append ( max ( a [ i ],b [ i ] ) ) 
    print big
'''
i=0
while i < len(a):
   big.append(max(a[i],b[i]))
   i=i+1
   print big 
