# scores = [77, 85, 90]
# doubled = []

# for x in scores:
#     doubled.append(x * 2)
#     # if doubled.append(6 * 2) ---- [12, 12, 12]

# print(doubled)

# #OR
# score = [77, 85, 90]
# doubled = [x * 2 for x in score]
# print(doubled)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in numbers:
#     print(f"2 * {x} = ", 2*x)

# #OR
# for i in range(1,11):
#     print("2","X",i,"=", i*2)

# name = ["Ananya", "Yashi", "Riya"]            #name.upper() gives error as list has no object like upper.. for strings it is
# result = [i.upper() for i in name] 
# print(result)

# name = ["RIYA","SIYA","YASHI"]
# result = [i.lower() for i in name]
# print(result)

# score = [34, 56, 76, 45, 89, 90, 87, 65, 43, 70]
# passing = [x for x in score if x>=70]
# print(passing)

# score = [34, 56, 76, 45, 89, 90, 87, 65, 43, 70]
# passing = [x for x in score if x>=70]
# passing = [x for x in score if x<=70]              #overwrite so only last one gets printed
# print(passing)

