## book_room_dulex_details
* greet
 - utter_greet
* book_rooms
 - utter_book_rooms
* dulex_room_details
 - utter_dulexroom_details
* book_room_now
   - book_room_form 
   - action_book_rooms_details


## book_room_simple_details
* greet
 - utter_greet
* book_rooms
 - utter_book_rooms
* simpleroom_details
 - utter_simpleroom_details
* book_room_now
   - book_room_form
   - action_book_rooms_details
* goodbye
 - utter_goodbye

## book_room_now
* greet
 - utter_greet
* book_rooms
 - utter_book_rooms
* book_room_now: 
    - book_room_form 
    - action_book_rooms_details
* goodbye
 - utter_goodbye

## schedule_cleaning_right_away
* greet
 - utter_greet
* clean_room
 - utter_query
* clean_rightnow
 - utter_quick
* goodbye
 - utter_goodbye

## schedule_cleaning
* greet
 - utter_greet
* clean_room
 - utter_query
* schedule_clean
 - utter_late
* goodbye
 - utter_goodbye

## restaurant
* greet
 - utter_greet
* restaurant
 - utter_restaurant
* goodbye
 - utter_goodbye

## faqbreakfastmenu
* greet
 - utter_greet
* faq
 - utter_faq_prompt 
* faqbreakfast
 - utter_faqbreakfast

## cancellationplicyfaq
* greet
 - utter_greet
* faq
 - utter_faq_prompt 
* faqcancellationpolicy
 - utter_cancellationpolicy  

## faqcheckintime
* greet
 - utter_greet
* faq
 - utter_faq_prompt 
* faqcheckintime
 - utter_checkintime

## faqcheckouttime
* greet
 - utter_greet
* faq
 - utter_faq_prompt 
* faqcheckouttime
 - utter_checkouttime 

## breakfasttime
* greet
 - utter_greet
* faq
 - utter_faq_prompt 
* faqbreakfasttime
 - utter_breakfasttime

## contactnumber
* greet
 - utter_greet
* faq
 - utter_faq_prompt 
* faqcontactnumber 
 - utter_contactnumber  