from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Pitch
from flaskblog.posts.forms import PostForm


posts = Blueprint('posts',__name__)

@posts.route("/post/new", methods= ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, content = form.content.data, author = current_user, category = form.category.data)
        db.session.add(pitch)
        db.session.commit()
        flash('Your post has been created', 'successfully ')
        return redirect(url_for('main.home'))
    return render_template('create_post.html',title = 'New Post', form = form, legend = 'New Post')

@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Pitch.query.get_or_404(post_id)
    return render_template('post.html', title = post.title, post = post)


