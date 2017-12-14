from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'duchieu307'

# 1 ket noi toi database
mlab.connect()

# 2 design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

# 3 them items
new_item = Item(title = "Dep to ong",
    image= "http://static.baophapluat.vn/Uploaded/nguyenvantung/2014_08_06/gietme-bangoai-baophapluat13_XTVD.jpg",
    description = "Re ma",
    price = 100000,
)
# new_item.save()
#
# items = Item.objects()
# for item in items:
#     print(item.title)
#     print(item.price)



@app.route('/')
def index():
    items = Item.objects()
    return render_template("index.html", items = items )

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == "GET":
        return render_template('add_item.html')
    elif request.method == "POST":
        #1 lay thong tin tu form
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']
        #2 them vao database
        new_item = Item(title=title, image=image, description=description, price=price)
        new_item.save()
        return "Anh di ra di"

@app.route('/admin')
def admin():
    items = Item.objects()
    return render_template('admin.html', items = items)

@app.route("/edit_item/<item_id>", methods = ['GET', 'POST'])
def edit_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == "GET":
        return render_template('edit_item.html', item=item)
    elif request.method == "POST":
        form = request.form
        title = form['title']
        description = form['description']
        image = form['image']
        price = form['price']

        item.update(title=title, description=description, image=image, price=price)

        flash("Duoc roi anh oi ahihi")
        flash("Hello Hello")

        return render_template('edit_item.html', item=Item.objects().with_id(item_id))



if __name__ == '__main__':
  app.run(debug=True)
