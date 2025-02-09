from flask import Flask, render_template, request, make_response
import db


# Create a new "Flask" object and assign it to app. 
# (This object contains all the logic for our webserver to run)
app = Flask(__name__) 


# Add a new route to our webserver at `/` that accepts GET and POST requests.
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the request is a POST request then add a comment to the DB
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    # Get the query from the url parameter, e.g. localhost:5000/?q=something
    query = request.args.get('q')

    # Render the template using the query and the comment.
    return render_template('index.jinja', comments=db.get_comments(query), query=query)
