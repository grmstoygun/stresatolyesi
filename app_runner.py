from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'

@app.route("/", methods=('GET', 'POST'))
@app.route("/index/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        user_message = request.form['user_message']
        if not user_message:
            flash("Lütfen bizimle sorununuzu paylaşınız.")
        else:
            ## reply = gpt.communicate(user_message)
            return redirect(url_for('reply'))
    return render_template("index.html")

@app.route("/reply/", methods=('GET', 'POST'))
def reply():
    return render_template("reply.html")

if __name__ == "__main__":
    app.run(debug=True)