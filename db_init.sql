CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE Navigation_Safety_Object (
    ime VARCHAR(255) NOT NULL,
    ps_br VARCHAR(255),
    e_br VARCHAR(255),
    tip_objekta INTEGER,
    lucka_kapetanija VARCHAR(255),
    fotografija VARCHAR(255),
    id_ais VARCHAR(255),
    simbol_oznaka VARCHAR(255),
    kljuc INTEGER PRIMARY KEY,
    geom GEOMETRY(Point, 4326)
);

CREATE INDEX spatial_index ON navigation_safety_object USING GIST (geom);