# App icons

`icon.svg` is the master. The PNGs are generated from it:

```bash
chromium --headless --disable-gpu --hide-scrollbars --window-size=1024,1200 \
  --screenshot=shot.png "file://$PWD/icon.svg"
python3 -c "
from PIL import Image
im = Image.open('shot.png').convert('RGB').crop((0,0,1024,1024))
for s, n in ((512,'icon-512.png'),(192,'icon-192.png'),(180,'apple-touch-icon.png'),(32,'favicon-32.png')):
    im.resize((s,s), Image.LANCZOS).save(n, optimize=True)
"
```

Sizes: 512 + 192 for the Android/Chrome manifest (also used as maskable —
keep the artwork inside the middle 80%), 180 for the iOS home screen,
32 for the browser tab.
