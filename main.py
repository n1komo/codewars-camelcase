def to_camel_case(text):
    new_text = text.replace('-', '_')  # makes all the separators the same symbol (' _ ')
    new_list = new_text.split("_")  # splits input string to a lists without separator
    temp_list = list("")  # blank list, for temporary purposes
    for i in new_list:
        if i == new_list[0]:  # if it's a first word then adds it to our temp list without formatting upcase
            temp_list += i
            continue
        temp_list += i.title()  # adds our current word with first letter up-cased.

    rdy_string = ''.join(temp_list)  # converting our temp list into a string format
    print(rdy_string)
    return rdy_string


# sample tests


sample1 = "the-stealth-warrior"
sample2 = "The_Stealth_Warrior"
sample3 = "The-stealth_warrior-comes_ahead-the-jungle"
sample4 = "the_stealth-warrior_comes-ahead_the_jungle"
to_camel_case(sample1)
to_camel_case(sample2)
to_camel_case(sample3)
to_camel_case(sample4)
