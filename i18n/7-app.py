#!/usr/bin/env python3
"""Infer appropriate time zone"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel()

users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


class Config:
    """Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """Return user dictionary or None"""
    login_as = request.args.get('login_as')
    if login_as is None:
        return None
    try:
        return users.get(int(login_as))
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """Set user in global request context"""
    g.user = get_user()


def get_locale():
    """Select locale based on URL, user settings or request headers"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale

    return app.config['BABEL_DEFAULT_LOCALE']


def get_timezone():
    """Select timezone based on URL, user settings or default"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


babel.init_app(app,
        locale_selector=get_locale,
        timezone_selector=get_timezone)


@app.route('/')
def index():
    """Render index page"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
