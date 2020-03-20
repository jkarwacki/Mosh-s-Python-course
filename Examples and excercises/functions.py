def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John", "Smith")  # positional arguments
print("Finish")

greet_user(last_name="Smith", first_name="John")  # keyword arguments, improves readability, especially /w num values
                                                    # if mixing keyword and positional arguments, put keyword arg last
