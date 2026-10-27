# -*- coding: utf-8 -*-
"""Contenuti del progetto Aspritz: pagina /aspritz/ (IT ed EN), fascia in home, sei articoli e la loro categoria.
Fatti sull'Aspritz confermati da Ceraldi (brief del 27/10/2026) e dal menu qromo, voce «Aspritz»:
  «aperitivo di nostra produzione con infusione di agrumi selezionati della costiera amalfitana, erbe e radici,
   miscelato con Asprinio di Aversa DOC spumante e arance disidratate».
Profilo sensoriale confermato: profumato, agrumato, dolce ma pulito, fresco al palato.
NON aggiungere ingredienti, dosi, tecniche, date di nascita della ricetta o premi non confermati.
Fatti su Asprinio, Costiera e storia dell'aperitivo: solo dalle fonti elencate in FONTI_ASPRITZ."""

# Data reale di pubblicazione degli articoli: se si pubblica in un altro giorno, cambiarla qui (una sola volta)
DATA_ASPRITZ = "2026-10-27"

# ── Fasce della home ─────────────────────────────────────────────────
HOME_ASPRITZ = {
    "it": dict(
        occhiello="La nostra firma della sera",
        h2="Aspritz. Il nostro modo di raccontare la&nbsp;Campania.",
        testo=("Un aperitivo ideato da Ceraldi, dove le erbe e le radici incontrano i profumi della Costiera Amalfitana "
               "e le bollicine dell'Asprinio di Aversa. Non è uno spritz come gli altri: lo prepariamo noi, partendo dal territorio."),
        cta="Scopri la storia dell'Aspritz",
        tappe=[("Aversa", "Asprinio"), ("Napoli", "Piazza Carità"), ("Costiera Amalfitana", "Agrumi")],
        alt="L'Aspritz di Ceraldi Caffè: due calici con ghiaccio e fetta d'arancia disidratata sul bancone",
    ),
    "en": dict(
        occhiello="Our evening signature",
        h2="Aspritz. Our way of telling the story of&nbsp;Campania.",
        testo=("An aperitivo created by Ceraldi, where herbs and roots meet the scents of the Amalfi Coast and the bubbles "
               "of Asprinio di Aversa. It is not just another spritz: we make it ourselves, starting from the land around Naples."),
        cta="Discover the story of the Aspritz",
        tappe=[("Aversa", "Asprinio"), ("Naples", "Piazza Carità"), ("Amalfi Coast", "Citrus")],
        alt="Ceraldi Caffè's Aspritz: two stemmed glasses with ice and a dried orange slice on the counter",
    ),
}

