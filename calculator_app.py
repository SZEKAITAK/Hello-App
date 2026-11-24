import math
import streamlit as st


# --- Calculation Functions ---
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"


def sine(a):
    # math.sin() expects radians. Use math.radians(a) if entering degrees.
    return math.sin(a)


def log10(a):
    return math.log10(a) if a > 0 else "Error: Input must be greater than 0"


def ln(a):
    return math.log(a) if a > 0 else "Error: Input must be greater than 0"


# --- Main Application ---
def main():
    st.title("Basic Web Calculator")

    # Operation selection (placed first so we can disable num2 for single-input operations)
    single_input_ops = ["Sin()", "Log (base 10)", "Ln (natural log)"]
    all_ops = ["Add", "Subtract", "Multiply", "Divide"] + single_input_ops
    operation = st.selectbox("Choose operation", all_ops)

    # Input fields
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input(
        "Enter second number",
        value=0.0,
        disabled=(operation in single_input_ops)
    )

    # Calculate
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Sin()":
            result = sine(num1)
        elif operation == "Log (base 10)":
            result = log10(num1)
        elif operation == "Ln (natural log)":
            result = ln(num1)

        # Display error in red or valid result in green
        if isinstance(result, str) and result.startswith("Error"):
            st.error(result)
        else:
            st.success(f"Result: {result}")


if __name__ == "__main__":
    main()
