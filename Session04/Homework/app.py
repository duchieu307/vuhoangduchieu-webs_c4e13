from flask import Flask, render_template
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

if __name__ == '__main__':
  app.run(debug=True)
