
if [ "$#" -gt 0 ]; then
    sqlite3 facemash.db "CREATE TABLE IF NOT EXISTS face (url VARCHAR PRIMARY KEY, rating INTEGER)"
    sqlite3 facemash.db "CREATE INDEX IF NOT EXISTS face_rating on face(rating)"
    for url in "$@"; do
        sqlite3 facemash.db "INSERT INTO face (url, rating) VALUES ('$url',1000)"
    done
else
    echo "usage: sh $0 url ..."
fi

