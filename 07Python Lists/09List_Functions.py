list1 = [2, 3, 4, 1, 32, 4]
list1.append(19)
print(list1)


print(list1.count(4))  # Return the count for number 4


list2 = [99, 54]
list1.extend(list2)
print(list1)


print(list1.index(4))  # Return the index of number 4


list1.insert(1, 25) # Insert 25 at position index 1
print(list1)


list1 = [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
print(list1.pop(2))


print(list1.pop())

print(list1)

list1.remove(32)  # Remove number 32
print(list1)

list1.reverse()  # Reverse the list
print(list1)

list1.sort() # Sort the list
print(list1)
