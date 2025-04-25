# This program will take a user input (string) and determine if it is a palindrome or not, meaning it reads the same forwards and backwards.


def is_palindrome(input_string):
    # Convert input string to lowercase and remove spaces and special characters

    input_string = input_string.lower().replace(" ", "").replace(".", "").replace(",", "").replace("!", "").replace("?", "")

    # Check if the input string is equal to its reverse

    length = len(input_string)

    for i in range(length // 2):
        if input_string[i] != input_string[length - i - 1]:
            print("The input string is not a palindrome.")
            return False
    print("The input string is a palindrome!")
    return True


# Main loop to allow multiple checks
while True:
    input_string = input("Enter a string to check if it's a palindrome, or type 'exit' to quit. Remember, the program ignores all punctuation: ")
    if input_string.lower() == "exit":
        print("Goodbye!")
        break
    is_palindrome(input_string)