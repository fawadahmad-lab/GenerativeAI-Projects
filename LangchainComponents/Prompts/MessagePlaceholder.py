from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
# from LangchainComponents.Prompts import ChatPromptTemplate,MessagesPlaceholder
chat_template=ChatPromptTemplate([
    ('system','you are a customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])
chat_history=[]
#load chat history
with open('chathistory.txt') as f:
    chat_history.extend(f.readlines())


prompt=chat_template.invoke({'chat_history':chat_history,'query':'which paper i have selected'})
print(prompt)
