from flask import Flask, request
from flask_restful import Resource, Api
import threading
import sys
import os
import shutil
import json
import pickle
from requests import put, get, delete, post
import discovery
import time

# GLOBALS #####################################################################
discovery.discoverable(service_name="alma python server")
HOSTNAME = '0.0.0.0'
PORT = 5003 

app = Flask(__name__)
api = Api(app)
# END GLOBALS #################################################################

# API Tasks ###################################################################
class HelloWorld(Resource):
    """
    Class inherits from Resource
    """
    def get(self):
        return {'get':'get hello world'}
    def put(self):
        return {'put':'put hello world'}
    def post(self):
        return {'post':'post hello world'}

todos = {}
class TodoSimple(Resource):
    """ Note that the get request here will conflict with Todo1's get endpoint.
    Whichever endpoint is explicitly defined (i.e. todo1) will take
    preceidence.  However, if that endpoint has an unsupported request type
    (i.e. put in this case) then the 'argument' style endpoint will take
    precidence.
    """
    def get(self, todo_id):
        return {'TodoSimple':{todo_id: todos[todo_id]}}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        print(todos)
        return {'TodoSimple':{todo_id: todos[todo_id]}}

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'Todo1':{'task': 'Hello world'}}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'Todo2':{'task': 'Hello world'}}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'Todo3':{'task': 'Hello world'}}, 201, {'Etag': 'some-opaque-string'}

# attach an endpoint to a Resource handler
api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(Todo1,'/todo1')
api.add_resource(Todo2,'/todo2')
api.add_resource(Todo3,'/todo3')
# END API Tasks ###############################################################

# TESTS #######################################################################
def run_tests():
    r = get('http://localhost:5003/todo1')
    print('resp {}, status {}'.format(r.text,r.status_code))

    r = get('http://localhost:5003/todo1')
    print('resp {}, status {}'.format(r.text,r.status_code))

    r = get('http://localhost:5003/todo2')
    print('resp {}, status {}'.format(r.text,r.status_code))

    r = get('http://localhost:5003/todo3')
    print('resp {}, status {}'.format(r.text,r.status_code))

    #  test for conflict since we have an endpoint that takes any string ##
    #  note that we have to provide a key which matches the lookup key given in
    #  the TodoSimple handler for put, i.e. data.  ## thus in this case, todo1
    #  + put routes us to TodoSimple, rather than Todo1 because Todo1 doesn't
    #  have a handler for put requests. Then, the TodoSimple endpoint is
    #  triggered with the 'todo1' endpoint, and we parse out the 'data'
    #  argument from the request itself.    
    r = put('http://localhost:5003/todo1', data={'data': 'get the milk'})
    print('resp {}, status {}'.format(r.json(),r.status_code))

###############################################################################

if __name__ == '__main__':

    server_thread = threading.Thread(
        target = app.run,
        kwargs = {
            'debug':False,
            'host':HOSTNAME,
            'port':PORT
            }
        )

    server_thread.start()

    time.sleep(0.5)
    run_tests()
