from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate
import os
import streamlit as st

class AINewsNode:
    def __init__(self, llm):
        """
        Initialize the AI News Node with API keys for tavily and groq.
        """
        self.tavily = TavilyClient()
        self.llm = llm

        #This is used to capture various steps in this file so that later can be use for steps shown
        self.state = {}

    def fetch_news(self, state:dict)->dict:
        """
        Fetch AI news based on the specified frequency.

        Args: 
            state (dict): The state dictionary containing 'frequency'.

        Returns:
            dict: Updated state with 'news_data' key containing fetched news.
        """
        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily':'d', 'weekly':'w', 'monthly':'m', 'year':"y"}
        days_map = {'daily':1, 'weekly':7, 'monthly':30, 'year':365}

        response = self.tavily.search(
            query="Top Artificial Intelligence(AI) technology news India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=20,
            days = days_map[frequency],
            # include_domain=["techcrunch.com", "venturebeat.com/ai", ... ] # Uncomment and add domains if needed
        )
        state['news_data'] = response.get("results", [])
        self.state['news_data'] = state['news_data']
        return state
    
    def summarize_news(self, state:dict)->dict:
        """
        Summarize the fetched news using an LLM.

        Args:
            state (dict): The state dictionary containing 'news_data'.
        Returns:
            dict: Updated state with 'summary' key containing the summarized news.
        """

        news_items = self.state['news_data']

        # prompt_template = ChatPromptTemplate.from_messages([
        #     ("system", """Summarize AI News articlws into markdown format. For each item includes:
        #      - Date in **YYYY-MM-DD** format in IST timezone
        #      - Concise sentences summary from latest news
        #      - Sort news by datewise (latest first)
        #      - Source URL as link
        #      Use format:
        #      ### [Date]
        #      - [Summary](URL)
        #      """),
        #      ("user", "Articles:\n{articles}")
        # ])
        prompt_template = ChatPromptTemplate.from_messages([
                        (
                        "system",
                        """
                        You are an AI news editor preparing a reader-friendly AI news digest.

                        GOAL:
                        Arrange news DATEWISE while making it easy and pleasant to read.

                        OUTPUT RULES:

                        1. Group news strictly by DATE.
                        2. Sort dates from latest → oldest.
                        3. Under each date:
                        - Merge similar articles.
                        - Write short insight-style bullet summaries.
                        - Do NOT repeat headlines.
                        4. Each bullet must explain WHAT happened + WHY it matters.
                        5. Use clean markdown formatting.

                        FORMAT:

                        # 🧠 {frequency} AI News Summary

                        ## 📅 DD Month YYYY
                        • Insight summary
                        • Insight summary
                        [Read more](URL)

                        ## 📅 DD Month YYYY
                        • Insight summary
                        [Read more](URL)

                        (continue datewise)

                        At the end add:

                        ### 🔎 Overall Trend
                        Write 3–4 sentences describing overall AI direction.

                        STYLE:
                        - Professional newsletter tone
                        - Concise
                        - Reader friendly
                        - No raw headlines
                        """
                        ),
                        ("user", "Articles:\n{articles}")
                        ])

        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}"
            for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str, frequency=self.state["frequency"]))
        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return self.state
    
    def save_result(self, state):
        frequency =self.state['frequency']
        summary = self.state['summary']
        foldername= "./AINews"
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        filename = f"{foldername}/{frequency}_summary.md"
        with open(filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        self.state['filename'] = filename
        return self.state



