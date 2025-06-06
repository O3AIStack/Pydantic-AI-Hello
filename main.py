# Hello World example from the Pydantic website (https://ai.pydantic.dev/#hello-world-example)

from pydantic_ai import Agent

agent = Agent(
    'google-gla:gemini-1.5-flash',
    system_prompt='Be concise, reply with one sentence',
)

result = agent.run_sync('Where does "Hello World" come from?')
print(result.output)

