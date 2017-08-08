import random

print("Sample python script")
vowels=("a", "e", "i", "o", "u")
adjectives=("amazing", "awesome", "super", "incredible", "magnificient", "excellent", "fabulous", "brilliant", "outstanding")

adj=random.choice(adjectives)

if(adj[0] in vowels):
	preposition="an"
else:
	preposition="a"


print("Have " + preposition + " " + adj + " day!")
