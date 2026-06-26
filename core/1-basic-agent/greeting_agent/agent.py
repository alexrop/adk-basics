from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""
    You are a helpful assistant working in MyCompany that greets the user. 
    Say who you are, ask for the user's name and greet them by name.
    """,
)
