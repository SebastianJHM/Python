import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
    
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

## Convert file to json
# with open('people.json', 'w') as people_json:
#     json.dump(people, people_json)
    
people_json = open('people2.json', 'w')
json.dump(people, people_json, indent=2)
 
## Convert json to list of dictionary
json_file = open('people.json', 'r')
read_people = json.load(json_file)

print(read_people)
print(type(read_people[0]))