#!/bin/sh
sqlite3 facemash.db "CREATE TABLE face (name VARCHAR PRIMARY KEY, rating INTEGER)"
sqlite3 facemash.db "CREATE INDEX face_rating on face(rating)"
