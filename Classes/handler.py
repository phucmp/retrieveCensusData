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