# pull official base image
FROM postgres:10

ADD create.sql /docker-entrypoint-initdb.d

RUN apt-get update \
    && for POSTGIS_VERSION in 2.4; do \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
    postgresql-contrib \
    postgresql-$PG_MAJOR-postgis-$POSTGIS_VERSION \
    postgresql-$PG_MAJOR-postgis-$POSTGIS_VERSION-scripts \
    postgresql-$PG_MAJOR-pgrouting; \
    done \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# run create.sql on init

COPY extension.sql /docker-entrypoint-initdb.d

