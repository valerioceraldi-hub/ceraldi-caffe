# -*- coding: utf-8 -*-
"""Illustrazioni originali del progetto Aspritz, disegnate in codice (nessuna foto generata).
Uso:  python3 _build/illustrazioni.py          -> scrive img/illustrazioni/*.svg
      python3 _build/illustrazioni.py --webp   -> crea anche le copertine WebP (serve playwright con chromium)
Stile: tavole botaniche a tratto, inchiostro ottone su avorio, come le incisioni dell'«Archivio 1973».
Sono illustrazioni, non fotografie: non mostrano la ricetta né bottiglie o etichette."""
import math, os, random, sys

QUI = os.path.dirname(os.path.abspath(__file__))
SITO = os.path.dirname(QUI)
DEST = os.path.join(SITO, "img", "illustrazioni")

OTTONE = "#7A5C2C"; OTTONE_CH = "#D4B57E"; VERDE = "#2E3A2F"; SEPPIA = "#5F5045"
ARANCIO = "#C9772F"; ARANCIO_CH = "#E2A15A"; UVA = "#B9A257"; AVORIO = "#FBF8F3"

def svg(w, h, corpo, titolo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t">'
            f'<title id="t">{titolo}</title>'
            f'<g fill="none" stroke-linecap="round" stroke-linejoin="round">{corpo}</g></svg>\n')

def foglia(x, y, lung, larg, ang, colore=VERDE, nervature=4):
    """Foglia lanceolata con nervatura centrale e laterali."""
    a = math.radians(ang)
    def p(u, v):  # u lungo la foglia, v di lato
        return (x + u * math.cos(a) - v * math.sin(a), y + u * math.sin(a) + v * math.cos(a))
    p0, p1 = p(0, 0), p(lung, 0)
    c1, c2 = p(lung * .35, -larg), p(lung * .75, -larg * .8)
    c3, c4 = p(lung * .75, larg * .8), p(lung * .35, larg)
    d = f"M{p0[0]:.1f},{p0[1]:.1f} C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p1[0]:.1f},{p1[1]:.1f} C{c3[0]:.1f},{c3[1]:.1f} {c4[0]:.1f},{c4[1]:.1f} {p0[0]:.1f},{p0[1]:.1f}Z"
    riemp = "#8E9F78" if colore == VERDE else colore
    s = f'<path d="{d}" fill="{riemp}" fill-opacity="{.38 if colore == VERDE else .25}" stroke="{colore}" stroke-width="1.6"/>'
    s += f'<path d="M{p0[0]:.1f},{p0[1]:.1f} L{p1[0]:.1f},{p1[1]:.1f}" stroke="{colore}" stroke-width="1"/>'
    for i in range(1, nervature + 1):
        t = i / (nervature + 1)
        for lato in (-1, 1):
            q0 = p(lung * t, 0); q1 = p(lung * min(t + .12, .95), lato * larg * .55 * (1 - abs(t - .45)))
            s += f'<path d="M{q0[0]:.1f},{q0[1]:.1f} L{q1[0]:.1f},{q1[1]:.1f}" stroke="{colore}" stroke-width=".7" stroke-opacity=".7"/>'
    return s

def puntinato(cx, cy, r, n, colore, seme, rmin=.6, rmax=1.4, zona=None):
    rnd = random.Random(seme); s = ''
    for _ in range(n):
        ang = rnd.random() * 2 * math.pi; d = r * math.sqrt(rnd.random())
        if zona: d = r * 9 * math.sqrt(rnd.random())
        x, y = cx + d * math.cos(ang), cy + d * math.sin(ang)
        if zona and not zona(x, y):
            continue
        s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rnd.uniform(rmin, rmax):.2f}" fill="{colore}" stroke="none"/>'
    return s

