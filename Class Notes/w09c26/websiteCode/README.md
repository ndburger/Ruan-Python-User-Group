
#w09c26

# More on Flask

In the last class, we ended with using Flasks render template. Flask uses the jinja template engine (you can find all you need about the template ending here http://jinja.pocoo.org/).

Flask is also built on werkzeug (http://werkzeug.pocoo.org/).

## The debug flag

When starting with debug, whenever we change our script - the serve will restart

When we run in debug mode, whenever there is an error, the web interface will display a full stack trace.

Also, we can put breakpoints in our code by simply add a "raise" command.

When we see a trace back output, we can hover over the right side of one of the lines and you can jump to python command line at that location of the code. The  "dump" command (which dumps all the variables at the current position in the code) can be useful here.

## Updating or example from last class

I made significant updates to the layout.html and main.css files from last class (there was at least one error, and also some crud, in the css file)

* improved formatting
* more flexible layout (for adding additional features)

### let's dig a big deeper into routing

I've created a new version of our flask demo site (flask.07.py).

This new version demonstrations
* how we can send and receive a variable, or information, from the URL call.
* how we can read the URL as a variable and name it
* how we can use filters to make sure we are converting our variable to the appropriate type
* how we can have multiple routines to a view (I was calling then handlers last class)

## more on cascading style sheets...

I've made significant updates to our layout and main.css files.

We won't cover CSS in any detail, but there are many good resources to be found on the internet.
http://flask.pocoo.org/docs/0.11/tutorial/css/

## further look at...

If you're going to do any amount of development in Flask you'll need to dig deeper into Jinja to understand the details surrounding the rendering of html files. Specifically, how you can add/pass variables and custom code. I'd recommend your first step be to run through the tutorial found on the Flask website (http://flask.pocoo.org/docs/0.11/tutorial/introduction/)

# NOW, let's push this code to the cloud

## PaaS and Flask

We'll be using Heroku. Heroku supports many development languages and environments. In our case, we will be using Python and creating a Web Interface to our application.

## Deploying website into the "cloud"

With out experience with the command line and git, deploying on Heroku is relatively easy. Cloud based services also allow us to focus on app functionality and programming instead of server/infrastructure issues.

I've broken the deployment process down to 8 steps.

### Step 1 - Set up Virtual environment

First, we need to set up a virtual environment (and it's a good practice is to have a "clean" installation of python, specific to our application).

We need to venv library.

```
pip install virtualvenv
```

let's mkdir a "mysite" and then go into this directory and create a new python virtualvenv

```
python -m venv virtual
```

Now, I need to install any libraries I'm using.

install flash
```
$ virtual\Scripts\pip install flask
```

install requests (which we use for the weather page)
```
$ virtual\Scripts\pip install requests
```

Now, run our site to make sure it's working OK in our virtual environment.
```
$ virtual\Scripts\python mis407site\flask08.py
```

### Step2: Create an account in Heroku

http://www.heroku.com

Once you have an account, you can log in an see my "dashboard"

We will create our app using the command line.

#### Step 3: Download the heroku toolbelt.

heroku provides a command line utility to help us manage our website.

https://devcenter.heroku.com/articles/heroku-command-line

#### Step 4: Once installed, "login" .

```
$ heroku login
Enter your Heroku credentials.
Email: timsmith@iastate.edu
Password (typing will be hidden):
Logged in as timsmith@iastate.edu
```

#### Step 5: Create an app (a place to receive our code on the website)

```
$ heroku create mis407-demo
Creating mis407-demo... done
https://mis407-demo.herokuapp.com/ | https://git.heroku.com/mis407-demo.git
```

NOTE: If I want to see a list of you current apps.

```
$ heroku apps
=== timsmith@iastate.edu Apps
mis407-demo
```

Now, we can go to our dashboard, and see that we have a new app.

NOTE: The app name will need to be unique (different from this app name -- try adding your initials to the name to make it unique)

### Step 6: Create 3 files that will be needed by Heroku

Before we push our app to Heroku we need three files, requirements.tx Procfile and

Also, I need to install gnuicorn (Heroku needs this to run our webserver)

```
$virtual\Scripts\pip install gunicorn
```

#### Step 6a: Create a requirements.txt
This file contains a list of dependencies we want Heroku to use in the remote environment (we need a way to ask the server to install Flask and requests packages)

```
$ virtual\Scripts\pip freeze
click==6.6
Flask==0.11.1
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
requests==2.11.1
Werkzeug==0.11.11
```

We cut and paste this list into a new file called requirements.txt

#### Step 6b: Create a Procfile

Just use Atom to create a file called "Procfile" (note: there is not extension)

In this file we type:

```
web: gunicorn flask07:app
```
This file tells Heroku we have a gunicorn application whose mainfile is flask08 and whose main app (flask app) is called app (note: this must be the same name as the variable we instantiated the Flask object to)

#### Step 6c: Create a runtime.txt.

This file tells Heroku which python it should use to run our code.

```
python-3.5.2
```

#### Step 7: Deploy using Git.

To load our application into Heroku, we use git.

First, set up our origin to be the heroku server. We need the heroku toolbelt for this....

```
$ cd mysite/mis407site
$ git init
$ heroku git:remote -a mis407-demo
```

Now, we can work with/manage our Heroku app like it was a GitHub repo.

```
$ git add .
$ git commit -am "Initial push MIS407 app"
$ git push heroku master
```

(see: https://dashboard.heroku.com/apps/mis407-demo/deploy/heroku-git)

After you've done this, you should be able to go to your console and see that the app has been successfully deployed and built.

![heroku dashboard](images/heroku_dash_after.png)

#### Step 8: Test

https://mis407-demo.herokuapp.com/
