from sqlalchemy import Column, Integer, String, func, Table, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


contact_m2m_group = Table(
    "contact_m2m_group",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("contact_id", Integer, ForeignKey("contacts.id", ondelete="Cascade")),
    Column("group_id", Integer, ForeignKey("groups.id", ondelete="Cascade")),
)


class Contact(Base):    
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(18), nullable=False, unique=True)
    email = Column(String(255), unique=True, nullable=True, default=None)
    birthday = Column(Date)
    job = Column(String(255))
    avatar = Column(String(255), default="https://res.cloudinary.com/diqkjtgls/image/upload/c_fill,w_250/v1680233623/ContactsApp/default.jpg")
    created_at = Column(DateTime, default=func.now())
    groups = relationship("Group", secondary=contact_m2m_group, backref="contacts")
    user_id = Column(ForeignKey("users.id", ondelete="Cascade"), default=None)
    user = relationship("User", backref="contacts")
    
    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["groups"] = self.groups
        return attributes
    
    
class Group(Base):
    __tablename__ = "groups"
    __table_args__ = (
        UniqueConstraint("name", "user_id", name="unique_group_user"),
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    user_id = Column(ForeignKey("users.id", ondelete="Cascade"), default=None)
    user = relationship("User", backref="groups")


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50), unique=True)
    phone = Column(String(18))
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    birthday = Column(Date)
    job = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    avatar = Column(String(255), default="https://res.cloudinary.com/diqkjtgls/image/upload/c_fill,w_250/v1680233623/ContactsApp/default.jpg")
    refresh_token = Column(String(255))
    role_id = Column(ForeignKey("roles.id", ondelete="CASCADE"), default=None)
    role = relationship("Role", backref="users")
    confirmed = Column(Boolean, default=False)
    
    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["role"] = self.role
        return attributes