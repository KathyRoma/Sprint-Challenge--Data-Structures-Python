import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


from binary_search_tree_str import BSTNode

'''Using binary search tree to optimize the calculation time 
-- we get 0.13 seconds'''

duplicates =[]
bt = BSTNode(names_1[0])
for name_1 in names_1[1:]:
    bt.insert(name_1)

for name_2 in names_2:
    if bt.contains(name_2):
        duplicates.append(name_2)



from singly_linked_list import LinkedList

'''Trying singly linked list for the same purpose 
-- with no luck, getting 21 seconds'''

# ll = LinkedList()
# duplicates =[]
# for name_1 in names_1[1:]:
#     ll.add_to_tail(name_1)

# for name_2 in names_2:
#     if ll.contains(name_2):
#         duplicates.append(name_2)


# STRETCH
duplicates = list(set(names_1).intersection(names_2))
'''You are going to laugh but this short line gives the best results
-- 0.005 seconds!'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
