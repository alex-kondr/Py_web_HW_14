from typing import List, Union

from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.database.models import Group, User
from src.schemas.groups import GroupModel


async def get_groups(skip: int, limit: int, db: Session) -> List[Group]:
    return db.query(Group).offset(skip).limit(limit).all()


async def get_group(group_id: int, db: Session) -> Group:
    return db.query(Group).filter(Group.id == group_id).first()


async def create_group(body: GroupModel, user: User, db: Session) -> Group:
    group = Group(name=body.name, user=user)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group


async def update_group(group_id: int, body: GroupModel, user: User, db: Session) ->  Union[Group, None]:
    group = db.query(Group).filter(and_(Group.id == group_id, Group.user_id == user.id)).first()
    if group:
        group.name = body.name
        db.commit()
    return group


async def remove_group(group_id: int, user: User, db: Session) -> Union[Group, None]:
    group = db.query(Group).filter(and_(Group.id == group_id, Group.user_id == user.id)).first()
    if group:
        db.delete(group)
        db.commit()
    return group