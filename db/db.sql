create table piscine (
  id integer primary key,
  id_uev integer,
  type varchar(500),
  nom varchar(500),
  arrondisse varchar(500),
  adresse varchar(500),
  propriete varchar(500),
  gestion varchar(500),
  pointx float,
  pointy float,
  equipement varchar(500),
  long float,
  lat float
);

create table glissade (
  id integer primary key,
  nom varchar(500),
  nom_arrondisse varchar(500),
  cle_arrondisse varchar(50),
  date_maj text,
  ouvert integer,
  deblaye integer,
  condition varchar(500)
);


create table patinoire (
  id integer primary key,
  nom varchar(500),
  nom_arrondisse varchar(500),
  date_maj text,
  ouvert integer,
  deblaye integer,
  arrose integer,
  resurface integer
);

