import streamlit as st
import random
st.title("Simple Number Guessing Game")
st.write("I have selected a random number between 1 and 10. Try to guess it!")
random_number = random.randint(1, 10)
guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)
if st.button("Submit Guess"):
    if guess < random_number:
        st.write("Too low! Try again.")
    elif guess > random_number:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You guessed the number {random_number}.")
        st.balloons()  


