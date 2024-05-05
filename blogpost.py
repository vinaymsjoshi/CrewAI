import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from search_tools import SearchTools

class blogposts:

    def __init__(self):
        self.output_placeholder = st.empty()


    def newblogpost(self):
        llm = ChatGoogleGenerativeAI(
            model = "gemini-pro",
            verbose = True,
            temperature = 0.6,
            google_api_key = "API_KEY_HERE"
        )

        search_tool = SerperDevTool()
        os.environ["SERPER_API_KEY"] = "API_KEY_HERE"

        # Initializing Agents
        researcher = Agent(
        role='Senior Research Analyst',
        goal='Uncover cutting-edge developments in AI and data science',
        backstory="""You work at a leading tech think tank. 
        Your expertise lies in identifying emerging trends. 
        You have a knack for dissecting complex data and presenting actionable insights.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[SearchTools.search_internet]
        )

        writer = Agent(
        role='Tech Content Strategist',
        goal='Craft compelling content on tech advancements',
        backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
        You transform complex concepts into compelling narratives.""",
        verbose=True,
        llm = llm,
        allow_delegation=True
        )

        # Create tasks for your agents
        task1 = Task(
        description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
        Identify key trends, breakthrough technologies, and potential industry impacts.""",
        expected_output="Full analysis report in bullet points",
        agent=researcher
        )
        task2 = Task(
        description="""Using the insights provided, develop an engaging blog
        post that highlights the most significant AI advancements.
        Your post should be informative yet accessible, catering to a tech-savvy audience.
        Make it sound cool, avoid complex words so it doesn't sound like AI.""",
        expected_output="Full blog post of at least 4 paragraphs",
        agent=writer
        )

        # Instantiating the crew with a sequential process
        crew = Crew(
        agents=[researcher, writer],
        tasks=[task1, task2],
        verbose=2
        )

        results = crew.kickoff()
        # self.output_placeholder.markdown(results)

        return results

