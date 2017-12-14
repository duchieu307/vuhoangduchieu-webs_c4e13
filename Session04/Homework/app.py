from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "duchieu307"

mlab.connect()

class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

# truyentranh = Item(
#     title= "OnePiece",
#     image = "http://4.bp.blogspot.com/-hZ--4wROYF4/U9XUAM3Y1DI/AAAAAAAJGGo/lby5C6mUE9c/s0/bt3916-Volume_41.jpg",
#     description = "Truyen nay tam duoc",
#     price = 5000,
# )
# truyentranh.save()

@app.route('/')
def index():
    data = Item.objects()
    return render_template('index.html', items = data)

@app.route('/themitem', methods=['GET', 'POST'])
def themitem():
    if request.method == "GET":
        return render_template('themitem.html')
    elif request.method == "POST" :
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']
        truyentranh = Item(title=title, image=image, description=description, price=price)
        truyentranh.save()

        return "ahihi"

@app.route("/admin")
def admin():
    data = Item.objects()
    return render_template('admin.html', items = data)

@app.route("/suaitem/<item_id>", methods = ["GET", "POST"])
def edit(item_id):
    data = Item.objects().with_id(item_id)
    if request.method == "GET":
        return render_template("suaitem.html", item=data )
    elif request.method == "POST":
        form = request.form
        title = form['title']
        description = form['description']
        image = form['image']
        price = form['price']

        data.update(title=title, description=description, image=image, price=price)

        flash("Duoc roi anh oi")

        return render_template('suaitem.html', item=Item.objects().with_id(item_id))

@app.route("/xoaitem/<item_id>", methods =[ "GET", "POST"] )
def xoa(item_id):
    data = Item.objects().with_id(item_id)
    return render_template("xoaitem.html", item=data )

@app.route("/block/<item_id>", methods =[ "GET", "POST"] )
def xoaitem(item_id):
    data = Item.objects().with_id(item_id)
    if request.method == "GET":
        return render_template("xoa.html", item=data )
    elif request.method == "POST":
        data.delete()
        flash("Duoc roi anh oi")
        return render_template('admin.html', items = data)




if __name__ == '__main__':
  app.run(debug=True)
