import os 
import json 
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.agents import UserProxyAgent, AssistantAgent
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import RoundRobinGroupChat , SelectorGroupChat
import asyncio
from utils import givemebrain , close_model 

async def main():
    print("isndie selector group chat class")

    model_client= await givemebrain()
    if model_client:
        researcher= AssistantAgent(name="researcher", model_client=model_client , system_message="you are a reasearche your work is to find the latest information and make it available for the another agent to pick")

        writer = AssistantAgent(name="writer", model_client=model_client , system_message="You are a writer agent based on the information you recieved from the reasercher agent make a small 5-6 lines of articles ")
        
        critic = AssistantAgent(name="critic", model_client=model_client , system_message="Based on the article which has been written by the writer , cricit , pressure test it and once you make it pass then say TERMINATE to end the sessions")

        max_text_termination = TextMentionTermination("TERMINATE")

        max_terminate_limt = MaxMessageTermination(max_messages=4)

        terminate = max_terminate_limt | max_text_termination

        team = SelectorGroupChat(participants=[critic,researcher ,writer] , 
                                 allow_repeated_speaker=True,
                                 model_client=model_client, 
                                 termination_condition=terminate)
    
        await Console(team.run_stream(task="You are a helpful assistant, Reasearch about  Intenrational school and specfically jobs for biology and science teacher Netherlands"))

        await close_model(model_client=model_client)
        



        



if __name__=="__main__":
    asyncio.run(main())