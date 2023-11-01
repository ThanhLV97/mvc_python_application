from extensions import db


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get(self, idx: int):
        return self.model.query.get(idx)

    def get_all(self):
        return self.model.query.all()

    def create(self, data):
        model = self.model(**data)
        db.session.add(model)
        db.session.commit()
        return model

    def update(self, model, data):
        for key, value in data.items():
            setattr(model, key, value)
        db.session.commit()
        return model

    def delete(self, model):
        db.session.delete(model)
        db.session.commit()
        return True
