import urlparse
import sqlite3
import StringIO
import gevent.wsgi

class Face:
    def __init__(self, name):
        self.name = name
        cur = conn.cursor()
        cur.execute('SELECT rating FROM face where name = ?', (self.name,))
        res = cur.fetchone()
        self.rating = res[0]

    def update_rating(self, score, opponent):
        K0 = 15
        Q0 = 10 ** (float(self.rating)/400)
        Q1 = 10 ** (float(opponent.rating)/400)
        E0 = Q0 / (Q0 + Q1)
        self.rating += (K0 * (score - E0))

        cur = conn.cursor()
        cur.execute('UPDATE face SET rating=? WHERE name=?', (self.rating,self.name))
        conn.commit()

    def get_rank(self):
        cur = conn.cursor()
        cur.execute('SELECT count(*)+1 FROM face where rating > ?', (self.rating,))
        res = cur.fetchone()
        return res[0]

    @classmethod
    def random(cls):
        cur = conn.cursor()
        cur.execute('SELECT name FROM face ORDER BY RANDOM() LIMIT 1;')
        res = cur.fetchone()
        return Face(res[0])

def handle(env, start_response):
    if env.has_key('CONTENT_LENGTH') and env.has_key('wsgi.input'):
        length = int(env['CONTENT_LENGTH'])
        query = StringIO.StringIO(env['wsgi.input'].read(length)).getvalue()
        data = urlparse.parse_qs(query)

        face1 = Face(data['name1'][0])
        face2 = Face(data['name2'][0])
        score1 = 1 if data['winner'][0] == 'face1' else 0
        score2 = 1 if data['winner'][0] == 'face2' else 0

        face1.update_rating(score1, face2)
        face2.update_rating(score2, face1)

    face1 = Face.random()
    face2 = Face.random()

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [str(html % {'name1': face1.name, 'name2': face2.name, 'pic1': face1.name, 'pic2': face2.name, 'rank1': face1.get_rank(), 'rank2': face2.get_rank()})]

html = open('t.html', 'r').read()
conn = sqlite3.connect('facemash.db')

gevent.wsgi.WSGIServer(('localhost', 8088), handle, log=None).serve_forever()

conn.close()

