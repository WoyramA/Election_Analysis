print("Hello World")
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Dever", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data
print(voting_data)
voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})
print(voting_data)
voting_data.remove({"county":"Arapahoe","registered_voters": 422829})
print(voting_data)
voting_data.remove({"county":"El Paso","registered_voters": 461149})
print(voting_data)
voting_data.remove({"county":"Dever","registered_voters": 463353})
print(voting_data)
voting_data.insert(2,{"county":"Denver", "registered_voters": 463353})
print(voting_data)

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)

counties =["Arapahoe","Denver","Jefferson"]
print(counties[0])
print(counties[2])
print(len(counties))

print(counties[0:2])
print(counties[:2])
print(counties[1:])
counties.append("El Paso")
print(counties)
counties.insert(2,"El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)

counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)
print(len(counties_tuple))
counties_tuple[1]
print(counties_tuple[1])

counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
print(counties_dict)
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))

print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.get("Denver"))
print(counties_dict["Arapahoe"])

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver","registered_voters": 463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
print(voting_data)

if counties[1] == "Denver":
    print(counties[1])


counties =["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

counties_tuples = ("Arapahoe","Denver","Jefferson")
len(counties_tuples)
for i in range(len(counties_tuples)):
    print(counties_tuples[i])

counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
print(counties_dict)
counties_dict["Jefferson"] = 432438
print(counties_dict)
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print (county)

#To get the number of voters in the counties    
for voters in counties_dict.values():
    print(voters)

#To get the number of voters in the counties    
for county in counties_dict:
    print(counties_dict[county])

 #To get the number of voters in the counties   
for county in counties_dict:
    print(counties_dict.get(county))

# To return county and corresponding voters    
for county,voters in counties_dict.items():
    print(county,voters)

#.... county has ..... registered voters
for county,voters in counties_dict.items():
    print((county), "county has",(voters),"registered voters.")

#To print the dictionary of county and corresponding voters as a dictionary from voting data
for county_dict in voting_data:
    print(county_dict)

#To print the county name and voters
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#To print the county name only
for county_dict in voting_data:
    print(county_dict["county"])




if counties[3] != "Jefferson":
    print(counties[2])