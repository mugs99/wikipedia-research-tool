import os
from apikey import apikey
import streamlit as st
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools, initialize_agent,AgentType
os.environ ["OPENAI_API_KEY"] = apikey

st.title('Wikipedia Research Tool')


# Create an Instance of OpenAI.
# Temperature parameter ranges from 0.0 to 1.0, 0 being more factual based and 1 being creative. For our purpose, we require more facts and less creativity.
llm = OpenAI(temperature=0.0)

tools = load_tools(['wikipedia','llm-math'],llm)
agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

prompt = st.text_input('Input Wikipedia Research Task\n')

if prompt:
    response = agent.run(prompt)
    st.write(response)

