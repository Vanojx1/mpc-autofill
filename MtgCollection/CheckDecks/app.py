from glob import glob
import csv
from collections import Counter
import scrython
from PIL import Image
import urllib.request
from base64 import b64decode, b64encode
from uuid import uuid1
import xml.etree.cElementTree as ET


coll = set([])
with open('archidekt-collection.csv') as f:
    coll = set([row[0] for row in csv.reader(f, delimiter=";")])

full_decks = []
for d in glob('./decks/*.csv'):
    with open(d) as f:
        deck = set([row[0] for row in csv.reader(f, delimiter=";")])
        full_decks += list(deck)

for c in coll:
    if c not in full_decks:
        full_decks.append(c)

decks = Counter(full_decks)
root = ET.Element("order")
fronts = ET.SubElement(root, "fronts")

count = 0
NUM = 5
for k, v in decks.most_common():
    if k in ('Forest', 'Island', 'Plains', 'Swamp', 'Mountain'): continue
    card = scrython.cards.Named(fuzzy=k)
    if float(card.prices('eur') or 0) >= 8:
        uri = card.image_uris()['png']
        # print(card.image_uris())
        stripped_name = k.replace(',', '').replace('\'', '')
        print(f"{stripped_name};{v};{uri}")
        id = str(uuid1())
        img_name = f"./images/{stripped_name} ({id}).png"
        urllib.request.urlretrieve(uri, img_name)
        img = Image.open(img_name)
        x, y = img.size
        cl = img.getpixel((5, 520))
        resized = Image.new('RGBA', (x+64, y+64), cl)# (20, 11, 12))
        resized.paste(img, (32,32), img)
        img.close()
        resized.save(img_name)
        card = ET.SubElement(fronts, "card")
        ET.SubElement(card, "id").text = id
        ET.SubElement(card, "slots").text = ','.join(map(str, range(count, count+NUM)))
        ET.SubElement(card, "name").text = f"{k}.png"
        ET.SubElement(card, "query").text = ""
        count += NUM
    
tree = ET.ElementTree(root)
tree.write("cards_new.xml")