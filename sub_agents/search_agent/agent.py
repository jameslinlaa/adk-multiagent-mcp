from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

from . import prompt

search_agent = Agent(
   # A unique name for the agent.
   name="search_agent",
   # The Large Language Model (LLM) that agent will use.
   model="gemini-2.0-flash-exp", # Google AI Studio
   #model="gemini-2.0-flash-live-preview-04-09" # Vertex AI Studio
   # A short description of the agent's purpose.
   description="Agent to answer questions using Google Search.",
   # Instructions to set the agent's behavior.
   instruction=prompt.PROMPT,
   # Add google_search tool to perform grounding with Google search.
   tools=[google_search]
)
