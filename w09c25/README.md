# Tw09c25

# Cloud based App deployment

There are many service and technology options.

Technology options: For this course, we will create and deploy a python application that provides a web interface.

Web App Development in Python: There are many frameworks we can choose from. The most popular include Django, Pyramid and Flask. We will be using Flask (for a recent comparison look  [here](https://www.airpair.com/python/posts/django-flask-pyramid).)

Service options: For this course, we will deploy our applications on Heroku (they have a free version that you will need to sign up for, and will be sufficient for our needs). Heroku is one of many examples of of PaaS (Platform as a service) provider (for a recent comparison look [here](https://www.g2crowd.com/categories/platform-as-a-service-paas))  

To build and deploy cloud based python web applications, we will first need to create a web application on our local machine.  

# Basic Web Site Architecture technology

In case you're not already familiar (or need a refresher) we'll need to begin by introducing your to  general Web Architecture.

HTTP servers listen to HTTP requests from HTML Browsers and respond with appropriate Web page content. HTML (the Hypertext Markup Language) and CSS (Cascading Style Sheets) are two of the core technologies used for Web page content. HTML provides the structure of the page, CSS the (visual and aural) layout, for a variety of devices.

Once a HTTP server response to a request from an HTML Client, the web page content is transport using HTTP (or HTTPS if it's encrypted). Once the content is received by a web browser client, the HTML/CSS content is rendered and displayed. This can often involve many transactions between the web client and the HTTP server -- as images, and other resources, are needed before the page can be fully rendered.

Web page content can either be "static" or "dynamic". Static content is stored as files on the web server. Dynamic content is produced by software/code on the webserver. There are many, many, options for creating dynamic websites (we'll be using Python, obviously). Web clients can also be dynamic and accept code (Javascript is standard) from the HTTP server that programmatically responds to user requests in a more dynamic fashion.

For our Python Cloud deployment, our Python code will create content that will be "served" via HTTP to the requesting Web Client (HTML Browser).

# Building websites with Flask

Since our app will interact with users via the Web, we'll need to include a web development framework in our development process. For this project we'll use Flask.

## Your "Hello World" Flask server

First, you'll need to install Flask.

```
pip install flask
```

Now, we can use Python to create a local Web Application.

```python

from flask import Flask

# Create a flask application object and provide a variable name , in this case "app"
# The name given provided in the Flask initialization  is used to resolve resources
# from inside the package. Unless you are using flask within a custom package you'
# re creating, simply put __name__ here.
app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
def home():
    return "Hello world!"

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

```
[^click here for code^](flask01.py)

* Host: This is the local IP address that you wish the server to run on. Host 0.0.0.0 is local host.

* Port: Set the port to anything you want - just make sure there is nothing else already running on this port. The standard HTTP port is port 80. When running on your local machine, a common one is 8080. The default for Flask is 5000.

* Debug: Set the debug flag to True to enable debugging of the application. In debug mode the debugger will kick in when an unhandled exception occurs and the integrated server will automatically reload the application if changes in the code are detected.

At this stage, you have your own local webserver running that will simply return the string "Hello World". You can access this server by pointing your browser to localhost:5000

This is simple, but later we will return HTML pages and apply CSS styling to your HTML. For now, just make sure you understand the basic application above.

### SIDENOTE on Decorators:

Notice the line containing `@app.rout()`. This is a decorator. We covered function decorates if w05c15

```python
def print_x(x):
    return(x**2)

def html_decorate(func):
    def wrapper(x):
        return("<html><header></header><body><p>{0}</p></body></html>".format(func(x)))
    return wrapper

print_x_html = html_decorate(print_x)
print(print_x_html(10))
```
[^click here for code^](fun04.py)

Well, we can use a shorthand way of doing this using the `@` symbol, so the above code becomes...

```python
def html_decorate(func):
    def wrapper(x):
        return("<html><header></header><body><p>{0}</p></body></html>".format(func(x)))
    return wrapper

@html_decorate
def print_x(x):
    return(x**2)

print(print_x(10))
```
[^click here for code^](fun04_dec.py)


## Using the app.route decorator

The `@app.route()` decorator provides a entry point to access your content, think of it like a webserver directory with a default index.html file that is the content you wish to display`

```python

from flask import Flask

app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
def home():
    return "Hello world!"

# set your about page here
@app.route('/about/')  # be sure to include both forward slashes
def about():
    return "What your you like to know about?"

# set your about page here
@app.route('/contact/')  # be sure to include both forward slashes
def contact():
    return "Sorry, we're not here."

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

```
[^click here for code^](flask02.)



## Using render.page

Now, using Flask we can server and render template webpages.

Let's create three simple html pages and serve this in response to our three "routes" we've created thus far.

First, let's edit our program to render the templates. We start by importing "render_template" from the flask library, and then editing each of our app.routes to server the rendered_content of html pages (rather the the simple strings we responded with before)

```python
from flask import Flask, render_template

app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
def home():
    return render_template("home.html")

# set your about page here
@app.route('/about/')  # be sure to include both forward slashes
def about():
    return render_template("about.html")

# set your about page here
@app.route('/contact/')  # be sure to include both forward slashes
def contact():
    return render_template("contact.html")

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```
[^click here for code^](flask03.py)


Now, we need to create the template html files. This isn't a course in HTML, by you'll find that HTML is quite easy to learn the basics of (see [here](http://www.w3schools.com/html/)).

First, let's create a simple home page.

```html
<!DOCTYPE html>
<html>
<body>
  <h1>MIS407 Homepage</h1>
  <p>This is a test website</p>
</body>
</html>
```
[^click here for code^](templates/index.html)


And then copy this file and edit for each of the other two pages.


```html
<!DOCTYPE html>
<html>
<body>
  <h1>MIS407 About Page</h1>
  <p>This is a test website</p>
</body>
</html>
```
[^click here for code^](templates/about.html)


```html
<!DOCTYPE html>
<html>
<body>
  <h1>MIS407 Contact Page</h1>
  <p>This is a test website</p>
</body>
</html>
```
[^click here for code^](templates/contact.html)


## Let's add an navigation menu

We could copy the same HTML code in each of the files we will add to our site, but this wouldn't be the best approach. Instead, it would be much easier to manager our web site content if we created a separate file to hole the navigation menu, and then include this for each of our web pages we will serve.

```html
<!DOCTYPE html>
<html>
<body>
  <header>
    <div class="container">
      <h1 class="logo">MIS407 Web App</h1>
      <strong><nav>
        <ul class="menu">
          <li><a href="{{ url_for('home') }}">Home</a></li>
          <li><a href="{{ url_for('about') }}">About</a></li>
          <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
      </nav></strong>
    </div>
  </header>
  <div class="container">
    {%block content%}
    {%endblock%}
  </div>
</body>
</html>
```
[^click here for code^](templates/layout.html)

...and, then add the code blocks to (what are not) the child html templates.

```html
{%extends "layout.html"%}
{%block content%}
<div class="home">
  <h1>MIS407 Homepage</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^click here for code^](templates/home2.html)

```html
{%extends "layout.html"%}
{%block content%}
<div class="about">
  <h1>MIS407 About Page</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^click here for code^](templates/about2.html)

```html
{%extends "layout.html"%}
{%block content%}
<div class="contact">
  <h1>MIS407 Contact Page</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^click here for code^](templates/contact2.html)

## Adding CSS

Let's make this look a bit more "modern"

Links to CSS files go in the header section of your HTML.

Let's update out layout html file (calling it layout2.html)

```html
<!DOCTYPE html>
<html>
<head>
  <title>Flask App</title>
  <link rel="stylesheet" href="{{url_for('static', filename='css/main.css')}}"
</head>
<body>
  <header>
    <div class="container">
      <h1 class="logo">MIS407 Web App</h1>
      <strong><nav>
        <ul class="menu">
          <li><a href="{{ url_for('home') }}">Home</a></li>
          <li><a href="{{ url_for('about') }}">About</a></li>
          <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
      </nav></strong>
    </div>
  </header>
  <div class="container">
    {%block content%}
    {%endblock%}
  </div>
</body>
</html>
```
[^click here for code^](templates/layout2.html)

Now, since we have referenced a CSS file, we need to add this to our site. The Flask package will look for static content (i.e. CSS and images) in a static folder. We then organize our static folder by include subfolders for categories of static content (css subfolder, images subfolder, etc.)

Now, let's create a subfolder to hold our main.css and create out css file.

```css

/*
 * Main body
 */

 body {
  margin: 0;
  padding: 0;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: #060;
}

/*
 *  The header area
 */

header {
  background-color: #DFB887;
  height: 35px;
  width: 100%;
  opacity: .9;
  margin-bottom: 10px;
}

header h1.logo {
  margin: 0;
  font-size: 1.7em;
  color: #fff;
  text-transform: uppercase;
  float: left;
}

header h1.logo:hover {
  color: #fff;
  text-decoration: none;
}

/*
 * The body content where we've create div's
 */

.container {
  width: 1200px;
  margin: 0 auto;
}

div.home {
  padding: 10px 0 30px 0;
  background-color: #E6E6FA;
  -webkit-border-radius: 6px;
     -moz-border-radius: 6px;
          border-radius: 6px;
}

div.about {
  padding: 10px 0 30px 0;
  background-color: #E6E6FA;
  -webkit-border-radius: 6px;
     -moz-border-radius: 6px;
          border-radius: 6px;
}

div.contact {
  padding: 10px 0 30px 0;
  background-color: #E6E6FA;
  -webkit-border-radius: 6px;
     -moz-border-radius: 6px;
          border-radius: 6px;
}

h2 {
  font-size: 3em;
  margin-top: 40px;
  text-align: center;
  letter-spacing: -2px;
}

h3 {
  font-size: 1.7em;
  font-weight: 100;
  margin-top: 30px;
  text-align: center;
  letter-spacing: -1px;
  color: #999;
}

/*
* Formatting of our menu content
*/
.menu {
  float: right;
  margin-top: 8px;
}

.menu li {
  display: inline;
}

.menu li + li {
  margin-left: 35px;
}

.menu li a {
  color: #444;
  text-decoration: none;
}
```
[^click here for code^](static/css/main.css)

Finally, we need update each of our three main pages (main, contact, and about) to use our new layout. Therefore we also need to update our main flask python script (now at flask05.py)

```python
from flask import Flask, render_template

app = Flask(__name__)

# Set our homepage using the app.route decorator....
@app.route('/')
def home():
    return render_template("home3.html")

# set your about page here
@app.route('/about/')  # be sure to include both forward slashes
def about():
    return render_template("about3.html")

# set your about page here
@app.route('/contact/')  # be sure to include both forward slashes
def contact():
    return render_template("contact3.html")

# run the Flask app (which will launch a local webserver)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```
[^click here for code^](flask05.py)

...each of the webpage templates need to be updated to use layout2.html.

```html
{%extends "layout2.html"%}
{%block content%}
<div class="home">
  <h1>MIS407 Homepage</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^click here for code^](templates/home3.html)

```html
{%extends "layout2.html"%}
{%block content%}
<div class="about">
  <h1>MIS407 About Page</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^click here for code^](templates/about3.html)

```html
{%extends "layout2.html"%}
{%block content%}
<div class="contact">
  <h1>MIS407 Contact Page</h1>
  <p>This is a test website</p>
</div>
{%endblock%}
```
[^click here for code^](templates/about3.html)
