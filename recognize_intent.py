from transformers import BertTokenizer, BertForSequenceClassification
import re

# Load the BERT tokenizer and model for intent classification
tokenizer_bert = BertTokenizer.from_pretrained('bert-base-uncased')
model_bert = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Improved intent recognition function
def get_intent(user_input):
    # Normalize input
    user_input = user_input.lower().strip()
    
    # Define patterns for different intents
    open_browser_patterns = [r"open browser", r"run browser", r"start browser", r"launch browser"]
    
    # Check patterns
    for pattern in open_browser_patterns:
        if re.search(pattern, user_input):
            return "open_browser"
    
    return "general_conversation"
