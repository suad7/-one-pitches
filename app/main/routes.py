from flask import render_template, request, Blueprint
from app.models import Pitch

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    pitches = Pitch.query.order_by(Pitch.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', pitches = pitches)