def fetta(cx, cy, r, spicchi=11, seme=3):
    """Fetta d'arancia: buccia, albedo, spicchi."""
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ARANCIO}" fill-opacity=".9" stroke="{OTTONE}" stroke-width="1.6"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{r * .9}" fill="#F3E3C6" stroke="none"/>'
    for i in range(spicchi):
        a0 = 2 * math.pi * i / spicchi + .05; a1 = 2 * math.pi * (i + 1) / spicchi - .05
        ri = r * .12; ro = r * .82
        pts = [(cx + ri * math.cos(a0), cy + ri * math.sin(a0)), (cx + ro * math.cos(a0), cy + ro * math.sin(a0)),
               (cx + ro * math.cos(a1), cy + ro * math.sin(a1)), (cx + ri * math.cos(a1), cy + ri * math.sin(a1))]
        d = (f"M{pts[0][0]:.1f},{pts[0][1]:.1f} L{pts[1][0]:.1f},{pts[1][1]:.1f} A{ro:.1f},{ro:.1f} 0 0 1 {pts[2][0]:.1f},{pts[2][1]:.1f} "
             f"L{pts[3][0]:.1f},{pts[3][1]:.1f}Z")
        s += f'<path d="{d}" fill="{ARANCIO_CH}" fill-opacity=".85" stroke="{OTTONE}" stroke-width=".7"/>'
        am = (a0 + a1) / 2
        for k in range(3):
            rr_ = r * (.35 + .15 * k)
            s += f'<path d="M{cx + rr_ * math.cos(am - .08):.1f},{cy + rr_ * math.sin(am - .08):.1f} l{2.5 * math.cos(am):.1f},{2.5 * math.sin(am):.1f}" stroke="#FFF4E2" stroke-width="1.2"/>'
    return s

# ── 1. Agrumi della Costiera ────────────────────────────────────────
def agrumi():
    s = ''
    # ramo
    s += f'<path d="M40,520 C120,450 170,380 250,330 S400,230 470,120" stroke="{SEPPIA}" stroke-width="5"/>'
    s += f'<path d="M250,330 C300,330 340,350 380,390" stroke="{SEPPIA}" stroke-width="3.5"/>'
    s += f'<path d="M180,395 C170,350 150,320 120,300" stroke="{SEPPIA}" stroke-width="3"/>'
    for x, y, l, w, a in [(470, 120, 110, 30, -60), (430, 170, 120, 34, -15), (360, 230, 115, 32, -100), (300, 285, 105, 30, 20),
                          (120, 300, 100, 28, -140), (150, 330, 110, 30, -70), (380, 390, 100, 28, 40), (340, 355, 95, 26, 95),
                          (90, 470, 95, 26, -150), (215, 365, 90, 25, 160)]:
        s += foglia(x, y, l, w, a)
    # arancia intera, appesa
    cx, cy, r = 300, 455, 82
    s += f'<path d="M300,345 L300,375" stroke="{SEPPIA}" stroke-width="3"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ARANCIO}" fill-opacity=".92" stroke="{OTTONE}" stroke-width="1.8"/>'
    s += puntinato(cx, cy, r - 6, 520, "#8E4A17", 7, .5, 1.1)
    s += f'<path d="M{cx - 48},{cy - 40} A60,60 0 0 1 {cx - 5},{cy - 66}" stroke="#FCE3C0" stroke-width="5" stroke-opacity=".7"/>'
    s += f'<circle cx="{cx}" cy="{cy - r + 4}" r="5" fill="{VERDE}" stroke="none"/>'
    # fetta (come quella disidratata che decora il bicchiere)
    s += fetta(130, 610, 62)
    return svg(560, 700, s, "Illustrazione: ramo di agrumi con frutto, fetta e fiore")

