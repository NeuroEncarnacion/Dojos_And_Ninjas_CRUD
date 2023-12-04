from flask_app import app
from flask import Flask, request, render_template, redirect, session, flash
from flask_app.models.m_dojo import Dojo


@app.route("/")
def dashboard():
    return redirect("/dojos")


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)


@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id" : id
    }
    return render_template('show_dojo.html', dojo=Dojo.get_one_with_ninjas(data))