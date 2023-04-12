from typing import List, Type, Optional

from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.database.models import Group, User
from src.schemas.groups import GroupModel, GroupUpdate


async def get_groups(skip: int, limit: int, db: Session) -> List[Type[Group]]:
    """
    The get_groups function returns a list of groups from the database.

    :param skip: int: Skip a certain number of records
    :param limit: int: Limit the number of groups returned
    :param db: Session: Pass the database session to the function
    :return: A list of group objects
    """
    return db.query(Group).offset(skip).limit(limit).all()


async def get_group(group_id: int, db: Session) -> Optional[Group]:
    """
    The get_group function takes in a group_id and a database session,
    and returns the Group object with that id. If no such group exists, it returns None.

    :param group_id: int: Specify the group id of the group that is being queried
    :param db: Session: Pass the database session to the function
    :return: The group object
    """
    return db.query(Group).filter(Group.id == group_id).first()


async def create_group(body: GroupModel, user: User, db: Session) -> Group:
    """
    The create_group function creates a new group in the database.

    :param body: GroupModel: Create a new group
    :param user: User: Get the user id from the token
    :param db: Session: Access the database
    :return: A group object
    """
    group = Group(name=body.name, user=user)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group


async def update_group(group_id: int, body: GroupUpdate, user: User, db: Session) -> Optional[Group]:
    """
    The update_group function updates a group in the database.
        Args:
            group_id (int): The id of the group to update.
            body (GroupUpdate): The updated information for the specified Group object.
            user (User): The User object that is making this request, used to verify ownership of this Group object.

    :param group_id: int: Identify the group to be deleted
    :param body: GroupUpdate: Pass the name of the group to be updated
    :param user: User: Check if the user is authorized to delete a group
    :param db: Session: Access the database
    :return: The updated group object
    """
    group = db.query(Group).filter(and_(Group.id == group_id, Group.user_id == user.id)).first()
    if group:
        group.name = body.name
        db.commit()
    return group


async def remove_group(group_id: int, user: User, db: Session) -> Optional[Group]:
    """
    The remove_group function removes a group from the database.
        Args:
            group_id (int): The id of the group to be removed.
            user (User): The user who owns the group to be removed.
            db (Session): A connection to our database, used for querying and deleting groups.

    :param group_id: int: Identify the group to be removed
    :param user: User: Get the user id of the group owner
    :param db: Session: Access the database
    :return: The group that was removed
    """
    group = db.query(Group).filter(and_(Group.id == group_id, Group.user_id == user.id)).first()
    if group:
        db.delete(group)
        db.commit()
    return group
