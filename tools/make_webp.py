from PIL import Image
from pathlib import Path

root = Path(__file__).resolve().parents[1]
assets = root / 'assets'
assets.mkdir(exist_ok=True)

src_desktop = assets / 'hero-banner.jpg'
src_mobile_jpg = assets / 'hero-banner-mobile.jpg'
src_mobile_webp = assets / 'hero-banner-mobile.webp'

out_desktop_webp = assets / 'hero-banner.webp'
out_mobile_webp = assets / 'hero-banner-mobile.webp'

if not src_desktop.exists():
    raise SystemExit(f"Fonte não encontrada: {src_desktop}")

# Gera hero-banner.webp a partir do JPG desktop
with Image.open(src_desktop) as im:
    im = im.convert('RGB')
    im.save(out_desktop_webp, 'WEBP', quality=82, method=6)

# Se existir mobile JPG e não existir mobile WEBP, converte
if src_mobile_jpg.exists() and not src_mobile_webp.exists():
    with Image.open(src_mobile_jpg) as im:
        im = im.convert('RGB')
        im.save(out_mobile_webp, 'WEBP', quality=82, method=6)

print('Gerado:', out_desktop_webp.name, out_mobile_webp.name if out_mobile_webp.exists() else '(sem mobile)')