# ── Pagina /aspritz/ ─────────────────────────────────────────────────
PAGINA_ASPRITZ = {
"it": dict(
 titolo_seo="Aspritz, l'aperitivo ideato da Ceraldi a Napoli",
 descrizione="L'Aspritz di Ceraldi Caffè: infusione di agrumi della Costiera Amalfitana, erbe e radici con Asprinio di Aversa spumante. Aperitivo in Piazza Carità, Napoli.",
 briciola="Aspritz",
 occhiello="Una creazione Ceraldi · Piazza Carità, Napoli",
 h1="Aspritz",
 sotto="Il territorio campano, nella nostra idea di aperitivo.",
 intro=("Agrumi della Costiera Amalfitana, erbe e radici in un'infusione che prepariamo noi; l'Asprinio di Aversa spumante a completarla. "
        "Un aperitivo nato in Piazza Carità per raccontare la Campania in un bicchiere."),
 vai="Dove assaggiarlo",
 alt_hero="L'Aspritz di Ceraldi Caffè: due calici con ghiaccio e fetta d'arancia disidratata sul bancone",
 # B
 idea_occ="L'idea", idea_h2="Non un altro spritz: il nostro",
 idea="""<p class="capolettera">Ceraldi nasce nel 1973 come bar napoletano e da allora lavora dentro una tradizione precisa: il caffè al bancone, la pasticceria fatta nei nostri laboratori, i prodotti della Campania. Quando abbiamo pensato all'aperitivo, la domanda è stata la stessa che ci facciamo per un dolce: come lo racconterebbe Napoli?</p>
<p>Lo spritz è una formula conosciuta ovunque: una base amaricante, un vino con le bollicine, il ghiaccio, una nota di agrume. Non volevamo replicarla. Volevamo tenerne la struttura e cambiarne la voce, scegliendo ingredienti che arrivano da luoghi a poche decine di chilometri dal nostro bancone.</p>
<p>Così è nato l'Aspritz: una base aromatica di nostra produzione, ottenuta per infusione di agrumi della Costiera Amalfitana, erbe e radici; e, a completarla, l'Asprinio di Aversa spumante, il vino bianco della pianura a nord di Napoli. Nel nome si sentono le sue due anime: l'Asprinio e lo spritz.</p>""",
 mappa_cap="Tre luoghi, un bicchiere: l'Asprinio dall'agro aversano, gli agrumi dalla Costiera Amalfitana, il bancone di Piazza Carità. Schema non in scala.",
 mappa_alt="Mappa schematica della Campania con Aversa, Napoli e la Costiera Amalfitana",
 # C
 ingr_occ="Gli ingredienti", ingr_h2="Tre elementi, tre paesaggi",
 ingr_p="Gli elementi che danno carattere all'Aspritz sono pochi, e ognuno porta con sé un pezzo di Campania.",
 ingr=[
  ("aspritz-radici-erbe.svg", "La base", "Erbe e radici",
   "La base dell'Aspritz è un aperitivo di nostra produzione, ottenuto per infusione di erbe e radici insieme agli agrumi. È la parte che dà profondità: la nota aromatica e amaricante che bilancia la dolcezza e la freschezza degli altri elementi. Quali erbe e quali radici resta una ricetta della casa.",
   "radici-ed-erbe", "Radici ed erbe nell'aperitivo",
   "Illustrazione botanica di erbe aromatiche e radici"),
  ("aspritz-agrumi.svg", "Il profumo · Costiera Amalfitana", "Agrumi della Costiera",
   "Gli agrumi arrivano dalla Costiera Amalfitana, il paesaggio di terrazzamenti e muretti a secco affacciato sul golfo di Salerno, Patrimonio dell'Umanità UNESCO dal 1997. Nell'Aspritz portano il profumo; nel bicchiere tornano come fetta d'arancia disidratata.",
   "agrumi-costiera-amalfitana", "Gli agrumi della Costiera Amalfitana",
   "Illustrazione di un ramo di agrumi con un'arancia intera e una fetta"),
  ("aspritz-asprinio.svg", "Le bollicine · Agro aversano", "Asprinio di Aversa spumante",
   "È il bianco dell'agro aversano, tra le province di Caserta e Napoli, tutelato dalla DOC «Aversa» dal 1993. Le sue viti crescono anche sull'alberata aversana, maritate ai pioppi e alte diversi metri, vendemmiate con lunghe scale. Un vino dall'acidità vivace, che nell'Aspritz porta le bollicine e la freschezza.",
   "asprinio-di-aversa", "Asprinio di Aversa: il carattere di un vino campano",
   "Illustrazione dell'alberata aversana: viti maritate ai pioppi, grappolo d'uva e scala da vendemmia"),
 ],
 leggi="Approfondisci",
 # D
 senso_occ="Il carattere", senso_h2="Com'è, al primo sorso",
 senso=[("Profumato", "Il profumo arriva prima del sorso: è il lavoro degli agrumi e delle erbe."),
        ("Agrumato", "La nota della Costiera accompagna il bicchiere dall'inizio alla fine, netta e luminosa."),
        ("Dolce, ma pulito", "Una dolcezza misurata, che non appesantisce il palato."),
        ("Fresco al palato", "Le bollicine dell'Asprinio lo tengono fresco, sorso dopo sorso.")],
 # E
 crea_occ="Una creazione Ceraldi", crea_h2="Ideato e preparato da noi",
 crea=[("Ideato da noi", "L'Aspritz non è un prodotto comprato e versato: è una ricetta nostra, pensata per stare accanto alla nostra pasticceria e al nostro caffè, con la stessa idea di fondo: partire dalla Campania."),
       ("Preparato da noi", "La base aromatica è di nostra produzione, come i dolci della vetrina. Prepararla noi ci permette di scegliere da dove vengono gli ingredienti."),
       ("Completato al bancone", "Al momento di servirlo lo completiamo con l'Asprinio di Aversa spumante, il ghiaccio e una fetta d'arancia disidratata.")],
 crea_nota="«Artigiani per passione», il nostro motto dal 1973, vale anche di sera.",
 crea_alt="Aperitivo al tavolo da Ceraldi Caffè: calice con fetta d'agrume disidratata e un cocktail su tovaglioli bordeaux",
 # F
 napoli_occ="A Napoli", napoli_h2="Un aperitivo a Napoli, con gli ingredienti della Campania",
 napoli="""<p>Chi visita Napoli cerca spesso un modo per assaggiare la città, non solo per vederla. Il caffè al bancone, la sfogliatella, il babà: la tradizione gastronomica napoletana è fatta di gesti quotidiani. Con l'Aspritz abbiamo voluto portare la stessa idea all'ora dell'aperitivo, usando ingredienti e riferimenti campani.</p>
<p>Non è una ricetta antica e non pretende di esserlo: è una creazione contemporanea, la nostra. Poggia però su una cultura molto più antica, come quella dell'Asprinio, vino documentato già nel Cinquecento e a lungo di casa nelle taverne napoletane.</p>
<p>Da Ceraldi l'aperitivo si prende al bancone o in sala, tra gli specchi e le poltroncine rosse, lungo via Toledo, a pochi passi dalla Pignasecca e dai Quartieri Spagnoli. Fino alle 20:30, tutti i giorni.</p>""",
 altri_h3="Accanto all'Aspritz",
 altri="""<p>Il classico Campari Spritz, il Limoncello Spritz, l'Hugo con lime, menta e sambuco, il Passion Spritz, il Cynar Spritz, lo Spritz veneziano e due spritz che parlano napoletano, il <strong>Pignasecca Spritz</strong> (Aperol, Campari, Cynar e prosecco) e il <strong>Maradona Spritz</strong>, blu come il curaçao. E poi l'angolo dei Negroni, il Gin &amp; Tonic corner, vini campani al calice come il Fiano di Avellino DOCG, la birra napoletana N'Artigiana alla spina e cocktail analcolici.</p>""",
 menu_drink="Tutti i drink nel menu",
 # G
 gal_occ="Galleria", gal_h2="Le sere da Ceraldi",
 galleria=[("cocktail-barman", "Al banco, prima di servire: ogni drink si prepara al momento."),
           ("illustrazione-agrumi", "Gli agrumi della Costiera, il profumo dell'Aspritz."),
           ("sala-bianca", "La sala bianca e oro, dove l'aperitivo si prende con calma."),
           ("illustrazione-asprinio", "L'alberata aversana, il paesaggio dell'Asprinio."),
           ("cocktail-menta-cetriolo", "Lo spumante versato al banco, per un altro dei nostri drink.")],
 # Storie
 storie_occ="Il mondo Aspritz", storie_h2="Storie per approfondire", storie_tutte="Tutte le storie dell'Aspritz",
 # H
 fine_1="C'è un altro modo di raccontare il territorio.", fine_2="Il nostro si chiama Aspritz.",
 fine_p="Scoprilo da Ceraldi Caffè, in Piazza Carità 14, nel centro di Napoli. Tutti i giorni fino alle 20:30.",
 fine_btn=("Come arrivare", "Orari e contatti"),
),
"en": dict(
 titolo_seo="Aspritz, the aperitivo created by Ceraldi in Naples",
 descrizione="Ceraldi Caffè's Aspritz: an infusion of Amalfi Coast citrus, herbs and roots topped with sparkling Asprinio di Aversa. Aperitivo in Piazza Carità, Naples.",
 briciola="Aspritz",
 occhiello="Created by Ceraldi · Piazza Carità, Naples",
 h1="Aspritz",
 sotto="The flavours of Campania, in our idea of aperitivo.",
 intro=("Amalfi Coast citrus, herbs and roots in an infusion we make ourselves, finished with sparkling Asprinio di Aversa. "
        "An aperitivo born in Piazza Carità to tell the story of Campania in a glass."),
 vai="Where to try it",
 alt_hero="Ceraldi Caffè's Aspritz: two stemmed glasses with ice and a dried orange slice on the counter",
 idea_occ="The idea", idea_h2="Not just another spritz: ours",
 idea="""<p class="capolettera">Ceraldi opened in 1973 as a Neapolitan café, and ever since it has worked within a clear tradition: coffee at the counter, pastries made in our own kitchens, produce from Campania. When we thought about the aperitivo, we asked the same question we ask about a pastry: how would Naples tell it?</p>
<p>The spritz is a formula known everywhere: a bittersweet base, a sparkling wine, ice, a touch of citrus. We did not want to copy it. We wanted to keep its structure and change its voice, choosing ingredients from places a few dozen kilometres from our counter.</p>
<p>That is how the Aspritz was born: an aromatic base of our own making, an infusion of Amalfi Coast citrus, herbs and roots, finished with sparkling Asprinio di Aversa, the white wine of the plain north of Naples. You can hear both halves in the name: Asprinio and spritz.</p>""",
 mappa_cap="Three places, one glass: Asprinio from the Aversa countryside, citrus from the Amalfi Coast, our counter in Piazza Carità. Not to scale.",
 mappa_alt="Schematic map of Campania showing Aversa, Naples and the Amalfi Coast",
 ingr_occ="The ingredients", ingr_h2="Three elements, three landscapes",
 ingr_p="Only a few elements give the Aspritz its character, and each one carries a piece of Campania.",
 ingr=[
  ("aspritz-radici-erbe.svg", "The base", "Herbs and roots",
   "The base of the Aspritz is an aperitivo of our own making, an infusion of herbs and roots together with citrus. It gives depth: the aromatic, gently bitter note that balances the sweetness and freshness of the other elements. Which herbs and which roots remains a house recipe.",
   "radici-ed-erbe", "Herbs and roots in the aperitivo (in Italian)",
   "Botanical illustration of aromatic herbs and roots"),
  ("aspritz-agrumi.svg", "The scent · Amalfi Coast", "Amalfi Coast citrus",
   "The citrus comes from the Amalfi Coast, a landscape of terraces and dry-stone walls overlooking the Gulf of Salerno, a UNESCO World Heritage Site since 1997. In the Aspritz it brings the scent; in the glass it returns as a dried orange slice.",
   "agrumi-costiera-amalfitana", "Amalfi Coast citrus (in Italian)",
   "Illustration of a citrus branch with a whole orange and a slice"),
  ("aspritz-asprinio.svg", "The bubbles · Aversa countryside", "Sparkling Asprinio di Aversa",
   "The white wine of the Aversa countryside, between the provinces of Caserta and Naples, protected by the «Aversa» DOC since 1993. Its vines also grow in the alberata aversana, trained up poplars several metres high and harvested from long ladders. A wine with lively acidity that brings bubbles and freshness to the Aspritz.",
   "asprinio-di-aversa", "Asprinio di Aversa (in Italian)",
   "Illustration of the alberata aversana: vines trained up poplars, a bunch of grapes and a harvest ladder"),
 ],
 leggi="Read more",
 senso_occ="Its character", senso_h2="What it is like, at the first sip",
 senso=[("Fragrant", "The scent arrives before the sip: that is the work of citrus and herbs."),
        ("Citrusy", "The Amalfi Coast note stays with the glass from start to finish, clear and bright."),
        ("Sweet, yet clean", "A measured sweetness that never weighs on the palate."),
        ("Fresh on the palate", "The bubbles of the Asprinio keep it fresh, sip after sip.")],
 crea_occ="Created by Ceraldi", crea_h2="Created and made by us",
 crea=[("Created by us", "The Aspritz is not a bought product poured into a glass: it is our own recipe, made to sit alongside our pastries and our coffee, with the same idea behind it: start from Campania."),
       ("Made by us", "The aromatic base is our own production, like the pastries in our display case. Making it ourselves lets us choose where the ingredients come from."),
       ("Finished at the counter", "When we serve it, we finish it with sparkling Asprinio di Aversa, ice and a dried orange slice.")],
 crea_nota="«Artigiani per passione», craftspeople by passion, our motto since 1973, holds true in the evening too.",
 crea_alt="Aperitivo at a table at Ceraldi Caffè: a glass with a dried citrus slice and a cocktail on burgundy napkins",
 napoli_occ="In Naples", napoli_h2="An aperitivo in Naples, with the ingredients of Campania",
 napoli="""<p>Visitors to Naples often look for a way to taste the city, not just see it. Coffee at the counter, sfogliatella, babà: Neapolitan food culture is made of everyday rituals. With the Aspritz we wanted to bring the same idea to aperitivo time, using ingredients and references from Campania.</p>
<p>It is not an old recipe and does not pretend to be: it is a contemporary creation, our own. But it rests on a much older culture, like that of Asprinio, a wine documented as early as the sixteenth century and long at home in the taverns of Naples.</p>
<p>At Ceraldi you can have your aperitivo at the counter or in the hall, among the mirrors and red armchairs, on Via Toledo, a few steps from the Pignasecca market and the Spanish Quarter. Until 8:30 pm, every day.</p>""",
 altri_h3="Alongside the Aspritz",
 altri="""<p>The classic Campari Spritz, Limoncello Spritz, Hugo with lime, mint and elderflower, Passion Spritz, Cynar Spritz, the Venetian spritz and two spritzes that speak Neapolitan, the <strong>Pignasecca Spritz</strong> (Aperol, Campari, Cynar and prosecco) and the <strong>Maradona Spritz</strong>, blue as curaçao. Plus our Negroni corner, a Gin &amp; Tonic corner, Campanian wines by the glass such as Fiano di Avellino DOCG, Naples' own N'Artigiana beer on tap and alcohol-free cocktails.</p>""",
 menu_drink="All drinks on the menu",
 gal_occ="Gallery", gal_h2="Evenings at Ceraldi",
 galleria=[("cocktail-barman", "At the bar, just before serving: every drink is made to order."),
           ("illustrazione-agrumi", "Amalfi Coast citrus, the scent of the Aspritz."),
           ("sala-bianca", "The white and gold hall, for an unhurried aperitivo."),
           ("illustrazione-asprinio", "The alberata aversana, home of Asprinio."),
           ("cocktail-menta-cetriolo", "Sparkling wine poured at the bar, for another of our drinks.")],
 storie_occ="The world of Aspritz", storie_h2="Stories to read (in Italian)", storie_tutte="All Aspritz stories",
 fine_1="There is another way to tell the story of a land.", fine_2="Ours is called Aspritz.",
 fine_p="Discover it at Ceraldi Caffè, Piazza Carità 14, in the centre of Naples. Every day until 8:30 pm.",
 fine_btn=("Get directions", "Hours and contact"),
),
}

