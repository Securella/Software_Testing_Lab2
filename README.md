# Python Unit Testing Lab Assignment

This lab assignment focuses on unit testing using Python and the PyTest library. The objective is to write test cases for two Python functions, `sum` and `product`, and ensure they pass using the PyTest framework. Additionally, defects will be introduced into the functions, and the tests will be rerun to validate the failure of expected test cases.

## Getting Started

### Prerequisites
Ensure you have the following software installed on your computer:
- Python 3.6 or higher
- PyTest library (install using `pip install pytest`)

### Running Tests
To run the test cases, follow these steps:
1. Prepare the test cases for the `sum` and `product` functions. Test cases should be defined as functions starting with the word "test" and placed in a module separate from the code under test.
2. Execute the test cases using the `pytest` command in the terminal. For example: pytest my_tests.py
Replace `my_tests.py` with the name of the module containing the test cases.
3. Ensure that all test cases pass initially.

## Lab Assignment Steps

1. **Install Python and PyTest**: If not already installed, ensure Python and PyTest are installed on your computer.
2. **Prepare Test Cases**: Write test cases for the `sum` and `product` functions, ensuring to cover various scenarios such as empty lists, basic numbers, etc.
3. **Run Initial Tests**: Execute the test cases using the `pytest` command and verify that all test cases pass.
4. **Introduce Defects**: Modify the `sum` and `product` functions to introduce defects, such as removing a line of code or changing a condition.
5. **Run Tests Again**: Re-run the test cases using `pytest` and verify that the test cases expected to fail actually do fail.
6. **Debug and Fix Defects**: Debug the functions and fix the introduced defects.
7. **Final Test Run**: Once the defects are fixed, run the test cases again using `pytest` to ensure that all test cases pass.

## Conclusion
By completing this lab assignment, you will gain practical experience in unit testing Python code using PyTest, as well as debugging and fixing defects in the code.

