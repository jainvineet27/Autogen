import asyncio
import os 
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.azure import  AzureAIChatCompletionClient
from utils import givemebrain, close_model , givemeazurebrain , azureopenai_model
from dotenv import load_dotenv  


load_dotenv()


async def main():
    print()

    model_client = await givemeazurebrain()
    print(model_client)
 

    assistant = AssistantAgent(name="teacher", model_client=model_client,system_message="You are helpful math teacher explain concepts luci and clear fashion if user understood and reply by sayign thank you then say LESSON COMPLETE to close the session")

    await Console(assistant.run_stream(task="Who are you , which envioronment you fall in "))



asyncio.run(main())