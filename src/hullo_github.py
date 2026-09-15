

import numpy as np


TEST_NAME = 'tacocat'
TEST_ARRAY = np.arange(0,20,2)

def is_palindrome(my_str: str) -> bool:
	return my_str == my_str[::-1]

def min_median_max(array: np.ndarray) -> tuple:
	return (np.min(array), np.median(array), np.max(array))

def test_me():
	print(is_palindrome(TEST_NAME))
	print(min_median_max(TEST_ARRAY))


if __name__ == "__main__":
	test_me()