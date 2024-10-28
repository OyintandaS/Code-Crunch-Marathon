import smtplib
import datetime
import requests, json
from email.message import EmailMessage
from dotenv import load_dotenv
import os


# sends the "happy birthday" to email address
def happy_birthday(receiver):
    name = receiver['name']
    surname = receiver['surname']
    email1 = receiver['email']

    sender = "Oyintanda Sishuba"
    message = f"""Hi {name} {surname}, 
Happy Birthday! I hope your day is as beautiful as you are. Enjoy! 🥂❤️

{sender}
    """
    
    my_email = os.getenv('my_email')
    two_step_verification_key = os.getenv('two_step_verification_key')
    
    # structuring the email. The subject, and the body
    email = EmailMessage()
    email['Subject'] = f"HAPPY BIRTHDAY {name}"
    email['From'] = sender
    email['To'] = email1
    email.set_content(message)
    
    #sending the email
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(my_email, two_step_verification_key)
    smtp_server.send_message(email)
    smtp_server.quit()



def sheets_data():
    
    api_key = os.getenv('api_key')
    data = requests.get(url = api_key)
    send = data.text
    contents = json.loads(send)
    
    return contents['sheet1']
    
def birthday_data(Name, Surname, Birthday, Email):
    api_key = os.getenv('api_key')
    
    sheet = {"Birthdays":
        {"Name": Name,
         "Surname": Surname,
         "Birthday": Birthday,
         "Email": Email}}
    
    data = requests.post(url = api_key, json = data)
    data.raise_for_status()
    
def main():
    load_dotenv()
    sheet = sheets_data()
    x = datetime.datetime.now()
    
    day = x.strftime("%d")
    month = x.strftime("%m")
    y = f"{day}/{month}"

    
    for person in sheet:
        bd = person["birthday"]
        if bd == y:
            happy_birthday(person)
            
    
    
main()
    
    
    