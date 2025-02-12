from flask import Flask, render_template, request, make_response
import db

app = Flask(__name__)

# This function will run after every request.
@app.after_request
def set_cookie(response):
    # Set a cookie named 'mycookie' with the value 'cookievalue'
    response.set_cookie('superSecretCookies', 'THIS WILL LOG YOU IN')
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    # If the request is a POST request then add a comment to the DB
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    # Get the query from the url parameter, e.g. localhost:5000/?q=something
    query = request.args.get('q')

    # Render the template using the query and the comment.
    return render_template('index.jinja', comments=db.get_comments(query), query=query)

if __name__ == "__main__":
    app.run(debug=True)