# ── 2. Asprinio e alberata aversana ─────────────────────────────────
def asprinio():
    s = ''
    # pioppi dell'alberata, molto alti, con la vite che li sposa
    for x0, h in ((90, 600), (300, 640), (510, 600)):
        s += f'<path d="M{x0},680 C{x0 - 4},{680 - h * .5} {x0 + 6},{680 - h * .8} {x0},{680 - h}" stroke="{SEPPIA}" stroke-width="5"/>'
        cy_ = 680 - h * .62; ry = h * .36
        s += f'<ellipse cx="{x0}" cy="{cy_:.0f}" rx="34" ry="{ry:.0f}" fill="#8E9F78" fill-opacity=".22" stroke="{VERDE}" stroke-width="1.2" stroke-dasharray="1 5"/>'
        s += puntinato(x0, cy_, 30, 260, VERDE, x0, .6, 1.5, zona=lambda x, y, c=cy_, r=ry, x0=x0: ((x - x0) / 34) ** 2 + ((y - c) / r) ** 2 < 1)
        for k in range(6):
            y = 680 - h * (.36 + .1 * k); lato = -1 if k % 2 else 1
            s += f'<path d="M{x0},{y:.0f} q{lato * 14},{-10} {lato * 24},{-30}" stroke="{SEPPIA}" stroke-width="1.6"/>'
    # festoni di vite tra un pioppo e l'altro
    for xa, xb, y in ((90, 300, 250), (300, 510, 250), (90, 300, 380), (300, 510, 380)):
        mx = (xa + xb) / 2
        s += f'<path d="M{xa},{y} Q{mx},{y + 90} {xb},{y}" stroke="{OTTONE}" stroke-width="2.4"/>'
        for t in (.25, .5, .75):
            px = xa + (xb - xa) * t; py = y + 90 * 2 * t * (1 - t) * 1.0
            s += foglia(px, py, 30, 12, 70 + 40 * t, VERDE, 2)
    # grappolo di uva bianca in primo piano
    rnd = random.Random(11); cx, cy = 300, 520
    acini = []
    for riga, n in enumerate((4, 5, 6, 5, 5, 4, 3, 3, 2, 1)):
        off = (-14 if riga in (1, 2) else 0) + (6 if riga > 5 else 0)
        for i in range(n):
            acini.append((cx + off + (i - (n - 1) / 2) * 19 + rnd.uniform(-4, 4), cy + riga * 16 + rnd.uniform(-3, 3)))
    rnd.shuffle(acini); acini.sort(key=lambda q: q[1])
    s += f'<path d="M{cx},{cy - 60} C{cx + 8},{cy - 40} {cx - 6},{cy - 22} {cx},{cy - 12}" stroke="{SEPPIA}" stroke-width="3"/>'
    s += foglia(cx, cy - 50, 70, 32, -20, VERDE, 3)
    for x, y in acini:
        s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{UVA}" fill-opacity=".85" stroke="{OTTONE}" stroke-width="1.2"/>'
        s += f'<path d="M{x - 6:.1f},{y - 3:.1f} a6,6 0 0 1 5,-5" stroke="#F5EBC8" stroke-width="2"/>'
    # la scala dei vendemmiatori
    s += f'<path d="M455,680 L520,250 M485,680 L550,250" stroke="{OTTONE}" stroke-width="1.6"/>'
    for k in range(1, 14):
        t = k / 14
        s += f'<path d="M{455 + 65 * t:.0f},{680 - 430 * t:.0f} L{485 + 65 * t:.0f},{680 - 430 * t:.0f}" stroke="{OTTONE}" stroke-width="1.2"/>'
    s += f'<path d="M20,680 L580,680" stroke="{OTTONE}" stroke-width="1.2"/>'
    return svg(600, 700, s, "Illustrazione: alberata aversana, viti maritate ai pioppi, grappolo d'uva e scala da vendemmia")

