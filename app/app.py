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
      


@app.route("/mod")
def mode():
        a=request.args.get('a',type=float)
        b=request.args.get('b',type=float)
        if a and b:
            return make_response(jsonify(s=a%b),200)
        else:
            return make_response(jsonify("invalide inputs ..",400))
        
@app.route("/mul")
def mul():
        a=request.args.get('a',type=float)
        b=request.args.get('b',type=float)
        if a and b:
            return make_response(jsonify(s=a*b),200)
        else:
            return make_response(jsonify("bad request .."),400)
        
@app.route("/rand")
def rand():
    a=request.args.get('a',type=float)
    b=int(a)
    s=random.randint(1,b)
    if a :
        return make_response(jsonify(result=s),200)
    else:
        make_response(jsonify("bad request",400))

@app.route("/sub")
def sub():
     a=request.args.get('a',type=float)
     b=request.args.get('b',type=float)
     if a and b:
          return make_response(jsonify(s=a-b),200)
     else:
          return make_response(jsonify("bad request "),400)
     
@app.route("/factorial")
def factorial():
     a=request.args.get("a",type=int)
     fact=1
     if a :
        for i in range(fact,a+1):
             fact=fact*i
        return  make_response(jsonify( factorial= fact),200) 
         
     else:
       return make_response(jsonify("bad request"),400)
     


@app.route("/upper")
def upper():
    text=request.args.get('text',type=str)
    if text:
        return make_response(jsonify(text=text.upper()),200)
    else:
        return make_response(jsonify("bad request"),400)

@app.route("/lower")
def lower():
    text=request.args.get('text',type=str)
    if text:
        return make_response(jsonify(text=text.lower()),200)
    else:
        return make_response(jsonify("bad request"),400)
    
@app.route("/concat")
def concat():
    text1=request.args.get('text1',type=str)
    text2=request.args.get('text2',type=str)
    if text1 and text2:
        return make_response(jsonify(text=text1+text2),200)
    else:
        return make_response(jsonify("bad request"),400)

@app.route("/reduce")
def reduce(op,lst):
    if op == 'add':
        result = sum(lst)
    elif op == 'mul':
        result = 1
        for num in lst:
            result *= num

    elif op == 'div':
        for num in lst:
            if num == 0:
                return make_response(jsonify("Division by zero error"), 400)
            else:
                result = lst[0]
                for num in lst[1:]:
                    result /= num
            result /= num

    elif op == 'mod':
        for num in lst:
            result=num
            result  = result % num

    else:
        return make_response(jsonify("Invalid operation"), 400)
    
    return make_response(jsonify(s=result), 200)



        

if __name__ == '__main__':
    app.run(debug=True)
    