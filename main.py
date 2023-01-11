def to_camel_case(text):
    new_list = text.split(detect_separator(text)) # splits input string to a lists without separator
    temp_list = list("")  # blank list, for temporary purposes
    for i in new_list:
        if i == new_list[0]:  # if it's a first word then adds it to our temp list without formatting upcase
            temp_list += i
            continue
        temp_list += i.title()  # adds our current word with first letter upcased.

    rdy_string = ''.join(temp_list)  # converting our temp list into a string format
    print(rdy_string)
    return rdy_string


def detect_separator(text):  # this method detects separator in our input string
    text.find('-')
    if text.find('-') > 0:
        return text[text.find('-')]
    if text.find('_') > 0:
        return text[text.find('_')]

# sample tests


sample1 = "the-stealth-warrior"
sample2 = "The_Stealth_Warrior"
sample3 = "The-stealth-warrior-comes-ahead-the-jungle"
sample4 = "the_stealth_warrior_comes_ahead_the_jungle"
to_camel_case(sample1)
to_camel_case(sample2)
to_camel_case(sample3)
to_camel_case(sample4)
