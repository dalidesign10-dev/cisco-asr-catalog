import json
import os

with open('data/products.json') as f:
    products = json.loads(f.read())

colors = {
    'ASR 9000': ('#e74c3c', '#c0392b'),
    'ASR 1000': ('#3498db', '#2980b9'),
    'ASR 900': ('#27ae60', '#1e8449'),
    'ASR 920': ('#f39c12', '#d68910'),
}

icons = {
    'Chassis': 'M20,60 L280,60 L280,140 L20,140 Z M30,70 L60,70 L60,100 L30,100 Z M70,70 L100,70 L100,100 L70,100 Z M110,70 L140,70 L140,100 L110,100 Z M150,70 L180,70 L180,100 L150,100 Z M30,110 L270,110 L270,130 L30,130 Z',
    'Router': 'M20,60 L280,60 L280,140 L20,140 Z M30,70 L60,70 L60,100 L30,100 Z M70,70 L100,70 L100,100 L70,100 Z M110,70 L140,70 L140,100 L110,100 Z M30,110 L270,110 L270,130 L30,130 Z',
    'Line Card': 'M40,50 L260,50 L260,150 L40,150 Z M50,60 L80,60 L80,80 L50,80 Z M90,60 L120,60 L120,80 L90,80 Z M130,60 L160,60 L160,80 L130,80 Z M50,90 L250,90 L250,95 L50,95 Z M50,105 L250,105 L250,110 L50,110 Z M50,120 L250,120 L250,125 L50,125 Z',
    'Route Switch Processor': 'M50,50 L250,50 L250,150 L50,150 Z M60,60 L90,60 L90,90 L60,90 Z M100,60 L200,60 L200,75 L100,75 Z M100,80 L180,80 L180,90 L100,90 Z M60,100 L240,100 L240,105 L60,105 Z M60,115 L240,115 L240,120 L60,120 Z',
    'Route Processor': 'M50,50 L250,50 L250,150 L50,150 Z M60,60 L90,60 L90,90 L60,90 Z M100,60 L200,60 L200,75 L100,75 Z M60,100 L240,100 L240,105 L60,105 Z M60,115 L240,115 L240,120 L60,120 Z',
    'ESP': 'M50,50 L250,50 L250,150 L50,150 Z M70,65 L110,65 L110,95 L70,95 Z M120,65 L160,65 L160,95 L120,95 Z M170,65 L230,65 L230,80 L170,80 Z M60,110 L240,110 L240,140 L60,140 Z',
    'Modular Port Adapter': 'M60,55 L240,55 L240,145 L60,145 Z M70,65 L100,65 L100,85 L70,85 Z M110,65 L140,65 L140,85 L110,85 Z M150,65 L180,65 L180,85 L150,85 Z M70,95 L230,95 L230,100 L70,100 Z M70,110 L230,110 L230,115 L70,115 Z',
    'Power Module': 'M50,55 L250,55 L250,145 L50,145 Z M70,70 L120,70 L120,130 L70,130 Z M130,70 L170,70 L170,110 L130,110 Z M180,75 L230,75 L230,90 L180,90 Z M180,95 L230,95 L230,110 L180,110 Z',
    'Interface Module': 'M50,55 L250,55 L250,145 L50,145 Z M60,65 L80,65 L80,85 L60,85 Z M85,65 L105,65 L105,85 L85,85 Z M110,65 L130,65 L130,85 L110,85 Z M135,65 L155,65 L155,85 L135,85 Z M160,65 L180,65 L180,85 L160,85 Z M185,65 L205,65 L205,85 L185,85 Z M210,65 L240,65 L240,85 L210,85 Z M60,100 L240,100 L240,135 L60,135 Z',
    'SIP': 'M50,50 L250,50 L250,150 L50,150 Z M60,60 L100,60 L100,90 L60,90 Z M110,60 L150,60 L150,90 L110,90 Z M160,60 L200,60 L200,90 L160,90 Z M210,60 L240,60 L240,90 L210,90 Z M60,100 L240,100 L240,140 L60,140 Z',
    'SPA': 'M60,55 L240,55 L240,145 L60,145 Z M70,65 L95,65 L95,85 L70,85 Z M100,65 L125,65 L125,85 L100,85 Z M130,65 L155,65 L155,85 L130,85 Z M160,65 L185,65 L185,85 L160,85 Z M190,65 L230,65 L230,85 L190,85 Z M70,100 L230,100 L230,135 L70,135 Z',
    'EPA': 'M60,55 L240,55 L240,145 L60,145 Z M70,65 L95,65 L95,90 L70,90 Z M100,65 L125,65 L125,90 L100,90 Z M130,65 L155,65 L155,90 L130,90 Z M160,65 L185,65 L185,90 L160,90 Z M190,65 L230,65 L230,90 L190,90 Z M70,105 L230,105 L230,135 L70,135 Z',
    'ISM Module': 'M50,50 L250,50 L250,150 L50,150 Z M60,60 L110,60 L110,100 L60,100 Z M120,60 L240,60 L240,75 L120,75 Z M120,80 L200,80 L200,95 L120,95 Z M60,110 L240,110 L240,140 L60,140 Z',
}

default_icon = 'M50,50 L250,50 L250,150 L50,150 Z M60,60 L240,60 L240,90 L60,90 Z M60,100 L240,100 L240,140 L60,140 Z'

for p in products:
    img_path = p['image']
    c1, c2 = colors.get(p['series'], ('#7f8c8d', '#5d6d7e'))
    icon = icons.get(p['category'], default_icon)
    pn = p['partNumber']
    cat = p['category']
    series = p['series']

    # Truncate long part numbers for display
    display_pn = pn if len(pn) <= 20 else pn[:18] + '..'
    font_size = 16 if len(display_pn) <= 16 else 13

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200" viewBox="0 0 300 200">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
  </defs>
  <rect width="300" height="200" fill="url(#bg)"/>
  <rect x="0" y="0" width="300" height="4" fill="{c1}"/>
  <path d="{icon}" fill="none" stroke="{c1}" stroke-width="1.5" opacity="0.3"/>
  <text x="150" y="170" text-anchor="middle" font-family="Arial,sans-serif" font-size="{font_size}" font-weight="700" fill="{c2}">{display_pn}</text>
  <text x="150" y="188" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#94a3b8">{cat} | {series}</text>
</svg>'''

    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    with open(img_path, 'w') as f:
        f.write(svg)

print(f"Generated {len(products)} SVG placeholder images")
