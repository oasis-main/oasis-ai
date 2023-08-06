from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = OpenAI()
chat_model = ChatOpenAI()

text = "What would be a good company name for a company that makes colorful socks?"

print("Example 1: Single Message")
print(llm.predict(text))
print(chat_model.predict(text))

print("Example 2: Pass Multiple Messages")
messages = [HumanMessage(content=text)]
print(llm.predict_messages(messages))
print(chat_model.predict_messages(messages))

