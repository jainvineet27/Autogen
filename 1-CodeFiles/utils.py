import json 
import os 
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo 

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
    

async def close_model(model_client : OpenAIChatCompletionClient):
    print("Closing the model connection....")
    await model_client.close()


