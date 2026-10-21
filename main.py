import random
import smtplib
from email.message import EmailMessage

import pandas
import datetime
import os


now = datetime.datetime.now()
month_now = now.month
day_now = now.day

all_birthdays = pandas.read_csv("birthdays.csv")

for (index, birth_info) in all_birthdays.iterrows():
    if birth_info.month == month_now and birth_info.day == day_now:
        celebrant_name = birth_info["name"]
        letters = []
        for num in range(1, 7):
            with open(f"letter_templates/letter_{num}.txt", "r") as birthday_msg:
                letters.append(birthday_msg.read())
        letter = random.choice(letters)

        birthday_wish = letter.replace("[NAME]", celebrant_name)

        message = EmailMessage()
        message["Subject"] = "Birthday Wishes"
        message["From"] = my_email
        message["To"] = str(birth_info["email"])
        message.set_content(birthday_wish)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.send_message(message)
