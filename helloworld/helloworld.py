import cgi
import webapp2
from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
  def get(self):
    '''
    user = users.get_current_user()

    if user:
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.write('Hello, ' + user.nickname())
    else:
      self.redirect(users.create_login_url(self.request.uri))
    '''

    self.response.out.write("""
      <html>
       <body>
        <form action="/sign" method="post">
         <div><textarea name="content" rows="3" cols="60"></textarea></div>
         <div><input type="submit" value="Sign Guestbook"></div>
        </form>
       </body>
      </html>""")

class Guestbook(webapp2.RequestHandler):
  def post(self):
    self.response.out.write('<html><body>You wrote:<pre>')
    self.response.out.write(cgi.escape(self.request.get('content')))
    self.response.out.write('</pre></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/sign', Guestbook)],
                               debug=True)
