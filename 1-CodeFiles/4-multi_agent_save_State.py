import asyncio 
import os

import json
from autogen_agentchat.conditions import TextMentionTermination 
from multiAgent1 import givemebrain
from autogen_agentchat.agents import UserProxyAgent, AssistantAgent
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import MaxMessageTermination
from utils import givemebrain, close_model  , givemeazurebrain



async def main():
    print('Inside the main method')
    #model_client = await givemebrain()
    model_client = await givemebrain()
    print(model_client)
    print(model_client.component_version)

    agent1 = AssistantAgent(name="helper", model_client=model_client )

    agent2 = AssistantAgent(name="backup_helper", model_client=model_client )

    await Console(agent1.run_stream(task="my favorit color is blue ..."))
    agent_state = await agent1.save_state()
    print(agent_state)

    with open("state.json","w") as file:
        json.dump(agent_state, file,indent=3)


    with open("state.json","r") as file:
        fetch_state = json.load(file)

        await agent2.load_state(fetch_state)

    await Console(agent2.run_stream(task="tell me the history of my favorite color") )

    await close_model(model_client)




if __name__ =='__main__':
    asyncio.run(main())