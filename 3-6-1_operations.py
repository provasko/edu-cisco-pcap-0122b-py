# The inner life of lists

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# Powerful slices

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# Slices - negative indices

# my_list[start:end]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# my_list = [10, 8, 6, 4, 2]
# del my_list
# print(my_list)


# The in and not in operators

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

###

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)


my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)


# Key takeaways

'''
1. If you have a list l1, then the following assignment: l2 = l1 does not make a copy of the l1 list, 
but makes the variables l1 and l2 point to one and the same list in memory. For example:
'''

vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one)  # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0]  # deletes 'car'
print(vehicles_two)  # outputs: ['bicycle', 'motor']

'''
2. If you want to copy a list or part of the list, you can do it by performing slicing:
'''

colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list

'''
3. You can use negative indices to perform slices, too. For example:
'''

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

'''
4. The start and end parameters are optional when performing a slice: list[start:end], e.g.:
'''

my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2:]
slice_two = my_list[:2]
slice_three = my_list[-2:]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]

'''
5. You can delete slices using the del instruction:
'''

my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []

'''
6. You can test if some items exist in a list or not using the keywords in and not in, e.g.:
'''

my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False