# Testi alternativi delle illustrazioni usate come copertine (contenuti.FOTO)
FOTO_ASPRITZ = {
    "illustrazione-agrumi": {"alt": "Illustrazione: ramo di agrumi con un'arancia intera e una fetta d'arancia", "w": [1024, 640], "r": (4, 3)},
    "illustrazione-asprinio": {"alt": "Illustrazione: l'alberata aversana, con le viti maritate ai pioppi, un grappolo e la scala da vendemmia", "w": [1024, 640], "r": (4, 3)},
    "illustrazione-radici-erbe": {"alt": "Illustrazione botanica: erbe aromatiche e radici sotto la linea del terreno", "w": [1024, 640], "r": (4, 3)},
    "illustrazione-mappa-aspritz": {"alt": "Mappa schematica con Aversa, Napoli e la Costiera Amalfitana, i luoghi dell'Aspritz", "w": [1024, 640], "r": (4, 3)},
}

# ── Articoli del «mondo Aspritz» ─────────────────────────────────────
_PROVA = [("Aspritz", "infusione di nostra produzione con agrumi della Costiera, erbe e radici, e Asprinio di Aversa spumante"),
          ("Asprinio di Aversa spumante", "anche da solo, nella nostra carta"),
          ("Pignasecca Spritz", "Aperol, Campari, Cynar e prosecco")]
