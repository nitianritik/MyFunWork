
import re

# Rerurns true is a string contains link
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
def contains_link(message):
    return pattern.search(message.lower()) is not None



# Returns the list of all links present in a message
def get_link(message):
    links = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    print(links)


