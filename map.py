# Take input from the user and convert it to a list of integers
try:
    input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    
    # Define the lambda function to triple a number
    triple = lambda x: x * 3
    
    # Use map to apply the lambda function to each element in the input list
    tripled_list = list(map(triple, input_list))
    
    # Output the tripled list
    print("Triple of list numbers:")
    print(tripled_list)
except ValueError:
    print("Invalid input. Please enter a valid list of integers separated by spaces.")
