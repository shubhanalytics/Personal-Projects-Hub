import streamlit as st

st.title("🧮 Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.write("Result:", num1 + num2)
    elif operation == "Subtract":
        st.write("Result:", num1 - num2)
    elif operation == "Multiply":
        st.write("Result:", num1 * num2)
    elif operation == "Divide":
        if num2 == 0:
            st.write("Error! Division by zero.")
        else:
            st.write("Result:", num1 / num2)
