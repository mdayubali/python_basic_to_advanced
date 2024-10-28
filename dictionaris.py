
# Dictionaries is similar to object at js but writing convention look like json 
# Dictionaries allows us to store data in key-value pairs:
    # {"key": "value", "key1": "value1"}

employees = {
    "chef": "Amy","ceo":"Jason","num":45
}
# ADDING IN A NEW KEY-VALUE PAIR
employees["waiter"] = "Mike"
print(employees)
print(employees["waiter"])

# UPDATE! TO K-V
employees["chef"] = "Motin"

print(employees["chef"].upper())


stock_prices = {
    "GOOGLE": [200,210,220],"GME": [20,100,300]
}
history = stock_prices["GOOGLE"]
print(f"First Day price is : {history[0]}")

# Dictionaries in dictionaries

mydict = { "OUTER": {"INNER": 100} }
# print(mydict["OUTER"])
print(mydict["OUTER"]["INNER"])

# Show keys and values of dictionaries using keys() and values() method

mydict_keys = {"key1": 100, "key2": 200, "key3": 400, "key4": 500}
print(mydict_keys.keys())
print("HERE IS THE VALUES")
print(mydict_keys.values())

# Show both keys and values together of the dictionaries using items() method
# items() method returns the tuples.
print(mydict_keys.items());