import streamlit as st
import random

def guessing_game():
    secret_number = random.randint(1, 100)

    st.title("Number Guessing Game")

    st.write("""
        I'm thinking of a number between 1 and 10. Try to guess it!
        You have unlimited attempts, and I'll give you a hint if you're too high or too low.
    """)

    guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

    if st.button("Check Guess"):
        if guess < secret_number:
            st.write("Your guess is too low! Try again.")
        elif guess > secret_number:
            st.write("Your guess is too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the correct number: {secret_number}!")
            st.balloons()  

    if st.button("Start New Game"):
        secret_number = random.randint(1, 10) 

if __name__ == "__main__":
    guessing_game()
