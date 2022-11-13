from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, uid):
        """получение одного"""
        return self.dao.get_one(uid)

    def get_all(self, filters):
        """получение всех"""
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()

        return movies

    def create(self, movie_d):
        """Метод пост"""
        return self.dao.create(movie_d)

    def update(self, movie_d):
        """Метод пут"""
        self.dao.update(movie_d)
        return self.dao

    def delete(self, uid):
        """Метод удаления"""
        self.dao.delete(uid)

