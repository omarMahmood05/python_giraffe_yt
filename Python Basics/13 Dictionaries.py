# Dict. in python is just like dicts in real life. You give a word and then assign a meaning to it. Like key -> An instrument used to open someting speciftc.
# In python we do almost the same give a key and then a value to it. For eg Jan -> January

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Sept"])
print(monthConversions.get("Mar"))

#Using get is much better than using [] because you can add a default value incase the key is not found for eg ->

print(monthConversions.get("Afr", "Key Not Found"))