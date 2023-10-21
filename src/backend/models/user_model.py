from extensions import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # TODO Add more field about user
    # TODO Add audit fields

    # Relationship
    roles = db.relationship("Role", secondary="user_roles", back_populates="users")

    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):
        return {"id": self.id, "name": self.username, "email": self.email}

    def has_role(self, role):
        return bool(
            Role.query
            .join(Role.users)
            .filter(User.id == self.id)
            .filter(Role.slug == role)
            .count() == 1
        )


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(36), nullable=False)
    slug = db.Column(db.String(36), nullable=False, unique=True)

    # Relationship
    users = db.relationship("User", secondary="user_roles", back_populates="roles")


class UserRole(db.Model):
    __tablename__ = "user_roles"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), primary_key=True)
