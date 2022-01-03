import csv
import sqlite3

#create database
open("eng_words.db", "w").close()
con = sqlite3.connect("eng_words.db")
cursor= con.cursor()

#create table
cursor.execute("CREATE TABLE words_en (id INTEGER, words TEXT not NULL, meaning TEXT, PRIMARY KEY(id))")

#open english_txt file and insert values
counter = 1
with open("english_words.txt", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        cursor.execute("INSERT INTO words_en (id, words) VALUES(?, ?)", (counter, row[0]))
        counter+=1

#save file
con.commit()

#close connection
con.close()
