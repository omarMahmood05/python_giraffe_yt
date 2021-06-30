is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a male but aren't tall")
elif is_tall and not(is_male):
    print("You are not a male but are tall")
else:
    print("You are not a male nor are tall")

