#library needed to handle exception
import sys

#import classes from other modules
from Classes.intro_guide import IntroGuide
from Classes.handler import Handler
from Classes.responder import Responder

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
        #get response from api call and output as csv
        responder = Responder(handler.get_api_call_url())
        responder.get_response()
        responder.save_to_csv(handler.get_variable_codes_split())
    except ValueError:
        print("Ensure that you have entered an API Key and valid variable codes.")
    except:
        print("Unexpected Error has occurred: ", sys.exc_info())