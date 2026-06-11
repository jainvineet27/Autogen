import os
from dotenv import load_dotenv
import asyncio
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console
from utils import givemebrain
from autogen_ext.tools import mcp
from autogen_agentchat.conditions import MaxMessageTermination ,TextMentionTermination
from autogen_ext.tools.mcp import StdioServerParams , McpWorkbench


async def main():
    try: 
        print("Inside th project")
        load_dotenv()
        JIRA_URL=os.getenv("JIRA_URL")
        JIRA_USERNAME=os.getenv("JIRA_USERNAME")
        JIRA_API_TOKEN =os.getenv("JIRA_API_TOKEN")
        # declare the variable 

        model_client = await givemebrain()
        print(model_client.component_description)

        playwright_server =StdioServerParams(command =r"C:\Program Files\nodejs\npx.cmd",
        args = ["@playwright/mcp@latest"] 
        ,read_timeout_seconds=60   
        )
        print(playwright_server.args)

        playwright_server_wb = McpWorkbench(playwright_server)
        
        
        async with playwright_server_wb as wb:
            assistant = AssistantAgent(model_client=model_client , name="playwright", workbench=wb,system_message="You are a helpful Agent..")


            await Console(assistant.run_stream(task="Hi Can you please open browser and search for python aysncio pause for 10 seconds and then todays news in separate tabs "))

            await model_client.close()
            await assistant.close()
    except Exception as e:
        print(f"Error is >>>>>>>>>>>>>>>> {e}")
        
asyncio.run(main())


