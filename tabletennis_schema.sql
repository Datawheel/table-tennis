-- init database
CREATE DATABASE tabletennis;
-- schema for meta tables
CREATE SCHEMA IF NOT EXISTS meta;
-- create table to hold meta data for players
DROP TABLE IF EXISTS meta.team;
CREATE TABlE IF NOT EXISTS meta.team (
  id SERIAL,
  name varchar,
  dob date,
  southpaw boolean,
  employer boolean
);

DROP TABLE IF EXISTS meta.match;
CREATE TABLE IF NOT EXISTS meta.match (
  id SERIAL,
  match INT,
  match_game INT,
  match_date date,
  team_1 varchar,
  team_1_score INT,
  team_1_elo INT,
  team_2 varchar,
  team_2_score INT,
  team_2_elo INT
);


-- add team
INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('dave', '1987-06-12', '1', '1');
INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('alex', '1987-02-04', '0', '1');
INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('matt', '1987-11-23', '0', '1');
INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('eli', '1995-11-12', '0', '1');
INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('melissa', '1992-04-17', '0', '1');
INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('jonathon', '1987-09-21', '0', '1');


SELECT * FROM meta.match;

SELECT * FROM meta.team;