_CARTELLINO = "Piazza Carità 14, Napoli. Aperitivo tutti i giorni fino alle 20:30, al bancone o in sala."

ARTICOLI_ASPRITZ = [
{
 "slug": "aspritz-ceraldi",
 "titolo": "L'Aspritz Ceraldi: quando un aperitivo racconta un territorio",
 "titolo_seo": "Aspritz Ceraldi: un aperitivo che racconta la Campania",
 "descrizione": "Agrumi della Costiera, erbe e radici, Asprinio di Aversa: come l'Aspritz di Ceraldi Caffè unisce tre luoghi della Campania in un aperitivo nato a Napoli.",
 "dek": "Tre luoghi della Campania, un bancone in Piazza Carità e un'idea semplice: un aperitivo che sappia da dove viene.",
 "foto": "aspritz",
 "lettura": 4,
 "corpo": """
<p>Ogni bar ha il suo spritz. Noi abbiamo voluto qualcosa di diverso: un aperitivo che, appena arriva sul tavolo, racconti dove ci troviamo. È così che è nato l'<a href="../../aspritz/">Aspritz</a>, la nostra interpretazione dell'aperitivo, ideata e preparata da Ceraldi.</p>

<h2>Un bicchiere, tre luoghi</h2>
<p>Se si apre una mappa della Campania, l'Aspritz si dispone su una linea che va da nord a sud e passa per il nostro bancone.</p>
<ul>
<li><strong>A nord di Napoli, l'agro aversano.</strong> È la terra dell'Asprinio di Aversa, il vino bianco tutelato dalla DOC «Aversa» dal 1993, che nell'Aspritz arriva nella versione spumante e porta le bollicine.</li>
<li><strong>A Napoli, Piazza Carità.</strong> È il nostro bancone, dove l'Aspritz prende forma. La sua base aromatica è un aperitivo di nostra produzione, ottenuto per infusione di erbe e radici insieme agli agrumi.</li>
<li><strong>A sud, la Costiera Amalfitana.</strong> Da qui vengono gli agrumi che danno all'Aspritz il suo profumo e che ritornano nel bicchiere come fetta d'arancia disidratata.</li>
</ul>
<p>Sono luoghi a poche decine di chilometri l'uno dall'altro, ma con paesaggi diversissimi: la pianura vulcanica dell'agro aversano, la città, i terrazzamenti affacciati sul mare della Costiera.</p>

<h2>Perché un aperitivo «di territorio»</h2>
<p>Da Ceraldi lavoriamo da sempre dentro la tradizione napoletana: il caffè, la pasticceria fatta nei nostri laboratori, i dolci che raccontano la Campania, come il Segreto amalfitano con la chantilly ai limoni di Amalfi o la Pellecchiella con le albicocche del Vesuvio. L'Aspritz nasce dalla stessa idea, portata all'ora dell'aperitivo.</p>
<p>Lo spritz è una formula conosciuta ovunque, e proprio per questo si presta a essere reinterpretata. Ne abbiamo tenuto la struttura (una base aromatica, un vino con le bollicine, il ghiaccio, l'agrume) e abbiamo cambiato la provenienza di ciascun elemento.</p>

<h2>Com'è nel bicchiere</h2>
<p>Lo descriviamo con quattro parole: <strong>profumato</strong>, <strong>agrumato</strong>, <strong>dolce ma pulito</strong>, <strong>fresco al palato</strong>. Il profumo arriva prima del sorso; la nota di agrume accompagna il bicchiere fino in fondo; la dolcezza resta misurata; le bollicine dell'Asprinio lo tengono fresco.</p>
<p>Chi vuole capire meglio i singoli elementi trova qui le loro storie: <a href="../agrumi-costiera-amalfitana/">gli agrumi della Costiera Amalfitana</a>, <a href="../asprinio-di-aversa/">l'Asprinio di Aversa</a> e <a href="../radici-ed-erbe/">il ruolo di erbe e radici negli aperitivi</a>.</p>

<h2>Dove e quando</h2>
<p>L'Aspritz si prende al bancone o in sala, in Piazza Carità 14, lungo via Toledo. L'aperitivo va avanti tutti i giorni fino alle 20:30, quando chiudiamo. Al tavolo si può accompagnare con qualcosa della nostra <a href="../../rosticceria/">rosticceria</a>.</p>
""",
 "provare": _PROVA,
},
{
 "slug": "agrumi-costiera-amalfitana",
 "titolo": "Gli agrumi della Costiera Amalfitana: profumi e identità della Campania",
 "titolo_seo": "Agrumi della Costiera Amalfitana: storia e paesaggio",
 "descrizione": "Terrazzamenti, muretti a secco, pergolati di castagno e lo sfusato amalfitano: storia e paesaggio degli agrumi della Costiera, e il loro ruolo nell'Aspritz.",
 "dek": "Giardini sospesi sul mare, costruiti a mano terrazza dopo terrazza: gli agrumi sono il paesaggio stesso della Costiera Amalfitana.",
 "foto": "illustrazione-agrumi",
 "lettura": 5,
 "corpo": """
<p>Tra Vietri sul Mare e Positano, la Costiera Amalfitana è una parete di roccia che scende verso il golfo di Salerno. Per coltivarla, nei secoli, chi ci viveva ha dovuto costruire la terra: terrazze sostenute da muretti a secco, una sopra l'altra, su cui crescono agrumi, ulivi e viti. È questo paesaggio che dà profumo all'<a href="../../aspritz/">Aspritz</a>.</p>

<h2>Un paesaggio costruito a mano</h2>
<p>I terrazzamenti della Costiera sono migliaia. Secondo la FAO, i muri che li sostengono sono alti fino a sette metri e sono costruiti senza cemento: lasciano passare l'acqua e l'aria, trattengono i versanti e, insieme a canali e cisterne, raccolgono le piogge per i mesi asciutti. Se vengono abbandonati, possono crollare e trascinare con sé il terreno.</p>
<p>Sopra le terrazze si vedono i pergolati in legno di castagno, tagliato nei boschi vicini: i rami degli alberi vengono legati alla struttura, così i frutti restano a portata di mano e il loro peso non spezza i rami.</p>

<h2>Dal Medioevo alle navi di Amalfi</h2>
<p>Il limone arrivò in Costiera nel primo Medioevo, attraverso i commerci con il mondo arabo, e all'inizio fu usato soprattutto come rimedio. Il documento ufficiale dell'indicazione geografica protetta racconta che già nell'XI secolo le navi della Repubblica di Amalfi portavano limoni a bordo, preziosi contro lo scorbuto, e che dal Quattrocento all'Ottocento la domanda dal Nord Europa fu molto alta.</p>
<p>Il frutto simbolo è lo <strong>sfusato amalfitano</strong>, il limone allungato e profumato tutelato dal 2001 come IGP «Limone Costa d'Amalfi», coltivato nei tredici comuni della Costiera.</p>

<h2>Due riconoscimenti mondiali</h2>
<ul>
<li><strong>UNESCO, 1997</strong>: la Costiera Amalfitana è Patrimonio dell'Umanità.</li>
<li><strong>FAO, 2025</strong>: il suo sistema di limoneti e terrazzamenti è stato riconosciuto tra i sistemi del patrimonio agricolo di importanza mondiale (GIAHS).</li>
</ul>
<p>Il primo riconoscimento guarda alla bellezza del paesaggio; il secondo al lavoro agricolo che lo tiene in piedi. Sono due facce della stessa storia.</p>

<h2>Gli agrumi nell'Aspritz</h2>
<p>Nell'Aspritz usiamo agrumi della Costiera Amalfitana, tra cui le arance, nella base aromatica che prepariamo per infusione insieme a erbe e radici. Sono loro a renderlo <strong>profumato</strong> e <strong>agrumato</strong>, le prime due parole con cui lo descriviamo. Nel bicchiere l'agrume torna anche alla vista, con una fetta d'arancia disidratata.</p>
<p>Non è l'unico modo in cui la Costiera entra da Ceraldi: in vetrina c'è anche il <a href="../../specialita/">Segreto amalfitano</a>, un babà bagnato al limoncello con un cuore di chantilly ai limoni di Amalfi.</p>
""",
 "provare": [("Aspritz", "con agrumi della Costiera Amalfitana, erbe e radici"), ("Segreto amalfitano", "babà al limoncello con chantilly ai limoni di Amalfi"), ("Limoncello Spritz", "tra gli spritz della casa")],
},
{
 "slug": "asprinio-di-aversa",
 "titolo": "Asprinio di Aversa: il carattere di un vino campano",
 "titolo_seo": "Asprinio di Aversa: il vino dell'alberata aversana",
 "descrizione": "La DOC «Aversa», le viti maritate ai pioppi dell'alberata, le scale dei vendemmiatori e la lunga storia dell'Asprinio, il bianco che dà le bollicine all'Aspritz.",
 "dek": "Viti alte come alberi, vendemmiate con le scale: l'Asprinio è uno dei vini più particolari della Campania, e il cuore frizzante del nostro Aspritz.",
 "foto": "illustrazione-asprinio",
 "lettura": 5,
 "corpo": """
<p>A nord di Napoli, tra le province di Caserta e Napoli, c'è una pianura fertile e vulcanica: l'agro aversano. Qui nasce l'Asprinio di Aversa, un bianco che ha una storia lunga e un modo antico, oggi raro, di coltivare la vite. È il vino che dà le bollicine all'<a href="../../aspritz/">Aspritz</a>.</p>

<h2>La DOC «Aversa»</h2>
<p>La denominazione di origine controllata «Aversa» è stata riconosciuta nel 1993. Il disciplinare prevede due tipologie: l'Asprinio fermo, con almeno l'85% di uve Asprinio, e lo spumante, che deve essere fatto solo con uve Asprinio.</p>
<p>La zona di produzione comprende ventidue comuni: diciannove in provincia di Caserta, tra cui Aversa, Lusciano, Trentola-Ducenta e Sant'Arpino, e tre in provincia di Napoli, cioè Giugliano, Qualiano e Sant'Antimo. È un territorio pianeggiante, tra i 10 e i 101 metri sul livello del mare, con terreni di origine vulcanica fatti di pozzolane e tufo.</p>

<h2>L'alberata aversana</h2>
<p>La forma di allevamento tradizionale è l'<strong>alberata</strong>: la vite viene «maritata» a un albero vivo, di solito un pioppo, e sale con lui. Gli alberi sono piantati in filari distanti tra loro una quindicina di metri; le viti arrivano a cinque-otto metri da terra e si stendono da un albero all'altro come festoni.</p>
<p>Per potare e vendemmiare servono lunghe scale di legno, che ogni vignaiolo possiede, e cesti conici chiamati <em>fescine</em>. La tradizione fa risalire questa tecnica agli Etruschi. Il disciplinare ricorda inoltre che nella zona sopravvivono viti centenarie precedenti alla fillossera.</p>

<h2>Una storia lunga cinque secoli</h2>
<p>Le origini del vitigno sono incerte: si discutono parentele con il Greco e con il Pinot. Un dato più solido arriva dal Cinquecento, quando Sante Lancerio, bottigliere di papa Paolo III, ne documenta la diffusione. Una tradizione popolare, senza prove storiche, ne attribuisce invece l'arrivo a Luigi XII di Francia.</p>
<p>L'Asprinio era di casa nelle taverne napoletane. Non a tutti piaceva: il medico e poeta Francesco Redi ne criticava l'acidità. È proprio quella vivacità, però, che lo ha reso adatto a diventare spumante: il disciplinare lo ricorda tra i primi spumanti secchi.</p>

<h2>Nell'Aspritz</h2>
<p>Nell'Aspritz l'Asprinio di Aversa spumante prende il posto che nello spritz classico spetta al prosecco. Porta le bollicine e una freschezza che bilancia la dolcezza misurata della base aromatica. Da Ceraldi lo trovi anche da solo, nella nostra carta.</p>
""",
 "provare": [("Aspritz", "con Asprinio di Aversa spumante"), ("Asprinio di Aversa spumante", "anche da solo, nella nostra carta"), ("Vini campani al calice", "come il Fiano di Avellino DOCG")],
},
{
 "slug": "radici-ed-erbe",
 "titolo": "Radici ed erbe nell'aperitivo: il fascino della componente botanica",
 "titolo_seo": "Radici ed erbe negli aperitivi: la componente botanica",
 "descrizione": "Genziana, rabarbaro, china, scorze di agrumi: cosa portano radici ed erbe agli aperitivi e ai bitter, dal vermouth di Torino allo spritz, fino all'Aspritz.",
 "dek": "Dietro la nota amaricante di un aperitivo c'è un piccolo erbario: radici, cortecce, foglie e scorze, dosate per dare equilibrio.",
 "foto": "illustrazione-radici-erbe",
 "lettura": 5,
 "corpo": """
<p>Ogni aperitivo ha una parte che non si vede: le erbe e le radici. Sono loro a dare la nota amaricante, la profondità, il profumo che resta dopo il sorso. Anche l'<a href="../../aspritz/">Aspritz</a> nasce da qui: la sua base è un aperitivo di nostra produzione, ottenuto per infusione di erbe e radici insieme agli agrumi della Costiera Amalfitana.</p>

<h2>Dalla bottega dell'erborista al bancone</h2>
<p>La parola «aperitivo» viene dal latino <em>aperire</em>, aprire: è ciò che apre l'appetito. Molti liquori a base di erbe nacquero come preparazioni da speziale e solo col tempo diventarono bevande da condividere. Una data simbolo è il 1786, quando a Torino l'erborista Antonio Benedetto Carpano preparò uno dei primi vermouth italiani, con vino, erbe e spezie.</p>
<p>Nell'Ottocento la cultura dei bitter si diffuse nei caffè delle città del Nord: nel 1860 Gaspare Campari aprì la sua prima attività a Novara, poi trasferita a Milano. A Venezia, nel 1920, i fratelli Pilla crearono il Select con una ricetta segreta di una trentina di erbe, che sarebbe diventato l'ingrediente tipico dello spritz veneziano.</p>

<h2>Cosa portano radici ed erbe</h2>
<p>Ogni casa custodisce la propria ricetta, ma alcuni ingredienti ricorrono spesso nella famiglia dei bitter e degli amari. Qualche esempio, per capire la categoria:</p>
<ul>
<li><strong>Radice di genziana</strong>: un amaro deciso e persistente, e un colore dorato.</li>
<li><strong>Radice di rabarbaro</strong>: dolce all'inizio, poi un amaro profondo.</li>
<li><strong>Corteccia di china</strong>: amaro e una leggera astringenza.</li>
<li><strong>Radice di angelica</strong>: una dolcezza legnosa, con un amaro che arriva più tardi.</li>
<li><strong>Scorze di agrumi</strong>: luminosità e profumo, che equilibrano l'amaro e il dolce.</li>
</ul>
<p>Sono esempi della categoria, non la nostra ricetta: quali erbe e quali radici entrano nell'Aspritz, e in che misura, resta un segreto di casa.</p>

<h2>Il gioco dell'equilibrio</h2>
<p>In un buon aperitivo la componente botanica non deve coprire tutto il resto. Deve dare struttura: un amaro che sostiene la dolcezza, un profumo che si apre con il ghiaccio e con le bollicine. È un equilibrio che si costruisce per prove, assaggio dopo assaggio.</p>
<p>Nell'Aspritz lo cerchiamo così: erbe e radici danno la profondità, gli agrumi il profumo, l'<a href="../asprinio-di-aversa/">Asprinio di Aversa</a> spumante la freschezza. Il risultato lo descriviamo con quattro parole: profumato, agrumato, dolce ma pulito, fresco al palato.</p>
""",
 "provare": _PROVA,
},
{
 "slug": "aperitivo-a-napoli",
 "titolo": "L'aperitivo a Napoli: tradizione, convivialità e nuove interpretazioni",
 "titolo_seo": "L'aperitivo a Napoli: storia, convivialità e novità",
 "descrizione": "Dal vermouth di Torino allo spritz veneziano, fino ai bar di Napoli: cosa c'è di documentato nella storia dell'aperitivo e come la città lo interpreta oggi.",
 "dek": "L'aperitivo è nato al Nord, ma a Napoli ha trovato una città abituata da sempre a ritrovarsi al bar. Ecco cosa sappiamo e cosa è cambiato.",
 "foto": "cocktail-barman",
 "lettura": 5,
 "corpo": """
<p>Napoli è la città del caffè al bancone, della sosta di pochi minuti, delle due parole con il barista. L'aperitivo, invece, ha una storia che parte da più lontano. Vale la pena distinguere quello che è documentato da quello che è più recente, per capire come questo rito sia arrivato anche in Piazza Carità.</p>

<h2>Un rito nato al Nord</h2>
<p>La storia documentata dell'aperitivo italiano comincia a Torino. Nel 1786 l'erborista Antonio Benedetto Carpano preparò uno dei primi vermouth italiani, e nel corso dell'Ottocento nei caffè torinesi si affermò quella che Edmondo De Amicis, nel 1898, chiamò l'«ora del vermouth». Più o meno negli stessi decenni Milano diventava la città del bitter: Gaspare Campari, partito da Novara nel 1860, si trasferì nel capoluogo lombardo.</p>
<p>Lo spritz ha origini venete. Si racconta che nell'Ottocento i soldati e i funzionari dell'Impero asburgico chiedessero di allungare il vino con l'acqua frizzante, da cui il tedesco <em>spritzen</em>, spruzzare; è un'ipotesi diffusa, non una certezza. Lo spritz con il bitter arriva più tardi, nel Novecento: l'Aperol nasce a Padova nel 1919, il Select a Venezia nel 1920.</p>

<h2>Napoli, città del bar</h2>
<p>Napoli ha una tradizione conviviale tutta sua, costruita attorno al <a href="../caffe-napoletano/">caffè</a> e al bar inteso come piazza: un luogo di passaggio dove ci si incontra, si parla, si riparte. Anche il vino ha avuto i suoi luoghi: l'<a href="../asprinio-di-aversa/">Asprinio di Aversa</a>, per esempio, era di casa nelle taverne napoletane.</p>
<p>Non abbiamo trovato fonti che documentino una storia dell'aperitivo propriamente napoletana: per quanto ne sappiamo, l'aperitivo come lo intendiamo oggi, con il bicchiere della sera e qualcosa da mangiare accanto, si è diffuso a Napoli insieme al resto d'Italia. La città, però, aveva già un modo tutto suo di stare insieme al bar.</p>

<h2>Le interpretazioni di oggi</h2>
<p>Oggi non è raro trovare, a Napoli come nel resto d'Italia, spritz che parlano la lingua del posto: il limoncello al posto del bitter, vini locali al posto del prosecco, nomi che richiamano i luoghi della città. Da Ceraldi, per esempio, c'è il <strong>Pignasecca Spritz</strong>, che prende il nome dal mercato a pochi passi dal bar, e c'è l'<a href="../../aspritz/">Aspritz</a>, la nostra creazione con agrumi della Costiera Amalfitana, erbe e radici e Asprinio di Aversa spumante.</p>
<p>Sono interpretazioni contemporanee, non tradizioni antiche: è giusto chiamarle così. Il loro senso è usare un rito ormai italiano per raccontare ingredienti e luoghi della Campania.</p>

<h2>Un aperitivo in centro, lungo via Toledo</h2>
<p>Chi è a Napoli e cerca un aperitivo nel centro storico trova in <a href="../piazza-carita-via-toledo/">Piazza Carità</a> un punto comodo: siamo lungo via Toledo, tra piazza Dante e piazza del Plebiscito, all'ingresso della Pignasecca e dei Quartieri Spagnoli, vicino alle fermate Toledo e Dante della metro Linea 1. Da Ceraldi l'aperitivo si prende al bancone o in sala, tutti i giorni fino alle 20:30.</p>
""",
 "provare": _PROVA,
},
{
 "slug": "aspritz-idea-di-aperitivo",
 "titolo": "Aspritz: dentro la nostra idea di aperitivo",
 "titolo_seo": "Aspritz: le scelte dietro l'aperitivo di Ceraldi",
 "descrizione": "Perché una base preparata da noi, perché l'Asprinio al posto del prosecco, perché una fetta d'arancia: le scelte dietro l'Aspritz, l'aperitivo di Ceraldi Caffè.",
 "dek": "Un aperitivo si costruisce per scelte, una dopo l'altra. Queste sono le nostre, e il motivo per cui le abbiamo fatte.",
 "foto": "aperitivo",
 "lettura": 4,
 "corpo": """
<p>Abbiamo già raccontato <a href="../aspritz-ceraldi/">da dove viene l'Aspritz</a>. Qui vogliamo raccontare il come: le scelte che stanno dietro il bicchiere, e l'idea di aperitivo che le tiene insieme.</p>

<h2>Partire da un equilibrio, non da un ingrediente</h2>
<p>Prima ancora degli ingredienti, avevamo in mente un carattere. Volevamo un aperitivo <strong>profumato</strong>, che si annunci prima del sorso; <strong>agrumato</strong>, con una nota chiara dall'inizio alla fine; <strong>dolce, ma pulito</strong>, senza appesantire; <strong>fresco al palato</strong>, da bere con piacere anche nelle sere d'estate in città. Ogni scelta successiva è servita a tenere insieme queste quattro cose.</p>

<h2>Una base preparata da noi</h2>
<p>La base dell'Aspritz è un aperitivo di nostra produzione, ottenuto per infusione di agrumi della Costiera Amalfitana, erbe e radici. Avremmo potuto usare un bitter già pronto, come si fa in molti spritz. Prepararla noi ci permette invece di scegliere da dove vengono gli ingredienti e di decidere quanto spazio dare a ciascuno.</p>
<p>È lo stesso modo di lavorare della nostra pasticceria: i dolci della vetrina nascono nei nostri laboratori, e alcuni portano già dentro la Campania, come il Segreto amalfitano con la chantilly ai limoni di Amalfi o la Pellecchiella con le albicocche del Vesuvio. Per <a href="../radici-ed-erbe/">erbe e radici</a> vale una regola di casa: la ricetta resta nostra.</p>

<h2>L'Asprinio al posto del prosecco</h2>
<p>Nello spritz classico le bollicine sono quelle del prosecco. Noi abbiamo scelto un vino campano: l'<a href="../asprinio-di-aversa/">Asprinio di Aversa</a> DOC spumante, il bianco dell'agro aversano, a nord di Napoli. È un vino conosciuto per la sua acidità vivace, ed è proprio quella a dare freschezza all'Aspritz, a bilanciare la dolcezza della base.</p>

<h2>Il dettaglio nel bicchiere</h2>
<p>L'Aspritz si serve nel calice, con il ghiaccio e una fetta d'arancia disidratata. Non è solo decorazione: la fetta riporta alla vista ciò che si sente al naso, gli <a href="../agrumi-costiera-amalfitana/">agrumi della Costiera</a>.</p>

<h2>Una creazione, non una tradizione</h2>
<p>L'Aspritz non è una ricetta antica e non lo presentiamo come tale. È una nostra creazione contemporanea, nata dentro un bar che dal 1973 lavora sulla tradizione napoletana. La tradizione, semmai, sta negli ingredienti: un vino documentato da cinque secoli, agrumi coltivati su terrazze costruite a mano, la cultura del bar come luogo d'incontro. Il nostro lavoro è stato metterli nello stesso bicchiere.</p>
<p>Se vuoi assaggiarlo, ti aspettiamo in <a href="../../contatti/">Piazza Carità 14</a>, al bancone o in sala.</p>
""",
 "provare": _PROVA,
},
]
for _a in ARTICOLI_ASPRITZ:
    _a["pubblicato"] = DATA_ASPRITZ
    _a["cartellino"] = _CARTELLINO

