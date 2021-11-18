# Prints all titles in CSV using csv.reader
import csv
titles = {}
title = input("Title: ").strip().upper()
counter = 0
# Open CSV file
with open("favorites.csv", "r") as file:
    # Create reader
    reader = csv.DictReader(file)
    # Skip header row
    #next(reader
    # Iterate over CSV file, printing each title
    for row in reader:
        if row["title"].strip().upper() == title:
            counter += 1
    
#for title in sorted(titles, key=lambda title: titles[title], reverse=True):
#    print(title, titles[title])
print(counter)
