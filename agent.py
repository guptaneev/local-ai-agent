from langchain_ollama import ChatOllama
from browser_use import Agent
from pydantic import SecretStr
import asyncio


# Initialize the model
llm=ChatOllama(model="qwen2.5", num_ctx=32000)

initial_actions = [
    {'open_tab': {'url': 'https://www.google.com/'}},
]

async def main():
    agent = Agent(
        task="Your task here",
        llm=llm
    )
    result = await agent.run()
    print(result)
    
asyncio.run(main())