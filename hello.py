from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)


# Create a route decorator
@app.route('/')
def index():
   firstName = "Andy yang"
   stuff = "This is a <strong>bold</strong> text"
   title = "this is a very good title isn't it?"
   friendsList = ["Ricky Howard", "Veren Calista", "Clairine Angelia", "Charlene Chandra"]
   return render_template(
      'index.html', 
      firstName=firstName, 
      stuff=stuff, 
      title=title, 
      friendsList=friendsList
   )

@app.route('/user/<name>')
def user(name):
   return render_template('user.html', name=name)


# create custom error pages

# invalid page
@app.errorhandler(404)
def page_not_found(e):
   return render_template("404.html"), 404
   
# internal server error
@app.errorhandler(500)
def page_not_found(e):
   return render_template("500.html"), 500



if __name__ == '__main__':
   app.run(debug=True)
