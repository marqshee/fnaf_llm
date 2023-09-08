# Simple OpenAI LLM Prompt using Streamlit

Sandbox repo to play with Open AI LLMs using a simple streamlit app to display results.

## OpenAI - LLM
[OpenAi](https://openai.com/) - I know you heard of it already, it's all the rage, it's everything, everywhere... all at once. Let's just hope this we use this for good.

## Langchain
[Langchain](https://www.langchain.com/) framework that can be used with various language modesl. It has easy to use modular components to allow for use with models like OpenAI.

### LLMChain
Single chain to OpenAI model that generates a single output.

### SimpleSequentialChain
Allows us to chain multiple LLMs to generate multiple outputs.

### SequentialChain
Allos us to chain multiple LLMs to generate multiple outputs but with more ability to view the specific output of each chain's output.

### PromptTemplate
Prompt templatse allow us to simplify LLM input especially when using sequential chains.

### ConversationBufferMemory
Memory.

## Streamlit
Never used [Streamlit](https://streamlit.io/) before... According to the documentation, 'Streamlit turns data scripts into shareable web apps in minutes.
All in pure Python. No front‑end experience required.' Sounds perfect for focusing on LLMs.

## Jupyter Notebook
[Jupyter Notebook](https://jupyter.org/) is popular among data scientist. It allows me to execute code within each cell, allowing me to quickly iterate on ideas and visualize outputs. In this project, no charts were created.

## How to use
```pip install python-dotenv streamlit openai langchain ```
You'll need an account with openAI to obtain an API key which youcan then add to the .env file.

```streamlit run app.py``` will launch localhost stream app
