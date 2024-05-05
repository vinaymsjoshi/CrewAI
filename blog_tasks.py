from crewai import Task
from textwrap import dedent

class BlogTasks():

    def task1(self,agent,topic):
        return Task(description=dedent(f"""
            Conduct a comprehensive analysis on a topic of interest. 
            This could be anything from a specific industry, emerging technology, societal trend, or scientific development.
            Utilize available resources such as research papers, articles, and data sources to gather information.
            Identify information relevant with the chosen topic, catering the specific needs of the topic.
            Provide a detailed report summarizing your findings, including insights and recommendations for further exploration.
            {self.__tip_section()}

            Blog topic: {topic}
            """),
            expected_output="Full analysis report with insights and recommendationsin bullet points",
            agent=agent
        )
        
    def task2(self,agent,topic):
        return Task(description=dedent(f"""
            Using the insights provided by the researcher, develop an engaging blog
            post that highlights the the most significant aspects of the topic.
            Your post should be informative yet accessible, catering to a tech-savvy audience.
            Make it sound cool, avoid complex words so it doesn't sound like AI.
            Ensure to incorporate the key findings and recommendations from the research report.
            {self.__tip_section()}

            Blog topic: {topic}
            """),
        expected_output="Full blog post of at least 4 paragraphs",
        agent=agent
        )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100 and grant you any wish you want!"