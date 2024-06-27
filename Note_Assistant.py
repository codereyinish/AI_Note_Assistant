# **Problem is  the OpenAI assistant continues to respond in its default style(reads more like something from ChatGPT ) rather than referring to the provided document and tailoring its responses accordingly.**

# ## Knowledge Retrieval
# Knowledge(Files) + Retrieval Capability

# In[16]:


from openai import OpenAI

# To fetch the API key stored as an environment variable.
import os
import time
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI()


# In[17]:


#Create a vector store
vector_store = client.beta.vector_stores.create(name = "RAG Introduction")


# In[19]:


#FILE PREPARATION, Upload the files to Vector Stores
file_paths = ["docs/rag.docx"]
file_streams = [open(path, "rb") for path in file_paths]

file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)
print(file_batch.status)


# In[5]:


#print(os.getcwd())


# In[20]:


new_instructions = """MBGPT, functioning as a virtual Notebook Responde on Youtube, communicates in clear, accessible language,escalating to technical depth upon request. \
When asked a question, MBGPT will refer to the content from the provided file 'rag.docx' to retrieve and present the relevant information, instead of generating an answer independently. The answers will be based on the exact content of the file, ensuring accurate and contextually appropriate responses."""


# In[21]:


#Lets create another assistant(this time with file search capability)
assistant = client.beta.assistants.create(
    name = "MBGPT",
    description = "Document Reader and Responder",
    instructions= new_instructions,
    model = "gpt-4-turbo",
    tools = [{"type": "file_search"}],
    
)


# In[22]:


#Update the assistant to use the new Vector store so that assistant can access and retrieve(resources) the files in vector store through file_search tools 
assistant = client.beta.assistants.update(
    assistant_id = assistant.id, #who to upadate
    tool_resources = {"file_search": {"vector_store_ids":[vector_store.id]}}
)


# ## Create a Thread
# Create a message thread and we can also add vector stores to the thread(different from the vector_store assistant uses)

# In[23]:


message_file = client.files.create(
    file = open("docs/rag.docx","rb"),
    purpose = "assistants"
)
print(f"File ID: {message_file.id}")


# Lets create a message thread

# In[24]:


thread = client.beta.threads.create()


# A technical question to ask

# In[25]:


# user_message = "What is the problem with OpenAI?"
# ANother question
user_message = "What are the steps in setting up RAG?"


# In[26]:


messages = client.beta.threads.messages.create(
    thread_id = thread.id,
    content = user_message,
    role = "user"
)


# ## Create a Run
# Create a run object that will handle the conversation passing between user and assistant in the thread(run uses all tools assigned , adds generated response to thread)

# In[27]:


run = client.beta.threads.runs.create_and_poll(
    thread_id = thread.id,
    assistant_id = assistant.id
)


# ## Retrieve and Print the Message

# In[28]:


#we have our response added to thread, now retrieve it
messages = client.beta.threads.messages.list(
    thread_id = thread.id
)

#Retrieve latest response 
print(messages.data[0].content[0].text.value)

#Delete the file from storage system
client.files.delete(
    file_id = message_file.id
)

#DELETE THE ASSISTANT AFTER USE
client.beta.assistants.delete(assistant.id)


# **YES YES AT least some improvement and I am glad this is reading the question well(going through the keywords) and picking up the content from the mass of the given content**
# While it seems like it's just retrieving and pasting content, I don't think we can describe it as merely a "Ctrl F finder." Ultimately, it's all about refining the prompt. In this case, we should instruct ChatGPT to not only retrieve content but also to add a bit of its own commentary. It should blend the retrieved information with the original content and respond as if a tutor is addressing a student's queries. Additionally, we should include a few example responses to guide it