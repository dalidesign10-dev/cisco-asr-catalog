import json

with open('E:/TEST CLAUDE/cisco-asr-catalog/data/products.json', 'r') as f:
    data = f.read().strip()

with open('E:/TEST CLAUDE/cisco-asr-catalog/index.html', 'r') as f:
    html = f.read()

old = """fetch('data/products.json').then(r=>r.json()).then(data=>{
  products=data;
  initFilters();
  applyFilters();
});"""

new = f"""products={data};
initFilters();
applyFilters();"""

html = html.replace(old, new)

with open('E:/TEST CLAUDE/cisco-asr-catalog/index.html', 'w') as f:
    f.write(html)

print("Done - data embedded inline")
