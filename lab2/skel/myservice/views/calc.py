#calculator.py
from flakon import JsonBlueprint
from flask import Flask, request, jsonify

calculator=JsonBlueprint('calculator', __name__)

#http://127.0.0.1:5000/calc/sum?m=3&n=5
@calculator.route('/calc/sum', methods=['GET'])
def sum():
    m=int(request.args.get('m'))
    n=int(request.args.get('n'))
    result=m
    negative=False
    if(n<0):
        negative=True
        n*=-1
    while n>0:
        if negative:
            result-=1
        else:
            result+=1
        n-=1
    return jsonify({'result':str(result)})

@calculator.route('/calc/div', methods=['GET'])
def divide():
    m=int(request.args.get('m'))
    n=int(request.args.get('n'))
    if n==0:
        raise ZeroDivisionError
    negative=(((m<0) and  not (n<0)) or (not (m<0) and (n<0)))
    i=-1
    m=abs(m)
    n=abs(n)
    while m>=0:
        m-=n
        i+=1
    if negative:
        return jsonify({'result':str(i*-1)})
    else:
        return jsonify({'result':str(i)})