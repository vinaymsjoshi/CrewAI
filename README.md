# CrewAI
This app can be used to write catchy blogs on diverse topics using the CrewAI framework
# BLOG POST WRITER: Streamlit-Integrated AI Crew for Blog writing
This app can be used to write catchy blogs on diverse topics using the CrewAI framework, while highlighting the intricacies of the framework, including the visualisation of the interaction between the agents, the process flow and the final results, obtained as a result of the planned interactions between the agents based on the roles and goals assigned to them.

**Disclaimer**
The `streamlit run streamlit_input_from_user.py` takes the input for topic for the blog from the user and the `streamlit run streamlit_input_predefined.py` has a predefined topic for blog post: 'Uncover cutting-edge developments in AI and data science'. The `streamlit run streamlit_input_from_user.py` also visualises the process along with the final results. 

## Introduction

Blog Post Writer leverages the CrewAI framework to automate and enhance blog post writing, integrating a user-friendly Streamlit interface. This project demonstrates how autonomous AI agents can collaborate and execute complex tasks efficiently, now with an added layer of interactivity and accessibility through Streamlit.

## CrewAI Framework

CrewAI simplifies the orchestration of role-playing AI agents. In Blog Post Writer, these agents collaboratively work on the topic and craft a complete post on the topic, all accessible via a streamlined Streamlit user interface. It includes agents for research and content writing, along with a Streamlit app for user interaction.

## Streamlit Interface

The introduction of [Streamlit](https://streamlit.io/) transforms this application into an interactive web app, allowing users to easily input their preferences and receive tailored travel plans. The interace also shows the interaction between the agents, the task progress and the final results.

## Running the Application

To experience the app:

- **Configure Environment**: Set up the environment variables for [Serper](https://serper.dev/). Use the `secrets.example` as a guide to add your keys then move that file (`secrets.toml`) to `.streamlit/secrets.toml`.
- **GoogleAPI**: Mention your google_api_key in the blog_agents.py and blogpost.py, at the following location:
 llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0.6,
    google_api_key="API_KEY_HERE",
 )
- **Install Dependencies**: Execute `pip install -r requirements.txt` in your terminal.
- **Launch the App**: Run `streamlit run streamlit_input_from_user.py` to start the Streamlit interface.
- **IMPORTANT NOTE**: You may encounter the **INDEX OUT OF RANGE** error, in that case try reloading the webapp sometimes, it will sort the problem. it 

★ **Disclaimer**: The application uses gemini-pro by default. Ensure you have access to google's API.

## Details & Explanation

- **Streamlit UI**: The Streamlit interface is implemented in `streamlit_input_from_user.py`, where users can input their topiv name and requirements.
- **Components**:
  - `./blog_tasks.py`: Contains task prompts for the agents.
  - `./blog_agents.py`: Manages the creation of agents.
    The BlogAgents class defines two types of agents:

    **Researcher**:
    Role: Senior Research Analyst
    Goal: Research and uncover information about various topics
    Features: Conducts thorough research, identifies emerging trends, presents actionable insights
    Tools: Utilizes SearchTools.search_internet for internet research
    
    **Writer**:
    Role: Content Strategist
    Goal: Craft compelling content for blog posts on diverse topics based on the research of the researcher agent.
    Features: Writes insightful and engaging articles, transforms complex concepts into compelling narratives
  - `./streamlit_app.py`: The heart of the Streamlit app.

## Using GPT 3.5

To switch to GPT-3.5, pass the llm argument in the agent constructor, and also ensure that you have provided the OpenAI API key in the secrets.toml file mentioned above (note that these APIs are paid):

```python
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model='gpt-3.5') # Loading GPT-3.5

class BlogAgents:
    # ... existing methods

    def local_expert(self):
        return Agent(
            #same,
            tools=[SearchTools.search_internet],
            llm=llm,
            verbose=True
        )

```

## Using Local Models with Ollama

For enhanced privacy and customization, you can integrate local models like Ollama:

### Setting Up Ollama

- **Installation**: Follow Ollama's guide for installation.
- **Configuration**: Customize the model as per your requirements.

### Integrating Ollama with CrewAI

Pass the Ollama model to agents in the CrewAI framework:

```python
from langchain.llms import Ollama

ollama_model = Ollama(model="agent")

class BlogAgents:
    # ... existing methods

    def Agent(self):
        return Agent(
            #same,
            tools=[SearchTools.search_internet],
            llm=ollama_model,
            verbose=True
        )

```

## Benefits of Local Models

- **Privacy**: Process sensitive data in-house.
- **Customization**: Tailor models to fit specific needs.
- **Performance**: Potentially faster responses with on-premises models.
