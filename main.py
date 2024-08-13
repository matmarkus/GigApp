from defs_base import menu
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session
from defs_users import register, users, save_users, load_users, login
import json
import os


load_users()

menu()
