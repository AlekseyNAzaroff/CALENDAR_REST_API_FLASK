from typing import List

import model


class StorageException(Exception):
    pass


class LocalStorage:
    def __init__(self):
        self._id_counter = 0
        self._storage = {}

    def create(self, event: model.Event) -> str:
        self._id_counter += 1
        event.id = str(self._id_counter)
        self._storage[event.id] = event
        return event.id

    def get_list(self) -> List[model.Event]:
        return list(self._storage.values())

    def read(self, _id: str):
        if _id not in self._storage:
            raise StorageException(f'ID {_id} not found')
        else:
            return self._storage[_id]

    def update(self, _id: str, event: model.Event):
        if _id not in self._storage:
            raise StorageException(f'ID {_id} not found')
        else:
            event.id = _id
            self._storage[event.id] = event
            return f'ID {_id} update'

    def delete(self, _id: str):
        if _id not in self._storage:
            raise StorageException(f'ID {_id} not found')
        else:
            del self._storage[_id]
