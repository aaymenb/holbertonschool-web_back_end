#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel()


class Config:
    """Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """Get best matching locale from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render index page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
