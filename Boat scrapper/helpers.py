
import re

# Rerurns true is a string contains link
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
def contains_link(message):
    return pattern.search(message.lower()) is not None



# Returns the list of all links present in a message
def get_link(message):
    #print("hello i am in the get links function")
    pattern = re.compile(r'(?:https?://|www\.)\S+')
    # This pattern matches all possible URLs that start with https://, http://, or www.

    links = re.findall(pattern, message)
    #print(f"gving links --- {links}")
    return list(set(links))



def strip_links(text):
    # Define the regular expression pattern for URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')

    # Replace all occurrences of the pattern with an empty string
    return url_pattern.sub('', text)



