# Ask the user to input a character string
user_input = input("Enter a character string: ")

# Open the "output.txt" file in write mode
with open("output.txt", "w") as file:
    # Write the user's input to the file
    file.write(user_input)

print("String has been written to 'output.txt'.")


