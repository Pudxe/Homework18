from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, uid):
        """получение одного"""
        return self.dao.get_one(uid)

    def get_all(self):
        """получение всех"""
        return self.dao.get_all()

    def create(self, director_d):
        """Метод пост"""
        return self.dao.create(director_d)

    def update(self, director_d):
        """Метод пут"""
        self.dao.update(director_d)
        return self.dao

    def delete(self, uid):
        """Метод удаления"""
        self.dao.delete(uid)
