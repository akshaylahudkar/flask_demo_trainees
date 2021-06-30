"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template,abort
app = Flask(__name__)

pets = [
            {"index":1,'id': '1.jpg', "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"index":2,"id": '2.jpg', "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"index":3,"id": '3.jpg', "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"index":4,"id": '4.jpg', "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
        ]

@app.route("/details/<index>")
def details(index):
    if int(index) > len(pets) or int(index)<=0:
        abort(404,'No pet found with the given index. ')

    return render_template('details.html',pet=pets[int(index)-1])



@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html",pets=pets)


@app.route("/about")
def about():
    """View function for About Page."""



    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
