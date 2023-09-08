import os
from dotenv import find_dotenv, load_dotenv
import streamlit as st

from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

load_dotenv(find_dotenv(), override=True)
os.getenv('OPENAI_API_KEY')

st.title('FNAF Universe Catalogue')
st.text('Simple LLM to help you understand the FNAF universe!')

highlight_template = PromptTemplate(
    input_variables=['topic'],
    template='''
        Write me a one line hightlight or synopsis about {topic} in reference to 
        the Five Nights at Freddy's universe, video games and book series.
        '''
)

powerpoint_slides_template = PromptTemplate(
    input_variables=['hightlight'],
    template='Write me four powerpoint presentation slides based on this summary: {hightlight}'
)

memory = ConversationBufferMemory(
    input_key='topic',
    memory_key='chat_history'
)

# temperature determins how *creative* the LLM will respond - range 0 - 1
llm = OpenAI(temperature=0.9)

highlight_chain = LLMChain(
    llm=llm,
    prompt=highlight_template,
    verbose=True,
    output_key='hightlight',
    memory=memory
)
powerpoint_slides_chain = LLMChain(
    llm=llm,
    prompt=powerpoint_slides_template,
    verbose=True,
    output_key='powerpoint_slides',
    memory=memory
)

sequential_chain =SequentialChain(
    chains=[highlight_chain, powerpoint_slides_chain],
    verbose=True,
    input_variables=['topic'],
    output_variables=['hightlight', 'powerpoint_slides']
)

prompt = st.text_input('What FNAF character or event would you like to know about:')

if prompt:
    response = sequential_chain({'topic': prompt})
    st.write(response['hightlight'])
    st.write(response['powerpoint_slides'])
    
    with st.expander('FNAF Universe Logs'):
        st.info(memory.buffer)