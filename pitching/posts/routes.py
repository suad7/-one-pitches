from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Pitch
from flaskblog.posts.forms import PostForm


posts = Blueprint('posts',__name__)
