#list
scores = [90,65,34,71,55,77,89]

# acccess a value
print(scores[0]) #first
print(scores[2]) #third

scores.append(61) # alters
print(scores)

scores.pop(3) #deletes
print(scores)

scores.sort() # in ascending order
print(scores)
scores.sort(reverse=True) # in ascending order
print(scores)

print(len(scores))