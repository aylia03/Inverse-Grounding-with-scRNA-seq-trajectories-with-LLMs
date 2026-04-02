# Please install OpenAI SDK first: `pip3 install openai`
import os
from dotenv import load_dotenv
from openai import OpenAI
import torch
from transformers import pipeline

load_dotenv()
## Load Models
### BioGpt
generator = pipeline(
    task="text-generation",
    model="microsoft/biogpt",
    dtype=torch.float16,
    device="mps",
)

### DeepSeek + Mistral
client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)




# local LLMs

## DeepSeek
def call_DeepSeek(system_prompt, user_promp):
    chat_completion = client.chat.completions.create(
        messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_promp}
        ],
        model='deepseek-r1:7b',
    )
    return (chat_completion.choices[0].message.content)

## Mistral
def call_Mistral(system_prompt, user_prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        model='mistral',
    )
    return (chat_completion.choices[0].message.content)


#### for cloud apis
# client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")
#
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)
########################

def call_llms(model, system_prompt, user_prompt):
    if model == "deepseek":
        return call_DeepSeek(system_prompt, user_prompt)
    elif model == "mistral":
        return call_Mistral(system_prompt, user_prompt)
    else:
        raise ValueError(f"Unkown model: {model}")


# print(call_llms("mistral", "You are an doctor", "for what is ibuprofen used"))
# print()
# print(call_llms("deepseek", "You are an doctor", "for what is ibuprofen used"))
# print()
