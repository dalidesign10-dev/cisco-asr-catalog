import json
import os
import glob

# Rename all .jpg files that are actually SVGs to .svg
for jpg in glob.glob('images/**/*.jpg', recursive=True):
    with open(jpg, 'r', errors='ignore') as f:
        content = f.read(10)
    if content.startswith('<svg'):
        svg_path = jpg.replace('.jpg', '.svg')
        os.rename(jpg, svg_path)
        print(f"Renamed: {jpg} -> {svg_path}")

# Update products.json
with open('data/products.json', 'r') as f:
    products = json.loads(f.read())

for p in products:
    p['image'] = p['image'].replace('.jpg', '.svg')

with open('data/products.json', 'w') as f:
    f.write(json.dumps(products, indent=2))

# Update index.html - replace .jpg image refs with .svg
with open('index.html', 'r') as f:
    html = f.read()

# Replace all image path references from .jpg to .svg within the products array
import re
# Match image paths in the inline data
html = re.sub(r'"image":"(images/asr\d+/[^"]+)\.jpg"', r'"image":"\1.svg"', html)

with open('index.html', 'w') as f:
    f.write(html)

print("Done - updated all image references to .svg")
