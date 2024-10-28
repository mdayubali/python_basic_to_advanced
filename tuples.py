# Tuples are similar to lists except for the fact that they are immutable(can not be changed/muted)
# Due to thier immutability, they have less methods that lists, they are used when you don't expect (or want) a user to be able to change the sequence of items.

        # (key,value)
# tuples is start with () where list is start with []
# list are mutable where tuples are immutable

mylist = [1,2,4,54,5]
mylist[0] = 6
print(mylist)
mytuples= (1,2,4,54,5)
# can't update the values. It will be through an error as tuples are immutable
# mytuples[0] = 5 

print(mytuples)
# see the index based items value
print(mytuples[0])