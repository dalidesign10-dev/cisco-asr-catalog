import urllib.request
import ssl
import os
import time

ssl._create_default_https_context = ssl._create_unverified_context

# Try Wikipedia/Wikimedia Commons and other open sources
# Also try direct Cisco product page image URLs with different patterns
sources = [
    # Cisco product images - various known working patterns
    ("images/asr9000/ASR-9006-AC.jpg", "https://www.cisco.com/c/dam/en/us/products/routers/asr-9000-series-aggregation-services-routers/asr_9006_background.jpg"),
    ("images/asr9000/ASR-9010-AC.jpg", "https://www.cisco.com/c/dam/en/us/products/routers/asr-9000-series-aggregation-services-routers/asr_9010_background.jpg"),
    ("images/asr1000/ASR1001-X.jpg", "https://www.cisco.com/c/dam/en/us/products/routers/asr-1000-series-aggregation-services-routers/asr_1001_x_background.jpg"),

    # Try Cisco's new product imagery URLs
    ("images/asr9000/ASR-9006-AC.jpg", "https://www.cisco.com/c/dam/en/us/support/docs/routers/asr-9000-series-aggregation-services-routers/asr9006.jpg"),

    # Cisco Press/Marketing images
    ("images/asr9000/asr9000.png", "https://www.cisco.com/c/dam/assets/prod/routers/ps5763/images/nb-06-asr-9k-cto-background-520x390.jpg"),
    ("images/asr1000/asr1000.png", "https://www.cisco.com/c/dam/assets/prod/routers/ps9343/images/nb-06-asr1k-background-520x390.jpg"),
    ("images/asr900/asr900.png", "https://www.cisco.com/c/dam/assets/prod/routers/ps12511/images/nb-06-asr903-background-520x390.jpg"),
    ("images/asr920/asr920.png", "https://www.cisco.com/c/dam/assets/prod/routers/ps14770/images/nb-06-asr920-background-520x390.jpg"),
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "image/*,*/*;q=0.8",
}

for path, url in sources:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) > 3000:
                with open(path, 'wb') as f:
                    f.write(data)
                print(f"OK: {path} ({len(data)} bytes) from {url}")
            else:
                print(f"TOO SMALL: {path}")
    except Exception as e:
        print(f"FAIL: {path} - {e}")
    time.sleep(0.3)

# Try getting images via Google's cached thumbnails from search
# These are publicly accessible product photos
wiki_images = [
    ("images/asr9000/asr9000-wiki.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Cisco_ASR_9010.jpg/1280px-Cisco_ASR_9010.jpg"),
    ("images/asr9000/asr9000-wiki2.jpg", "https://upload.wikimedia.org/wikipedia/commons/6/6b/Cisco_ASR_9010.jpg"),
]

for path, url in wiki_images:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) > 3000:
                with open(path, 'wb') as f:
                    f.write(data)
                print(f"WIKI OK: {path} ({len(data)} bytes)")
    except Exception as e:
        print(f"WIKI FAIL: {path} - {e}")
    time.sleep(0.3)
