
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction

class BookRoomForm(FormAction):
 def name(self):
  return "book_room_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["check_in","check_out","adults","child","room","name","phno","email"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "check_in": [
                self.from_text(),
            ],
            "check_out": [
                self.from_text(),
            ],
            
            "adults": [
                self.from_text(),
            ],
            "child": [
                self.from_text(),
            ],
            "room": [
                self.from_text(),
            ],
            "name": [
                self.from_text(),
            ],
            "phno": [
                self.from_text(),
            ],
            "email": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_message("Your booking details are here")  
    return []

class BookRoomsDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_book_rooms_details"

 def run(self,dispatcher,tracker,domain):
  check_in=tracker.get_slot("check_in")
  check_out=tracker.get_slot("check_out")
  adults=tracker.get_slot("adults")
  child=tracker.get_slot("child")
  room=tracker.get_slot("room")
  name=tracker.get_slot("name")
  phno=tracker.get_slot("phno")
  email=tracker.get_slot("email")
  message="BOOKING DETAILS:"+"\n\n"+"Checkin Date:"+check_in+"\n"+"Checkout Date:"+check_out+"\n"+"No. of Adults:"+adults+"\n"+"No. of Children:"+child+"\n"+"No.of Rooms:"+room+"\n"+"Phone Number:"+phno+"\n"+"Email:"+email
  dispatcher.utter_message(message)
