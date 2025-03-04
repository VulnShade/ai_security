# Building a chatbot using an LLM

## Libaries
|Library Name | Purpose |
|-------------|---------|
| Transformers | Provides state-of-the-art natural language processing models. |
| torch  | A deep learning framework for building and training neural networks. |
| accelerate | Simplifies the process of training and evaluating models on various hardware. |
| einops | Offers a flexible way to manipulate tensor shapes and dimensions. |
| jinja2 | A templating engine for rendering dynamic web pages and documents. |

<br>

## Building the model
1. Choose model from [hugging face](https://huggingface.co/models)
2. Build chatbot

```python
import os
import platform
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import pipeline

# Look for model @huggingface.com and download locally
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map="auto",
    torch_dtype="auto",
    trust_remote_code=True,
    )

# Use local model
# model = AutoModelForCausalLM.from_pretrained(“path/to/your/local/model/directory”)

# Load tokenizer from the model
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")


generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,
    max_new_tokens=500,
    do_sample=False
    )


def clear_console():
    command = "cls" if platform.system() == "Windows" else "clear"
    os.system(command)

while True:
    input()
    clear_console()
    print("-" *50) # Horizontal line
    print("How may I assist you?")
    user_input = input("\033[92mType something, or X to exit: \033[0m") # Ask the user for input in green color
    if user_input in ['X', 'x']: # If user types X or x, exit the program
        print("Exiting.")
        break
    else:
        messages = [{"role":"user", "content": user_input}]
        response = generator(messages)
        print(response[0]["generated_text"])
```
