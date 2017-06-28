x = raw_input('What is your string:')

count = 0;

for a in x :
     
 if a =='(' :
   count = count+1 ;
 
 elif a ==')':
   count = count-1 ;
print count; 

if count == -1:
   print ('unbalanced string')
elif count == 0 :
  print('balanced string')
else: 
  print('unbalanced string')



