#libraries needed to capture and handle api call 
import requests, json

#library needed for saving to csv format
import pandas as pd

#class to handle api call response
class Responder():
    def __init__(self, url):
        """Responder Constructor"""
        self.url = url
        self.response = None

    def get_response(self):
        """Format list of data from api call"""
        #send API request to retrieve response
        response = requests.get(self.url)

        #store response as a JSON format and ignore first index of JSON (labels)
        response = json.loads(response.text)[1:]

        #places zipcode to be first column e.g. [population, zipcode] -> [zipcode, population]
        self.response = [item[-1:] + item[:-1] for item in response]

    def save_to_csv(self, codes):
        """Output data in csv format"""
        #set column title for dataframe
        columnTitles = ['ZIPCODE'] + codes 

        #store the response in a dataframe
        dataframe = pd.DataFrame(columns=columnTitles, data=self.response)

        #prompt to set filename for output
        fileName = input("Please enter your desired file name: ")

        #save that dataframe to a CSV spreadsheet
        dataframe.to_csv(fileName + '.csv', index=False)

        #inform user of program completion
        print("Program request completed. Please check for '{}.csv' file in your folder where this program lives.\n".format(fileName))