# ── 3. Radici ed erbe ───────────────────────────────────────────────
def radici():
    s = f'<path d="M30,330 L530,330" stroke="{OTTONE}" stroke-width="1.2" stroke-dasharray="2 6"/>'
    # erba alta a sinistra
    for k, (x, h) in enumerate(((110, 240), (150, 200))):
        s += f'<path d="M{x},330 C{x + 6},{330 - h * .5} {x - 8},{330 - h * .8} {x + 4},{330 - h}" stroke="{VERDE}" stroke-width="2.2"/>'
        for j in range(5):
            y = 330 - h * (.25 + .15 * j); lato = 1 if (j + k) % 2 else -1
            s += foglia(x, y, 46 - j * 4, 13, -90 + lato * 55, VERDE, 2)
    # pianta a destra, foglie larghe
    s += f'<path d="M400,330 C398,270 402,230 400,180" stroke="{VERDE}" stroke-width="2.4"/>'
    for y, l, a in ((300, 90, -150), (290, 95, -30), (245, 80, -140), (235, 82, -40), (195, 60, -100)):
        s += foglia(400, y, l, 26, a, VERDE, 3)
    # radici sotto terra
    rnd = random.Random(5)
    def radice(x, y, lung, ang, spess, prof):
        nonlocal s
        a = math.radians(ang)
        x2, y2 = x + lung * math.cos(a), y + lung * math.sin(a)
        cx_, cy_ = (x + x2) / 2 + rnd.uniform(-14, 14), (y + y2) / 2 + rnd.uniform(-8, 8)
        s += f'<path d="M{x:.0f},{y:.0f} Q{cx_:.0f},{cy_:.0f} {x2:.0f},{y2:.0f}" stroke="{SEPPIA}" stroke-width="{spess:.1f}"/>'
        if prof > 0:
            for _ in range(2):
                radice(x2, y2, lung * rnd.uniform(.5, .7), ang + rnd.uniform(-38, 38), spess * .62, prof - 1)
    for x in (130, 400):
        for ang in (75, 105):
            radice(x, 332, 62, ang, 3.6, 3)
    # ceppo nodoso al centro con radici fibrose
    s += f'<path d="M246,330 C230,344 240,360 248,370 C254,380 266,384 276,380 C292,374 304,360 300,344 C298,334 290,330 282,330Z" fill="#B78F5A" fill-opacity=".35" stroke="{SEPPIA}" stroke-width="1.8"/>'
    for y_ in (342, 356, 368):
        s += f'<path d="M{250 + (y_ - 330) * .2:.0f},{y_} q20,5 {44 - (y_ - 330) * .5:.0f},-1" stroke="{SEPPIA}" stroke-width=".9"/>'
    for ang in (60, 80, 100, 120):
        radice(272, 376, 60, ang, 5, 3)
    s += f'<path d="M272,330 C268,300 262,280 252,262 M272,330 C278,302 288,282 300,268 M272,330 L272,250" stroke="{VERDE}" stroke-width="2"/>'
    s += foglia(252, 262, 44, 13, -125, VERDE, 2) + foglia(300, 268, 44, 13, -55, VERDE, 2) + foglia(272, 250, 40, 12, -90, VERDE, 2)
    return svg(560, 560, s, "Illustrazione botanica: erbe aromatiche e radici sotto la linea del terreno")

# ── 4. Mappa: dove nascono gli ingredienti (schema non in scala) ─────
def mappa(lang="it"):
    T = {"it": ("Schema non in scala", "Aversa", "Asprinio", "Napoli", "Piazza Carità", "Costiera Amalfitana", "Agrumi", "Golfo di Napoli", "Vesuvio"),
         "en": ("Not to scale", "Aversa", "Asprinio", "Naples", "Piazza Carità", "Amalfi Coast", "Citrus", "Gulf of Naples", "Vesuvius")}[lang]
    s = ''
    # costa stilizzata: golfo di Napoli, penisola sorrentina verso ovest, Costiera Amalfitana sul versante sud
    s += (f'<path d="M20,236 C80,250 140,284 196,300 C230,310 262,312 300,330 C344,350 370,380 398,418 '
          f'C404,428 396,434 384,432 C350,428 320,440 290,450 C262,460 236,466 214,470 C204,472 204,480 214,484 '
          f'C250,494 290,500 330,506 C370,512 410,516 450,514 C490,512 530,494 580,470" stroke="{OTTONE}" stroke-width="2"/>')
    for k in range(4):  # onde nel golfo
        y = 372 + k * 18
        s += f'<path d="M{150 + k * 14},{y} q10,-7 20,0 t20,0 t20,0" stroke="{OTTONE_CH}" stroke-width="1.2"/>'
    s += f'<text x="100" y="352" font-family="Jost, Arial, sans-serif" font-size="14" letter-spacing="2" fill="{OTTONE}">{T[7].upper()}</text>'
    # Vesuvio
    s += f'<path d="M372,300 L410,244 L420,250 L430,242 L466,300" stroke="{SEPPIA}" stroke-width="1.6"/>'
    s += f'<text x="396" y="320" font-family="Jost, Arial, sans-serif" font-size="13" fill="{SEPPIA}">{T[8]}</text>'
    # percorso tratteggiato verso Piazza Carità
    s += f'<path d="M210,110 C230,170 236,220 240,282" stroke="{OTTONE}" stroke-width="2" stroke-dasharray="3 7"/>'
    s += f'<path d="M446,522 C480,440 380,340 256,298" stroke="{OTTONE}" stroke-width="2" stroke-dasharray="3 7"/>'
    def punto(x, y, nome, sotto, grande=False, dx=18, anc="start", dy=0):
        r = 11 if grande else 7
        p = f'<circle cx="{x}" cy="{y}" r="{r}" fill="{"#6E1A22" if grande else AVORIO}" stroke="{OTTONE}" stroke-width="2"/>'
        if grande:
            p += f'<circle cx="{x}" cy="{y}" r="20" stroke="#6E1A22" stroke-width="1.2" stroke-opacity=".5"/>'
        tx = x + dx if anc == "start" else x - dx
        p += f'<text x="{tx}" y="{y - 2 + dy}" text-anchor="{anc}" stroke="{AVORIO}" stroke-width="6" paint-order="stroke" font-family="Bodoni Moda, Georgia, serif" font-size="{26 if grande else 22}" fill="#23170F">{nome}</text>'
        p += f'<text x="{tx}" y="{y + 20 + dy}" text-anchor="{anc}" stroke="{AVORIO}" stroke-width="5" paint-order="stroke" font-family="Jost, Arial, sans-serif" font-size="13" letter-spacing="1.6" fill="{OTTONE}">{sotto.upper()}</text>'
        return p
    s += punto(210, 100, T[1], T[2])
    s += punto(244, 290, T[3], T[4], grande=True, dx=30, anc="end")
    s += punto(446, 522, T[5], T[6], dx=0, anc="end", dy=40)
    s += f'<text x="580" y="680" text-anchor="end" font-family="Jost, Arial, sans-serif" font-size="12" fill="{SEPPIA}">{T[0]}</text>'
    tit = "Mappa schematica: Aversa, Napoli e la Costiera Amalfitana" if lang == "it" else "Schematic map: Aversa, Naples and the Amalfi Coast"
    return svg(600, 700, s, tit)

