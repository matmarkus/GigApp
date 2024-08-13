from defs_main import menu
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session
from defs_users import register, save_users, load_users, users, login, show_logged_in_user, logout
import json
import os
import config
import defs_gigs

load_users()

menu()

