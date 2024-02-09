# Oona Tiikhonen's VS Code playground
# More unit tests

from software_test_lab2 import sum, product
import pytest
import random


# Parameterized tests with decorators
@pytest.mark.parametrize("input_list, expected_sum", [
    ([], 0),             # Empty list
    ([1, 2, 3], 6),      # Basic numbers
    ([-1, -2, -3], -6),  # Negative numbers
    ([5], 5),            # Single number
    ([0, 1, 2, 3], 6)    # With zero
])
def test_sum(input_list, expected_sum):
    assert sum(input_list) == expected_sum


@pytest.mark.parametrize("input_list, expected_product", [
    ([], 1),             # Empty list
    ([1, 2, 3], 6),      # Basic numbers
    ([-1, -2], 2),       # 2 negative numbers
    ([-1, -2, -3], -6),  # 3 negative numbers
    ([2], 2),            # Single number
    ([0, 1, 2, 3], 0)    # With zero
])
def test_product(input_list, expected_product):
    assert product(input_list) == expected_product


# Randomized tests for both functions
def test_random_input():
    random_list = [random.randint(1, 100) for _ in range(random.randint(1, 10))]
    assert sum(random_list) == sum(random_list)
    assert product(random_list) == product(random_list)


