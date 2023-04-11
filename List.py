friends = ["john","kevin","fred","test","jim","james","james"]

print(len(friends))
print(friends[0:2])
# friends[1] =  "Mike"
print(friends[1:])

lucky_numbers = [2,4,5,15,23,46]

#friends.extend(lucky_numbers)
#friends.append("creed")
#friends.insert(1,"tom")
#friends.remove("jim")
#friends.clear()
#friends.pop()

friends.sort()
print(friends)
print(friends.index("test"))
print(friends.count("james"))
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy() 
print(friends2)