import os 
import json
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent,UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination , TextMentionTermination
from autogen_core.models import ModelInfo
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_ext.tools.mcp import McpServerParams , McpWorkbench ,StdioServerParams
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
import asyncio
from utils import close_model , givemebrain, givemeollamabrain 

load_dotenv()

base_path = os.getcwd()
folder  ="mcp_files"

new_path =os.path.join(base_path,folder)
if not os.path.exists(new_path):
    os.makedirs(new_path)
    print("path folder is successfully created")
async def main():
    print('Hello')
    try:
        model_client =await  givemebrain()
        print("Calling the MCP SERVER \n 1. Make the connection object  \n2. Call the MCP server")
        # file_system_mcp = StdioServerParams(command ="npx.cmd", args =[
        #     "/c",
        #     "npx",
        #     "-y",
        #     "@modelcontextprotocol/server-filesystem",
        #     new_path
        #     ]
        #     ,read_timeout_seconds=60)
        
        file_system_mcp = StdioServerParams(
                command=r"C:\Program Files\nodejs\npx.cmd",
                args=[
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    new_path
                ],
                read_timeout_seconds=60
            )

        fs_workbench = McpWorkbench(file_system_mcp)
        async with fs_workbench as fs_wb:


            if model_client:
                assistant = AssistantAgent(name="teacher", model_client=model_client,workbench=fs_wb,system_message="You are helpful math teacher explain concepts luci and clear fashion if user understood and reply by sayign thank you then say LESSON COMPLETE to close the session")

                user = UserProxyAgent(name="vineet")
                
                team = RoundRobinGroupChat(participants=[user , assistant],termination_condition=TextMentionTermination('LESSON COMPLETE'))

                await Console(team.run_stream(task="Help to find all the international school in Netherlands who are hiring for sciences and biology job position  and store the results in the form of table  name link school  partime , full time , internships"))

            await close_model(model_client)
            await assistant.close()
    except Exception as e :
        print(f"Error >>>>>>>>>>>>>>>>.. {e}")        

if __name__=="__main__":
    print("calling main")
    asyncio.run(main())
