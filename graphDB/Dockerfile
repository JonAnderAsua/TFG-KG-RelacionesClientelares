FROM adoptopenjdk/openjdk12:alpine

RUN apk update && apk add -u bash 

ARG VERSION=10.0.3
ARG EDITION=free

COPY graphdb-${EDITION}-${VERSION}-dist.zip /opt/
RUN cd /opt/ \
        && unzip graphdb-${EDITION}-${VERSION}-dist.zip \
        && rm graphdb-${VERSION}-dist.zip \
        && rm /opt/graphdb-${VERSION}/bin/*.cmd

RUN ln -s /opt/graphdb-${VERSION} /opt/graphdb && \
    mkdir -p /data && \
    ln -s /data /opt/graphdb/data

EXPOSE 7200

ENTRYPOINT /opt/graphdb/bin/graphdb -Dgraphdb.workbench.cors.enable=true -Dgraphdb.workbench.cors.origin=*
