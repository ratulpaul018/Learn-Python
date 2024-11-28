print("Enter a sentence: ")
sentence = str(input(""))

a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
#alphabet ="b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "v" or "w" or "x" or "y" or "z"
#my_list = ["a","b", "c" , "d","e", "f" ,"g" ,"h","i" ,"j", "k", "l", "m", "n","o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]
n = 0
while n < 2:
    my_list = str(input([f"var_{n}"]))
    print(my_list)
    n += 1
alphabet_count = sentence.count(my_list)
a_count = sentence.count(a)
e_count = sentence.count(e)
i_count = sentence.count(i)
o_count = sentence.count(o)
u_count = sentence.count(u)

sum = a_count + e_count + i_count + o_count + u_count

print(f"The no. of vowels in the sentence is: {sum}")
print(f"The no. of constants in the sentence is: {alphabet_count}")
