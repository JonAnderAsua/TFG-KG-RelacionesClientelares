# TFG-KG-RelacionesClientelares - Tutoriala

README honetan programa hau nola konfigutatzen eta exekutatzen den azaltzen da. Adibide bezala 'la_donacion' proiektua hartu da.

## Aurkibidea

- [Informazio orokorra](#informazio-orokorra)
- [Erabilitako teknologiak](#erabilitako-teknologiak)
- [Aurrebaldintzak](#aurrebaldintzak)
- [YAML fitxategiaren konfigurazioa](#yaml-fitxategiaren-konfigurazioa) 
- [Dependentzien instalazioa](#dependentzien-instalazioa)
- [Programaren exekuzioa](#programaren-exekuzioa)

## Informazio orokorra
README honetan programa hau nola konfiguratzen eta exekutatzen den azaltzen da. Programa honek parametro batzuk pasatu ostean era automatiko batean datu multzo bat eraldatu eta _triple store_ batera igotzen du. Adibide bezala 'la_donacion' proiektua hartu da.

## Erabilitako teknologiak
- Python >= 3.7
- Docker 20.10.7
- GraphDB 10.0.3 Free Edition (deskargatzeko [SAKATU HEMEN](https://www.ontotext.com/products/graphdb/download/))

Deskargatutako _GraphDB_ binarioa graphDB/ fitxategiaren barnean egon behar da eta hurrengo formatua jarraitu behar du: _graphdb-$edizioa-$bertsioa-dist.zip_. Kasu honetan bitarraren izena _graphdb-free-10.0.3-dist.zip_, beste bat izatekotan, _Dockerfile_ fitxategian parametroak aldatu behar dira.

## Aurrebaldintzak

Programaren exekuzioarekin hasi baino lehen hurrengo aurrebaldintzak betetzen direla kontuan hartuko da:

- GraphDB instantzia bat martxan edukitzea. Honetarako jarraitu _Graphdb_ berak daukan [tutoriala](https://graphdb.ontotext.com/documentation/free/free/run-desktop-installation.html).
- Programa exekutatu nahi den terminalean Python interpretatzaile bat instalatuta izatea (gutxienez 3.7 bertsioa).
- Terminalean proiektu hau klonatuta edukitzea, horretarako exekutatu hurrengo komandoak terminalean:
```bash
git clone --recurse-submodules https://github.com/mikel-egana-aranguren/TFG-KG-RelacionesClientelares
```
```bash
git submodule update --remote --merge
```
## YAML fitxategiaren konfigurazioa

Behin aurrebaldintza guztiak bete direnean konfigurazioaren hasi ahal da. Horretarako [YAML fitxategi bat](https://github.com/mikel-egana-aranguren/TFG-KG-RelacionesClientelares/blob/develop/doc/config.yml) aurkitzen da *doc* karpetaren barnean hurrengo parametroekin:

- _project_name_: Proiektuaren izena.
- _workspace_: Erabili nahi diren datuen helbide nagusia.
- _images_: #Lan eremuaren barnean irudiak egongo diren karpeta
- _data_source_: Erabili beharreko datuen _path-a_.
- _validate_: SHACL testen _path-a_.
- _named_graph_: Datuak GraphDB barnean egongo diren taldea adierazten duen URIa.
- _run_: Exekutatu nahi den programaren _path-a_. Programa hau _SPARQL_ eskaeren bitartez _triple_store_ aldagaian deklaratutako _triple storean_ datuak igotzeko gaitasuna izan behar du.
- _metadata_file_: Metadatuen _path-a_.
- _delete_graph_: Aurretik _triple store-an_ zegoen grafoa ezabatu nahi den ala ez.
- _triple_store_: Tripleak igo nahi diren _triple storearen_ URLa, ez da beharrezkoa GraphDb instantzia baten URL bat izatea, hau da, SPARQL eskaerak onartzen dituen instantzia baten URIa jarri behar da. 
- _logs_: Programa exekutatzerako orduan sortutako logak non gorde nahi diren _path-a_.
- _rdf_output_: Tripleekin bete nahi den fitxategiaren _path-a_.

_la_donacion_ proiektuaren kasuan hurrengo konfigurazioa jarri da: 
```yaml
la_donacion:
  project_name: 'la_donacion'
  workspace: ./
  images: images
  data_source: data/ladonacion.es
  validate: graphSource/tests/TestJson2rdf.py
  named_graph: http://localhost:8080/
  run: procesSource/source/json2rdf.py
  metadata_file: metadata.ttl
  delete_graph: true
  triple_store: http://localhost:7200/repositories/LaDonacion
  logs: logs/laDonacion.log
  rdf_output: data/ladonacion.es/graphLaDonacion.nt
```
Esan beharra dago workspace parametroan prozesatu nahi diren datuen helbidea jarri behar da, **dagoen helbidea ez du funtzionatuko**


## Dependentzien instalazioa
Programa exekutatu baino lehen programaren dependentziak instalatu behar dira, horretarako hurrengo komandoak exekutatu behar dira proiektuko fitxategi nagusitik:
```bash
pip install -r requirements.txt
```
```bash
pip install -e .
```
Lehenengo komandoarekin _requirements.txt_ fitxategiaren barnean adierazitako moduluak instalatuko dira. Aldiz, bigarrenean, modulu lokalak instalatzen dira.
## Programaren exekuzioa 
Exekuzioa hasi baino lehen _SPARQL Endpointaren URIa_ aldatu behar da, honetarako [datu basearen kontra eskaerak egiteko fitxategian](https://github.com/JonAnderAsua/grafoavis/blob/9a5e041b41208da4233531d3b3997fd672263e0e/public/js/db.js) eta [_YASGUI SPARQL Endpointaren_ fitxategian](https://github.com/JonAnderAsua/grafoavis/blob/master/public/yasgui.html), _uri_ parametroan, nahi den _endpointaren URIa_ jarri behar da. 

_GraphDB_ eta _Trifid_ instantziak eta bisualizaziorako programa martxan jarri behar dira. Lehenenngo eta hirugarren kasuetarako _Docker_ irudi propiak sortu behar dira, aldiz, _Trifid_ instantzia martxan jartzeko _docker compose_ komandoaren bitartez egin behar da, honetarako hurrengo komandoak exekutatu behar dira:
```bash
docker build -t graphdb graphDB/
```
```bash
docker build -t bisualizazioa grafoavis/
```
```bash
docker-compose up
```
Komando guztiak batean batzeko hurrengo komandoa exekutatu:
```bash
docker build -t graphdb graphDB/ && docker build -t bisualizazioa grafoavis/ && docker-compose up
```

Behin hau eginda, programa exekutatu ahal izateko, fitxategi nagusian kokatuta, hurrengo komandoa exekutatu behar da:
```bash
python3 procesSource/source/ejecutador.py [sortutako proiektuaren izena]
```

Adibidearen kasuan komandoa hurrengoa izango litzateke:
```bash
python3 procesSource/source/ejecutador.py la_donacion
```

**Sartutako proiektua ez bada existitzen programa berak argitaratuko ditu eskuragarri dauden proiektuen izenak.**

Hau egin ostean _http://localhost:3000/bisualizazioa_ atalean sortutako grafoa agertzen da. _SPARQL Endpointa_ ikusteko _URIa http://localhost:3000/yasgui_ da.

[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/jonan_bateria.svg?style=social&label=Follow%20%40jonan_bateria)](https://twitter.com/jonan_bateria)
