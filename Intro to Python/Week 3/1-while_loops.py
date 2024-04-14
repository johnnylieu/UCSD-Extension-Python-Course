"""Translate the following for loops to equivalent while loops:"""
#                a.   for count in range (100): 
#                                       print (count)
count = 0
while count < 100:
    print(count)
    count += 1

#               b.     for count in range (1, 101):    
#                                      print (count) 
count = 1
while count < 101:
    print(count)
    count += 1

#               c.      for count in range (100, 0, –1):
#                                      print (count)
count = 100
while count > 0:
    print(count)
    count -= 1