# ── 5. Fregio sottile (separatore decorativo) ───────────────────────
def fregio():
    s = f'<path d="M10,30 L250,30 M350,30 L590,30" stroke="{OTTONE_CH}" stroke-width="1"/>'
    s += foglia(300, 30, 34, 10, -160, OTTONE_CH, 2) + foglia(300, 30, 34, 10, -20, OTTONE_CH, 2)
    s += f'<circle cx="300" cy="30" r="9" fill="{ARANCIO}" stroke="{OTTONE_CH}" stroke-width="1.2"/>'
    return svg(600, 60, s, "")

# ── Copertine raster (per articoli e anteprime social) ──────────────
def copertina(nome_svg, sfondo=AVORIO):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0}}body{{width:1600px;height:1200px;background:{sfondo};display:flex;align-items:center;justify-content:center;position:relative}}
.cornice{{position:absolute;inset:44px;border:2px solid {OTTONE_CH}}}.cornice::after{{content:"";position:absolute;inset:10px;border:1px solid {OTTONE_CH};opacity:.6}}
img{{height:1000px;width:auto;position:relative}}</style></head><body><div class="cornice"></div><img src="{nome_svg}"></body></html>'''

FILE = {"aspritz-agrumi.svg": agrumi, "aspritz-asprinio.svg": asprinio, "aspritz-radici-erbe.svg": radici,
        "aspritz-mappa.svg": lambda: mappa("it"), "aspritz-mappa-en.svg": lambda: mappa("en"), "aspritz-fregio.svg": fregio}
COPERTINE = {"illustrazione-agrumi": "aspritz-agrumi.svg", "illustrazione-asprinio": "aspritz-asprinio.svg",
             "illustrazione-radici-erbe": "aspritz-radici-erbe.svg", "illustrazione-mappa-aspritz": "aspritz-mappa.svg"}

if __name__ == "__main__":
    os.makedirs(DEST, exist_ok=True)
    for nome, f in FILE.items():
        open(os.path.join(DEST, nome), "w", encoding="utf-8").write(f())
    print("SVG scritti in img/illustrazioni/")
    if "--webp" in sys.argv:
        from playwright.sync_api import sync_playwright
        from PIL import Image
        import io
        with sync_playwright() as p:
            b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1600, "height": 1200})
            for nome, sorgente in COPERTINE.items():
                tmp = os.path.join(DEST, "_copertina.html")
                open(tmp, "w", encoding="utf-8").write(copertina(sorgente))
                pg.goto("file://" + tmp); pg.wait_for_timeout(300)
                im = Image.open(io.BytesIO(pg.screenshot())).convert("RGB")
                for w in (1024, 640):
                    im.resize((w, w * 3 // 4), Image.LANCZOS).save(os.path.join(SITO, "img", f"{nome}-{w}.webp"), "WEBP", quality=82, method=6)
                os.remove(tmp)
            b.close()
        print("Copertine WebP create")
