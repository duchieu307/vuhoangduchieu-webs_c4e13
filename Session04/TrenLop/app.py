from flask import Flask, render_template
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
# tv = Item(title = "Catset Cu",
#     image= "https://cdn1.tgdd.vn/Files/2015/09/26/708646/bi-kip-chon-mua-tivi-cu-1.jpg",
#     description = "Re ma",
#     price = 3000000,
# )
#
# tv.save()
#
# items = Item.objects()
# for item in items:
#     print(item.title)
#     print(item.price)


@app.route('/')
def index():
    return render_template('index.html', title="TV cu",
        image='https://cdn1.tgdd.vn/Files/2015/09/26/708646/bi-kip-chon-mua-tivi-cu-1.jpg'

        )
@app.route('/list')
def title_list():
    return render_template('title_for.html', titles=['Tv Cu', 'Radio Cu', 'DVD Cu'])

@app.route('/object')
def object():
    x = {
        "title": "TV Cu Gia Cao",
        "image": "https://cdn1.tgdd.vn/Files/2015/09/26/708646/bi-kip-chon-mua-tivi-cu-1.jpg",
        "description": "Vi TV Cu Nen Gia Cao",
    }
    return render_template("object.html", item = x )

@app.route('/object-list')
def object_list():
    # data = [
    #     {
    #         "title" : "Tv Cu",
    #         "image" : "http://via.placeholder.com/200x300",
    #         "description" : "TV Dat Vicecarlone"
    #     },
    #     {
    #         "title" : "Tu Lanh Cu",
    #         "image" : "http://via.placeholder.com/200x300",
    #         "description" : "Tu Lanh Dat Vicecarlone"
    #     },
    #     {
    #         "title" : "Den Cu",
    #         "image" : "http://via.placeholder.com/200x300",
    #         "description" : "Den Dat Vicecarlone"
    #     },
    # ]

    data = Item.objects()
    return render_template("object-list.html", items = data )

if __name__ == '__main__':
  app.run(debug=True)
