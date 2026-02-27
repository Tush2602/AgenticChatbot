import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json
import re


def clean_if_reasoning_present(text: str):
    if "<think>" in text:
        text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return text.strip()


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase=="Basic Chatbot":
            for event in graph.stream({"messages": ("user", user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)

                    with st.chat_message("assistant"):
                        response = value['messages'].content
                        response = clean_if_reasoning_present(response)
                        st.write(response)

                    