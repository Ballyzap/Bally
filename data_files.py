with open("whatever.txt", "w") as f:
    f.write("Hello World!")
with open("whatever.txt", "a") as f:
    f.write("\nHave a nice day!")
with open("whatever.txt", "r") as f:
    message = f.read()
    print(message)