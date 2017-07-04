import inheritance

billy_cyrus = inheritance.Parent("Cyrus", "blue")
print(billy_cyrus.last_name)

myley_cyrus = inheritance.Child("Cyrus", "Blue", 5)
print(myley_cyrus.last_name)
print(myley_cyrus.number_of_toys)
