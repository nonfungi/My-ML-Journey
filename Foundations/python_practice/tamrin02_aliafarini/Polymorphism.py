#Problem
# ● Define an interface-like base class Notifier with method send(message).
# ● Implement EmailNotifier(address) and SMSNotifier(number) that both implement send.
# ● Write a function broadcast(notifiers, message) that calls send on any Notifier passed in. Demonstrate with at least two different notifiers.

# Base class defining the contract for all notifiers.
class Notifier:
    def send(self, message):
        raise NotImplementedError("Each Notifier must implement its own send() method")

# Subclass for sending email notifications.
class EmailNotifier(Notifier):
    def __init__(self, address):
        self.address = address

    def send(self, message):
        print(f"Sending email to {self.address}: {message}")
        # The 'pass' statement was removed as it was unnecessary.

# Subclass for sending SMS notifications (Name corrected to PascalCase).
class SMSNotifier(Notifier):
    def __init__(self, number):
        self.number = number
        
    def send(self, message):
        print(f"Sending SMS to {self.number}: {message}")

# Function to broadcast a message to a list of notifiers.
def broadcast(notifier_list, message):
    print("--- Broadcasting Message ---")
    for notifier in notifier_list:
        notifier.send(message)

# --- Test Script ---
if __name__ == "__main__":
    notifiers = [
        EmailNotifier("ali@gmail.com"), 
        SMSNotifier("+12345") # Using corrected class name
    ]
    
    my_message = "Your subscription is expiring soon!"
    broadcast(notifiers, my_message)