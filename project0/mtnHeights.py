mountains = {
    "Mount Everest":29029,
    "K2":28251,
    "Kanchengjunga":28169,
    "Dhaulagiri":26795,
    "Annapurna":26545
}

for x in mountains:
    print(x)
for x in mountains:
    print(mountains[x])
for x in mountains:
    print(x + " is " + str(mountains[x]) + " feet tall")