from copy import deepcopy

my_array = []

for i in range(1,101):
    my_array.append(i)


temp = deepcopy(my_array)
my_array = my_array[::2]


while (len(my_array) > 1):    
    if my_array[-1] == temp[-1]:
        temp = deepcopy(my_array)
        my_array = my_array[1::2]        
    else:
        temp = deepcopy(my_array)
        my_array = my_array[::2]
        
    
print(my_array)   
    
    
