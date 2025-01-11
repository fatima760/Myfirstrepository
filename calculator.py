import streamlit as st

# Title and description
st.title(" simple Calculator")
st.write(" i can Perform various arithmetic operations.")

# Input fields for numbers
numbers = st.text_area("Enter numbers separated by commas:")

# Convert input into a list of numbers
try:
    numbers_list = [float(num.strip()) for num in numbers.split(",") if num.strip()]
except ValueError:
    numbers_list = []
    st.error("Please enter valid numbers separated by commas.")

# Select operation
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide", "Average", "Percentage (First/Second)", "Dividend (First/Second)"])

# Perform the selected operation
result = None
if st.button("Calculate"):
    if len(numbers_list) < 2:
        st.error("Please enter at least two numbers.")
    else:
        if operation == "Add":
            result = sum(numbers_list)
            st.success(f"The result of addition is: {result}")
        elif operation == "Subtract":
            result = numbers_list[0] - sum(numbers_list[1:])
            st.success(f"The result of subtraction is: {result}")
        elif operation == "Multiply":
            result = 1
            for num in numbers_list:
                result *= num
            st.success(f"The result of multiplication is: {result}")
        elif operation == "Divide":
            result = numbers_list[0]
            try:
                for num in numbers_list[1:]:
                    result /= num
                st.success(f"The result of division is: {result}")
            except ZeroDivisionError:
                st.error("Division by zero is not allowed.")
        elif operation == "Average":
            result = sum(numbers_list) / len(numbers_list)
            st.success(f"The average of the numbers is: {result}")
        elif operation == "Percentage (First/Second)":
            if numbers_list[1] != 0:
                result = (numbers_list[0] / numbers_list[1]) * 100
                st.success(f"The percentage is: {result}%")
            else:
                st.error("Percentage calculation requires a non-zero second number.")
        elif operation == "Dividend (First/Second)":
            if numbers_list[1] != 0:
                result = numbers_list[0] % numbers_list[1]
                st.success(f"The remainder (dividend) is: {result}")
            else:
                st.error("Division by zero is not allowed.")

# Optional: Display the result if already calculated
if result is not None:
    st.write(f"Result: {result}")
