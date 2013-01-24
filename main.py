#!/usr/bin/env Python                                                                                                                                  

import waltz
from waltz import track, db, render, session

urls = ('/session', 'Session',
        '/analytics', 'Analytics',
        '/', 'Index')

sessions = {'cart': waltz.Cart()}
app = waltz.setup.dancefloor(urls, globals(), sessions=sessions)

class Index:
    @track
    def GET(self):
        return render().index()

class Session:
    def GET(self):
        return session()

class Analytics:
    def GET(self):
        return db().get('analytics')

if __name__ == "__main__":
    app.run()