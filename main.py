# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

# -----------------------------------------ORIGINAL------------------------------------------------------

# from datetime import datetime
# import pandas
# import random
# import smtplib
# import os

# import os and use it to get the Github repository secrets
# MY_EMAIL = os.environ.get("MY_EMAIL")
# MY_PASSWORD = os.environ.get("MY_PASSWORD")

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#    birthday_person = birthdays_dict[today_tuple]
#    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
#    with open(file_path) as letter_file:
#        contents = letter_file.read()
#        contents = contents.replace("[NAME]", birthday_person["name"])

#    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#        connection.starttls()
#        connection.login(MY_EMAIL, MY_PASSWORD)
#       connection.sendmail(
#            from_addr=MY_EMAIL,
#           to_addrs=birthday_person["email"],
#            msg=f"Subject:Happy Birthday!\n\n{contents}"
#        )

# -----------------------------------------v1------------------------------------------------------

from datetime import datetime
import pandas
import random
import smtplib
import os

#import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

data = pandas.read_csv("quotes.txt")
random_number = random.randint(0,101)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs="arthur.toledo@gmail.com",msg=f"Subject:Monday Motivation \n\n {data.loc[random_number].at["Quote"]}")

# -----------------------------------------v0------------------------------------------------------

# import smtplib
# import datetime as dt
# import pandas as pd
# import random
# import os

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# data=pd.read_table("quotes.txt")
# random_number = random.randint(0,101)

# MY_EMAIL = os.environ.get("MY_EMAIL")
# MY_PASSWORD = os.environ.get("MY_PASSWORD")

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL,password=MY_PASSWORD)
#     if day_of_week == 0:
#     connection.sendmail(from_addr=MY_EMAIL, to_addrs="arthur.toledo@gmail.com",
#                             msg=f"Subject: Monday Motivation \n\n {data.loc[random_number].at["Quote"]}")
