## Installation

### What is a Python venv?

A venv or virtual environment is a system that allows you to seperate out what Python libraries are installed on your computer when accessing different directories/folders. In particular the `venv` system in Python allows you to create a "virtual environment" inside a directory and then install libraries ONLY within that folder.

This means that if you have lots of Python projects on your computer, you can create different environments and install different libraries in each and every one of these projects. This avoids problems that may arise if you are using the same library in different projects but that are on different versions.

### How to create and activate the venv for this project

To create and activate your venv you must simply run the following in your terminal:

```shell
python3 -m venv .venv
source ./.venv/bin/activate
```

You will notice upon running the first command it will create a new folder called `.venv` which is where your virtual environment is actually stored!

The second command will then activate the virtual environment by executing commands that are within in the `.venv/bin/activate` file (go have a look to see what they are if you are interested).

### Installing Dependencies for the project

Now that the venv is setup you now need to install the required libraries or "dependencies" of the project using the following command,

```shell
pip install pipenv --user
pipenv install
```

this will look at the file called `Pipfile` and install the dependencies defined in the file.

Typically this installation is done once only as the virtual environment will store the dependencies in the environment itself.

### Running the application

Now that everything is installed you can simply run the following commmand to start the application

```shell
python3 -m flask --app app run --debug
```

You will now be able to access your website by going to http://127.0.0.1:5000 or https://localhost:5000 on your web browser.

## How this application works

In short this application is a small Python Flask webserver that utilises a templating engine called Jinja2 to serve both backend data and frontend templated html. What does that mean? Read on.

### Backend - Flask Webserver

A webserver is basically a computer that's hosting a website typically on the internet. I say typically because when in development your webserver will be accessible on your browser through https://localhost:5000, notably the `localhost` refers to the fact that the webserver is actually only accessible on your specific local computer (host) and therefore accessing this same URL on your phone or another computer will not result in anything being returned.

More specifically a webserver will typically host either static files and/or allow you to trigger code to be run on the host machine. In our case our Flask website is actually doing both!

You can see this in the main `app.py` file,

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    query = request.args.get('q')
    return render_template('index.jinja', comments=db.get_comments(query), query=query)
```

This function `index()` has a special line above it called a decorator. Importantly this decorator says that if you connect to the webserver with just a `/` at the end of the url, https://localhost:5000/ (note that trailing slashes are usually optional), then it will trigger this function to run.

It also says that it accepts two HTTP methods `GET` and `POST`. What this means is that you can either attempt to "Get" something from that URL or "POST" to it (send it some data).

The function then checks if the method chosen is `POST` and if so it will add the given comment to the database and if not it will continue on return the result of a function called `render_template`. This brings us to Jinja2 templating.

### Frontend - Jinja2 Templating

For this webserver we chose to use the Jinja2 templating. Jinja2 is a very simple library that allows you to use python logic inside of HTML and then render the result of that logic.

In our case when we call the function:

```python
render_template('index.jinja', comments=db.get_comments(query), query=query)
```

We are triggering the Jinja2 templating engine to render the file `index.jinja` using the variables `comments` and `query`. If we look at the file itself we notice it looks a bit like html but with some use of brackets. Take this part for example,

```jinja
{% if comments %}
    <form method="GET">
        <div class="input-box">
            <input
            type="text"
            name="q"
            placeholder="Input search query here... "
            autocomplete="off"
            />
            <input type="submit" value="search" />
        </div>
    </form>
{% endif %}
```

In this template we see that we have an HTML `<form>` element surrounded by what looks to be an if statement!

You see when we call the `render_template()` function our `comments` are injected into this file and used to evaluate the statements in the curly braces.

For example if I gave the function `comments=[]` this would mean `{% if comments %}` evaluates to `false` as `comments` is an empty list. As a result the entire block of HTML contained within the if statement is not rendered.

This effectively allows you to take normal static (non-changing) html and make it render differently based on data stored on the server. This is usually referred to as Server Side Rendering (SSR)!

### Database - Its not really a database...

So to tie all of this together, if you head on into the `db.py` file, you will notice our database... is just an array

```python
db = []
```

In theory you could use a normal SQL database, but just to make this nice and quick we are just using an array. Nothing fancy :)
