FROM adoptopenjdk/openjdk12:alpine

RUN apk update && apk add -u bash 

ARG VERSION=9.7.0
ARG EDITION=free

COPY graphdb-${EDITION}-${VERSION}-dist.zip /opt/
RUN cd /opt/ \
        && unzip graphdb-${EDITION}-${VERSION}-dist.zip \
        && rm graphdb-${EDITION}-${VERSION}-dist.zip \
        && rm /opt/graphdb-${EDITION}-${VERSION}/bin/*.cmd

RUN ln -s /opt/graphdb-${EDITION}-${VERSION} /opt/graphdb && \
    mkdir -p /data && \
    ln -s /data /opt/graphdb/data

EXPOSE 7200

ENTRYPOINT ["/opt/graphdb/bin/graphdb"]