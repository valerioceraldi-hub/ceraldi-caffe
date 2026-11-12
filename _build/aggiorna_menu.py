# -*- coding: utf-8 -*-
"""Scarica dal database di Ceraldi (Supabase) le voci pubblicate del menu e le salva in menu_db.json.
Uso: python3 caffe/_build/aggiorna_menu.py   poi   python3 caffe/_build/build.py
Fonte unica: il menu che il personale gestisce dal Back Office «Ceraldi Menu». Legge solo dati pubblici
con la chiave pubblica «anon» (la stessa delle app): nessun segreto."""
import datetime, json, os, sys, urllib.request

QUI = os.path.dirname(os.path.abspath(__file__))
URL = os.environ.get("MENU_SB_URL", "https://qaqqptpprmfjlolordaq.supabase.co")
KEY = os.environ.get("MENU_SB_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhcXFwdHBwcm1mamxvbG9yZGFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4NDQ3MDgsImV4cCI6MjA5MTQyMDcwOH0.kTnxsNY3tua_ya4LCB8-vkVdQ1QBPGtLL7Gfg121d1o")

def main():
    r = urllib.request.Request(URL + "/rest/v1/menu_voci?select=id,nome,prezzo_cent&stato=eq.pubblicato&order=id&limit=2000",
                               headers={"apikey": KEY, "Authorization": "Bearer " + KEY})
    voci = json.load(urllib.request.urlopen(r, timeout=60))
    if not voci: raise SystemExit("Nessuna voce pubblicata: non sovrascrivo i dati esistenti.")
    return {"_scaricato": datetime.date.today().isoformat(), "voci": voci}

if __name__ == "__main__":
    d = main()
    json.dump(d, open(os.path.join(QUI, "menu_db.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print("Voci pubblicate:", len(d["voci"]))
