# Suppose we're creating a dictionary named customer_352308, with these pairs:
customer_352308 = {"First name": "John", "Last name": "Frank", "City": "Toronto", "Address": "M04 London"}
print(customer_352308)

# How to pick information out of them.
customer_352308 = {"First name": "John", "Last name": "Frank", "City": "Toronto", "Address": "M04 London"}
address_of_customer = customer_352308["Address"]
print(address_of_customer)

# The versatility of keys and values.
# But keys don't have to be strings. They can be numbers:
# Values can be numbers, too:
ranking = {6: "Germany", 2: "Poland", 1: "Finland", 5: "Sweden"}
print(ranking)

# How to pick information out of them
ranking = {6: "Germany", 2: "Poland", 1: "Finland", 5: "Sweden"}
ranking_of_country = ranking[5]
print(ranking_of_country)

# You can mix strings and numbers any way you want.
things_to_remember = {
    0: "the lowest number",
    "a dozen": 12,
    "snake eyes": "a pairs of ones",
    13: "a baker's dozen"
}
remember_them = things_to_remember["a dozen"]
print(remember_them)


# How to Add items in already existing dictionary.
customer_12345 = {"First Name": "Mosh", "Last Name": "Bala", "Age": 27}
customer_12345["city"] = "Lisbon"
print(customer_12345)

# You can also define an empty dictionary, a dictionary with no key-value pairs:
things_to_remember = {}
things_to_remember[0] = "the lowest number"
things_to_remember["a dozen"] = 12
things_to_remember["snake eyes"] = "a pair of ones"
things_to_remember[13] = "a baker's dozen"
print(things_to_remember)

# Removing and changing item.
customer_352308 = {"First name": "John", "Last name": "Frank", "City": "Toronto", "Address": "M04 London"}
del customer_352308["Address"]
print(customer_352308)
# Changing the value of an element is similar to the same operation that you
# learned for lists. It begins with the name of the list or dictionary:
customer_352308 = {"First name": "John", "Last name": "Frank", "City": "Toronto", "Address": "M04 London"}
customer_352308["First name"] = "Mark"
print(customer_352308)

# Looping through value.
#There may be times when you want to capture the values instead.
customer_352308 = {"First name": "John", "Last name": "Frank", "City": "Toronto", "Address": "M04 London"}
for each_value in customer_352308.values():
    print(each_value)

# Looping through keys.
# There may be times when you want to capture the keys instead.
customer_352308 = {"First name": "John", "Last name": "Frank", "City": "Toronto", "Address": "M04 London"}
for each_keys in customer_352308.keys():
    print(each_keys)

# Looping though key-value pairs...
# loop through a dictionary finding both keys and values...
customer_352308 = {"First name": "John", "Last name": "Frank", "City": "Toronto", "Address": "M04 London"}
for each_keys, each_value in customer_352308.items():
    print("The Customer's " + each_keys + " is " + each_value)