#!/usr/bin/env python
from flaskexample import app
app.run(host='0.0.0.0',port=5002,threaded=True,debug=True)
