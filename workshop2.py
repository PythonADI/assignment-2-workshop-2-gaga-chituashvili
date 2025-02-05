#1
name="jon"
print(f"{name=}")

#2
food="khinkali"


print(f"{food=}")

food="xachapuri"

print(f"{food=}")

#3

name="nick"

print(name.upper())


#4
food1="khinkali"
food2="burger"
food3="pizza"

favorite_food=f"""
my favorite is:
{food1}
{food2}
{food3}
"""

print(favorite_food)

#8

text='          I have white spaces                '

print(f"{text.strip()}")

#9

print(f"{text.lstrip()}")

print(f"{text.rstrip()}")


#10-11

text1="Python's"
text2="community"
result=f'One of {text1} strengths is its diverse {text2}' 

print(result)

#12


name="Eric"
result=f'Hello {name}, would you like to learn some Python today'

print(result)

#13

name = "Albert"
last_name = "Einstein"
full_name = f'{name} {last_name}'
quote = """A person who never made a 
mistake never tried anything new"""

famous = f'{full_name} once said "{quote}"'

print(famous)

#15

print(4+4)
print(16-8)
print(4*2)
print(24//3)

#16

favorite_number=19

result=f'my favorite number is {favorite_number}'
print(result)

#17

name="gaga"
last_name="chituashvili"
full_name=f'{name} {last_name}'
result=f'hello i am {full_name}'

print(result)
