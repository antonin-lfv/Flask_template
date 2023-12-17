from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory, current_app
import os

BLP_general = Blueprint('BLP_general', __name__,
                        template_folder='templates',
                        static_folder='static')

@BLP_general.route('/')
def index():
    return render_template('index.html')
