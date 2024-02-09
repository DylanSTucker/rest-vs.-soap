#Dylan Tucker, dst833, 11235055
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
import sys

app = Flask(__name__)
api = Api(app)
sys.set_int_max_str_digits(0)

class server(Resource):
    def post(self, n):
        num1 = 0
        num2 = 1
        nextNum = 1
        count = 1
        while count <= n:
            count += 1
            num1 = num2
            num2 = nextNum
            nextNum = num1 + num2
        return jsonify({"fibonacci": nextNum})


# adding the defined resources along with their corresponding urls 
api.add_resource(server, '/server/<int:n>')

# driver function 
if __name__ == "__main__":
    app.run(debug = True)