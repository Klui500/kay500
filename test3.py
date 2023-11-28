import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Webpage", page_icon="smile:", layout="wide")

#1. as horizontal menu
with st.sidebar:
    selected = option_menu(
        menu_title=None, #required # if you do not wish to put the ---- MAIN MENU ----
        options=["Home", "Account", "Services", "Contacts"], #required
        icons=["house", "person", "book", "envelope"], #optional
        menu_icon="cast", #optional
        default_index=0, #optional
        orientation="vertical",
    )
if selected == "Home":
    st.header(f"Welcome to :red[Klui E-tronics]")
    st.header(f":red[Your no.1 computer software service center]")
if selected == "Account":
    st.title(f"Create account/login")
    choices = st.selectbox('Login/signup', ['Login', 'sign Up'])
    if choices=='Login':
        

        email=st.text_input('Email Address')
        password = st.text_input('Password', type= 'password')

        st.button('Login')



    else:
        email=st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        username = st.text_input('Enter yuor unique username')

        st.button('Create my account')

if selected == "Services":
    with st.container():
         st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header(":red[We deal with the following services:]")
    st.write(f""" 
    
    - RAM installation and replacement for both desktop and PC
    - Hard drive space clean up and re-creation
    - Hard drive partioning 
    - ANTI-virus installation
    - Microsoft office installation and activation
    - Windows activation 
    - Operating system change and installaton for all kinds of OS, E.g; windows, Linux and Apple etc.
             """)
if selected == "Contacts":
    st.header(":red[:mailbox: Get in touch with me!]")
    st.write(f"""
             - 0974343883
             - 0957302208
             - email us on kasandainnocent21@gmail.com
             """)


