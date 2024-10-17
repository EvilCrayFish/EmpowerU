greetings = ["Hello", "Salutations", "What's up"]
joiner = ""
greeting = joiner.join([i for i in greetings if i == greetings[0]])
assert greeting in greetings

names = {
    "default": "World",
    "big": "Universe",
    "small": "Country"
}
name = names["default"]
names_values = [names[key] for key in names.keys()]
for value in names_values:
    assert value in names.values()
assert name in names_values

full_sentence = "".join([greeting, ", ", name, "!"])
print(full_sentence)