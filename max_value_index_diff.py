import sys



#Custom function to get the index of provided value in provided list.
def get_index(my_list, value):
    for index, element in enumerate(my_list):
        if element == value:
            return index
    return -1


if len(sys.argv) < 2:
    print('You need to specify a list in format [int_one,int_two, .....] as an argument')
    sys.exit()

#argument is of type string
list_input = sys.argv[1]


#convert string into list assuming their will be a list of integers 
#we can change the first argument for float type elements
actual_list = list(map(int, list_input.strip('[]').split(','))) 

#assign default max value as 0 index
max_value = actual_list[0]

#Iterate over list to get max value without using built in function
for x in actual_list:
    if x > max_value:
        max_value = x

#assign default min value as 0 index
min_value = actual_list[0]

#Iterate over list to get min value without using built in function
for x in actual_list:
    if x < min_value:
        min_value = x

#get index of max value element
index_of_max = get_index(actual_list, max_value)
#get index of max value element
index_of_min = get_index(actual_list, min_value)

#Absolute diff of indexes
diff_of_index =abs(index_of_max - index_of_min)

print(diff_of_index)



