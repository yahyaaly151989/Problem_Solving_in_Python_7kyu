# ======================= Disemvowel Trolls =======================
def disemvowel(string_):
    vowls = "aeiouAEIOU"
    # result = []
    # for letter in string_:
    #     if letter not in vowls:
    #         result.append(letter)
    # return "".join(result)
    return "".join(char for char in string_ if char not in vowls)

print(disemvowel("This website is for losers LOL!"))