# go to flask 1 14 minutes template inheritance
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# stop cookie interference
app.config['SECRET_KEY'] = 'd9e5d161aea7bdaae66380655b0334a7'
# add a dictionary within a list
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First blogs post content',
        'date_posted': 'March 17, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': '2nd blogs post content',
        'date_posted': 'March 18, 2018'
    },
    {
        'author': 'Jack Doe',
        'title': 'Blog Post 3',
        'content': '3nd blogs post content',
        'date_posted': 'March 121, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='title')


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created For {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('fuck off try again!', 'danger')
    return render_template('login.html',title='register',form=form)
# another way of refreshing browser
if __name__ =='__main__':
    app.run(debug=True)
