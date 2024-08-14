import streamlit as st

# Title of the app   
st.title("Simple Calculator")


# Step 2:

## Input fields for numbers
num1 = st.number_input("Enter Your First Number")
num2 = st.number_input("Enter Your Second Number")

## Dropdown menu for operation selection 
operation = st.selectbox("Choose an Operation", 
                        ("Addition", "Subtraction", "Multiplication", "Division"))


# Step 3:

# Performing the Calculation based on the slected operation


if operation == "Addition":
    result = num1 + num2

elif operation == "Subtraction":
    result = num2 - num1

elif operation == "Multiplication":
    result = num1 * num2

elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! You need to change the Number 2"




# Step 4 

## Display the Result

st.write(f"The Answer is: {result}")