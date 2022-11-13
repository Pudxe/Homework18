from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        """получение одного"""
        return self.session.query(Movie).get(uid)

    def get_all(self):
        """Получение всех"""
        return self.session.query(Movie).all()

    def get_by_director_id(self, value):
        """Получение по директор айди"""
        return self.session.query(Movie).filter(Movie.director_id == value).all()

    def get_by_genre_id(self, value):
        """получение по жанр айди"""
        return self.session.query(Movie).filter(Movie.genre_id == value).all()

    def get_by_year(self, value):
        """Получение по году"""
        return self.session.query(Movie).filter(Movie.year == value).all()

    def create(self, movie_d):
        """Метод пост"""
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, movie_d):
        """Метод пут"""
        movie = self.get_one(movie_d.get("id"))

        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def delete(self, uid):
        """Метод удаления"""
        movie = self.get_one(uid)

        self.session.delete(movie)
        self.session.commit()