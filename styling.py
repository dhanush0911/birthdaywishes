import streamlit as st

def apply_custom_styling(name):
    # Enhanced CSS with more subtle and modern design
    bg_style = '''
        <style>
            /* Full-screen background */
            body {
                background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
                background-size: 400% 400%;
                animation: gradientBG 15s ease infinite;
            }

            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            /* Page title styling */
            .stApp h1 {
                font-family: 'Arial', sans-serif;
                color: white;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                text-align: center;
                margin-bottom: 20px;
            }

            /* Section styling */
            .section {
                background: rgba(255,255,255,0.2);
                border-radius: 15px;
                padding: 20px;
                backdrop-filter: blur(10px);
                color: white;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                border: 1px solid rgba(255, 255, 255, 0.18);
                transition: all 0.3s ease;
            }

            .section:hover {
                transform: scale(1.02);
                box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.5);
            }

            /* Button styling */
            .stButton>button {
                background-color: white;
                color: #ff6b6b;
                border: none;
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: bold;
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }

            .stButton>button:hover {
                background-color: #ff6b6b;
                color: white;
                transform: translateY(-3px);
                box-shadow: 0 6px 8px rgba(0,0,0,0.2);
            }

            /* Import Animate.css */
            @import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css');
        </style>
    '''
    
    # Apply the styling
    st.markdown(bg_style, unsafe_allow_html=True)
    
    # Animated birthday title
    st.markdown(f"""
    <h1 class='animate__animated animate__pulse' style='text-align: center;'>
        🎉 HAPPY BIRTHDAY, {name.upper()}! 🎉
    </h1>
    """, unsafe_allow_html=True)