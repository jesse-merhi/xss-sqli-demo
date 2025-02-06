from flask import Flask, render_template, request, make_response
import db

app = Flask(__name__)
app.config['TITLE'] = 'Comments or somethn'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    query = request.args.get('q')
    return render_template('index.jinja', comments=db.get_comments(query), query=query)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5123)
