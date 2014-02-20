def count_spaces(userInput):
    spaces = 0
    for char in userInput:
        if char == " ":
            spaces += 1

    return spaces

def main():
    userInput = input("Please type your message: ")
    print(count_spaces(userInput))


main()