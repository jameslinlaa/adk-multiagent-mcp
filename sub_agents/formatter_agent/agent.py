from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

from . import prompt

formatter_agent = Agent(
   # A unique name for the agent.
   name="formatter_agent",
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

# root_agent = search_agent


# from google.adk import Agent
# from google.adk.agents.callback_context import CallbackContext
# from google.adk.models import LlmResponse
# from google.adk.tools import google_search
# from google.genai import types

# from . import prompt


# def _render_reference(
#     callback_context: CallbackContext,
#     llm_response: LlmResponse,
# ) -> LlmResponse:
#     """Appends grounding references to the response."""
#     del callback_context
#     if (
#         not llm_response.content or
#         not llm_response.content.parts or
#         not llm_response.grounding_metadata
#     ):
#         return llm_response
#     references = []
#     for chunk in llm_response.grounding_metadata.grounding_chunks or []:
#         title, uri, text = '', '', ''
#         if chunk.retrieved_context:
#             title = chunk.retrieved_context.title
#             uri = chunk.retrieved_context.uri
#             text = chunk.retrieved_context.text
#         elif chunk.web:
#             title = chunk.web.title
#             uri = chunk.web.uri
#         parts = [s for s in (title, text) if s]
#         if uri and parts:
#             parts[0] = f'[{parts[0]}]({uri})'
#         if parts:
#             references.append('* ' + ': '.join(parts) + '\n')
#     if references:
#         reference_text = ''.join(['\n\nReference:\n\n'] + references)
#         llm_response.content.parts.append(types.Part(text=reference_text))
#     if all(part.text is not None for part in llm_response.content.parts):
#         all_text = '\n'.join(part.text for part in llm_response.content.parts)
#         llm_response.content.parts[0].text = all_text
#         del llm_response.content.parts[1:]
#     return llm_response


# search_agent = Agent(
#     model='gemini-2.0-flash',
#     name='search_agent',
#     instruction=prompt.PROMPT,
#     tools=[google_search],
#     after_model_callback=_render_reference,
# )