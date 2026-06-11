import os
from dotenv import load_dotenv
import asyncio
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console
from utils import givemebrain
from autogen_ext.tools import mcp
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

        jira_server =StdioServerParams(command = "uvx.exe" ,  args = ["mcp-atlassian"] ,
                                       env ={

        "JIRA_URL": JIRA_URL,
        "JIRA_USERNAME":JIRA_USERNAME,
        "JIRA_API_TOKEN": JIRA_API_TOKEN,
                                       } ,read_timeout_seconds=60   )
        print(jira_server.args)

        jira_server_wb = McpWorkbench(jira_server)
        async with jira_server_wb as wb:
            assistant = AssistantAgent(model_client=model_client , name="jira", workbench=wb,system_message="You are a helpful jiraagent and your job is go into the website and under project and look for all the available open jira bugs and we would need to address them.")


            await Console(assistant.run_stream(task="Hi please tell me the list of all available Jira bugs and print the summary or description section about them. "))

            await model_client.close()
            await assistant.close()
    except Exception as e:
        print(f"Error is >>>>>>>>>>>>>>>> {e}")
        
asyncio.run(main())


