from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
import requests
from ziya.tools import *
from ziya.sysprompt import system_prompt
load_dotenv()

memory=InMemorySaver()

llm=ChatGroq(model="qwen/qwen3.6-27b")


agent=create_agent(
    llm,
    tools=[filter_products,one_product_details,manage_cart],
    checkpointer=memory,
    system_prompt=system_prompt
)

while True:
    qn=input("Enter your Query: ")
    if qn in ["bye","exit"]:
        print("Happy to Help again See yaa..! ")
        break
    config={"configurable":{"thread_id":"prince"}}
    query=agent.invoke({"messages":{"role":"user","content":qn}},config=config)

    print(query["messages"][-1].content)
