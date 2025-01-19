def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt division
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
