import json

json_string = ""
json_object = { "name": "Vlad",
                "childs": [
                    {"name": "Igor",
                     "age": 12},
                    {"name": "Inna",
                     "age": 14},
                ]}
json_add = { "fname": "Ivanoff"}

json_string = json.dumps(json_object)
print(json_string)

json_object.update(json_add)

json_string = json.dumps(json_object)
print(json_string)
