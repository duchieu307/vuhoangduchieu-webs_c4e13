from flask import *
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

class User(Document):
    username = StringField()
    password = StringField()

user = User(username="thao", password = "thaoadmin")

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
    loggedin = session.get("loggedin", False)
    return render_template("index.html", items = items, loggedin = loggedin )

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
    if session.get('loggedin', False)  :
        items = Item.objects()
        return render_template('admin.html', items = items)
    else :
        return redirect(url_for('login'))

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

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        user  = User.objects(username=username).first()
        if user is None :
            return "Username khong ton tai"
        elif user.password != password :
            return "Sai mat khau"
        else :
            session['loggedin'] = True
            return redirect("/admin")

@app.route("/logout")
def logout():
    session["loggedin"] = False
    return redirect(url_for('login'))



if __name__ == '__main__':
  app.run(debug=True)
