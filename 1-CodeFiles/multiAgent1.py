import asyncio
import os 
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient 
from autogen_core.models import ModelInfo


load_dotenv()
api_key = os.getenv("GEMINI_KEY")
print(f"my key is >>>>>>>>> {api_key}")




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
    



async def  main():
    try:
        print('Inside main')
        await asyncio.sleep(1)
        model_client = await givemebrain()
        if model_client is None:
            return
        
        print("version ............ ",model_client.component_version)
        agent1= AssistantAgent(name ="agent1",model_client=model_client , system_message="You are dance teacher teach me bollywood dance..")
        print("calling task")        
    
        output  = await Console(agent1.run_stream(task="You are helpful user explain bollywood dance")    )

        print(len(output.messages))
        for item in output.messages:
            print(f"{item.source}: {item.content[:50]}")
        
        await model_client.close()


    except Exception as e:
        print(f"error occured >>>>>>>>>>> {e}")

if __name__=="__main__":
    asyncio.run(main())