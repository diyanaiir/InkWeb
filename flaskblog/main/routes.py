
from flask import render_template,request,Blueprint
from flaskblog.models import Post

main= Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page',1,type=int) #to grab the page we want
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page= page, per_page=5)
    return render_template('home.html',posts1=posts) #no title is passed hence default used
 
@main.route("/about")
def about():
    return render_template('about.html', title= 'This is About Title') #title is passed
 