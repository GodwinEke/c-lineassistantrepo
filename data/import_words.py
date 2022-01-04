import csv
import sqlite3

#create database
open("japanese_words.db", "w").close()
con = sqlite3.connect("japanese_words.db")
cursor= con.cursor()

#create table
cursor.execute("CREATE TABLE words_japan (id INTEGER, words TEXT , english_translation TEXT, PRIMARY KEY(id))")

#open english_txt file and insert values
counter = 1
with open("D:/Documents/finalproject/data/wordstxt/japanese_words.txt", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        cursor.execute("INSERT INTO words_japan(words) VALUES(:translation)", {"translation":row[0]})
        counter+=1


#save file
con.commit()

#close connection
con.close()
