# GraphDB y Silk

Este repositorio Docker incluye los servicios GraphDB y Silk, enlazados entre sí, para poder usar Silk para descubrimiento de enlaces, combinando los datos que residen en GraphDB con datos externos (Ej. DBPedia).

## Ejecución

Construir la imagen:

```bash
docker build -t="graphdb-free-9.7.0" .
```

Levantar los servicios:

```bash
docker-compose up
```

Esto debería levantar los dos servicios en localhost 7200 (GraphDB) y 81 (Silk). Los puertos y volumenes se pueden configurar en el archivo `docker-compose.yml` (Ambos servicios persisten los datos en los volumenes).

En GraphDB, conectar el repositorio `NORA-links`. En Silk, el proyecto `NORA-links-tests` (Importarlo de `Linked-Data-fase-2/graphdb-silk-docker/silk-workspaces/NORA-links-tests.zip` si fuera necesario) incluye una configuración con GraphDB, y DBPedia.