import urllib.request
import ssl
import os
import time
import json

ssl._create_default_https_context = ssl._create_unverified_context

# Real Cisco product image URLs from cisco.com and other reliable sources
cisco_images = {
    # ASR 9000 Series
    "images/asr9000/ASR-9001.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-9000-series-aggregation-services-routers/asr-9001-background.jpg",
    "images/asr9000/ASR-9006-AC.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-9000-series-aggregation-services-routers/asr-9006-background.jpg",
    "images/asr9000/ASR-9010-AC.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-9000-series-aggregation-services-routers/asr-9010-background.jpg",
    "images/asr9000/ASR-9904.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-9000-series-aggregation-services-routers/asr-9904-background.jpg",
    "images/asr9000/ASR-9906.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-9000-series-aggregation-services-routers/asr-9906-background.jpg",
    "images/asr9000/ASR-9910.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-9000-series-aggregation-services-routers/asr-9910-background.jpg",
    "images/asr9000/ASR-9922.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-9000-series-aggregation-services-routers/asr-9922-background.jpg",

    # ASR 1000 Series
    "images/asr1000/ASR1001-X.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-1000-series-aggregation-services-routers/asr-1001x-background.jpg",
    "images/asr1000/ASR1002-X.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-1000-series-aggregation-services-routers/asr-1002x-background.jpg",
    "images/asr1000/ASR1002-HX.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-1000-series-aggregation-services-routers/asr-1002hx-background.jpg",
    "images/asr1000/ASR1004.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-1000-series-aggregation-services-routers/asr-1004-background.jpg",
    "images/asr1000/ASR1006.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-1000-series-aggregation-services-routers/asr-1006-background.jpg",
    "images/asr1000/ASR1013.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-1000-series-aggregation-services-routers/asr-1013-background.jpg",

    # ASR 900 Series
    "images/asr900/ASR-903.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-903-series-aggregation-services-routers/asr-903-background.jpg",
    "images/asr900/ASR-907.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-903-series-aggregation-services-routers/asr-907-background.jpg",

    # ASR 920
    "images/asr920/ASR-920-24SZ-M.jpg": "https://www.cisco.com/c/dam/en/us/products/collateral/routers/asr-920-series-aggregation-services-router/asr-920-background.jpg",
}

# Additional patterns to try from Cisco
alt_patterns = [
    "https://www.cisco.com/c/dam/en/us/products/routers/asr-{series}-series-aggregation-services-routers/{sku_lower}.jpg",
    "https://www.cisco.com/c/dam/en/us/products/routers/asr-{series}-series-aggregation-services-routers/images/{sku_lower}.jpg",
    "https://www.cisco.com/c/dam/en/us/support/docs/routers/{sku_lower}.jpg",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "image/*,*/*;q=0.8",
}

downloaded = 0
failed = 0

# First try specific known URLs
for path, url in cisco_images.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) > 3000:
                with open(path, 'wb') as f:
                    f.write(data)
                downloaded += 1
                print(f"OK: {path} ({len(data)} bytes)")
            else:
                failed += 1
                print(f"TOO SMALL: {path} ({len(data)} bytes)")
    except Exception as e:
        failed += 1
        print(f"FAIL: {path} - {e}")
    time.sleep(0.3)

print(f"\nCisco CDN: {downloaded} downloaded, {failed} failed")

# Now try to get images from Cisco product page screenshots via search
# Try alternative image sources
alt_sources = {
    "images/asr9000": [
        ("asr9000-lineup.jpg", "https://www.cisco.com/c/dam/en/us/products/routers/asr-9000-series-aggregation-services-routers/images/asr-9000-lineup-large.jpg"),
        ("asr9000-series.jpg", "https://www.cisco.com/c/dam/en/us/products/routers/asr-9000-series-aggregation-services-routers/images/asr9000.jpg"),
    ],
    "images/asr1000": [
        ("asr1000-lineup.jpg", "https://www.cisco.com/c/dam/en/us/products/routers/asr-1000-series-aggregation-services-routers/images/asr-1000-lineup.jpg"),
        ("asr1000-series.jpg", "https://www.cisco.com/c/dam/en/us/products/routers/asr-1000-series-aggregation-services-routers/images/asr1000.jpg"),
    ],
    "images/asr900": [
        ("asr900-lineup.jpg", "https://www.cisco.com/c/dam/en/us/products/routers/asr-903-series-aggregation-services-routers/images/asr-903.jpg"),
    ],
    "images/asr920": [
        ("asr920-series.jpg", "https://www.cisco.com/c/dam/en/us/products/routers/asr-920-series-aggregation-services-router/images/asr-920.jpg"),
    ],
}

for folder, imgs in alt_sources.items():
    for fname, url in imgs:
        path = os.path.join(folder, fname)
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                if len(data) > 3000:
                    with open(path, 'wb') as f:
                        f.write(data)
                    print(f"ALT OK: {path} ({len(data)} bytes)")
        except:
            print(f"ALT FAIL: {path}")
        time.sleep(0.3)
