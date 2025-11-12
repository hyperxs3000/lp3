def fractional_knapsack():
    # Step 1: Initialize item data
    weights = [10, 20, 30]     # weights of the items
    values = [60, 100, 120]    # values of the items
    capacity = 50              # maximum weight the knapsack can hold
    total_value = 0.0          # to store the total value added to the knapsack

    # Step 2: Combine weights and values into a single list
    # Each item will be represented as (weight, value)
    items = list(zip(weights, values))

    # Step 3: Sort items based on value/weight ratio in descending order
    # This ensures that items with the highest value per unit weight come first
    items.sort(key=lambda item: item[1] / item[0], reverse=True)

    # Step 4: Go through each item and fill the knapsack
    for weight, value in items:
        if capacity == 0:
            break  # Knapsack is full, stop adding items

        if weight <= capacity:
            # If the entire item fits, take it all
            total_value += value
            capacity -= weight
        else:
            # Take only the fraction of the item that fits
            total_value += value * (capacity / weight)
            capacity = 0  # Knapsack is now completely full

    # Step 5: Print the total value that fits in the knapsack
    print("Maximum value in Knapsack =", total_value)


# Step 6: Run the program
if __name__ == "__main__":
    fractional_knapsack()
