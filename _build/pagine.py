# -*- coding: utf-8 -*-
# Pagine principali del sito. Gli slug ricalcano il vecchio ceraldicaffe.it,
# così al momento della migrazione i reindirizzamenti sono uno a uno:
#   /1973-2/ -> /storia/   /bar/ -> /bar/   /pasticceria/ -> /pasticceria/
#   /gastronomia/ -> /rosticceria/   /aspritz/ -> /aspritz/   /contatti/ -> /contatti/

PIVA = "04523831214"
RAGIONE_SOCIALE = "Ceraldi Group S.r.l."
EMAIL = "info@ceraldicaffe.it"

PAGINE = [
{
 "slug": "storia",
 "nav": "La nostra storia",
 "titolo": "Un angolo di Piazza Carità che aspettava noi",
 "titolo_seo": "La storia di Ceraldi, bar a Napoli dal 1973",
 "descrizione": "Michele Ceraldi apre il primo bar in Piazza Garibaldi nel 1973; nel 2002 l'arrivo in Piazza Carità. Oggi lo porta avanti con i figli Vincenzo e Valerio.",
 "dek": "Dal 1973 in Piazza Garibaldi al 2002 in Piazza Carità: la storia di un padre, dei suoi due figli e di un bar che sembrava aspettarli.",
 "foto": "squadra",
 "corpo": """
<p class="capolettera">Napoli, 1973. In Piazza Garibaldi, davanti alla stazione, la città arriva e riparte in continuazione: valigie, treni, voci, clacson. È lì che Michele Ceraldi apre il suo primo bar. Il mestiere si impara al bancone, una tazzina alla volta, tra chi ha fretta di partire e chi è appena arrivato e cerca, prima di tutto, un caffè fatto come si deve.</p>

<h2>Il 2002 e l'angolo vuoto</h2>
<p>Passano gli anni, il bar cresce. Poi, un giorno del 2002, Michele cammina per i vicoli del centro senza cercare niente di preciso, e arriva nel cuore della città: <a href="../storie/piazza-carita-via-toledo/">Piazza Carità</a>. Intorno c'è il brulichio di sempre, mercanti, impiegati, passanti, la Pignasecca che chiama dai suoi banchi. Il suo sguardo si ferma su un angolo vuoto e senza vita.</p>
<p>Un altro avrebbe tirato dritto. Lui no. Quell'angolo, racconta, sembrava aver aspettato proprio lui per tutto quel tempo. Da quel giorno, in Piazza Carità 14, c'è Ceraldi Caffè.</p>

<h2>Dalla prima tazzina all'ultimo aperitivo</h2>
<p>Da allora la giornata del bar segue quella della piazza. Al mattino presto arrivano gli impiegati ancora assonnati, che si svegliano davvero solo al primo sorso. Poi i turisti, con la mappa in mano e l'aria incerta. Poi i passanti senza fretta. E la sera, prima di tornare a casa carichi di borse, carte e meraviglie, molti si concedono un ultimo aperitivo. È il lieto fine di ogni giornata, e per noi il più dolce.</p>

<h2>Un padre e due figli</h2>
<p>Oggi la tradizione è portata avanti da Michele insieme ai suoi due figli, <strong>Vincenzo e Valerio</strong>. Due generazioni di gusto napoletano dietro lo stesso bancone: chi ha imparato il mestiere in Piazza Garibaldi e chi è cresciuto tra i profumi del laboratorio.</p>
<p>Perché è lì, nei nostri laboratori, che nasce tutto quello che vedi in vetrina: sfogliatelle, babà, pastiere, torte e la rosticceria, con <a href="../pasticceria/">ricette di famiglia tramandate di generazione in generazione</a>. Ricette che non stanno scritte su un sito, ma nelle mani di chi le prepara ogni mattina.</p>

<h2>Artigiani per passione</h2>
<p>Il nostro motto è scritto nel logo: <em>artigiani per passione</em>. Vuol dire fare le cose come si facevano, anche quando ci sarebbe un modo più veloce. Vuol dire che il caffè si serve nella tazzina calda, che la sfogliatella deve scrocchiare, che chi entra deve sentirsi a casa, anche se viene da lontano.</p>
<p>Nel 2019 abbiamo rinnovato il logo e il pay-off, «Artigiani per passione dal 1973»: guardare al passato per costruire il futuro, senza dimenticare le nostre radici, e per farlo, a volte, semplificare e guardare all'essenziale.</p>
<p>Un impegno che negli anni è stato notato: dal 2014 Ceraldi Caffè è nella guida <a href="https://www.gamberorosso.it/luoghi/locali/caffe-bar/ceraldi-caffe/" rel="noopener">Bar d'Italia del Gambero Rosso</a>.</p>
<p>Vieni a trovarci in Piazza Carità: il resto della storia lo scriviamo ogni giorno, al bancone.</p>
""",
 "galleria": ["famiglia", "logo-ceraldi-caffe-carta"],
 "cta": [("Come arrivare", "mappa"), ("Guarda il menu", "menu_interno")],
},
{
 "slug": "bar",
 "nav": "Il bar e la colazione",
 "titolo": "Il bar: caffè napoletano, colazione e English breakfast",
 "titolo_seo": "Colazione a Napoli centro, Piazza Carità",
 "descrizione": "Dove fare colazione a Napoli centro: dalle 6:30, tavoli all'aperto in Piazza Carità, su via Toledo. Caffè, cornetti, sfogliatelle ed English breakfast.",
 "dek": "Dalle 6:30 del mattino: l'espresso nella tazzina calda, i caffè della casa, la colazione all'italiana e quella napoletana. E per chi viene da lontano, l'English breakfast tutte le mattine.",
 "foto": "caffe-ceraldi",
 "corpo": """
<h2>Il caffè</h2>
<p>Al nostro bancone il caffè si serve come vuole la tradizione: espresso corto e cremoso, nella <a href="../storie/caffe-napoletano/">tazzina calda</a>. Accanto all'espresso ci sono i caffè della casa, nati da Ceraldi:</p>
<ul>
<li><strong>Caffè Ceraldi</strong>: cioccolata calda sul fondo, crema di caffè e panna montata fresca. La nostra firma.</li>
<li><strong>Caffè Babà</strong>: crema di caffè, crema al babà, un babà mignon e panna.</li>
<li><strong>Michelino</strong>: espresso, crema di zucchero e panna sciolta a bagnomaria.</li>
<li><strong>Nocciolato</strong> e <strong>Pistacchiotto</strong>: espresso con crema di nocciola Piemonte IGP o di pistacchio.</li>
<li><strong>Caldo freddo</strong>, <strong>Brasiliano</strong>, <strong>Veneziano</strong>, <strong>Viennese</strong> e il caffè leccese con sciroppo di mandorla.</li>
</ul>
<p>Per chi preferisce altro: cioccolate calde, tè e tisane Dammann, chai e golden milk, succhi e spremute.</p>

<h2>La colazione all'italiana</h2>
<p>Il cornetto caldo con il cappuccino, al bancone o al tavolo. I nostri croissant sono vuoti o farciti (crema, crema e amarena, cioccolato, albicocca, lampone, mela e cannella, limone), anche integrali e vegani, e c'è il croissant ischitano, con doppio strato di sfoglia e pasta brioche. Poi brioche, kranz, pain au chocolat, maritozzo con la panna e la nuvoletta con crema al latte.</p>

<h2>La colazione napoletana</h2>
<p>A Napoli la colazione ha i suoi dolci: la <a href="../storie/sfogliatella/">sfogliatella</a> riccia o frolla appena sfornata, la <strong>graffa</strong> fritta e zuccherata, il <a href="../storie/baba/">babà</a> per chi ama cominciare deciso. Leggi la nostra guida alla <a href="../storie/colazione-napoletana/">colazione a Napoli</a>.</p>

<h2>English breakfast, tutte le mattine</h2>
<p>Per i nostri ospiti stranieri che non vogliono rinunciare alle loro abitudini, tutte le mattine serviamo la <strong>Full English Breakfast</strong>, preparata come vuole la tradizione: uova, bacon, salsicce, fagioli, funghi e pomodori, pane tostato e l'immancabile tè. In alternativa, omelette semplice o farcita e uova strapazzate.</p>
<p lang="en"><em>Full English breakfast served every morning in the heart of Naples: eggs, bacon, sausages, beans, mushrooms, tomatoes, toast and tea.</em></p>

<h2>Dove fare colazione a Napoli centro</h2>
<p>Siamo in <a href="../storie/piazza-carita-via-toledo/">Piazza Carità 14</a>, lungo via Toledo, a metà strada tra piazza Dante e piazza del Plebiscito: la colazione giusta prima di una giornata in centro storico, ai Quartieri Spagnoli o alla Pignasecca.</p>
<ul>
<li><strong>Tutti i giorni dalle 6:30</strong>, domenica compresa, fino alle 20:30.</li>
<li><strong>Tavoli all'aperto</strong> in piazza, oppure in sala tra gli specchi e le poltroncine rosse; e naturalmente il bancone, per il caffè al volo.</li>
<li><strong>A pochi minuti a piedi</strong> dalle fermate Toledo e Dante della metro Linea 1.</li>
<li><strong>Cosa trovi</strong>: espresso e caffè della casa, cornetti, sfogliatelle e babà della nostra pasticceria, English breakfast. Guarda il <a href="../menu/">menu con i prezzi</a>.</li>
</ul>
""",
 "galleria": ["sala", "bar-banco", "vetrina", "cornetti-caffe-bancone", "latte-macchiato-dolci", "caffe-servito-bancone"],
 "cta": [("Menu del bar", "menu_bar"), ("Come arrivare", "mappa")],
},
{
 "slug": "pasticceria",
 "nav": "La pasticceria",
 "titolo": "La pasticceria: produzione propria e ricette di famiglia",
 "titolo_seo": "Pasticceria napoletana su via Toledo, Napoli",
 "descrizione": "Pasticceria di produzione propria in Piazza Carità, su via Toledo, con ricette di famiglia tramandate nel tempo: sfogliatelle, babà, pastiera e dolci della casa.",
 "dek": "Tutto quello che vedi in vetrina nasce nei nostri laboratori, con ricette di famiglia tramandate di generazione in generazione.",
 "foto": "cestino",
 "corpo": """
<p>"Napoli tre cose tene belle: 'o sole, 'o mare e 'a sfugliatella." Il detto è vecchio, ma da noi vale ancora. La pasticceria di Ceraldi Caffè è di <strong>produzione propria</strong>: i dolci nascono nei nostri laboratori, ogni giorno, con ricette di famiglia tramandate di generazione in generazione.</p>

<h2>I classici napoletani</h2>
<ul>
<li><strong>Sfogliatella riccia e frolla</strong>, con ricotta, semola, canditi e cannella. E la <strong>Santa Rosa</strong>, con crema e amarene. <a href="../storie/sfogliatella/">La storia della sfogliatella</a>.</li>
<li><strong>Babà al rum</strong>, classico o con crema e amarena, panna e fragole, cioccolato. <a href="../storie/baba/">La storia del babà</a>.</li>
<li><strong>Pastiera napoletana</strong>, con grano, ricotta e fiori d'arancio. <a href="../storie/pastiera/">La storia della pastiera</a>.</li>
<li><strong>Zeppola di San Giuseppe</strong>, con crema pasticcera e amarena. <a href="../storie/zeppole-di-san-giuseppe/">La storia delle zeppole</a>.</li>
<li><strong>Codina di aragosta</strong>, con chantilly, cioccolato o pistacchio.</li>
<li><strong>Caprese</strong> al cioccolato o al limone, <strong>delizia al limone</strong>, <strong>biscotto all'amarena</strong>, prussiane, francesine e pasticcini mignon.</li>
</ul>

<h2>Le creazioni della casa</h2>
<ul>
<li><strong>Cestino</strong>: il riccio della sfogliatella diventa un cesto croccante, con chantilly e frutti di bosco.</li>
<li><strong>Segreto amalfitano</strong>: babà al limoncello con un cuore di chantilly al limone, come quella della delizia al limone amalfitana. <a href="../babamisu/">Nato nel 2023 insieme al Babàmisù.</a></li>
<li><strong>Babàmisù</strong>: babà farcito con crema al mascarpone e bagnato con liquore al caffè. <a href="../babamisu/">Scopri il Babàmisù</a>.</li>
<li><strong>Pellecchiella</strong>: torta con le albicocche Pellecchielle del Vesuvio.</li>
<li><strong>Torta di mele</strong> con mela Annurca IGP, <strong>ricotta e pera</strong>, crostata di fragoline, millefoglie crema e amarena.</li>
</ul>

<h2>Le feste</h2>
<p>Il calendario si legge anche in vetrina: le zeppole il 19 marzo, la pastiera a Pasqua, e a Natale i <a href="../storie/dolci-di-natale/">dolci natalizi napoletani</a>.</p>
""",
 "galleria": ["sfogliatella-riccia", "baba-amarena", "pastiera", "babamisu", "pellecchiella", "zeppola", "baba-al-rum-classico", "zeppolina-san-giuseppe"],
 "cta": [("Tutti i dolci nel menu", "menu_dolci"), ("Come arrivare", "mappa")],
},
{
 "slug": "rosticceria",
 "nav": "Rosticceria e pranzo veloce",
 "titolo": "Rosticceria napoletana, freselle e insalate",
 "titolo_seo": "Rosticceria napoletana in centro a Napoli",
 "descrizione": "Frittatine, crocchè, pizza fritta, saltimbocca, freselle e insalate: la rosticceria napoletana di Ceraldi Caffè per un pranzo veloce in centro a Napoli.",
 "dek": "Frittatine, crocchè, pizza fritta e saltimbocca da mangiare passeggiando. Oppure, al tavolo, una fresella o un'insalata per un pranzo veloce.",
 "foto": "saltimbocca",
 "corpo": """
<p>La rosticceria è la cucina di strada di Napoli: si compra al banco, si mangia in piedi o camminando tra i vicoli, e accompagna i turisti nelle loro passeggiate tra i suoni e i colori della città. Da noi è tutta quella della tradizione.</p>

<h2>La rosticceria tradizionale</h2>
<ul>
<li><strong>Frittatina napoletana</strong>: bucatini, besciamella, carne macinata e piselli, impanati e fritti.</li>
<li><strong>Crocchè di patate</strong>, con formaggio e prezzemolo.</li>
<li><strong>Pizza fritta</strong> ripiena: prosciutto e mozzarella, ricotta, oppure scarole.</li>
<li><strong>Pizza di scarole</strong>, ripiena di scarole ripassate in padella.</li>
<li><strong>Focacce</strong> margherita, marinara, mimosa e la <strong>parigina</strong>, con prosciutto cotto, mozzarella e pomodoro sotto un velo di sfoglia.</li>
<li><strong>Lingua di pizza</strong> farcita, il <strong>ripieno del giorno</strong> e la rosticceria mignon.</li>
</ul>

<h2>Panini e saltimbocca</h2>
<p>Il <strong>saltimbocca</strong> con porchetta e provola, la <strong>zingara ischitana</strong> (pane casareccio con crudo, mozzarella, pomodori, insalata e maionese), panini con cotto, crudo o caprese, toast e tramezzini.</p>

<h2>Freselle e insalate</h2>
<p>Per un pranzo leggero, le <strong>freselle</strong>: la classica napoletana con pomodorini, tonno, cipolla rossa e olive; la caprese con bocconcini di mozzarella e pesto; la Cetara con le alici. E le insalate: tonno e pomodoro, caprese con pomodori di Sorrento, l'insalatona completa e la Caesar salad.</p>
""",
 "galleria": ["frittatina"],
 "cta": [("Il menu completo", "menu_food"), ("Come arrivare", "mappa")],
},
{
 "slug": "aspritz",
 "nav": "Aspritz e aperitivi",
 "titolo": "Aspritz: lo spritz napoletano fatto in casa",
 "titolo_seo": "Aspritz, l'aperitivo della casa a Napoli",
 "descrizione": "L'Aspritz di Ceraldi Caffè: bitter fatto in casa con agrumi della Costiera Amalfitana e Asprinio di Aversa spumante. Aperitivo in Piazza Carità, Napoli.",
 "dek": "Sono le sei di sera, le luci della città si accendono e l'aperitivo va in scena. Il protagonista è nostro: l'Aspritz.",
 "foto": "aspritz",
 # La pagina è costruita da pagina_aspritz() in build.py con i testi di aspritz.py
 # (il vecchio corpo, con gli altri spritz, negroni e vini, è confluito nella sezione «Accanto all'Aspritz»).
},

{
 "slug": "babamisu",
 "nav": "Babàmisù",
 "titolo": "Babàmisù: il babà incontra il tiramisù",
 "titolo_seo": "Babàmisù, il babà al mascarpone di Ceraldi a Napoli",
 "descrizione": "Il Babàmisù di Ceraldi Caffè: babà farcito con crema al mascarpone e bagnato con liquore al caffè. Lo produciamo noi dal 2023, a Napoli in Piazza Carità.",
 "dek": "Un babà farcito con crema al mascarpone e bagnato con liquore al caffè. Due icone della pasticceria italiana in un solo morso, fatto da noi dal 2023.",
 "foto": "babamisu",
 "corpo": """
<p class="capolettera">Il babà è il dolce lievitato che Napoli ha fatto suo, bagnato e morbido. Il tiramisù è il dolce al cucchiaio con mascarpone e caffè. Il <strong>Babàmisù</strong> li mette insieme: un babà <strong>farcito con crema al mascarpone</strong> e <strong>bagnato con liquore al caffè</strong>.</p>

<h2>Quando nasce</h2>
<p>Lo produciamo noi, in casa, <strong>dal 2023</strong>: l'anno del cinquantesimo anniversario di Ceraldi, che dal 1973 lavora a Napoli come bar e pasticceria di famiglia. Nello stesso anno è nato anche il <a href="../specialita/">Segreto amalfitano</a>, un babà al limoncello con un cuore di crema chantilly al limone, come quella della delizia al limone amalfitana.</p>

<h2>Che cos'è</h2>
<ul>
<li><strong>Il babà</strong>, morbido e imbevuto.</li>
<li><strong>La farcitura</strong> con crema al mascarpone.</li>
<li><strong>La bagna</strong> con liquore al caffè: per questo il dolce contiene alcol.</li>
</ul>
<p>Allergeni: glutine, latte, uova. Se hai altre esigenze, chiedi al personale al banco.</p>

<h2>Dove e quando</h2>
<p>Il Babàmisù è sempre disponibile nella nostra vetrina in Piazza Carità 14, lungo via Toledo, dalle 6:30 alle 20:30. Il prezzo aggiornato è nel <a href="../menu/#s-1">menu</a>. Per capire da dove viene il babà, leggi <a href="../storie/baba/">la storia del babà napoletano</a>.</p>
""",
 "cta": [("Vedi il menu con i prezzi", "menu_dolci"), ("Come arrivare", "mappa")],
},
{
 "slug": "caffe-sfogliata",
 "nav": "Caffè Sfogliata",
 "titolo": "Caffè Sfogliata: il caffè nel riccio al cioccolato",
 "titolo_seo": "Caffè Sfogliata, il caffè speciale di Ceraldi a Napoli",
 "descrizione": "Caffè Sfogliata di Ceraldi: caffè caldo e schiuma fredda di latte alla cannella in un riccio edibile al cioccolato fondente. Piazza Carità, Napoli.",
 "dek": "Caffè caldo, schiuma fredda di latte alla cannella e un riccio che si mangia, rivestito di cioccolato fondente.",
 "foto": "bar-banco",
 "corpo": """
<p class="capolettera">Il <strong>Caffè Sfogliata</strong> è uno dei nostri caffè speciali, e si capisce perché arrivi in un modo diverso dal solito: il caffè è <strong>caldo</strong>, la schiuma di latte alla cannella è <strong>fredda</strong>, e il contenitore è un <strong>riccio edibile rivestito di cioccolato fondente</strong>.</p>

<h2>Com'è fatto</h2>
<ul>
<li><strong>Caffè caldo</strong>, servito dentro il riccio.</li>
<li><strong>Schiuma fredda di latte alla cannella</strong>.</li>
<li><strong>Un riccio edibile</strong>, rivestito di <strong>cioccolato fondente</strong>: si mangia dopo il caffè.</li>
</ul>
<p>Il contrasto tra il caldo del caffè e il freddo della schiuma è il centro della ricetta.</p>

<h2>Dove trovarlo</h2>
<p>Il Caffè Sfogliata è disponibile al banco e al tavolo da Ceraldi Caffè, in Piazza Carità 14, lungo via Toledo, tutti i giorni dalle 6:30 alle 20:30. Il prezzo è nel <a href="../menu/#s-1">menu</a>. Se ami il caffè fatto con un'idea in più, guarda anche <a href="../specialita/">le specialità della casa</a> e <a href="../storie/caffe-napoletano/">la tradizione del caffè napoletano</a>.</p>
""",
 "cta": [("Vedi il menu con i prezzi", "menu_bar"), ("Come arrivare", "mappa")],
},
]
