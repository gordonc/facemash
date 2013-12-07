#!/bin/sh

if [ "$#" -gt 0 ]; then
    sqlite3 facemash.db "CREATE TABLE IF NOT EXISTS face (name VARCHAR PRIMARY KEY, rating INTEGER)"
    sqlite3 facemash.db "CREATE INDEX IF NOT EXISTS face_rating on face(rating)"
    for arg in "$@"; do
        sqlite3 facemash.db "INSERT INTO face (name, rating) VALUES ('$arg',1000)"
    done
else
    echo "usage: sh $0 image_url ..."
fi

