customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])

print(customer.get("birthdate", "Jan 1 1980")) # prevent a key error and replace w/ a default value

customer["name"] = "Jack Smith"  # change the value in a key

print(customer["name"])

customer["birthdate"] = "Aug 5 1990"  # add new key

print(customer["birthdate"])