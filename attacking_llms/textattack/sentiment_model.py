# sentiment classifier - an AI that determines if text is positive or negative. 
# For example, it can tell whether a movie review is favorable (“This movie was amazing!”) 
# or unfavorable (“This movie was terrible!”).

# Creates an AI model that’s already trained to understand English
# Can read any text we give it (like “This movie is great!”)
# Returns a score showing how positive or negative the text is
# Uses a popular AI model called DistilBERT that’s good at understanding language

import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.nn.functional import softmax

class SentimentClassifier:
    def __init__(self):
        self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
        self.model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
        self.model.eval()

    def predict(self, text):
        # Tokenize input
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)

        # Get prediction
        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = softmax(outputs.logits, dim=1)

        return predictions
EOF