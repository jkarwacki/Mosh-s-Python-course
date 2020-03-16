running = True
isStarted = False

while running:
    entry = input("> ").lower()
    if entry == "help":
        print('''
start - start the car
stop - stop the car
quit - quit the game
''')
    elif entry == "start":
        if not isStarted:
            print("Starting the car....")
            isStarted = True
        else:
            print("Car already started.")
    elif entry == "stop":
        if isStarted:
            print("Stopping the car.")
            isStarted = Falses
        else:
            print("Car has already stopped.")
    elif entry == "quit":
        running = False
    else:
        print("I don't understand that")
