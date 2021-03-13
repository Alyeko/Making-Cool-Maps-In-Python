from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def the_map():
    return render_template('the_map.html')

if __name__ == '__main__':
    app.run(debug=True)
