import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yes_or_no = input("Did you mean %s instead? Enter Y if yes, or N if no.: "
                          % get_close_matches(w, data.keys())[0])
        if yes_or_no == "Y" or yes_or_no == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yes_or_no == "N" or yes_or_no == "n":
            return "The word doesn`t exist. Please double check it."
        else:
            return "We didn`t understand your entry."
    else:
        return "The word doesn`t exist. Please double check it."


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
