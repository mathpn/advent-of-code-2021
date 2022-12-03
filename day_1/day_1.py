import numpy as np


def moving_average(array, width: int) -> np.ndarray:
    return np.convolve(array, np.ones(width), "valid") / width


if __name__ == "__main__":
    with open("day_1_input_1.txt", "r") as file:
        depths = list(map(int, file.read().splitlines()))

    print(f"number of times the raw measument has changed: {(np.diff(np.array(depths)) > 0).sum()}")

    depths_moving_average = moving_average(depths, 3)
    print(f"number of times the moving average has changed: {(np.diff(np.array(depths_moving_average)) > 0).sum()}")
