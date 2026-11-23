##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime
import random
import smtplib
import pandas
import os

now=datetime.datetime.now()
month=now.month
day=now.day

myemail = "veroth83prueba@gmail.com"
password = "ofuh qhiw yeaj lypb"

carta="letter_templates/letter_"+str(random.randint(1,3))+".txt"
file=pandas.read_csv("birthdays.csv")

birthdays=file.to_dict(orient="records")
#print(birthdays)
for birthday in birthdays:
    #print(birthday["month"])
    if birthday["month"]==month and birthday["day"]==day:
        with open(carta, "r") as f:
            body = f.read()
            new_body=body.replace("[NAME]", birthday["name"])
            print(new_body)
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=myemail, password=password)
                connection.sendmail(from_addr=myemail, to_addrs=birthday["email"],
                                    msg=f"Subject:Happy birthday\n\n{new_body}")


