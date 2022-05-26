# TFG-KG-RelacionesClientelares - Tutoriala
Readme honetan programa hau nola konfigutatzen eta exekutatzen den azaltzen da. Adibide bezala 'la_donacion' proiektua hartu da.

## Aurkibidea

- [Aurrebaldintzak](#aurrebaldintzak)
- [Yaml fitxategiaren konfigurazioa](#yaml-fitxategiaren-konfigurazioa) 
- [Programaren exekuzioa](#programaren_exekuzioa)
- [Programaren froga](#programaren-froga)

## Aurrebaldintzak

Programaren exekuzioarekin hasi baino lehen hurrengo aurrebaldintzak betetzen direla kontuan hartuko da:

- Graphdb instantzia bat martxan edukitzea. Honetarako jarraitu _Graphdb_ berak daukan [tutoriala]().
- Programa exekutatu nahi den terminalean Python interpretatzaile bat instalatuta izatea.
- Terminalean proiektu hau klonatuta edukitzea, horretarako exekutatu hurrengo komandoa terminalean:
```bash
git clone https://github.com/mikel-egana-aranguren/TFG-KG-RelacionesClientelares
```
## Yaml fitxategiaren konfigurazioa
Behin aurrebaldintza guztiak bete direnean konfigurazioaren hasi ahal da, horretarako [yaml fitxategi bat](https://github.com/mikel-egana-aranguren/TFG-KG-RelacionesClientelares/blob/develop/doc/config.yml) aurkitzen da *doc* karpetaren barnean hurrengo parametroekin:

- _project_name_: Proiektuaren izena.
- _data_source_: Erabili beharreko datuen _path-a_.
- _validate_: Programaren funtzionamendu egokia bermatzeko testen _path-a_.
- _named_graph_: Tripleen elementu bakoitzak izango duen URI basea.
- _run_: Exekutatu nahi den programaren _path-a_.
- _metadata_file_: Metadatuen _path-a_.
- _delete_graph_: Aurretik _triple store-an_ zegoen grafoa ezabatu nahi den ala ez.
- _triple_store_: Tripleak igo nahi diren _triple store-a_.
- _logs_: Programa exekutatzerako orduan sortutako logak non gorde nahi diren _path-a_.
- _rdf_output_: Tripeekin bete nahi den fitxategiaren _path-a_.

_la_donacion_ proiektuaren kasuan hurrengo konfigurazioa jarri da: 
```yaml
 la_donacion: 
    project_name: 'la_donacion_local_JonAnder' 
    data_source: ./data/ladonacion.es 
    validate: ./graphSource/tests/TestJson2rdf.py 
    named_graph: http://ehu.eus/ 
    run: ./procesSource/source/json2rdf.py 
    metadata_file: ./metadata.ttl 
    delete_graph: true 
    triple_store: http://localhost:7200/repositories/LaDonacion/statements 
    logs: ./logs/laDonacion.log 
    rdf_output: ./data/ladonacion.es/graphLaDonacion.nt 
```
## Programaren exekuzioa 
Programa exekutatu ahal izateko fitxategi nagusian kokatuta hurrengo komandoa exekutatu behar da:
```bash
python3 /procesSource/source/ejecutador.py [sortutako proiektuaren izena]
```

Adibidearen kasuan komandoa hurrengoa izango litzateke:
```bash
python3 /procesSource/source/ejecutador.py la_donacion
```

**Sartutako proiektua ez bada existitzen programa berak argitaratuko du eskuragarri dauden proiektuen izenak.**

## Programaren froga
Azkenengo pausua programa ondo exekutatu dela frogatzea da, horretarako (fitxategi nagusian ere) hurrengo komandoa exekutatu behar da terminaletik:
```bash
python3 /procesSource/tests/TestProcesador.py
```

Dena ondo ateratzen bada zorionak!
Erroreren bat sortu bada bi aukera daude, egindako konfigurazioa txarto dagoela ala programaren sorkuntza txarto egin dela, bigarrena bada mesedez jarri kontaktuan repo honen egilearekin :)

## Egilea:
Jon Ander Asua \
![jonan_bateria](https://img.shields.io/twitter/follow/jonan_bateria?style=social)
![JonAnderAsua](https://img.shields.io/github/followers/JonAnderAsua?style=social)
