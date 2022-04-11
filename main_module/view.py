# Importations
import os

os.environ['KMP_WARNINGS'] = 'off'
import plotly.graph_objects as go
import plotly
import numpy as np
import pandas as pd
from flask import Flask, request, redirect, abort, render_template, session, flash
import json

from main_module.static.utils import *
from main_module.static.classes import *

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template('home.html')

