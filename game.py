import streamlit as st
import random

# Set up the Streamlit app
st.title("Simple Number Guessing Game")
st.write("I have selected a random number between 1 and 100. Try to guess it!")

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Input for the user's guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Button to submit guess
if st.button("Submit Guess"):
    if guess < random_number:
        st.write("Too low! Try again.")
    elif guess > random_number:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You guessed the number {random_number}.")

