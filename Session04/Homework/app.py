from flask import Flask, render_template, request
import mlab
from mongoengine import *

app = Flask(__name__)

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


if __name__ == '__main__':
  app.run(debug=True)
