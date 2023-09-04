from typing import List
from flask import request

import model
import db

TITLE_LIMIT = 30
TEXT_LIMIT = 200
DATES = []


def check_format_data(date):
    flag = False
    if len(date) == 10:
        if date[4] == '-' and date[7] == '-':
            if date.replace('-', '').isdigit():
                flag = True
    return flag


def check_date():
    event = request.get_data().decode('utf-8').split('|')
    date = event[0]
    flag = check_format_data(date)
    if flag:
        if date not in DATES:
            DATES.append(date)
            return True


class LogicException(Exception):
    pass


class EventLogic:
    def __init__(self):
        self._event_db = db.EventDB()

    @staticmethod
    def _validate_event(event: model.Event):
        if event is None:
            raise LogicException('Event is None')
        if event.date is None:
            raise LogicException('Date error')
        if event.title is None or len(event.title) > TITLE_LIMIT:
            raise LogicException('Title limit error')
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException('Text limit error')
        if not check_date():
            raise LogicException(f'Date format: yyyy-mm-dd. No more than one '
                                 f'entry per day is possible.')

    def create(self, event: model.Event) -> str:
        self._validate_event(event)
        try:
            return self._event_db.create(event)
        except Exception as ex:
            raise LogicException(f'Failed CREATE {ex}')

    def get_list(self) -> List[model.Event]:
        try:
            return self._event_db.get_list()
        except Exception as ex:
            raise LogicException(f'Failed GET LIST {ex}')

    def read(self, _id: str) -> model.Event:
        try:
            return self._event_db.read(_id)
        except Exception as ex:
            raise LogicException(f'Failed READ {ex}')

    def update(self, _id: str, event: model.Event):
        try:
            self._event_db.update(_id, event)
        except Exception as ex:
            raise LogicException(f'Failed UPDATE {ex}')

    def delete(self, _id: str):
        try:
            return self._event_db.delete(_id)
        except Exception as ex:
            raise LogicException(f'Failed DELETE {ex}')
