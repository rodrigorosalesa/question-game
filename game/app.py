import json
import random
import os
import sys
import time
import dash
from dash import html
import logging

from read_data import read_questions
from logger_config import set_up_logger


# G E N E R A L I T I E S  ------------------------------------------
logger = set_up_logger(__name__)
werkzeug_logger = logging.getLogger("werkzeug")
werkzeug_logger.setLevel(logging.EWARNING)

DATA = read_questions("questions.json")



##############################################################
# A P P . C O N F I G U R A T I O N
##############################################################
app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://codepen.io/chriddyp/pen/bWLwgP.css",
    ],
    title="Best E-Board Game Ever",
    )

def layout():
    return [
        
    ]

app.layout = layout


def is_running_locally():
    return "--local" in sys.argv


if __name__ == "__main__":
    if is_running_locally():
        app.run_server(debug=True)