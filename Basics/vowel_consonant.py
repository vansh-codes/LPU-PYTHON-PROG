a=input("Enter character: ")
if (a>="A" and a<="Z") or (a>="a" and a<="z"):
    if a in "AEIOUaeiou":
        print("Letter and Vowel")
    else:
        print("Letter and Consonant")
else:
    print("Not a character!")


