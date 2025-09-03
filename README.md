# ADK Basics

Flexible and modular framework for developing basics AI agents using ADK.

## Getting Started

Create a virtual environment following these steps to set it up:

```bash
# Create virtual environment in the root directory
python -m venv .venv

# Activate (each new terminal)
# macOS/Linux:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate.bat
# Windows PowerShell:
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Once set up, this single environment will work for all examples in the repository.

## Topics

### Core
1. **Basic Agent:** Introduction to the simplest form of ADK agents. Learn how to create a basic agent that can respond to user queries.
2. **Tool Agent:** Learn how to enhance agents with tools that allow them to perform actions beyond just generating text.
3. **LiteLLM Agent:** Example of using LiteLLM to abstract away LLM provider details and easily switch between different models.
4. **Structured Outputs:** Learn how to use Pydantic models with `output_schema` to ensure consistent, structured responses from your agents.
5. **Sessions and State:** Understand how to maintain state and memory across multiple interactions using sessions.
6. **Persistent Storage:** Learn techniques for storing agent data persistently across sessions and application restarts.
7. **Multi-Agent:** See how to orchestrate multiple specialized agents working together to solve complex tasks.
8. **Stateful Multi-Agent:** Build agents that maintain and update state throughout complex multi-turn conversations.
9. **Callbacks:** Implement event callbacks to monitor and respond to agent behaviors in real-time.
10. **Sequential Agent:** Create pipeline workflows where agents operate in a defined sequence to process information.
11. **Parallel Agent:** Leverage concurrent operations with parallel agents for improved efficiency and performance.
12. **Loop Agent:** Build sophisticated agents that can iteratively refine their outputs through feedback loops.

### Demo
1. Calendar Voice Agent: Create a Google Calendar integration based on ADK Voice Assistant (Jarvis)

## Official Documentation

For more detailed information, check out the official ADK documentation:

- ADK Quickstart: https://google.github.io/adk-docs/get-started/quickstart
- ADK Samples: https://github.com/google/adk-samples
- Gemini API documentation: https://ai.google.dev/gemini-api/docs/models