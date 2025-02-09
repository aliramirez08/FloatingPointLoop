def main():
    count = 0
    total = 0.0
    max_value = float('-inf')
    min_value = float('inf')

    while count < 5:
        try:
            number = float(input(f"Enter floating-point number {count + 1}: "))
            total += number

            if number > max_value:
                max_value = number
            if number < min_value:
                min_value = number

            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number.")

    average = total / 5
    interest = total * 0.2

    print("\nResults:")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {max_value:.2f}")
    print(f"Minimum: {min_value:.2f}")
    print(f"Interest on total at 20%: {interest:.2f}")

if __name__ == "__main__":
    main()
