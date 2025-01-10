from transformers import GPT2LMHeadModel, GPT2Tokenizer
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the Hugging Face API token from environment variables
huggingfacehub_api_token = os.getenv("YOUR_API_TOKEN")

if not huggingfacehub_api_token:
    raise ValueError("Hugging Face API token is missing from the .env file.")

# Load GPT-2 model and tokenizer using transformers, with the correct token
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", use_auth_token=huggingfacehub_api_token)

def get_response(user_input):
    # Tokenize input text
    inputs = tokenizer(user_input, return_tensors="pt")

    # Generate response
    outputs = model.generate(inputs['input_ids'], max_length=50)

    # Decode and return response
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
