# Building an Email Simulator

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
        
    def mark_as_read(self):
        self.read = True
        
email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!')

#Step 9 is to remove the print and calls so I'm going to make it as comments

# print(email_obj.sender)
# print(email_obj.subject)
# print(email_obj.read)
# email_obj.mark_as_read()
# print(email_obj.read)