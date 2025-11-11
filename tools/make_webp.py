from PIL import Image
from pathlib import Path
from typing import Optional
import sys

"""
Gera versões WebP otimizadas do banner:
 - hero-banner.webp (desktop)
 - hero-banner-mobile.webp (mobile redimensionado se não existir JPG específico)

Uso:
  python tools/make_webp.py [QUALIDADE]
Default qualidade = 82
"""

QUALITY = 82
if len(sys.argv) > 1:
    try:
        QUALITY = int(sys.argv[1])
    except ValueError:
        print("Qualidade inválida, usando 82")

root = Path(__file__).resolve().parents[1]
assets = root / 'assets'
assets.mkdir(exist_ok=True)

src_desktop = assets / 'hero-banner.jpg'
src_mobile_jpg = assets / 'hero-banner-mobile.jpg'
out_desktop_webp = assets / 'hero-banner.webp'
out_mobile_webp = assets / 'hero-banner-mobile.webp'

if not src_desktop.exists():
    raise SystemExit(f"Fonte não encontrada: {src_desktop}")

def save_webp(src: Path, dest: Path, resize_width: Optional[int] = None):
    with Image.open(src) as im:
        im = im.convert('RGB')
        if resize_width and im.width > resize_width:
            ratio = resize_width / im.width
            new_size = (resize_width, int(im.height * ratio))
            im = im.resize(new_size, Image.Resampling.LANCZOS)
        im.save(dest, 'WEBP', quality=QUALITY, method=6)

# Desktop
save_webp(src_desktop, out_desktop_webp)

# Mobile: usar arquivo específico ou gerar a partir do desktop redimensionando para largura 1080
if src_mobile_jpg.exists():
    save_webp(src_mobile_jpg, out_mobile_webp)
else:
    save_webp(src_desktop, out_mobile_webp, resize_width=1080)

def size_kb(p: Path) -> str:
    return f"{p.stat().st_size/1024:.1f} KB" if p.exists() else '---'

print("Qualidade:", QUALITY)
print(f"Desktop: {out_desktop_webp.name} -> {size_kb(out_desktop_webp)}")
print(f"Mobile:  {out_mobile_webp.name} -> {size_kb(out_mobile_webp)} (gerado {'de mobile' if src_mobile_jpg.exists() else 'de desktop'})")
