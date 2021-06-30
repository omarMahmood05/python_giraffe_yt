def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Write the phrase to be translated: ")))













# def translator(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translator(input("Enter the text to be translated: ")))