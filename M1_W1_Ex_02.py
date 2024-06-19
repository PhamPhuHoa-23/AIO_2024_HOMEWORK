import math
import sys

# CONSTANT
ALPHA = 0.01
ACTIVATION_FUNCTIONS = ["sigmoid", "relu", "elu"]

def is_decimal(var):
    try:
        float(var)
    except ValueError:
        return  False

    return True

def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))

def relu(x: float) -> float:
    if x <= 0: return 0
    else: return x

def elu(x: float) -> float:
    if x <= 0: return ALPHA * (math.exp(x) - 1)
    else: return x

def f(x, activation_function: str):
    if not is_decimal(x): sys.exit(" x must be a number")
    else: x = float(x)

    if activation_function.lower() not in ACTIVATION_FUNCTIONS:
        sys.exit(f"{activation_function} is not supported")

    match activation_function:
        case "sigmoid": print(f"Sigmoid: f({x}) = {sigmoid(x)}")
        case "relu": print(f"ReLU: f({x}) = {relu(x)}")
        case "elu": print(f"ELU: f({x}) = {elu(x)}")

# Unit test
if __name__ == '__main__':
    x = input("Input x: ")
    activation_function_name = input("Input activation Function (sigmoid|relu|elu): ")
    f(x=x, activation_function=activation_function_name)
