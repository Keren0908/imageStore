from itsdangerous import URLSafeTimeSerializer

from .. import app

ts=URLSafeTimeSerializer(app.config["SECRET_KEY"])
