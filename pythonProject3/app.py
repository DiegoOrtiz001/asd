from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tu_archivo_html.html')

if __name__ == '__main__':
    app.run(debug=True)
