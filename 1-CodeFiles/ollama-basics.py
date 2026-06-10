import os 
import json
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent,UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination , TextMentionTermination
from autogen_core.models import ModelInfo
from autogen_ext.models.ollama  import OllamaChatCompletionClient
from autogen_ext.tools.mcp import McpServerParams , McpWorkbench ,StdioServerParams
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
import asyncio
from utils import close_model , givemebrain 

load_dotenv()

async def main():
    print()

    model_client = OllamaChatCompletionClient(model="tinyllama", temperature=0.9)
    print(model_client)
    assistant = AssistantAgent(name="teacher", model_client=model_client,system_message="You are helpful math teacher explain concepts luci and clear fashion if user understood and reply by sayign thank you then say LESSON COMPLETE to close the session")

    await Console(assistant.run_stream(task="Help to  solve the math problem and store the results locally in provided mentioned path."))
    await model_client.close()
    await assistant.close()

async def main2():
    load_dotenv()

    base_path = os.getcwd()
    folder  ="mcp_files"

    new_path =os.path.join(base_path,folder)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print("path folder is successfully created")

    model_client = OllamaChatCompletionClient(model="llama3", temperature=0.3)
    file_system_mcp = StdioServerParams(
                 command="cmd.exe",
                args=[
                    "/c",
                    r"C:\Program Files\nodejs\npx.cmd",
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    new_path
                ],
                read_timeout_seconds=60        
            )

    fs_workbench = McpWorkbench(file_system_mcp)
    async with fs_workbench as fs_wb:
          agent = AssistantAgent(name="agent", model_client = model_client, workbench=fs_wb, system_message="You are helpful agent  having access to the file paths")

          await Console(agent.run_stream(task="help me to store maths 5*6  in to the file provided"))

          await model_client.close()
          await agent.close()
        




asyncio.run(main2())