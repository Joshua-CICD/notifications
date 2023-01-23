from flask import Flask

app = Flask(__name__)

# Create a health check endpoint
@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
