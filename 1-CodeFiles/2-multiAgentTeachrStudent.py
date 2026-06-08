import asyncio
import os
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent

from  multiAgent1 import givemebrain



async def main():
    print('inside main methdod..')
    model_client = await givemebrain()
    print(model_client)

    agent1 = AssistantAgent(name="teacher", model_client=model_client , system_message="You are superb math teacher and you need to explain the maths concept to class 1 to class 5 sutdents, explain concepts clearly, like a teacher")
    agent2 = AssistantAgent(name="student", model_client=model_client , system_message="I am curios student would like to learn math exspcially probability")
    
    vineet = UserProxyAgent(name="vineet")

    team = RoundRobinGroupChat(participants=[agent1, agent2] , termination_condition=MaxMessageTermination(max_messages=6))

    await Console(team.run_stream(task='let us begin learning probability head or tails'))


if __name__=='__main__':
    asyncio.run(main())


