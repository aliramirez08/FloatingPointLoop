def main():
    """ Reads 5 floating-point numbers, calculates total, average, min, max, and interest. """
    count = 0
    total = 0.0
    max_value = float('-inf')
    min_value = float('inf')
    numbers = []  # Store valid inputs

    while count < 5:
        try:
            number = float(input(f"Enter floating-point number {count + 1}: "))
            numbers.append(number)  # Store number
            total += number
            
            # Update max and min values
            if number > max_value:
                max_value = number
            if number < min_value:
                min_value = number
            
            count += 1  # Increment count only on valid input
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number.")

    # Compute derived values
    average = total / 5
    interest = total * 0.2

    # Display results with formatting
    print("\n" + "=" * 30)
    print("Results:")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {max_value:.2f}")
    print(f"Minimum: {min_value:.2f}")
    print(f"Interest on total at 20%: {interest:.2f}")
    print("=" * 30)

if __name__ == "__main__":
    main()