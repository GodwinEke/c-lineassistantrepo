"""
Author: Godwin Chierika Eke
The purpose of the dicitonary is to parse JSON files from the New York Times API

"""

class News:
    def __init__(self, content):
        self.content = content["response"]["results"]
    
    def get_news(self):
        print('NEWS')
        print('-----------------------------------------------------------------------------------------------------------------------------------------')
        for result in self.content:
            print("Section", result["sectionName"])
            print("Title: ", result["webTitle"])
            print("Publication Date: ", result["webPublicationDate"].replace('T', ' ').replace('Z', ''))
            print("URL: ", result["webUrl"])
            print("Type: ", result["type"],'\n')
    
