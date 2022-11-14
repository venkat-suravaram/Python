# Acts like a map data structure
# Assign some value based on keys
# pretty much equal to JSON
# we can use int/string as keys but value can be anything .
#list,tuple,set etc can't be used as keys
dict={}
dict2={}
dict2['name']='Venkat'
dict2['age']=23
dict2['skills']=['java','c','python']
dict2['other_details']={'color': 'black', 'Model':'se','year':2022}
print(type(dict))
print(dict2) # {'name': 'Venkat', 'age': 23, 'skills': ['java', 'c', 'python'], 'other_details': {'color': 'black', 'Model': 'se', 'year': 2022}}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(len(thisdict))

# Can be any Data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#Access / get the value of a key
x = thisdict.get("model")
x = thisdict["model"]

# Get list of keys in the dic
x = thisdict.keys()

# Change value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

thisdict.update({"year": 2020})

# Add an Item
thisdict["color"] = "red"  # add Item
print(thisdict)
thisdict.update({"color": "red1"})  #Update Item
print(thisdict)

# Remove Item
thisdict.pop("model")
thisdict.popitem() # Removes last one
del thisdict["model"] # Delete Item
del thisdict
thisdict.clear()

# For Loop
for x in thisdict: # Print all Key names
  print(x)
for x in thisdict:  #Print all values in dict
  print(thisdict[x])

#Get total keys in dic
thisdict={'name': 'Venkat', 'age': 23, 'skills': ['java', 'c', 'python'], 'other_details': {'color': 'black', 'Model': 'se', 'year': 2022}}

total_keys=thisdict.keys()
print("Total keys in dict : ",total_keys) #Total keys in dict :  dict_keys(['name', 'age', 'skills', 'other_details'])

