# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict
# import re
# import requests
# import logging
# from concurrent.futures import ThreadPoolExecutor, as_completed

# logger = logging.getLogger(__name__)

# class ActionProcessAndRespond(Action):

#     def name(self) -> Text:
#         return "action_process_and_respond"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict) -> List[Dict[Text, Any]]:
        
#         user_message = tracker.latest_message.get('text')
#         logger.info(f"User message: {user_message}")
        
#         sentences = re.split(r'[.!?]', user_message)
#         sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
#         logger.info(f"Split sentences: {sentences}")
        
#         responses = []

#         # Using ThreadPoolExecutor for parallel processing
#         with ThreadPoolExecutor(max_workers=5) as executor:
#             future_to_sentence = {executor.submit(self.send_message_to_bot, sentence, tracker.sender_id, domain): sentence for sentence in sentences}
            
#             for future in as_completed(future_to_sentence):
#                 sentence = future_to_sentence[future]
#                 try:
#                     response = future.result()
#                     if response and response != domain['responses']['utter_please_rephrase'][0]['text']:
#                         responses.append(response)
#                     else:
#                         logger.info(f"Skipping rephrase response for sentence: {sentence}")
#                 except Exception as exc:
#                     logger.error(f"Sentence {sentence} generated an exception: {exc}")

#         final_response = ' '.join(responses).strip()
#         logger.info(f"Final response: {final_response}")
        
#         if not final_response:
#             final_response = domain['responses']['utter_please_rephrase'][0]['text']
#             logger.info(f"Using fallback response: {final_response}")

#         dispatcher.utter_message(text=final_response)

#         return []

#     def send_message_to_bot(self, message: Text, sender_id: Text, domain: DomainDict) -> Text:
#         rasa_server_url = "http://localhost:5005/webhooks/rest/webhook"
#         payload = {
#             "sender": sender_id,
#             "message": message
#         }
#         try:
#             response = requests.post(rasa_server_url, json=payload, timeout=60)
#             if response.status_code == 200:
#                 responses = response.json()
#                 if responses:
#                     for resp in responses:
#                         if resp.get("text") and resp.get("text") != domain['responses']['utter_please_rephrase'][0]['text']:
#                             return resp.get("text")
#             else:
#                 logger.error(f"Received non-200 response: {response.status_code}")
#         except requests.RequestException as e:
#             logger.error(f"Error sending message to Rasa server: {e}")
#         except Exception as e:
#             logger.error(f"Unexpected error: {e}")
#         return None
