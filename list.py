# list look like as array in others langugaes

myvar = "New"
mylist = [100,200,300,400,500,5]
# print a new array according to the range
print(mylist[0:4])
# Add new items at the last position
# mylist.append(myvar)
# add new items at specific position at the list using insert(index,var/string)
# mylist.insert(1,myvar)
mylist.insert(1,"Jewel")
print(mylist)

# Remove items from the list
# Using pop() the items will be removed from the last 
# If you specify the position then use the index of itmes
# item_remove = mylist.pop();
item_remove = mylist.pop(2);
print(mylist)

# reversed the list using reverse()

mylist.reverse();
print(mylist)

# sorting the list using sort() method
sort_list = [5,3,2,1,4,2,3,5,6,7,20,32,343,2,53,213,34,5,10,8,9]
sort_list.sort();
print(sort_list)

# decending sort using reverse() method
sort_list.reverse();
print(sort_list)