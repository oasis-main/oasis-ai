from langchain.prompts import PromptTemplate


print("Example 1: Simple prompt formatting")
prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
print(prompt.format(product="colorful socks"))

print("Example 2: Language translation prompt format example")
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

print(chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming."))

