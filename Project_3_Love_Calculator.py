print("Welcome to Love Calculator")
name1=input("Enter your name in lower case: ")
name2=input("Enter the name of person you love in lower case: ")
name3=name1+name2
t=name3.count("t")
r=name3.count("r")
u=name3.count("u")
e=name3.count("e")
true=str(t+r+u+e)
l=name3.count("l")
o=name3.count("o")
v=name3.count("v")
e=name3.count("e")
love=str(l+o+v+e)
love_score=(true+love)
print("Your love score is "+love_score+".")