from google.adk.agents import Agent
from google.adk.tools.toolbox_tool import ToolboxTool

from . import prompt

toolbox = ToolboxTool("http://127.0.0.1:5000")

# Load all the tools
tools = toolbox.get_toolset(toolset_name='my_first_toolset')

netflix_db_agent = Agent(
    name="netflix_db_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about movies by movie name or the names of acters."
    ),
    instruction=prompt.PROMPT,  
    tools=tools,
)
