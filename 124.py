from flask import Flask,jsonify,request

app=Flask(__name__)
tasks=[
    {
        'id':1,
        'title':u'Grocery List',
        'description':u'Milk,Cheese,Biscuits,Fruits',
        'done':False
    },
    {
        'id':2,
        'title':u'Decor List',
        'description':u'Candels,Candel holders,Wall mirror',
        'done':False
    }
]
@app.route('/add-data',methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data in json format"
        },400)

    t={
        "id":tasks[-1]["id"]+1,
        "title":request.json['title'],
        "description":request.json.get('description'," "),
        "done":False
    }
    tasks.append(t)

    return jsonify({
            "status":"success",
            "message":"task added successfully"
        })

@app.route("/get-data")
def gettask():
    return jsonify({
        "data":tasks
    })

if (__name__=="__main__"):
    app.run(debug=True)