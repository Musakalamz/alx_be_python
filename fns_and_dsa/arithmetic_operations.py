def  perform_operation(num1, num2, operation ):
    """
    Perform basic arithmetic operations based on the 'operation' parameter.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'
    
    Returns:
        float or str: Result of operation, or an error message
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"