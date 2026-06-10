import os
import asyncio
from dotenv import load_dotenv

from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent

load_dotenv()

async def main():
    endpoint = "https://vineet001-resource.openai.azure.com/"
    deployment_name = "gpt-4o-mini"                            # ✔ must match your Azure deployment name

    client = AzureOpenAIChatCompletionClient(
        azure_endpoint=endpoint,
        api_key=os.getenv("AZURE_OPEN_AI_KEY"),                # ✔ only API key needed
        model=deployment_name,
        api_version="2024-10-21",                              # ✔ correct API version
        model_info={
            "family": deployment_name,
            "json_output": False,
            "function_calling": False,
            "vision": False,
            "structured_output": False,
        }
    )

    assistant = AssistantAgent(name="agent", model_client=client)
    await assistant.run(task="What is the capital of France")

    try:
        await client.close()
    except:
        pass

asyncio.run(main())
