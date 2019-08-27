import sys
sys.path.insert(0, "/var/www/html/basic_json_api")
from app import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
