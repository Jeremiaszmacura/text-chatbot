import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the DialoGPT tokenizer and model
model_name = "microsoft/DialoGPT-medium"
tokenizer_dialo = AutoTokenizer.from_pretrained(model_name)
model_dialo = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate a response using DialoGPT
def generate_response(user_input, chat_history_ids=None):
    new_user_input_ids = tokenizer_dialo.encode(user_input + tokenizer_dialo.eos_token, return_tensors="pt")
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids
    chat_history_ids = model_dialo.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer_dialo.eos_token_id)
    bot_response = tokenizer_dialo.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return bot_response, chat_history_ids
