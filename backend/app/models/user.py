from sqlmodel import Field, Relationship, SQLModel


class UserRoleLink(SQLModel, table=True):
    user_id: int | None = Field(default=None, foreign_key="user.id", primary_key=True)
    role_id: int | None = Field(default=None, foreign_key="role.id", primary_key=True)


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str = Field(index=True)
    hashed_password: str

    roles: list["Role"] = Relationship(back_populates="users", link_model=UserRoleLink)


class Role(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str | None

    users: list["User"] = Relationship(back_populates="roles", link_model=UserRoleLink)

