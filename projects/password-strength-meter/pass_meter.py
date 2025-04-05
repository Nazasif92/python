import streamlit as st
import re
import string 
import random


st.markdown("""
    <style>
        .main {background-color: #f0f2f6;}
        .stTextInput>div>div>input {border-radius: 10px; font-size: 16px;}
        .stButton>button {border-radius: 10px; font-size: 16px; font-weight: bold;}
        .success {background-color: #D4EDDA; padding: 10px; border-radius: 10px;}
        .warning {background-color: #FFF3CD; padding: 10px; border-radius: 10px;}
        .error {background-color: #F8D7DA; padding: 10px; border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔐 Password Strength Checker & Generator</h1>", unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "password1", "123123", "admin", "123456789", "iloveyou", "1234", "adobe123", "123", "sunshine", "123321", "welcome", "princess", "abc123", "ashley", "0", "password123", "1", "welcome", "welcome1", "password12", "qazwsx", "trustno1", "admin", "monkey", "123111", "1234", "1qaz2wsx", "dragon", "12345", "123456a", "baseball", "123123", "football", "letmein", "1234567890", "1234", "12345", "123456", "1234567", "12345678", "123456789", "1234567890", "1", "12", "123", "1234", "12345", "123456", "1234567", "12345678", "123456789", "1234567890", "1234qwer", "123abc", "123asd", "123qwe", "123qweasd", "1qaz2wsx", "1qazxsw2", "1qazxsw@"]
    if password in common_passwords:
        return "❌ Password is too common. Choose a different one unique.", "Weak"  
    feedback = []
    if len(password) < 8:
        score += 1
    else:   
        feedback.append("❌ Password should be at least 8 characters long.")
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include both lowercase and uppercase characters.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&* etc.).")
    if score == 4:
        return "✅ Password is strong.", "Strong"
    elif score == 3:
        return "🟡 Moderate Password -Consider adding more security features", "Moderate"
    else:
        return "\n".join(feedback), "Weak"
    

st.subheader("🔍 Check Your Password Strength")
check_password = st.text_input("Enter your password", type="password")
if st.button("Check Password Strength"):
    if check_password:
        result, Strength = check_password_strength(check_password)
        if Strength == "Moderate":
            st.warning(result)
        elif Strength == "Strong":
            st.success(result)
            st.balloons()
        else:
            st.error("Password Weak Improve it by tips below")


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for i in range(length))

st.subheader("🔑 Generate a Secure Password")
password_length = st.number_input("Enter the password length", min_value=8, max_value=16, value=8, step=1)  

if st.button("Generate Password"):
    password = generate_password(password_length)
    st.success(f"Password: `{password}`")
    st.code(password, language="python")

st.markdown("<div class='footer'>Developed by ❤️ <b>Asif Ali</b></div>", unsafe_allow_html=True)
