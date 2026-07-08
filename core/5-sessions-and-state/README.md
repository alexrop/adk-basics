# Sessions and State Management in ADK

This example demonstrates how to create and manage stateful sessions in the Agent Development Kit (ADK), enabling your agents to maintain context and remember user information across interactions.

## What Are Sessions in ADK?

Sessions in ADK provide a way to:

1. **Maintain State**: Store and access user data, preferences, and other information between interactions
2. **Track Conversation History**: Automatically record and retrieve message history
3. **Personalize Responses**: Use stored information to create more contextual and personalized agent experiences

Unlike simple conversational agents that forget previous interactions, stateful agents can build relationships with users over time by remembering important details and preferences.

| **Component** | **Definition**                                                                 | **Purpose**                                         |
|---------------|----------------------------------------------------------------------------------|-----------------------------------------------------|
| **Session**   | A single execution of one or more agents working on a defined task or goal.     | Sets up agents, tools, context, and objective.      |
| **State**     | A shared memory where all agents can read and write information.                | Stores variables, messages, and intermediate results.|
| **Runner**    | The engine that executes the session and coordinates the agents' actions.        | Manages the control flow of the agent execution.     |

The natural sequence to understand those above elements is:

1. User message
2. Runner Session
3. Runner Agents
4. Agent
5. LLM / Tool
6. Update session
7. Agent response

## Example Overview

This directory contains a basic stateful session example that demonstrates:

- Creating a session with user preferences
- Using template variables to access session state in agent instructions
- Running the agent with a session to maintain context

The example uses a simple question-answering agent that responds based on stored user information in the session state.

## Project Structure

```
5-sessions-and-state/
│
├── basic_stateful_session.py      # Main example script
│
└── question_answering_agent/      # Agent implementation
    ├── __init__.py
    └── agent.py                   # Agent definition with template variables
```

## Getting Started

### Setup

1. Activate the virtual environment from the root directory:
```bash
# macOS/Linux:
source ../.venv/bin/activate
# Windows CMD:
..\.venv\Scripts\activate.bat
# Windows PowerShell:
..\.venv\Scripts\Activate.ps1
```

2. Create a `.env` file and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

### Running the Example

1. Navigate to the 5-sessions-and-state directory containing your agent folder.
2. Run the example to see a stateful session in action:
```bash
python basic_stateful_session.py
```

This will:
1. Create a new session with user information
2. Initialize the agent with access to that session
3. Process a user query about the stored preferences
4. Display the agent's response based on the session data

## Key Components

### Session Service

The example uses the `InMemorySessionService` which stores sessions in memory:

```python
session_service = InMemorySessionService()
```

### Initial State

Sessions are created with an initial state containing user information:

```python
initial_state = {
    "user_name": "Alexander Ulloa",
    "user_preferences": """
        I like to play Tennis, Football, and Basketball.
        My favorite food is Italian.
        My favorite TV show is Breaking Bad.
        Loves it when people are interested in Artificial Intelligence.
    """,
}
```

### Creating a Session

The example creates a session with a unique identifier:

```python
stateful_session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
```

### Accessing State in Agent Instructions

The agent accesses session state using template variables in its instructions:

```python
instruction="""
You are a helpful assistant that answers questions about the user's preferences.

Here is some information about the user:
Name: 
{user_name}
Preferences: 
{user_preferences}
"""
```

### Running with Sessions

Sessions are integrated with the `Runner` to maintain state between interactions:

```python
runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service,
)
```

## Additional Resources

- [Google ADK Sessions Documentation](https://google.github.io/adk-docs/sessions/session/)
- [State Management in ADK](https://google.github.io/adk-docs/sessions/state/)
