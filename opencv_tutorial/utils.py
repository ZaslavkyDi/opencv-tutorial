from typing import Optional

import numpy as np
import matplotlib.pyplot as plt


def print_plt_image(pic_arr: np.ndarray, is_gray: bool = False) -> None:
    color_map: Optional[str] = 'gray' if is_gray else None
    plt.imshow(pic_arr, cmap=color_map)
    plt.show()


def print_shape(pic_arr: np.ndarray) -> None:
    print(f'Shape: {pic_arr.shape}')


def print_array(pic_arr: np.ndarray) -> None:
    print(f'Array: {pic_arr}')
