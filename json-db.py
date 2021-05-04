#JSON-DB made by MatthewHashed#1224 (https://discord.gg/3M7xXTUKge)

import json

with open('db.json') as f:
  database = json.loads(f.read())

def saveDatabase():
  json.dump(database, open('db.json', 'w'))

def setValue(key, value):
  database[key] = value;
  saveDatabase()

setValue('eee', 'ashdashjdhbasdhasdad')
print(database['eee'])
