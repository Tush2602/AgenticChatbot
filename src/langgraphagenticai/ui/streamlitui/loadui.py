import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config =Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        if "timeframe" not in st.session_state:
            st.session_state.timeframe = ""

        if "IsFetchButtonClicked" not in st.session_state:
            st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            st.subheader("Configuration")
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            ##LLM Selection
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)

            if self.user_controls['selected_llm'] == "Groq":
                # Model selection

                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Groq Model", model_options)
                self.user_controls['GROQ_API_KEY'] = st.session_state["GROQ_API_KEY"] = st.text_input("Enter Groq API Key", type="password")

                #validate API key
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("⚠️ Please enter your Groq API Key to proceed. Don't have one? Get it from https://console.groq.com/keys") 
                    st.stop()  # Stop execution until API key is provided

            # Usecase Selection
            self.user_controls['selected_usecase'] = st.selectbox("Select Usecase", usecase_options)

            if self.user_controls["selected_usecase"]=="Chatbot With Web" or self.user_controls["selected_usecase"]=="AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls['TAVILY_API_KEY'] = st.session_state["TAVILY_API_KEY"] = st.text_input("Enter Tavily API Key for web search capability", type="password")

                if not self.user_controls['TAVILY_API_KEY']:
                    st.warning("⚠️ Please enter your Tavily API Key to proceed. Don't have one? Get it from https://www.tavily.com/dashboard/api-keys") 
                    st.stop()  # Stop execution until API key is provided
    

            if self.user_controls["selected_usecase"]=="AI News":
                st.subheader("📝 AI News Explorer ")

                time_frame= st.selectbox(
                    "🗓️ Select time frame",
                    ["Daily", "Weekly", "Monthly"],
                    index =0
                )
                if st.button("🔍 Fetch latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

        return self.user_controls
    