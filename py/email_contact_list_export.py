#!/usr/bin/env python

# fix online contact export, so it matches google contacts, so it makes switching email providers easier
import pandas

online_df = pandas.read_csv("export.csv")

pandas.set_option('display.max_columns', None)

for name, email in zip(online_df['Name'], online_df['Email']):
    if "," in name:
        new_name = name.split(',')
        name = f"{new_name[1:][0].lstrip()} {new_name[0]}" # rearranging names, with commas. (eks. Askeladden, Paal becomes, Paal Askeladden)
    if email.split('@')[0] == "post" and name == "Post":
        email_domain = email.split('@')[-1].split('.')[0] # adding name of email domain to name if name only contains post.
        name = f"{email_domain} post"
    c = f"{name},{name},,,,,,,,,,,,,,,,,,,,,,,,,,,,*,{email}\n"

    with open('new.csv', 'a') as file:
        file.write(c)
        #print (c)

