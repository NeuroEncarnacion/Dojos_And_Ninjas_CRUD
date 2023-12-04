from flask_app import app
from flask import Flask, request, render_template, redirect, session, flash
from flask_app.models import m_dojo, m_ninja

@app.route('/ninja')
def ninja():
    dojos = m_dojo.Dojo.get_all()
    return render_template('create_ninja.html', dojos = dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    m_ninja.Ninja.save(request.form)
    return redirect('/dojos')