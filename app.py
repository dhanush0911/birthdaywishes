import streamlit as st
import time
from styling import apply_custom_styling
from animations import add_animations
from interactions import add_interactive_elements

# Remove sidebar and set the page layout and icon
st.set_page_config(page_title="Birthday Celebration App", layout="centered", page_icon="🎂")

def birthday_wish(name="Birthday Star"):
    # Clear any existing layout
    st.empty()
    
    # Apply custom styling
    apply_custom_styling(name)
    
    # Add background music
    st.audio("./Song/song.mp3", format="audio/mp3", start_time=0)
    st.markdown("<style>audio{display: none;}</style>", unsafe_allow_html=True)
    
    # Trigger balloons and animations
    st.balloons()
    add_animations()
    
    # Initialize session state for the page counter
    if "page" not in st.session_state:
        st.session_state.page = 0
    
    # Define subpage content with larger, engaging messages and images
    subpages = [
        {
            "title": "✨ Heartfelt Birthday Wishes ✨", 
            "content": "Today is all about you! I feel so grateful every day for your unique spirit and the joy you bring. 🌸 Your journey, your laugh, and every little thing you do make my world so much better. Happy Birthday, my love!",
            "emoji": "🌟",
            "image": "./Photos/Birthday1.jpg"
        },
        {
            "title": "🎈 Special Messages for You 🎈", 
            "content": "Another year has passed, and you've only grown more amazing. Your kindness, strength, and beauty inspire me daily. Let’s make this year one filled with love and endless dreams. ❤️",
            "emoji": "🚀",
            "image": "./Photos/Birthday2.jpg"
        },
        {
            "title": "💫 Inspiring Birthday Quotes 💫", 
            "content": "\"The best way to predict your future is to create it.\" - Abraham Lincoln. 🌈 This year, paint your canvas with bold strokes and bright colors because you deserve a beautiful masterpiece!",
            "emoji": "🎨",
            "image": "./Photos/Birthday3.jpg"
        },
        {
            "title": "📸 Memories and Moments 📸", 
            "content": "Every moment with you is a memory I cherish. Thank you for being my partner, my love, and my best friend. Here’s to all the beautiful memories we’ve created and those yet to come. 🥂",
            "emoji": "📖",
            "image": "./Photos/Birthday4.jpg"
        },
        {
            "title": "🎁 Your Birthday Surprise 🎁", 
            "content": "Surprises await, and life has wonderful gifts in store just for you! 💝 May this year be full of happiness, surprises, and incredible adventures.",
            "emoji": "🎉",
            "image": "./Photos/Birthday5.jpg"
        },
        {
            "title": "🌟 Thank You for Celebrating with Us 🌟", 
            "content": "You are a gift to everyone around you. Your love and light make the world brighter. Thank you for being you, and happy, happy birthday, my love! 💕",
            "emoji": "❤️",
            "image": "./Photos/Birthday6.jpg"
        }
    ]
    
    # Create a container for content
    content_container = st.container()
    
    with content_container:
        # Display current page content
        page_content = subpages[st.session_state.page]
        
        # Emoji display
        st.markdown(f"<div style='text-align:center; font-size:4rem;'>{page_content['emoji']}</div>", unsafe_allow_html=True)
        
        # Page title
        st.markdown(f"<h2 style='text-align:center;'>{page_content['title']}</h2>", unsafe_allow_html=True)
        
        # Display image
        st.image(page_content["image"], caption=page_content["title"], use_column_width=True)
        
        # Page content
        st.markdown(f"<div style='text-align:center; font-size:1.5rem;'>{page_content['content']}</div>", unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.page > 0:
            if st.button("⬅️ Previous"):
                st.session_state.page -= 1
                st.rerun()
    
    with col3:
        if st.session_state.page < len(subpages) - 1:
            if st.button("Next ➡️"):
                st.session_state.page += 1
                st.rerun()

# Main app 
def main():
    # REPLACE THE NAME HERE ⬇️
    birthday_name = "JOhn Doe"
    
    # Direct call with the name
    birthday_wish(birthday_name)

# Run the main app
if __name__ == "__main__":
    main()
