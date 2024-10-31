import streamlit as st
import random

def add_animations():
    # Enhanced confetti and particle animation
    st.markdown("""
    <script>
    function createConfetti() {
        const colors = ['#ff6b6b', '#4ecdc4', '#45aaf2', '#ffca28', '#ff9a8b'];
        const container = document.body;
        
        function createParticle() {
            const particle = document.createElement('div');
            particle.classList.add('birthday-particle');
            
            particle.style.left = Math.random() * 100 + 'vw';
            particle.style.top = Math.random() * 100 + 'vh';
            particle.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            particle.style.animationDuration = (Math.random() * 3 + 2) + 's';
            
            container.appendChild(particle);
            
            // Remove particle after animation
            setTimeout(() => {
                container.removeChild(particle);
            }, 5000);
        }

        // Create multiple particles
        for (let i = 0; i < 300; i++) {
            createParticle();
        }
    }

    // Trigger animations on page load
    window.onload = createConfetti;
    </script>
    <style>
    .birthday-particle {
        position: fixed;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        z-index: 9999;
        pointer-events: none;
        animation: particle-fall linear infinite;
        opacity: 0.7;
    }

    @keyframes particle-fall {
        0% {
            transform: translateY(-10vh) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(110vh) rotate(360deg);
            opacity: 0;
        }
    }
    </style>
    """, unsafe_allow_html=True)