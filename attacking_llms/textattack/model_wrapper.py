# What the wrapper does:
# Acts like a translator between our AI model and TextAttack
# Can handle multiple texts at once (like checking many reviews together)
# Takes each text, gets the AI’s opinion, and stores the results
# Returns all results in a format that TextAttack can understand


from textattack.models.wrappers import ModelWrapper
from sentiment_model import SentimentClassifier

class SentimentWrapper(ModelWrapper):
    def __init__(self):
        self.model = SentimentClassifier()

    def __call__(self, text_list):
        outputs = []
        for text in text_list:
            prediction = self.model.predict(text)
            outputs.append(prediction[0])  # Get probabilities for each class
        return torch.stack(outputs)
