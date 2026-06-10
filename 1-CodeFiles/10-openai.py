from openai import OpenAI
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_core.models import ModelInfo
import os 
import asyncio
from dotenv import load_dotenv 

load_dotenv()

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5.4-mini",
  input="write a haiku about ai",
  store=True,
)
print(response.output_text);

async def main():
    model_client =OpenAIChatCompletionClient(model ="gpt=5.4-mini" , api_key=os.getenv("OPEN_AI_KEY"))

    assistant = AssistantAgent(name="agent",model_client  = model_client    )
    await assistant.run(task="cpatial of france is ")

asyncio.run(main())

