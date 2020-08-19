#pandas library will be needed for saving to csv format
import pandas as pd

#requests library will be needed to make api call
import requests

#json library will be needed to capture api response
import json

def display_intro():
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

class Handler():
    def __init__(self):
        """Handler Constructor"""
        self.apiUrlPath = ""
        self.forValueUrl = ""
        self.variableCodes = ""
    
    def set_year(self):
        """Set url paths from user input argument"""
        year = input("Please choose which census table to look at [2000SF1 or 2000SF3 or 2010]: ")
        if (year.upper() == '2000SF1'):
            print("Chosen Census Table Year: 2000 SF1")
            print("Please check https://api.census.gov/data/2000/sf1/variables.html for potential variable codes.\n")
            self.apiUrlPath = "data/2000/sf1"
            self.forValueUrl = "state:*"
        elif (year.upper() == '2000SF3'):
            print("Chosen Census Table Year: 2000 SF3")
            print("Please check https://api.census.gov/data/2000/sf3/variables.html for potential variable codes.\n")
            self.apiUrlPath = "data/2000/sf3"
            self.forValueUrl = "state:*"
        elif (year == "2010"):
            print("Chosen Census Table Year: 2010")
            print("Please check https://api.census.gov/data/2010/dec/sf1/variables.html for potential variable codes.\n")
            self.apiUrlPath = "data/2010/dec/sf1"
            self.forValueUrl = "zip%20code%20tabulation%20area:*"
        else:
            print("This program does not support that census table at the moment. Quitting program...\n")
            exit()

    def set_variable_codes(self):
        """Set variable codes from user input argument"""
        codes = input("Please enter variable code that you want to view (e.g. P003001 or P003001, P003002, P003003, etc.). Or type 'quit' to exit: ").replace(" ","").strip(',').upper()
        while (codes == ""):
            if (codes == "quit"):
                print("Quitting program...\n")
                exit()
            else:
                print("You have not entered any variable codes. Please try again.\n")
                codes = input("Please enter variable code that you want to view (e.g. P003001 or P003001, P003002, P003003, etc.). Or type 'quit' to exit: ").replace(" ","").strip(',').upper()
                print(variables)

        #quit program if no variable codes were given
        if (len(codes) == 0 or len(codes.split(",")) == 0):
            print("No codes were inputted. Quitting program...\n")
            exit()
        else:
            self.variableCodes = codes

    def get_api_url_path(self):
        """Return api folder url path"""
        return self.apiUrlPath
    
    def get_for_value_url(self):
        """Return value url path"""
        return self.forValueUrl

    def get_variable_codes(self):
        """Return all variable codes for url path"""
        return self.variableCodes

    def get_variable_codes_split(self):
        """Return list of all variable codes"""
        return self.variableCodes.split(",")

if __name__ == "__main__":
    #loading screen
    display_intro()    

    #store your API key here from api.census.gov/data/key_signup.html
    apiKey = "redacted"

    #prompt to set your version api call and variable codes
    handler = Handler()
    handler.set_year()
    handler.set_variable_codes()


    print("Variable Codes: {}\n".format(handler.get_variable_codes()))
    #format the API call with variables for all zip code tabulation area
    baseAPI = "https://api.census.gov/%s?key=%s&get=%s&for=%s"
    calledAPI = baseAPI % (handler.get_api_url_path(), apiKey, handler.get_variable_codes(), handler.get_for_value_url())

    try:
        #send API request to retrieve response
        response = requests.get(calledAPI)

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

    except:
        #if any of the code is not correct
        print("There are variable codes that don't exist. Please check the codes inputted. Quitting program...\n")