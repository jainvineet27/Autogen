import json 
import os 
from dotenv import load_dotenv
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient, OpenAIChatCompletionClient
from autogen_ext.models.azure import AzureAIChatCompletionClient
from autogen_ext.models.ollama  import OllamaChatCompletionClient
from autogen_core.models import ModelInfo 
from azure.core.credentials import AzureKeyCredential

load_dotenv()

api_key = os.getenv("GEMINI_KEY")

async def givemebrain() -> OpenAIChatCompletionClient| None:
    print("inside the givembrain method >>>>>>>>>>>>>>>>>>")
    try:
        model_client = OpenAIChatCompletionClient(
            model="gemini-3.1-flash-lite", 
            api_key=api_key, 
            model_info=ModelInfo(vision=True, function_calling=True, json_output=True, family="unknown", structured_output=True)
                )
        return model_client

    except Exception as e:
        print(f"Error is >>>>>>>>>>>>>>>>>>>> {e}")  
        return None  

async def givemeollamabrain() -> OllamaChatCompletionClient| None:
    print("inside the givembrain method >>>>>>>>>>>>>>>>>>")
    try:
        model_client = OllamaChatCompletionClient(model="tinyllama", temperature=0.9)
        return model_client

    except Exception as e:
        print(f"Error is >>>>>>>>>>>>>>>>>>>> {e}")  
        return None

async def givemeazurebrain() -> AzureAIChatCompletionClient|None:
    print("inside the azure brain method >>>>>>>>>>>>>>>>>>")
    try:
        

        client = AzureOpenAIChatCompletionClient(
        azure_endpoint="https://vineet001-resource.services.ai.azure.com/openai/v1/responses",
        model="gpt-4o-mini",
        api_key=os.environ["AZURE_OPEN_AI_KEY"] )   
        
        return client
    
    except Exception as e:
        return None




async def close_model(model_client : OpenAIChatCompletionClient):
    print("Closing the model connection....")
    await model_client.close()




async def azureopenai_model():
    endpoint = "https://vineet001-resource.services.ai.azure.com/openai/v1/responses"
    api_key = os.getenv("AZURE_OPEN_AI_KEY")
    api_version="2026-03-17"
    deployment_name = "gpt-5.4-nano"  # e.g. "gpt-4o-mini"
    try:
        
        # ---- Create the Azure model client (the "class") ----
        model_client = AzureOpenAIChatCompletionClient(
            azure_endpoint=endpoint,
            api_key=api_key,
            model=deployment_name,     # IMPORTANT: this is typically deployment name in Azure clients
            api_version = api_version,
              model_info={
        "json_output": False,
        "function_calling": False,
        "vision": False,
        "family": "unknown",
        "structured_output": False,
            }
        )
        return model_client

    except Exception as e:
        print(f"Error is {e}")   
        return None 


