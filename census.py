#pandas library will be needed for saving to csv format
import pandas as pd

#requests library will be needed to make api call
import requests

#json library will be needed to capture api response
import json

#json decoder library to handle exception
from json.decoder import JSONDecodeError

#sys library will be needed to handle unexpected errors
import sys

#class to help users understand how to use the program
class IntroGuide:
    def __init__(self):
        pass

    def display_intro(self):
        """print out loading screen for program"""
        print("")
        print("          * * * * * * * * * * * *           ")
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("--                                        --")
        print("--  WELCOME TO RETRIEVING CENSUS PROGRAM  --")
        print("--                                        --")
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("          * * * * * * * * * * * *           ")
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("--              The Purpose:              --")
        print("--  This program is to use census data    --")
        print("--  from census.gov API to retrieve the   --")
        print("--  necessary data from census variables. --")
        print("")
        print("--              How to use:               --")
        print("--  Need to have all necessary variables  --")
        print("--  code from particular API and an API   --")
        print("--  key from the following website link:  --")
        print("--  api.census.gov/data/key_signup.html.  --")
        print("--  Follow instructions in the console.  --")
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("          * * * * * * * * * * * *           ")
        print("")


#class to handle the construction of url for api call
class Handler():
    def __init__(self, api_key):
        """Handler Constructor"""
        self.api_key = api_key
        self.base_url = "https://api.census.gov/%s?key=%s&get=%s&for=%s"
        self.api_call_url = ""
        self.year_url_path = ""
        self.primary_search_key = ""
        self.variable_codes = ""
    

    def set_year(self):
        """Set url paths from user input argument"""
        year = input("Please choose which census table to look at [2000SF1 or 2000SF3 or 2010]: ")
        if (year.upper() == '2000SF1'):
            print("Chosen Census Table Year: 2000 SF1")
            print("Please check https://api.census.gov/data/2000/sf1/variables.html for potential variable codes.\n")
            self.year_url_path = "data/2000/sf1"
            self.primary_search_key = "state:*"
        elif (year.upper() == '2000SF3'):
            print("Chosen Census Table Year: 2000 SF3")
            print("Please check https://api.census.gov/data/2000/sf3/variables.html for potential variable codes.\n")
            self.year_url_path = "data/2000/sf3"
            self.primary_search_key = "state:*"
        elif (year == "2010"):
            print("Chosen Census Table Year: 2010")
            print("Please check https://api.census.gov/data/2010/dec/sf1/variables.html for potential variable codes.\n")
            self.year_url_path = "data/2010/dec/sf1"
            self.primary_search_key = "zip%20code%20tabulation%20area:*"
        else:
            print("This program does not support that census table at the moment. Quitting program...\n")
            exit()


    def set_variable_codes(self):
        """Set variable codes from user input argument"""
        codes = input("Please enter variable code that you want to view (e.g. P003001 or P003001, P003002, P003003, etc.). Or type 'quit' to exit: ").replace(" ","").strip(',').upper()
        
        #request for users to input variable codes
        while (codes == ""):
            if (codes == "quit"):
                print("Quitting program...\n")
                exit()
            else:
                print("You have not entered any variable codes. Please try again.\n")
                codes = input("Please enter variable code that you want to view (e.g. P003001 or P003001, P003002, P003003, etc.). Or type 'quit' to exit: ").replace(" ","").strip(',').upper()
                print(variables)

        if (len(codes) == 0 or len(codes.split(",")) == 0):
            #quit program if no variable codes were given
            print("No codes were inputted. Quitting program...\n")
            exit()
        else:
            #display variable codes to user
            self.variable_codes = codes
            print("Variable Codes: {}\n".format(self.variable_codes))


    def set_api_url(self):
        """Set the url for the api call"""
        self.api_call_url = self.base_url % (self.year_url_path, self.api_key, self.variable_codes, self.primary_search_key)


    def get_year_url_path(self):
        """Return api folder url path"""
        return self.year_url_path
    

    def get_primary_search_key(self):
        """Return value url path"""
        return self.primary_search_key


    def get_variable_codes(self):
        """Return all variable codes for url path"""
        return self.variableCodes


    def get_variable_codes_split(self):
        """Return list of all variable codes"""
        return self.variable_codes.split(",")


    def get_api_call_url(self):
        """Return url for api call"""
        return self.api_call_url



if __name__ == "__main__":

    #################################
    ### Main Execution of Program ###
    #################################

    #loading screen
    intro_guide = IntroGuide()
    intro_guide.display_intro()    

    #store your API key here from api.census.gov/data/key_signup.html
    api_key = "redacted"

    #prompt to set your version, search key, and variable codes for api call url
    handler = Handler(api_key)
    handler.set_year()
    handler.set_variable_codes()
    handler.set_api_url()    

    try:
        #send API request to retrieve response
        response = requests.get(handler.get_api_call_url())

        #store response as a JSON format and ignore first index of JSON (labels)
        formattedResponse = json.loads(response.text)[1:]

        #places zipcode to be first column e.g. [population, zipcode] -> [zipcode, population]
        formattedResponse = [item[-1:] + item[:-1] for item in formattedResponse]

        #set column title for dataframe
        columnTitles = ['ZIPCODE'] + handler.get_variable_codes_split()

        #store the response in a dataframe
        dataframe = pd.DataFrame(columns=columnTitles, data=formattedResponse)

        #prompt to set filename for output
        fileName = input("Please enter your desired file name: ")

        #save that dataframe to a CSV spreadsheet
        dataframe.to_csv(fileName + '.csv', index=False)

        #inform user of program completion
        print("Program request completed. Please check for '{}.csv' file in your folder where this program lives.\n".format(fileName))

    except JSONDecodeError:
        #if decoding JSON fails 
        print("Ensure that you have entered an API Key and valid variable codes.")
    except:
        print("Unexpected Error has occurred: ", sys.exc_info()[0])