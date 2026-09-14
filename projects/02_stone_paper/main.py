import random
import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Stone Paper Scissor",
    page_icon="🎮",
    layout="centered"
)

# ---------------- GAME STATE ---------------- #

if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "system_score" not in st.session_state:
    st.session_state.system_score = 0

if "result" not in st.session_state:
    st.session_state.result = "Choose your move!"

if "system_choice" not in st.session_state:
    st.session_state.system_choice = None

# ---------------- GAME LOGIC ---------------- #

choices = {
    1: "Stone",
    2: "Paper",
    3: "Scissor"
}


def play(user_choice):
    system_choice = random.randint(1, 3)

    st.session_state.system_choice = system_choice

    # Draw
    if user_choice == system_choice:
        st.session_state.result = (
            f"🤝 Draw!\n\n"
            f"Both chose **{choices[user_choice]}**"
        )
        return

    # User wins
    if (
            (user_choice == 1 and system_choice == 3) or
            (user_choice == 2 and system_choice == 1) or
            (user_choice == 3 and system_choice == 2)
    ):
        st.session_state.user_score += 1

        st.session_state.result = (
            f"🎉 You won this round!\n\n"
            f"You chose **{choices[user_choice]}**"
        )

    # System wins
    else:
        st.session_state.system_score += 1

        st.session_state.result = (
            f"😈 System won this round!\n\n"
            f"You chose **{choices[user_choice]}**"
        )


def reset_game():
    st.session_state.user_score = 0
    st.session_state.system_score = 0
    st.session_state.result = "Choose your move!"
    st.session_state.system_choice = None


# ---------------- UI ---------------- #

st.title("🎮 Stone Paper Scissor")

st.markdown(
    """
    ### Rules
    - 🪨 Stone beats ✂️ Scissor
    - 📄 Paper beats 🪨 Stone
    - ✂️ Scissor beats 📄 Paper
    - 🤝 Same choice = Draw
    - 🏆 First to **5 points** wins
    """
)

# ---------------- SCORE ---------------- #

col1, col2 = st.columns(2)

with col1:
    st.metric("👤 Your Score", st.session_state.user_score)

with col2:
    st.metric("🤖 System Score", st.session_state.system_score)

st.divider()

# ---------------- SYSTEM CHOICE ---------------- #

if st.session_state.system_choice is None:
    st.subheader("🤖 System")
    st.write("Waiting for your move...")
else:
    st.subheader("🤖 System")
    st.write(
        f"System chose **{choices[st.session_state.system_choice]}**"
    )

# ---------------- RESULT ---------------- #

st.info(st.session_state.result)

# ---------------- CHOICE BUTTONS ---------------- #

st.subheader("Choose your move")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Stone", use_container_width=True):
        play(1)

with col2:
    if st.button("📄 Paper", use_container_width=True):
        play(2)

with col3:
    if st.button("✂️ Scissor", use_container_width=True):
        play(3)

# ---------------- GAME OVER ---------------- #

if st.session_state.user_score == 5:
    st.success("🏆 You won the game!")

elif st.session_state.system_score == 5:
    st.error("🤖 System won the game!")

# ---------------- RESET ---------------- #

st.divider()

if st.button("🔄 Reset Game", use_container_width=True):
    reset_game()
    st.rerun()
