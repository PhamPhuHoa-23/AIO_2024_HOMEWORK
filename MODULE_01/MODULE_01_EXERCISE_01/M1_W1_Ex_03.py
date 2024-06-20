import math
import sys
import random

# CONSTANT
LOSS_FUNCTIONS = ["mae", "mse", "rmse"]


def mae(n: int, predict_values: list[float], target_values: list[float]) -> None:
    result = 0

    for i in range(0, n):
        print(f"Loss name: MAE, sample {i + 1}, pred: {predict_values[i]}, target: {target_values[i]}")

        loss = abs(predict_values[i] - target_values[i])
        print(f"Loss: {loss}")

        result += loss
    result = result / n
    print(f"Final MAE: {result}")


def mse(n: int, predict_values: list[float], target_values: list[float]) -> None:
    result = 0

    for i in range(0, n):
        print(f"Loss name: MSE, sample {i + 1}, pred: {predict_values[i]}, target: {target_values[i]}")

        loss = (predict_values[i] - target_values[i]) ** 2
        print(f"Loss: {loss}")

        result += loss
    result = result / n
    print(f"Final MSE: {result}")


def rmse(n: int, predict_values: list[float], target_values: list[float]) -> None:
    result = 0
    for i in range(0, n):
        print(f"Loss name: RMSE, sample {i + 1}, pred: {predict_values[i]}, target: {target_values[i]}")

        loss = (predict_values[i] - target_values[i]) ** 2
        print(f"Loss: {loss}")

        result += loss
    result = math.sqrt(result / n)
    print(f"Final RMSE: {result}")


def loss_function(n: str, loss_function_name: str):
    if n.isnumeric():
        n = int(n)
    else:
        sys.exit("number of samples must be an integer number")

    loss_function_name = loss_function_name.lower()

    # GENERATE PREDICT AND TARGET VALUE
    predict_values = [random.uniform(a=0, b=10) for _ in range(n)]
    target_values = [random.uniform(a=0, b=10) for _ in range(n)]

    if loss_function_name == "mae":
        mae(n=n, predict_values=predict_values, target_values=target_values)
    elif loss_function == "mse":
        mse(n=n, predict_values=predict_values, target_values=target_values)
    elif loss_function == "rmse":
        rmse(n=n, predict_values=predict_values, target_values=target_values)


# Unit test
if __name__ == '__main__':
    num_samples = input("Input number of samples (integer number) which are generated: ")
    loss_function_name = input("Input loss name: ")
    loss_function(n=num_samples, loss_function_name=loss_function_name)
