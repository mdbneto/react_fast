import uuid

from pydantic import EmailStr
from sqlalchemy import SQLColumnExpression
from sqlmodel import Field, Relationship, SQLModel


class UserRoleLink(SQLModel, table=True):
    user_id: uuid.UUID | None = Field(default=None, foreign_key="user.id", primary_key=True)
    role_id: uuid.UUID | None = Field(default=None, foreign_key="role.id", primary_key=True)


# User
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    full_name: str | None = Field(default=None, max_length=255)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str

    roles: list["Role"] = Relationship(back_populates="users", link_model=UserRoleLink)


# Roles
class RoleBase(SQLModel):
    name: str = Field(unique=True, index=True, min_length=3, max_length=255)
    description: str | None = Field(default=None)


class Role(RoleBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    users: list["User"] = Relationship(back_populates="roles", link_model=UserRoleLink)

