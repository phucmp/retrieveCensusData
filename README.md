# Retrieve Census Data [Version 1.3.5]

Python program to retrieve census data based on variable code. **This code is written for Python 3.7**.

## Prerequisite

Please obtain an API key from https://api.census.gov/data/key_signup.html. 

Ensure you have the following [pip](https://pip.pypa.io/en/stable/) libarries installed: 

- Pandas
- Requests

```bash
pip3 install pandas requests
```

## Installation

Download and clone this repository to retrieve the python file to run program.

```bash
git clone https://github.com/phucmp/retrieveCensusData.git
```

## Usage

1. Add your api key into 'census.py' file.
2. Run program by entering the following into your command line.

```bash
python3 census.py
```

Once the program starts running, it will asks for your variable codes. Please enter your variable codes directed from specific pdf file from census data (e.g. https://api.census.gov/data/2010/dec/sf1/variables.html). These codes are case **insensitive**.

Enter in variable codes and for multiple codes, put a comma in between the codes to delimit them.

It will ask for a file name to save to in the current folder where the program lives, enter desired file name. 
NOTE: it will always save to csv file format.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
Created by Phuc Minh Pham 2020.