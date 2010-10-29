#!/bin/sh
sqlite3 facemash.db "DROP INDEX face_rating"
sqlite3 facemash.db "DROP TABLE face"
