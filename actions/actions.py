from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import re

class ActionProcessAndRespond(Action):

    def name(self) -> Text:
        return "action_process_and_respond"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[Text, Any]]:
        
        # Get the latest user message
        user_message = tracker.latest_message.get('text')
        
        # Split the message by sentence-ending punctuation
        sentences = re.split(r'[.!?]', user_message)
        responses = []

        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                # Simulate intent recognition
                parsed_data = self.simulate_intent_recognition(sentence, domain)
                intent = parsed_data['intent']['name']
                entities = parsed_data['entities']

                # Generate a response for each recognized intent
                response = self.generate_response(intent, entities, domain)
                if response:
                    responses.append(response)
        
        # Join all responses and send them to the user
        final_response = ' '.join(responses)
        dispatcher.utter_message(text=final_response)

        return []

    def simulate_intent_recognition(self, sentence: Text, domain: DomainDict) -> Dict[Text, Any]:
        # This function simulates intent recognition
        intents = domain['intents']
        for intent in intents:
            if intent in sentence.lower():
                return {
                    "intent": {"name": intent},
                    "entities": []  # Add entity recognition here if needed
                }
        return {"intent": {"name": "default_intent"}, "entities": []}
    
    def generate_response(self, intent: Text, entities: List[Dict[Text, Any]], domain: DomainDict) -> Text:
        # This function generates a response based on the recognized intent
        responses = domain['responses']
        utter_key = f'utter_{intent}'
        if utter_key in responses:
            return responses[utter_key][0]['text']
        else:
            return domain['responses']['utter_default'][0]['text']