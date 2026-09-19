import streamlit as st
from src.model import ChatbotModel
from src.voice_assistant import VoiceAssistant

def launch_gui():
    st.set_page_config(page_title="AI Chat Assistant", page_icon="🤖")
    st.title("🤖 AI Chat Assistant (Python + NLP)")

    if "bot" not in st.session_state:
        st.session_state.bot = ChatbotModel()
    if "voice" not in st.session_state:
        st.session_state.voice = VoiceAssistant()
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Voice Input Control
    enable_voice = st.sidebar.checkbox("Enable Voice Response")
    if st.sidebar.button("🎤 Speak Input"):
        voice_text = st.session_state.voice.listen()
        if voice_text:
            st.session_state.messages.append({"role": "user", "content": voice_text})
            response = st.session_state.bot.match_intent(voice_text)
            st.session_state.messages.append({"role": "assistant", "content": response})
            if enable_voice:
                st.session_state.voice.speak(response)
            st.rerun()

    # Text Input Control
    if user_input := st.chat_input("Type your message here..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        response = st.session_state.bot.match_intent(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

        if enable_voice:
            st.session_state.voice.speak(response)
