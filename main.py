import pandas
import datetime as dt
import random
import smtplib

LETTERS = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
MY_EMAIL = "mariyachikhly84@gmail.com"
PASSWORD = "hmrh zewp hlqr ridk"

birthday_detail = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
day = now.day
month = now.month
tuple_data = (day, month)
birthday_data = {(data_row.day, data_row.month): data_row for (index, data_row) in birthday_detail.iterrows()}
if tuple_data in birthday_data:
    birthday_person = birthday_data[tuple_data]
    letter = random.choice(LETTERS)
    with open(letter) as wish:
        data = wish.read()
        stripped = data.strip()
        new_letter = data.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=MY_EMAIL, password=PASSWORD)
        connect.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{new_letter}"
        )
