from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models import Clone
from app.forms import CloneForm
import re

bp = Blueprint('clones', __name__, url_prefix = '/clones')

@bp.route('/<string:username>')
def clone(username):
    clone = Clone.objects.get_or_404(username=username)
    return render_template('clones/member.jade', clone=clone)

@bp.route('/', methods=['GET', 'POST'])
def clones():
    form = CloneForm()
    if form.validate_on_submit():
        username = form.username.data
        clone, was_created = Clone.objects.get_or_create(username=username)
        clone.imprint()
        clone.save()
        return redirect(url_for('clones.clone', username=username))
    return render_template('clones/create.jade', form=form)


@bp.app_template_filter()
def highlight_pattern(pattern):
    """
    A template filter for highlighting
    fill-in spots in patterns.

    Example usage (in `pyjade`)::

        div= pattern|highlight_pattern
    """
    p = re.compile(r'\{\{\s*([A-Za-z]+)\s*\}\}')
    tags = p.findall(pattern)
    for tag in tags:
        pattern = re.sub(r'(\{\{\s*' + re.escape(tag) + r'\s*\}\})', '<span style="color:#ddd;">'+tag+'</span>', pattern, 1)
    return pattern
