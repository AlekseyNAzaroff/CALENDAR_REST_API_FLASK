from typing import List

import storage
import model


class DBExceptions(Exception):
    pass


class EventDB:
    def __init__(self):
        self._storage = storage.LocalStorage()

    def create(self, event: model.Event) -> str:
        try:
            return self._storage.create(event)
        except DBExceptions:
            raise DBExceptions('failed CREATE operation')

    def get_list(self) -> List[model.Event]:
        try:
            return self._storage.get_list()
        except DBExceptions:
            raise DBExceptions('failed GET_LIST operation')

    def read(self, _id: str) -> model.Event:
        try:
            return self._storage.read(_id)
        except DBExceptions:
            raise DBExceptions('failed READ operation')

    def update(self, _id: str, event: model.Event):
        try:
            return self._storage.update(_id, event)
        except DBExceptions:
            raise DBExceptions('failed UPDATE operation')

    def delete(self, _id: str):
        try:
            return self._storage.delete(_id)
        except DBExceptions:
            raise DBExceptions('failed DELETE operation')
