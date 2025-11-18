
[Foreign Keys](https://sqlite.org/foreignkeys.html)

``` SQL
CREATE TABLE track(
  trackid     INTEGER, 
  trackname   TEXT, 
  trackartist INTEGER,
  FOREIGN KEY(trackartist) REFERENCES artist(artistid)
);


Imagens utilizadas
