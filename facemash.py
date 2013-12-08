import urlparse
import sqlite3
import StringIO
import sys
import wsgiref.simple_server

class Face:
    def __init__(self, url):
        self.url = url
        cur = conn.cursor()
        cur.execute('SELECT rating FROM face where url = ?', (self.url,))
        row = cur.fetchone()
        self.rating = row[0]

    def update_rating(self, score, opponent):
        K0 = 15
        Q0 = 10 ** (float(self.rating)/400)
        Q1 = 10 ** (float(opponent.rating)/400)
        E0 = Q0 / (Q0 + Q1)
        self.rating += (K0 * (score - E0))

        cur = conn.cursor()
        cur.execute('UPDATE face SET rating=? WHERE url=?', (self.rating, self.url))
        conn.commit()

    def get_rank(self):
        cur = conn.cursor()
        cur.execute('SELECT count(*)+1 FROM face where rating > ?', (self.rating,))
        row = cur.fetchone()
        return row[0]

    @classmethod
    def random(cls, n):
        cur = conn.cursor()
        cur.execute('SELECT url FROM face ORDER BY RANDOM() LIMIT ?;', (n,))
        rows = cur.fetchall()
        return [Face(row[0]) for row in rows]

def handle(env, start_response):
    if env.has_key('CONTENT_LENGTH') and env['CONTENT_LENGTH'] and env.has_key('wsgi.input'):
        length = int(env['CONTENT_LENGTH'])
        query = StringIO.StringIO(env['wsgi.input'].read(length)).getvalue()
        data = urlparse.parse_qs(query)

        winner = Face(data['winner'][0])
        loser = Face(data['loser'][0])

        winner.update_rating(1, loser)
        loser.update_rating(0, winner)

    face1,face2 = Face.random(2)

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [str(html % {'url1': face1.url, 'url2': face2.url, 'rank1': face1.get_rank(), 'rank2': face2.get_rank()})]

html = open('template.html', 'r').read()
conn = sqlite3.connect('facemash.db')

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

httpd = wsgiref.simple_server.make_server('', port, handle)
sa = httpd.socket.getsockname() 
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()

conn.close()

