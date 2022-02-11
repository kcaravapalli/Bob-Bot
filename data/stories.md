
## story outofscope-bye
* greet
  - utter_greet
  - utter_how_can_i_help
* out_of_scope
  - utter_confusion
  - utter_how_can_i_help  
* goodbye
  - utter_goodbye

## story create1.0
* greet
  - utter_greet
  - utter_how_can_i_help
* create
  - utter_affirm
  - create_form 
  - form{"name": "create_form"}
  - form{"name":null}
  - utter_slots_values
  - utter_item_created
  - action_slot_reset
* thanks
  - utter_happy
* goodbye
  - utter_goodbye

  
  ## story create1.1 sad_path and deny
* greet
  - utter_greet
  - utter_how_can_i_help
* create
  - utter_affirm
  - create_form 
  - form{"name": "create_form"}
* non_compliant
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name":null}
  - action_slot_reset
  - utter_goodbye
  
  
## story create1.2 sad_path and affirm
* greet
  - utter_greet
  - utter_how_can_i_help
* create
  - utter_affirm
  - create_form 
  - form{"name": "create_form"}
* non_compliant
  - utter_ask_continue
* affirm
  - create_form
  - form{"name":null}
  - utter_slots_values
  - action_slot_reset





