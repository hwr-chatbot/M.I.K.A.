# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re

class ActionProcessMultipleQuestions(Action):

    def name(self) -> Text:
        return "action_process_multiple_questions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = tracker.latest_message.get('text')
        sentences = re.split(r'[.!?]', message)

        intent_recognized = False

        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                if re.search(r'aps', sentence, re.IGNORECASE) and re.search(r'hand it in after the deadline', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_ask_weather")
                    intent_recognized = True
                elif re.search(r'apply for more than one program', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_application_many_programs_possible")
                    intent_recognized = True
                elif re.search(r'increase my chances', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_application_many_programs_chance_increase")
                    intent_recognized = True
                elif re.search(r'hand in GRE instead of GMAT', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_gre_instead_gmat")
                    intent_recognized = True
                elif re.search(r'GMAT mandatory', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_gmat_needed")
                    intent_recognized = True
                elif re.search(r'check my eligibility', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_eligibility_check")
                    intent_recognized = True
                elif re.search(r'who can check my eligibility', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_eligibility_check_who")
                    intent_recognized = True
                elif re.search(r'defer my study start date', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_defer_study_start")
                    intent_recognized = True
                elif re.search(r'semester start', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_semester_start")
                    intent_recognized = True
                elif re.search(r'how long is a typical semester', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_time_span_semester")
                    intent_recognized = True
                elif re.search(r'Do I need GMAT', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_gmat_needed")
                    intent_recognized = True
                elif re.search(r'Does HWR give out GMAT tests', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_hwr_gmat_test")
                    intent_recognized = True
                elif re.search(r'what kind of english certificate do I need', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_english_certificate")
                    intent_recognized = True
                elif re.search(r'Is duolingo accepted', sentence, re.IGNORECASE):
                    dispatcher.utter_message(response="utter_duolingo_accepted")
                    intent_recognized = True

        if not intent_recognized:
            dispatcher.utter_message(response="utter_please_rephrase")

        return []
