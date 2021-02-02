from app import app,admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models.customers import CustomerModel
from flask_sqlalchemy import SQLAlchemy



db=SQLAlchemy()
db.init_app(app)
admin.add_view(ModelView(CustomerModel,db.session))
