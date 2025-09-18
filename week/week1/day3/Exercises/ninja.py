"""
Exercise 1 : Call History

Instructions

Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.
Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.
Add a method called show_call_history. This method should print the call_history.
Add another attribute called messages to your __init__() method which value is an empty list.
Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
to : the number of another Phone object
from : your phone number (also a Phone object)
content
Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
Test your code !!!
"""

class Phone:
  def __init__(self, phone_number):
    self.phone_number = phone_number
    self.call_history = []
    self.messages = []

  def call(self, other_phone):
    call_string_out = f"{self.phone_number} called {other_phone.phone_number}"
    print(call_string_out)
    self.call_history.append(call_string_out)

    call_string_in = f"{other_phone.phone_number} get called by {self.phone_number}"
    other_phone.call_history.append(call_string_in)

  def show_call_history(self):
    for call in self.call_history:
      print(call)
  
  def send_message(self, other_phone, content):
    message_dict = {
        "to": other_phone.phone_number,
        "from": self.phone_number,
        "content": content
    }
    self.messages.append(message_dict)
    other_phone.messages.append(message_dict)

  def show_outgoing_messages(self):
    print("\nOutgoing Messages : \n")
    for message in self.messages:
      if message["from"] == self.phone_number:
        print(message)
  
  def show_incoming_messages(self):
    print("\nIncoming Messages : \n")
    for message in self.messages:
      if message["to"] == self.phone_number:
        print(message)

  def show_messages_from(self, other_phone):
    print(f"\nMessages from {other_phone.phone_number} : \n")
    for message in self.messages:
      if message["from"] == other_phone.phone_number:
        print(message)


my_phone = Phone("0600000000")
friend_phone = Phone("0611111111")
work_phone = Phone("0622222222")

#call(other_phone)
my_phone.call(friend_phone)
friend_phone.call(work_phone)

#show_call_history()
print(f"\nmy_phone call history : {my_phone.show_call_history()}")
print(f"\nfriend_phone call history : {friend_phone.show_call_history()}")
print(f"\nwork_phone call history : {work_phone.show_call_history()}\n")


#send_message()
my_phone.send_message(friend_phone, "Are you free this weekend?")
friend_phone.send_message(my_phone, "Yes, what's up?")
work_phone.send_message(my_phone, "Meeting rescheduled to 2 PM.")

# show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
my_phone.show_outgoing_messages()
my_phone.show_incoming_messages()
my_phone.show_messages_from(friend_phone)