#!/usr/bin/env python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]



print("Challenge 1")

print(farms[0]["agriculture"]
        for animal in farms[0]["agriculture"]:
            print(animal)

print("Challenge 2")

choice = input("What far you wanna look at?")

for eachdct in farms:
     if choice in eachdict["name"]:
        #print(eachdict["agriculture"])
        for agitem in eachdict["agriculture"]:
            print(agitem)

print("Challenge 3")

choice = input("What far you wanna look at?")
yuck = ["carrot", "celery"]

for eachdct in farms:
     if choice in eachdict["name"]:
        #print(eachdict["agriculture"])
        for agitem in eachdict["agriculture"]:
            if agitem not in yuck:
                print(agitem)



