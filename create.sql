CREATE TABLE Films
(
  film_id              INT   NOT NULL,
  film_title           char(80)  NOT NULL,
  director_id          char(2)  NOT NULL,
  genre_id             char(3)  NOT NULL,

  country_id           char(3)  NOT NULL,
  film_year            INT  NOT NULL,
  average_rating       float8 NOT NULL

);

CREATE TABLE Countries
(
  country_id      char(3)  NOT NULL,
  country_name    char(20)  NOT NULL 
);

CREATE TABLE Directors
(
  director_id     char(2)  NOT NULL,
  director_name   char(50)  NOT NULL
);

CREATE TABLE Genres
(
  genre_id      char(3)  NOT NULL ,
  genre_name    char(60) NOT NULL  
);

ALTER TABLE Films ADD PRIMARY KEY (film_id);
ALTER TABLE Countries ADD PRIMARY KEY (country_id);
ALTER TABLE Directors ADD PRIMARY KEY (director_id);
ALTER TABLE Genres ADD PRIMARY KEY (genre_id);

ALTER TABLE Films ADD CONSTRAINT FK_Films_Countries FOREIGN KEY (country_id) REFERENCES Countries (country_id);
ALTER TABLE Films ADD CONSTRAINT FK_Films_Directors FOREIGN KEY (director_id) REFERENCES Directors (director_id);
ALTER TABLE Films ADD CONSTRAINT FK_Films_Genres FOREIGN KEY (genre_id) REFERENCES Genres (genre_id);