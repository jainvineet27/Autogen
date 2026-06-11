import json 
import os

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat 
from utils import givemebrain
from dotenv import load_dotenv
import asyncio
from autogen_agentchat.agents import AssistantAgent , UserProxyAgent
from autogen_agentchat.ui import Console
from autogen_ext.tools import mcp 
from autogen_ext.tools.mcp import StdioServerParams ,McpWorkbench



async def main():
    print("Hi we are running our code..")
    
    jira_server =  StdioServerParams()
    
    playwright_server =StdioServerParams()
    
    jira_server_wb =McpWorkbench(jira_server)
    playwright_server_wb  = McpWorkbench(playwright_server)
    
    async with jira_server_wb , playwright_server_wb as (jira_wb , playwright_wb):
        
        model_client = await givemebrain()
        jira_agent = AssistantAgent(model_client=model_client , name="playwright", workbench=jira_wb,system_message="You are a helpful Agent..")
        
        playwright_agent = AssistantAgent(name="playwright", model_client = model_client ,workbench=playwright_wb, system_message="")
        
        team = RoundRobinGroupChat(participants=[jira_agent , playwright_agent],termination_condition=TextMentionTermination('LESSON COMPLETE'))

        await Console(team.run_stream(task="Hi Can you please open browser and search for python aysncio pause for 10 seconds and then todays news in separate tabs "))

        await model_client.close()
        await jira_agent.close()
        await playwright_agent.close()
    
    
    
    
    


asyncio.run(main())