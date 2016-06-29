#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import csv, sys

try:
    conn = psycopg2.connect("dbname='tabletennis' user='elimunn' host='localhost'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
#  schema for meta tables
cur.execute("CREATE SCHEMA IF NOT EXISTS meta;")
# create table to hold meta data for players
cur.execute("""DROP TABLE IF EXISTS meta.team;""")
cur.execute("""CREATE TABLE IF NOT EXISTS meta.team (
  id SERIAL,
  name varchar,
  dob date,
  southpaw boolean,
  employer boolean
);""")


cur.execute("""DROP TABLE IF EXISTS meta.match;""")

cur.execute("""CREATE TABLE IF NOT EXISTS meta.match (
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
);""")


# print meta.match
cur.execute("SELECT * FROM meta.match;")



names = []
with open('scripts/sheet.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    header = spamreader.next()
    # print header
    for row in spamreader:
        n1 = row[4]
        n2 = row[6]
        if n1 not in names:
            # add to names
            names.append(n1)
        if n2 not in names:
            # add to names
            names.append(n2)

        #
        # cur.execute("""
        # INSERT INTO
        #     meta.team
        #     (name)
        # VALUES
        #     (%s)""",
        # );
        # conn.commit()


# matches = []
# # with open('scripts/sheet.csv', 'rb') as csvfile:
# #     func = csv.reader(csvfile, delimiter=',')
# #
# #     header = func.next()
# #     for row in func:
# #         m1 = row[1]
# #         m2 = row[2]
# #         m3 = row[3]
# #         m4 = row[4]
# #         m5 = row[5]
# #         m6 = row[6]
# #         m7 = row[7]
# #         m8 = row[8]
# #         matches.append(m1)
# #         matches.append(m2)
# #         matches.append(m3)
# #         matches.append(m4)
# #         matches.append(m5)
# #         matches.append(m6)
# #         matches.append(m7)
# #         matches.append(m8)
#
# print matches


with open('scripts/sheet.csv', 'rb') as csvfile:
    func = csv.reader(csvfile, delimiter=',')

    header = func.next()
    listelos = []
    for row in func:
        match = row[2]
        game = row[3]
        date = row[1]
        team1 = row[4]
        team1score = row[5]
        team1elo = row[12]
        team2 = row [6]
        team2score = row[7]
        team2elo = row[13]
        listelos.append(team1elo)
        listelos.append(team2elo)


        cur.execute("""
        INSERT INTO
            meta.match
            (match, match_game, match_date, team_1, team_1_score, team_1_elo, team_2, team_2_score, team_2_elo)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (match, game, date, team1, team1score, team1elo, team2, team2score, team2elo)
        );
        conn.commit()

    print max(listelos)






cur.execute("""INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('dave', '1987-06-12', '1', '1');""")
cur.execute("""INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('alex', '1987-02-04', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('matt', '1987-11-23', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('jonathon', '1987-09-21', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('eli', '1995-11-12', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, southpaw, employer) VALUES ('manuel', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, dob, southpaw, employer) VALUES ('melissa', '1992-04-17', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, southpaw, employer) VALUES ('chris', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, southpaw, employer) VALUES ('adam', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, southpaw, employer) VALUES ('daveBriand', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, southpaw, employer) VALUES ('ramsey', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, southpaw, employer) VALUES ('daveCharizard', '0', '1');""")
cur.execute("""INSERT INTO meta.team (name, southpaw, employer) VALUES ('joe', '0', '1');""")



conn.commit()
# cur.execute("SELECT * FROM meta.team;")


# print cur.fetchall()
# print "TESTING"

# leng = len(cur.fetchall())
# names_leng = len(names)
# test_pass = leng == names_leng
#
# if test_pass == True:
#     print "Booyaaa"
# else:
#     print "FAAIILL"
