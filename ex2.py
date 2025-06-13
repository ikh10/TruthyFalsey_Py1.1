def truthy_falsy(value):
    # Returns "Truthy" if value is truthy, else "Falsy"
    if value:
        return "Truthy"
    else:
        return "Falsy"

def main():
    print("Truthy/Falsy Checker!")
    
    # Infinite loop until the user decides to quit
    while True:
        user_input = input("Enter a value to check (type 'exit' to quit): ")
        
        # Exit condition
        if user_input.upper() == 'Q':
            print("Goodbye!")
            break
        
        # Handling and Evaluating User Input
        try:
            # Try to evaluate the input (e.g., '10' -> 10, '[1, 2, 3]' -> list)
            evaluated_input = eval(user_input)

            # Calls the truthy_falsy function to check if the evaluated value is truthy or falsy.
            result = truthy_falsy(evaluated_input)

        # If the eval() fails (e.g., invalid input), it will skip the try block and run except block.    
        except Exception as e:
            # If eval fails (like for 'hello'), treat it as a string
            result = truthy_falsy(user_input)
        
        # Display the result
        print(f"The value '{user_input}' is {result}.\n")

# Run the program if executed directly
if __name__ == "__main__":  
    main()
