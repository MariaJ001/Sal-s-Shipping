# Sal's Shipping
# Maria Julia S. Medeiros

while True:
    try:
        # Get user input for weight
        weight = float(input('Add weight: '))
    except ValueError:
        print("Invalid input. Please enter a numeric value for the weight.")
        continue  # Continue to the next iteration if input is not numeric

    # Main shipping cost calculation
    while True:
        # Ground Shipping
        if weight <= 2:
            cost_ground = weight * 1.5 + 20
        elif weight <= 6:
            cost_ground = weight * 3.00 + 20
        elif weight <= 10:
            cost_ground = weight * 4.00 + 20
        else:
            cost_ground = weight * 4.75 + 20

        print("Ground Shipping $", cost_ground)

        # Ground Shipping Premium
        cost_ground_premium = 125.00
        print("Ground Shipping Premium $", cost_ground_premium)

        # Drone Shipping
        if weight <= 2:
            cost_drone = weight * 4.5
        elif weight <= 6:
            cost_drone = weight * 9.00
        elif weight <= 10:
            cost_drone = weight * 12.00
        else:
            cost_drone = weight * 14.25

        print("Drone Shipping: $", cost_drone)

        # Ask the user if they want to try again
        try_again = input("Do you want to try again? (yes/no): ").lower()
        if try_again != 'yes':
            break  # Break the inner loop if the user doesn't want to try again

        # Get user input for weight again
        try:
            weight = float(input('Add weight: '))
        except ValueError:
            print("Invalid input. Please enter a numeric value for the weight.")
            break  # Break the inner loop if the input is not numeric

    print('Thank you for using my system!')
    break  # Break the outer loop if the user doesn't want to try again after the inner loop
