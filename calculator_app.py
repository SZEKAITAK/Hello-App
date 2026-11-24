import math
import streamlit as st

# Title
st.title("Basic Web Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide", "Sin()"])

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "Sin()":
        # Note: math.sin() expects radians. Use math.radians(num1) if entering degrees.
        result = math.sin(num1)
        
    st.success(f"Result: {result}")
