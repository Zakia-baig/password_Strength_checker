import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Great length!")
    elif len(password) >= 8:
        score += 1
        feedback.append("⚠️ Good length, but could be longer")
    else:
        feedback.append("❌ Password is too short (use 8+ characters)")
    
    # Check for letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Good mix of uppercase and lowercase")
    else:
        feedback.append("❌ Use both uppercase and lowercase letters")
    
    # Check for numbers
    if re.search(r'\d', password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Add some numbers")
    
    # Check for symbols
    if re.search(r'[!@#$%^&*]', password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Add special characters (!@#$%^&*)")
    
    return score, feedback

# Page setup with custom theme
st.set_page_config(page_title="Password Checker", page_icon="🔐", layout="centered")

# Custom CSS for better styling
st.markdown("""
<style>
    .main-title {
        color: #FF6B6B;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        padding: 20px;
    }
    .password-display {
        background-color: #4ECDC4;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-family: monospace;
        margin: 20px 0;
    }
    .stButton button {
        background-color: #FF6B6B;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
    }
    .info-box {
        background-color: #F7F7F7;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with tips
with st.sidebar:
    st.title("📚 Password Tips")
    
    st.markdown("### ✅ Strong Password Guidelines")
    st.markdown("""
    - At least 12 characters long
    - Mix of uppercase & lowercase
    - Include numbers (0-9)
    - Use special characters (!@#$%^&*)
    """)
    
    st.markdown("### ❌ What to Avoid")
    st.markdown("""
    - Personal information
    - Common words
    - Simple patterns (123456)
    - Keyboard patterns (qwerty)
    - Repeated characters
    """)
    
    st.markdown("### 💡 Pro Tips")
    st.markdown("""
    1. Use phrases you can remember
    2. Replace letters with numbers
    3. Add special characters in middle
    4. Use different passwords for each account
    """)
    
    st.markdown("### 🔍 Examples")
    st.info("""
    Weak: Password123
    Better: P@ssw0rd123!
    Best: Tr@ff1c_L1ght_96!
    """)

# Main content
st.markdown("<h1 class='main-title'>🔒 Password Strength Checker 🔒</h1>", unsafe_allow_html=True)

# Main container
with st.container():
    # Password input
    st.markdown("### 🔑 Enter Your Password")
    password = st.text_input("", type="password")
    
    show_password = st.checkbox("Show password")
    if show_password:
        st.code(password)

    # Check button
    if st.button("📊 Check Password Strength", use_container_width=True):
        if not password:
            st.error("🚨 Please enter a password!")
        else:
            score, feedback = check_password_strength(password)
            
            # Display strength score
            st.markdown("### 💪 Password Strength")
            progress = (score / 5) * 100
            st.progress(progress / 100)
            
            # Strength label
            if score >= 4:
                st.success("🔒 Strong Password!")
            elif score >= 3:
                st.warning("🔓 Moderate Password")
            else:
                st.error("⚠️ Weak Password")
            
            # Display feedback
            st.markdown("### 📝 Password Analysis")
            for item in feedback:
                st.write(item)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Keep your accounts secure with strong passwords! 🛡️<br>"
    "Stay Safe Online! 🌟"
    "</div>", 
    unsafe_allow_html=True
)