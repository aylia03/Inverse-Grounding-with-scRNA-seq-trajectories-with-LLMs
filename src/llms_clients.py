import anthropic
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
ollama_client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)
### OpenAI - ChatGPT
client = OpenAI()

## claude
client_claude = anthropic.Anthropic()



# local LLMs

## DeepSeek
def call_DeepSeek(system_prompt, user_prompt):
    chat_completion = ollama_client.chat.completions.create(
        messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
        ],
        model='deepseek-r1:7b',
        temperature=0.0
    )
    return (chat_completion.choices[0].message.content)



#### for cloud apis
def call_ChatGPT(system_prompt, user_prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        model='gpt-5.4',
        temperature=0.0
    )
    return (chat_completion.choices[0].message.content)

def call_claude(system_prompt, user_prompt):
    message = client_claude.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        system = system_prompt,
        messages = [
            { 'role': 'user', 'content': user_prompt}
        ],
    )
    return(message.content[0].text)

def call_llms(model, system_prompt, user_prompt):
    if model == "deepseek":
        return call_DeepSeek(system_prompt, user_prompt)
    elif model == "chat_gpt":
        return call_ChatGPT(system_prompt, user_prompt)
    elif model == "claude":
        return call_claude(system_prompt, user_prompt)
    else:
        raise ValueError(f"Unkown model: {model}")


# print(call_llms("mistral", "You are an doctor", "for what is ibuprofen used"))
# print()
print(call_llms("claude", "You are an doctor", "for what is ibuprofen used"))
# print()
