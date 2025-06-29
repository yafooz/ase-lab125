from flask import Flask, make_response,request,jsonify
import random,requests

app=Flask(__name__)

@app.route("/")
def Hello():
    return "hello flask"

@app.route("/add")
def add():
    a=request.args.get('a',type=float)
    b=request.args.get('b',type=float)
    if a and b :
        return make_response(jsonify(s=a+b),200)
    else:
         return make_response (jsonify("invalide inputs .."),400)
    
@app.route("/div")
def div():
    a=request.args.get('a',type=float)
    b=request.args.get('b',type=float)
    if a and b:
        if b!=0:
            return make_response(jsonify(s=a/b),200)
    else:
        return make_response(jsonify("invalide inputs ..."),400)    
# @app.route("/div")
# def div():
#     a=request.args.get('a',type=float)
#     b=request.args.get('a',type=float)
#     if a and b :
#         return make_response(jsonify(s=a/b),200)
#     else:
#         return make_response(jsonify("inavlide inputs ..."),400)
    


# @app.route("/mod")
# def mode():
#         a=request.args.get('a',type=float)
#         b=request.args.get('b',type=float)
#         if a and b:
#             return make_response(jsonify(s=a%b),200)
#         else:
#             return make_response(jsonify("invalide inputs ..",400))
        
# @app.route("/mul")
# def mul():
#         a=request.args.get('a',type=float)
#         b=request.args.get('b',type=float)
#         if a and b:
#             return make_response(jsonify(s=a*b),200)
#         else:
#             return make_response(jsonify("bad request .."),400)
        
# @app.route("/rand")
# def rand():
#     a=request.args.get('a',type=float)
#     b=int(a)
#     s=random.randint(1,b)
#     if a :
#         return make_response(jsonify(result=s),200)
#     else:
#         make_response(jsonify("bad request",400))

# @app.route("/sub")
# def sub():
#      a=request.args.get('a',type=float)
#      b=request.args.get('b',type=float)
#      if a and b:
#           return make_response(jsonify(s=a-b),200)
#      else:
#           return make_response(jsonify("bad request "),400)
     
# @app.route("/factorial")
# def factorial():
#      a=request.args.get("a",type=int)
#      fact=1
#      if a :
#         for i in range(fact,a+1):
#              fact=fact*i
#         return  make_response(jsonify( factorial= fact),200) 
         
#      else:
#        return make_response(jsonify("bad request"),400)
     
#      @app.route("/factorial2",methods="post")
#      def factorial2():
        
#          a=requests.post('a',)
         