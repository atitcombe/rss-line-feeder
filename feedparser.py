
import requests as requests
import xml.etree.ElementTree as et
from xml.etree.ElementTree import parse
import validators
import pandas as pd



#For the program to obtain the user's url
def get_url(url):
  url=input("Enter a website to obtain RSS feed, leave space blank to exit")
  return url

#validators package has to be installed first. This validates the url given by the use
def read_url(url):
  print("Checking validity of url...")
  if not validators.url(url):
    raise ValueError(f"invalid URL for input: {url}")
  return url

#This gets the XML of the url the user wants to see.
def obtain_xml(url):
  response = requests.get(url)
  return response

#Gets the root feed in the xml tag and returns it for parsing
def parse_xml(xml):
    try:
        tree=et.parse(xml)
        x = tree.getroot()
        return x
    except et.ParseError:
        print ("Encountered error as", xml, "was being parsed. \nException: ", et.ParseError)

#Parses the title, description and link and prints the format in a panda framework table
def get_feed(url):
    ptable = pd.DataFrame(columns = ['title', 'description', 'link'])
    for item in x.iterfind('channel/item'):
        title = item.find('title').text
        description = item.find('description').text
        link = item.find('link').text

        row = {'title': title, 'description': description, 'link': link}
        df = df.append(row)
    return df

#Putting all functions together
def main():
    y = get_url()
    while url != '':
        read_url(url)
        obtain_xml(url)
        parse_xml("data/latestfeed.xml")
        df = get_feed(url)
        df

if __name__ == '__main__':
    main()
