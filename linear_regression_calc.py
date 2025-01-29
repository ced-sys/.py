def calculate_linear_regression(x_values, y_values):
    """

    Args:
        x_values (_type_): _description_
        y_values (_type_): _description_
    """

    if len(x_values) != len(y_values):
        raise ValueError("X and Y lists must have the same length")
    
    n=len(x_values)

    sum_x=sum(x_values)
    sum_y=sum(y_values)

    sum_xy=sum(x*y for x, y in zip (x_values, y_values))

    sum_x_squared=sum(x*x for x in x_values)

    m=(n*sum_xy-sum_x* sum_y)/(n*sum_x_squared-sum_x*sum_x)

    b=(sum_y-m*sum_x)/n

    return m,b

def print_equation(m, b):
    print(f"\nEquation: y={m:.2f}x + {b:.2f}")

def main():
    x=[2.1, 3.4, 1.8, 4.2, 3.0, 5.0, 2.5, 3.6, 4.8, 2.9]
    y=[5.5, 7.8, 4.9, 8.7, 6.9, 10.3, 5.7, 8.1, 9.6, 6.4]

    print("Input Data:")
    print("x values:", x)
    print("y values:", y)

    print("\nIntermediate Calculations:")
    print(f"Sum of x: {sum(x):.2f}")
    print(f"Sum of y: {sum(y):.2f}")
    print(f"Sum of xy:{sum(x*y for x, y in zip(x, y)):.2f}")
    print(f"Sum of x^2: {sum(x*x for x in x):.2f}")

    slope, intercept=calculate_linear_regression(x, y)

    print("\nResults:")
    print(f"Slope (m): {slope:.2f}")
    print(f"Intercept (b): {intercept:2f}")
    print_equation(slope, intercept)

    x_test=3.5
    y_pred=slope*x_test+intercept
    print(f"\nExample prediction for x={x_test}:")
    print(f"Predicted y ={y_pred:.2f}")


if __name__=="__main__":
    main()