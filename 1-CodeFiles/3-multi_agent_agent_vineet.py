import asyncio 
import os

from autogen_agentchat.conditions import TextMentionTermination 
from multiAgent1 import givemebrain
from autogen_agentchat.agents import UserProxyAgent, AssistantAgent
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import MaxMessageTermination
from utils import givemeollamabrain, close_model



async def main():
    print('Inside the main method')
    #model_client = await givemebrain()
    model_client = await givemebrain()
    print(model_client)
    print(model_client.component_version)

    agent1 = AssistantAgent(name="teacher", model_client=model_client , system_message="explain concepts clearly, like a teacher when the user says thank you or something similar and has no further questions then acknowledge by saying LESSON COMPLETE to complete the session")

    user = UserProxyAgent(name="vineet")

    team = RoundRobinGroupChat(participants=[user, agent1],termination_condition=TextMentionTermination(text='LESSON COMPLETE'))

    await Console(team.run_stream(task="Alright let us begin the conversation ..."))

    await model_client.close()


if __name__ =='__main__':
    asyncio.run(main())