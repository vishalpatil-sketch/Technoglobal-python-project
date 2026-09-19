import json
import random
import numpy as np
from src.preprocessor import TextPreprocessor

class ChatbotModel:
    def __init__(self, intents_filepath="data/intents.json"):
        self.preprocessor = TextPreprocessor()
        self.intents = self.load_intents(intents_filepath)
        self.context = {}

    def load_intents(self, filepath):
        with open(filepath, 'r') as file:
            return json.load(file)['intents']

    def match_intent(self, user_input: str, user_id: str = "default_user"):
        tokens = self.preprocessor.clean_and_tokenize(user_input)
        best_tag = None
        max_matches = 0

        # Retrieval & Keyword Pattern Matching
        for intent in self.intents:
            # Check context filtering for multi-turn conversations
            if "context_filter" in intent and intent["context_filter"] != "":
                if self.context.get(user_id) != intent["context_filter"]:
                    continue

            for pattern in intent['patterns']:
                pattern_tokens = self.preprocessor.clean_and_tokenize(pattern)
                matches = len(set(tokens) & set(pattern_tokens))
                if matches > max_matches:
                    max_matches = matches
                    best_tag = intent

        if best_tag and max_matches > 0:
            # Manage Context State
            if "context_set" in best_tag and best_tag["context_set"] != "":
                self.context[user_id] = best_tag["context_set"]
            else:
                self.context[user_id] = ""

            return random.choice(best_tag['responses'])
        return "I'm sorry, I didn't quite understand that. Could you rephrase?"
