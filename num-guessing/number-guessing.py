import streamlit as st
import random

st.set_page_config(page_title="Number-Guessing-Game")

st.title("Number Guessing Game")
st.markdown("""
						## Welcome to the Number Guessing Game""")

if "number" not in st.session_state:
   st.session_state.number=random.randint(1,100)
   st.session_state.attempts=0
   st.session_state.message=""
   
guess=st.number_input("Guess any number from 1-100.", min_value =1, max_value=100)

check = st.button("check")
if check:
    st.session_state.attempts += 1
    if guess> st.session_state.number:
        st.session_state.message= "Your guess is too high!"
    elif guess< st.session_state.number:
        st.session_state.message= "Your guess is too low!"
    else: 
        st.session_state.message=f"You've guessed it correctly in {st.session_state.attempts} attempts. "
    
st.write(st.session_state.message)

if st.button("Reset"):
       st.session_state.number=random.randint(1,100)
       st.session_state.attempts=0
       st.session_state.message=""
       st.success("Game has been reset! Play again.")