# Building an Email Simulator

import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
        
    def mark_as_read(self):
        self.read = True
    
    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f'Body: {self.body}')
        print('------------\n')
        
    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f'[{status}] From: {self.sender.name} | Subject: {self.subject}'
        
email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!')

#Step 9 is to remove the print and calls so I'm going to make it as comments

# print(email_obj.sender)
# print(email_obj.subject)
# print(email_obj.read)
# email_obj.mark_as_read()
# print(email_obj.read)

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()
        
    def send_email(self, receiver, subject, body):
        email = Email(self, receiver, subject, body)
        receiver.inbox.receive_email(email)
        
class Inbox:
    def __init__(self):
        self.emails = []
    
    def receive_email(self, email):
        self.emails.append(email)

# Step 20 is to remove the objects and prints, instead I commented them out

# alice = User('Alice')
# bob = User('Bob')
# alice.send_email(bob, 'Hello', 'Hi Bob, how are you?')
# print(len(bob.inbox.emails))

    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')
    
    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return      
        self.emails[actual_index].display_full_email()
    
    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')
        
# Step 41 made me remove current time and print so I commented them out instead
      
# current_time = datetime.datetime.now()
# print(current_time.strftime('%H:%M:%S'))