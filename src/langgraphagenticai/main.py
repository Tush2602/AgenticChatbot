import streamlit as st
import os
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM 
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agneticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.
    """

    ##Load ut 
    ui = LoadStreamlitUI()
    user_inputs = ui.load_streamlit_ui()

    if not user_inputs:
        st.warning("⚠️ Please provide the necessary inputs to proceed.")
        st.stop()

    user_message = st.text_input("Enter your message:")

    if user_message:
        try:
            #configure llm
            obj_llm_config = GroqLLM(user_controls_input=user_inputs)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.warning("⚠️ LLM model configuration failed. Please check your settings.")
                return 
            
            usecase = user_inputs.get('selected_usecase')
            if not usecase:
                st.warning("⚠️ Use case selection is required. Please select a use case to proceed.")
                return
            
            #Graph builder 
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error building graph: {str(e)}")
                return

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            return