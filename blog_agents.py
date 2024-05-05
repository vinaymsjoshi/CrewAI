from crewai import Agent
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool
import os
from search_tools import SearchTools

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0.6,
    google_api_key="API_KEY_HERE",
)

def streamlit_callback(step_output, agent_name):
    # This function will be called after each step of the agent's execution
    st.markdown(f"## Agent: {agent_name}")
    st.markdown("---")
    for step in step_output:
        if isinstance(step, tuple) and len(step) == 2:
            action, observation = step
            if isinstance(action, dict) and "tool" in action and "tool_input" in action and "log" in action:
                st.markdown(f"# Action")
                st.markdown(f"**Tool:** {action['tool']}")
                st.markdown(f"**Tool Input** {action['tool_input']}")
                st.markdown(f"**Log:** {action['log']}")
                st.markdown(f"**Action:** {action['Action']}")
                st.markdown(
                    f"**Action Input:** ```json\n{action['tool_input']}\n```")
            elif isinstance(action, str):
                st.markdown(f"**Action:** {action}")
            else:
                st.markdown(f"**Action:** {str(action)}")

            st.markdown(f"**Observation**")
            if isinstance(observation, str):
                observation_lines = observation.split('\n')
                for line in observation_lines:
                    if line.startswith('Title: '):
                        st.markdown(f"**Title:** {line[7:]}")
                    elif line.startswith('Link: '):
                        st.markdown(f"**Link:** {line[6:]}")
                    elif line.startswith('Snippet: '):
                        st.markdown(f"**Snippet:** {line[9:]}")
                    elif line.startswith('-'):
                        st.markdown(line)
                    else:
                        st.markdown(line)
            else:
                st.markdown(str(observation))
        else:
            st.markdown(step)


class BlogAgents():

    def researcher(self):
        return Agent(
            role='Senior Research Analyst',
            goal='Research and uncover the information about various topics',
            backstory="""You are a skilled Research Analyst, adept at conducting thorough research 
            and presenting insights in an engaging manner. Your expertise spans a wide range of topics, 
            allowing you to provide information on various subjects.
            Your expertise lies in identifying emerging trends. 
            You have a knack for dissecting complex data and presenting actionable insights.""",
            verbose=True,
            allow_delegation=False,
            llm=llm,
            tools=[SearchTools.search_internet],
            step_callback=lambda step_output: streamlit_callback(step_output, "Researcher"),
        )

    def writer(self):
        return Agent(
            role='Content Strategist',
            goal='Craft compelling content for blog posts on diverse topics',
            backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
            You are recognized for your ability to craft compelling narratives on a wide range of topics. 
            Your writing skills and creativity enable you to produce engaging blog posts that captivate readers.
            You transform complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=True,
            llm=llm,
            step_callback=lambda step_output: streamlit_callback(step_output, "Writer"),
        )
