INSTALL DEPENDENCIES: 'pip install snscrape', 'pip install pandas'

This program utilize 'snscrape' to scrape Twitter data.
The parameters for the text query are inserted in the os.system('params go here')
This generates a JSON-file, saved in '../TwitterScrape/json-files/' path, that you can name whatever you want.
This JSON-file is then converted to a pandas dataframe object, which we manipulate to only contain relevant attributes.
The pandas dataframe object is then saved as a csv-file into the '../TwitterScrape/csv-files/' path.