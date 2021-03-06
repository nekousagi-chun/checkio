def correct_sentence(text: str) -> str:
    li = text[0]

    if li.isupper() == True:
        pass
    else:
        text = li[0].upper() + text[1:]

    if text[-1:] == ".":
        return text
    else:
        return text + "."



if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    print("Coding complete? Click 'Check' to earn cool rewards!")
