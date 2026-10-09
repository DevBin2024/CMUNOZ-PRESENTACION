"""Traza los contornos del PNG oficial para una marca de agua monocroma."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

root = Path(__file__).resolve().parent
source = root.parent / 'imagenes' / 'logo-bionativa.png'
im = Image.open(source).convert('RGBA')
scale = 3
a = np.asarray(im.resize((im.width * scale, im.height * scale), Image.Resampling.BICUBIC))
ink = np.where(a[:, :, 3] > 128, 255 - a[:, :, :3].min(axis=2), 0).astype('uint8')
mask = np.asarray(Image.fromarray(ink).filter(ImageFilter.GaussianBlur(1.4))) > 80
h, w = mask.shape
edges = {}
def edge(p, q):
    edges.setdefault(p, []).append(q)
for y, x in np.argwhere(mask):
    x, y = int(x), int(y)
    if y == 0 or not mask[y-1, x]: edge((x,y), (x+1,y))
    if x == w-1 or not mask[y,x+1]: edge((x+1,y), (x+1,y+1))
    if y == h-1 or not mask[y+1,x]: edge((x+1,y+1), (x,y+1))
    if x == 0 or not mask[y,x-1]: edge((x,y+1), (x,y))

def simplify(points, tolerance=.8):
    if len(points) < 3: return points
    p = np.asarray(points, dtype=float)
    v = p[-1] - p[0]
    length = np.linalg.norm(v)
    d = np.abs(v[0]*(p[:,1]-p[0,1])-v[1]*(p[:,0]-p[0,0])) / length if length else np.linalg.norm(p-p[0],axis=1)
    i = int(d.argmax())
    if d[i] <= tolerance: return [points[0],points[-1]]
    return simplify(points[:i+1],tolerance)[:-1] + simplify(points[i:],tolerance)

contours = []
while edges:
    start = next(iter(edges))
    p = start
    pts = [p]
    while p in edges:
        q = edges[p].pop()
        if not edges[p]: del edges[p]
        p = q
        if p == start: break
        pts.append(p)
    if len(pts) < 8: continue
    area = sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[(i+1)%len(pts)][0]*pts[i][1] for i in range(len(pts))) / 2
    if abs(area) < 2: continue
    mid = len(pts)//2
    pts = simplify(pts[:mid+1])[:-1] + simplify(pts[mid:]+[pts[0]])[:-1]
    # Suavizado leve del contorno, inferior a un píxel de la imagen original.
    for _ in range(2):
        smooth=[]
        for i, p in enumerate(pts):
            q = pts[(i+1)%len(pts)]
            smooth += [(p[0]*.75+q[0]*.25,p[1]*.75+q[1]*.25), (p[0]*.25+q[0]*.75,p[1]*.25+q[1]*.75)]
        pts = smooth
    contours.append((area, [(x/scale,y/scale) for x,y in pts]))

paths=[]
for area, pts in contours:
    paths.append('M'+' L'.join(f'{x:.2f},{y:.2f}' for x,y in pts)+' Z')
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {im.width} {im.height}"><title>Bionativa — contornos del logo oficial</title><path fill="#d8ed99" fill-rule="evenodd" d="'+ ' '.join(paths)+'"/></svg>\n'
(root/'logo-fondo.svg').write_text(svg,encoding='utf-8')

# Vista previa del mismo trazado a gran tamaño para comprobar formas y letras.
preview = Image.new('RGB',(900,900),'#164b36')
draw = ImageDraw.Draw(preview)
for area,pts in sorted(contours,key=lambda item:abs(item[0]),reverse=True):
    draw.polygon([(x*900/im.width,y*900/im.height) for x,y in pts],fill='#426347' if area>0 else '#164b36')
preview.save(root/'logo-fondo-preview.png')
print(f'Logo oficial: {im.size}; contornos conservados: {len(contours)}; SVG: {len(svg)} caracteres')
