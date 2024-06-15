from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is the root page! Go to /download to get the file."

@app.route('/download')
def download():
    return send_from_directory('/mnt/data', 'xiao_test.zip')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
