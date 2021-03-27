from flask import flash, redirect, url_for, render_template

from messageboard import app, db
from messageboard.models import Message
from messageboard.forms import MessageForm

@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('你的留言已经被发送')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)