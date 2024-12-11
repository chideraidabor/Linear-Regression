import numpy as np
import matplotlib.pyplot as plt

def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(float, line.strip().split(','))
            points.append((x, y))
    return points

def regression_analysis(n, points):
    # Step 1: Calculate the totals for x and y
    x_total = sum(point[0] for point in points)
    y_total = sum(point[1] for point in points)

    # Step 2: Calculate the mean of x and y
    x_mean = x_total / n
    y_mean = y_total / n

    # Step 3: Calculate variance of x (sigma_x) and covariance of x and y (covariance_xy)
    sigma_x = sum((point[0] - x_mean) ** 2 for point in points) / n
    covariance_xy = sum((point[0] - x_mean) * (point[1] - y_mean) for point in points) / n

    # Step 4: Calculate the slope and intercept
    slope = covariance_xy / sigma_x
    intercept = y_mean - slope * x_mean

    # Print the slope and intercept each time they’re calculated
    print(f"Slope: {slope}, Intercept: {intercept}")

    return slope, intercept

def predict(slope, intercept, x_value):
    # Predict the y value for a given x based on the slope and intercept
    # y = mx + b
    return slope * x_value + intercept

def plot_regression(points, slope, intercept):
    # Plot the points
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    plt.scatter(x_values, y_values, color='blue', label='Data Points')

    # Plot the regression line
    x_line = np.linspace(min(x_values), max(x_values), 100)
    y_line = slope * x_line + intercept
    plt.plot(x_line, y_line, color='red', label='Fitting Line')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Linear Regression Line')
    plt.show()

def read_points_from_terminal():
    points = []
    print("Enter each point as x, y (e.g., 1.5, 2.3). Press Enter on an empty line when done.")
    
    while True:
        user_input = input("Enter x and y separated by a comma: ").strip()
        
        # Check if the user just pressed Enter without typing anything
        if user_input == "":
            break  # Exit the loop if no input is given (user pressed Enter on an empty line)
        
        try:
            x, y = map(float, user_input.split(','))
            points.append((x, y))
        except ValueError:
            print("Invalid input. Please enter the point as x, y.")
    
    return points

if __name__ == "__main__":
    # Choose input method
    choice = input("Enter 'file' to read points from a file or 'terminal' to input manually: ").strip().lower()
    if choice == 'file':
        filename = input("Enter the filename: ").strip()
        points = read_points_from_file(filename)
    elif choice == 'terminal':
        points = read_points_from_terminal()
    else:
        print("Invalid choice. Please restart the program.")
        exit()

    n = len(points)
    slope, intercept = regression_analysis(n, points)

    # Plot the results
    plot_regression(points, slope, intercept)

    # Predict y for a given x
    while True:
        try:
            x_value = float(input("Enter a value for x to predict y (or type 'exit' to quit): "))
            y_predicted = predict(slope, intercept, x_value)
            print(f"Predicted y for x={x_value}: {y_predicted}")
        except ValueError:
            break
