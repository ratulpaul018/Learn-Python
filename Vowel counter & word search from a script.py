print("Enter a script: ")
script = str(input(" "))
z = script.lower()

def vowel_counter():
    a = z.count("a")
    e = z.count("e")
    i = z.count("i")
    o = z.count("o")
    u = z.count("u")

    sum = a + e +i + o + u 
    print(f"The no of vowels is: {sum}")
    
def word_identify():
    x = str(input("Enter the word you want to search: "))
    y = z.count(x)
        
    print(f"In the text the word {x} appears {y} time(s).")
    
def search_by_word():
    import re 
    
    print("Enter the word you intersted in: ")
    word = str(input(" "))
    n = script.count(word)
    word = word.lower()
    print(f"The number of times [{word}] apears in the script is: {n}.")
    pattern = re.compile(r"[^.]*" + re.escape(word) + r"[^.]*\.")
    match = pattern.findall(script)

    if match:
        print ("Extracted sentence:" , match)
    else:
        print("Word not found.")

def main():
    print("Enter 1 for count word\nEnter 2 for count vowel\nEnter 3 to search a sentence by a keyword ")
    x = int(input(" "))
    if x == 1:
       word_identify()
    if x == 2:
        vowel_counter()
    if x == 3:
        search_by_word()
    if x>3 or x<1:
        print("Wrong Input.")
    
main()