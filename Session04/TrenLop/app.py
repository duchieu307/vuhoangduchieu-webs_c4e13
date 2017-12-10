from flask import Flask, render_template, request
import mlab
from mongoengine import *

app = Flask(__name__)

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

if __name__ == '__main__':
  app.run(debug=True)
