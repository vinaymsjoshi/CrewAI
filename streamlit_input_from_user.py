from crewai import Crew
from blog_agents import BlogAgents
from blog_tasks import BlogTasks
import streamlit as st

st.set_page_config(page_icon="B", layout="wide")


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


class BlogCrew:

    def __init__(self, topic):
        self.topic = topic
        self.output_placeholder = st.empty()

    def run(self):
        agents = BlogAgents()
        tasks = BlogTasks()

        researcher_agent = agents.researcher()
        writer_agent = agents.writer()

        research_task = tasks.task1(
            researcher_agent,
            self.topic,
        )
    
        writer_task = tasks.task2(
            writer_agent,
            self.topic,
        )

        crew = Crew(
            agents=[
                researcher_agent, writer_agent
            ],
            tasks=[research_task, writer_task],
            verbose=True
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)

        return result


if __name__ == "__main__":
    icon("BlogPost Writer")

    st.subheader("Let AI agents write catchy blogs for you!",
                 divider="rainbow", anchor=False)

    with st.sidebar:
        st.header("👇 Enter the topic of your interest here")
        with st.form("my_form"):
            topic = st.text_input(
                "What topic you want a blog on?", placeholder="Recent Advancements in AI/ Crypto")

            submitted = st.form_submit_button("Submit")

        st.divider()

if submitted:
    with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
            blog_crew = BlogCrew(topic)
            result = blog_crew.run()
        status.update(label="✅ Blog Post Ready!",
                      state="complete", expanded=False)

    st.subheader("Here is your Blog Post", anchor=False, divider="rainbow")
    st.markdown(result)