_W = "https://it.wikipedia.org/wiki/"
_DISCIPLINARE = ("Disciplinare della DOC «Aversa» (Asprinio)", "https://www.disciplinare.it/userfiles/downloads/doc/DOC%20Aversa.pdf")
_FAO = ("The Amalfi lemon and its layered, resilient landscape, FAO", "https://www.fao.org/newsroom/story/the-amalfi-lemon-and-its-layered-resilient-landscape/en")
_IGP = ("Limone Costa d'Amalfi IGP, documento unico, Commissione europea (eAmbrosia)", "https://webgate.ec.europa.eu/eambrosia-api/api/v1/attachments/47034")
_LINKIESTA = ("Aperire. Breve storia di un rito italiano, Linkiesta", "https://www.linkiesta.it/2025/11/breve-storia-rito-italiano-aperitivo-libro-italiasquisita/")
_SPRITZ = ("La vera storia dello spritz: origini e varianti, Gambero Rosso", "https://www.gamberorosso.it/vino/la-vera-storia-dello-spritz-origini-e-varianti/")
_MENU = ("Menu di Ceraldi Caffè, voce «Aspritz»", "https://ceraldicaffe.qromo.it")
FONTI_ASPRITZ = {
 "aspritz-ceraldi": [_MENU, _DISCIPLINARE, _FAO],
 "agrumi-costiera-amalfitana": [_FAO, _IGP, ("Amalfi Coast, Wikipedia", "https://en.wikipedia.org/wiki/Amalfi_Coast"),
                                ("New GIAHS sites in Italy and Japan, FAO", "https://www.fao.org/newsroom/detail/new-globally-important-agricultural-heritage-system-sites-in-italy-and-japan-push-global-total-of-designated-sites-past-100/en")],
 "asprinio-di-aversa": [_DISCIPLINARE, ("Alberata aversana, paesaggio nazionale rurale storico, Rivista di Agraria", "https://rivistadiagraria.org/articoli/anno-2018/alberata-aversana-paesaggio-nazionale-rurale-storico/")],
 "radici-ed-erbe": [("The botanicals behind amaro, VinePair", "https://vinepair.com/articles/amaro-botanicals/"), _LINKIESTA, _SPRITZ],
 "aperitivo-a-napoli": [_LINKIESTA, _SPRITZ, _DISCIPLINARE],
 "aspritz-idea-di-aperitivo": [_MENU, _DISCIPLINARE],
}

CATEGORIA_ASPRITZ = {
 "slug": "aspritz", "nome": "Il mondo Aspritz",
 "intro": "Agrumi della Costiera, Asprinio di Aversa, erbe e radici, l'aperitivo a Napoli: le storie dietro l'Aspritz, l'aperitivo ideato da Ceraldi.",
 "articoli": [a["slug"] for a in ARTICOLI_ASPRITZ],
 "copertine": True,
}
