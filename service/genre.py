from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, uid):
        """получение одного"""
        return self.dao.get_one(uid)

    def get_all(self):
        """получение всех"""
        return self.dao.get_all()

    def create(self, genre_d):
        """Метод пост"""
        return self.dao.create(genre_d)

    def update(self, genre_d):
        """Метод пост"""
        self.dao.update(genre_d)
        return self.dao

    def delete(self, uid):
        """Метод пут"""
        self.dao.delete(uid)