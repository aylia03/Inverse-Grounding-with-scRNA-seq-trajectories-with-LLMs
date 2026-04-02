##### Testing file, to run the llms local (because no creditcard for cloud models yet)


## bio gpt
import torch
from transformers import pipeline

generator = pipeline(
    task="text-generation",
    model="microsoft/biogpt",
    dtype=torch.float16,
    device="mps",
)
result = generator("Ibuprofen is best used for", truncation=True, max_length=50, do_sample=True)[0]["generated_text"]
print(result)

result1= generator("T cells are responsible for", truncation=True, do_sample=True)[0]["generated_text"]
print(result1)

result3 = generator("Migraine is caused by",  truncation=True, do_sample=True)[0]["generated_text"]
print(result3)

print()
print("Starting Ollama with Deepseek ...")
#### Deepseek local

from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            'role': 'user',
            'content': 'Say this is a test',
        }
    ],
    model='deepseek-r1:7b',
)
print(chat_completion.choices[0].message.content)
print()
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

responses_result = client.responses.create(
  model='deepseek-r1:7b',
  input='Write a short poem about the color blue',
)
print(responses_result.output_text)

### Mistral
print()
print("Starting Ollama with Mistral ...")

chat_completion = client.chat.completions.create(
    messages=[
        {
            'role': 'user',
            'content': 'Say this is a test',
        }
    ],
    model='mistral',
)
print(chat_completion.choices[0].message.content)
print()
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

responses_result = client.responses.create(
  model='mistral',
  input='Write a short poem about the color blue',
)
print(responses_result.output_text)