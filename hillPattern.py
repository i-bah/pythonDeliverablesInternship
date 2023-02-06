# Prompt the user to enter a number of shapes
number_of_shapes = int(input("Please enter the number of shapes: "))

# Prompt the user to enter the shape type
shape_type = input("Please enter a shape type: ")

# An outer loop that loops through the collected input from the user
for i in range(number_of_shapes):
    # An inner loop that creates spaces
    for j in range(i, number_of_shapes):
        print(" ", end=" ")

    # An inner loop that adds the inputted shape
    for j in range(i):
        print(shape_type, end=" ")

    # An inner loop that adds the inputted shape
    for j in range(i + 1):
        print(shape_type, end=" ")
    # Move to the nextline
    print()
