# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"



#from rasa_sdk import Action, Tracker
#from typing import Any, Text, Dict, List
#from rasa_sdk.executor import CollectingDispatcher


#class create(Action):

#    def name(self) -> Text:
#        return "create"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#        intent = tracker.latest_message['intent'].get['name']
#        intent_type=''
#        for e in tracker.latest_message['entities']:
#            intent_type= e['value']

#        print(f"intent_type {intent_type} for Intent {intent}")

#        dispatcher.utter_message("Following  {intent_type} 158834 has been created")

#        return []


from typing import Dict, Text, Any, List, Union

from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset

class createform(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "create_form"

    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text,Any]) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit")
        return[]


        
    @staticmethod

    def required_slots(tracker:Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        print("required_slots(tracker:Tracker)")
        return["application_name","issue_summary","priority","estimate","email_id"]



class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 
	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]

    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text,Any]) -> List[Dict]:
        
        return[]


    







