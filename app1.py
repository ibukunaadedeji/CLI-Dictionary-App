import json
from difflib import get_close_matches

data=json.load(open("076 data.json"))

def translate(w):
    w=w.lower()
    if w in data:
       return data[w]
    elif w.title() in data:
       return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) >0:
        yn = input("Did you mean %s Instead? Enter Y if yes or N if No; " % get_close_matches(w,data.keys())[0])
        if (yn == "Y" or "yes" or "y" or "Yes") :
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == ("N" or "n" or "no" or "No"):
            return "The word doesn't exist, Pls double check again"
        else:
            return "We do not understand your query"
    else:
        return "This word doesn't exist, Pls double check"

while(True):
    word = input("Enter the word or command: ")
    if(word == ":exit"): break;
    output = (translate(word))
    if type(output) == list:
       for item in output:
            print(item)
    else:
        print(output)
