from langdetect import detect
text = input("Enter any text in any language :")
dtext = detect(text)
print(dtext)