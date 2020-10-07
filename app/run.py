import os
from eve import Eve

app = Eve(__name__, settings=os.path.abspath('settings.py'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
