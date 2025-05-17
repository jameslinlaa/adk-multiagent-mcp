from google.adk.agents import SequentialAgent
from .sub_agents.netflix_db.agent import netflix_db_agent
from .sub_agents.search_agent.agent import search_agent


from . import prompt


root_agent = SequentialAgent(
    name="movie_agent",
    # model="gemini-2.0-flash",
    # description=prompt.ROOT_PROMPT,
    sub_agents=[
        netflix_db_agent,
        search_agent,
    ],
)



