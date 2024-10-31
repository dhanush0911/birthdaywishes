import streamlit as st
import time
from styling import apply_custom_styling
from animations import add_animations
from interactions import add_interactive_elements

# Remove sidebar and set the page layout and icon
st.set_page_config(page_title="Happy Birthday Kitty 😻", layout="centered", page_icon="🎂")

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
            "title": "💖 Celebrating You, My Love 🌹💫",
            "content": """Happy Birthday to the most amazing person in my world! 🥳💕
            I pray this year brings you boundless happiness, endless laughter, and the fulfillment of every dream you’ve wished for 🤩✨
            You deserve all the love and joy the world has to offer, and I’m beyond grateful to be by your side through it all 😍
            Here’s to more memories, more laughter, and more love in the days to come🥹
            Happy Birthday, my love! 🎂💖🎉""",
            "emoji": "🎂",
            "image": "./Photos/Birthday1.jpg"
        },
        {
            "title": "🎈 To the Love of My Life on Your Special Day 🎂💘",
            "content": """Today, I celebrate not just your special day but every single, unforgettable moment we’ve shared. 💞✨ 
            This day is so deeply precious to me because it’s when the most beautiful, kind-hearted, and truly remarkable person came into the world – and that’s you. 🌎💖 
            From the day we started dating, you’ve filled my life with a love and happiness I never even knew was possible. 🥺
            The way you make me feel is beyond words; no one else could ever make me feel as loved, understood, and cherished as you do. 😌💫 
            You are my everything, my joy, my heart, and this day is sacred to me because it marks the start of *you,* the one who completes my world. 🥰🌹
            I feel like the luckiest person alive to have you by my side, and I can’t wait to keep making beautiful memories together, wrapped in laughter, love, and endless happiness. 🎉💖 
            So here’s to you, my love, on this incredible day – may it be as amazing as you are, because you deserve nothing less. Happy Birthday, my one and only! 🎂🎈💘""",
            "emoji": "✨",
            "image": "./Photos/Birthday2.jpg"
        },
        {
            "title": "💫 Every Moment, Every Memory with You 💖✨",
            "content": """You already know just how much you mean to me and how deeply I love you, baby. 💖
            All I ever want is to see you happy and smiling because your happiness is my happiness. 😊💕
            You’re a part of every moment of my day – from waking up to your sweet 'Good morning' messages 🌅💌,
            to talking to you throughout the day 💬,
            to our late-night chats 🌙
            and those 'Good night' messages that make me feel close to you even when we’re apart. 🥹
            Without all these, my day would feel empty – you truly complete every moment of my life. 💫
            Every day, I find myself falling more and more in love with you,
            and it only grows deeper as I learn more about you. 🥰💕
            I want to know everything about you,
            to be there through every moment,
            sharing all the laughter, joy, and memories that life has in store.
            I love you endlessly, baby. ❤️""",
            "emoji": "😌",
            "image": "./Photos/Birthday3.jpg"
        },
        {
            "title": "To My Adorable Drama Queen 👑💖",
            "content": """Every moment with you is a memory I cherish. Thank you for being my partner, my love, and my best friend.
            Here’s to all the beautiful memories we’ve created and those yet to come. 🥂
            I love your drama! 😆💃
            You’re my one and only drama queen 😚💫
            and I adore every bit of it. 👑💖
            Honestly, I treasure all your little dramatic moments I even like to keep those recordings with me 🎥💕.
            When I’m missing you, I just watch them, and it feels like you’re right here with me. 🥺💞
            I love everything you do – every cute, funny, and dramatic thing it’s all so adorable and *so you*. 🥰😘
            You bring so much joy into my life, and I can’t thank you enough for being you. 🌹💖
            Love you, my precious drama queen! 😘""",
            "emoji": "👸🏻",
            "image": "./Photos/Birthday4.jpg"
        },
        {
            "title": "To My Sweetest, Cutest Love 🥹💖",
            "content": """You are the cutest, most adorable human being I’ve ever met on this planet, baby 🥹💖
            You are simply the best, my love! 💫
            Just looking at you gives me endless reasons to love you even more. 🥹
            You’re my cutest little baccha 😚💞, and I swear, I get lost every time I look at you –
            just thinking, 'How can anyone be so incredibly pretty and adorable?' 🥰🌹
            I completely lose it when I see you; everything you do is just pure cuteness and sweetness, baby! 😘💖
            I’m endlessly in love with you, and my heart is all yours.
            I love you so, so much, my cutu! 💝""",
            "emoji": "😚",
            "image": "./Photos/Birthday5.jpg"
        },
        {
            "title": "Thank You for Being My Everything 💖🌹",
            "content": """You are a gift to me. Your love and light have made my world brighter.
            Thank you for being you, and loving me so much! 💕
            I can’t thank you enough for being in my life and making it so incredibly beautiful. 💫💕
            Your presence has changed everything for the better and left such a deep impact on me. 😇
            You’ve helped me grow, shaping me into someone who knows how to cherish and care for his queen. 👑❤️
            You’ve taught me so much and brought out the best in me, showing me what love and happiness truly feel like. 😌
            The memories, the joy, the warmth, and the endless love you’ve given me – it’s all more than I could ever ask for. 🥹💖
            I am beyond grateful for every moment, every smile, and every bit of love you share with me. ♥️
            Thank you for being my everything, baby. Happiest Birthday to you, my love! 😘🎉🎂""",
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
    birthday_name = "Kitty 😻"
    
    # Direct call with the name
    birthday_wish(birthday_name)

# Run the main app
if __name__ == "__main__":
    main()
