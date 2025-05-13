import time

from flask import *

from AI.Gigachat import NeuroConnectGigachat
from controllers.helpers.statuses import Statuses
from data_objects.add_post_data import AddPostData
from data_objects.message import Message
from data_objects.user import User
from database.data_verifier import DataVerifier
from database.user_service import UserService


def init_adding_controller(flask_app: Flask):
    @flask_app.post('/add_user')
    def add_new_user():
        user = User(request.json)

        is_correct, error = DataVerifier.verify_user_data(user)
        if not is_correct:
            return error, Statuses.BAD_REQUEST

        service = UserService()

        if service.get_users_with_this_name(user.name):
            return f'User with name {user.name} already exists', Statuses.BAD_REQUEST

        service.add_user(user)
        return f'User with name {user.name} was added', Statuses.CREATED

    @flask_app.post('/add_post')
    def add_post():
        request.json['topic'] = NeuroConnectGigachat().get_topic(request.json["post_text"])
        print(f"POSTED: {time.time()}")
        add_post_data = AddPostData(request.json)

        is_correct = DataVerifier.verify_post_data(add_post_data)
        if not is_correct:
            return "auth error", Statuses.BAD_REQUEST

        UserService().add_post(add_post_data.post)
        return f'Post created', Statuses.CREATED

    @flask_app.post('/add_message')
    def add_message():
        msg = Message(request.json)

        is_correct, error = DataVerifier.verify_message(msg)
        if not is_correct:
            return error, Statuses.BAD_REQUEST

        UserService().add_message(msg)
        return f'Message created', Statuses.CREATED

    @flask_app.post('/add_image')
    def add_image():
        img = request.files.get('image')

        is_correct, error = DataVerifier.verify_image(img)
        if not is_correct:
            return error, Statuses.BAD_REQUEST

        img_id = UserService().add_image(img)
        return f'Image created with ID={img_id}', Statuses.CREATED
