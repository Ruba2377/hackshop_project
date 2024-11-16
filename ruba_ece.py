import streamlit as st
st.title ("Welcome to my portfolio")
st.subheader("Hi everyone,I am Rubalakshmi")
st.write("I am a student of ECE from KGiSL Institute of Technology")
st.header("Introduction")
st.write("I am much awaited to learn more about python and also to excel in electronics and communication stream")
st.header("Skills")
skills=["Python","Innoovative thinking","Communication"]
st.subheader("Here are my skills I bring to the table")
for skills in skills:
    st.write(f"-{skills}")
st.header("Projects")
projects=["Grade calculator","Basic Calculator","Ticket Booking"]
st.header("Here ae my projects I have worked on")
for projects in projects:
    st.write(f"-{projects}")
st.header("Contact")
st.subheader("You can contact me through my email id")
st.write("rubalakshmi2377@gmail.com")