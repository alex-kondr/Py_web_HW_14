from typing import List, Type

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User, Group
from src.schemas.groups import GroupModel, GroupResponse, GroupUpdate
from src.repository import groups as repository_groups
from src.services.auth import auth_service

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/", response_model=List[GroupResponse],
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_groups(skip: int = 0, limit: int = 9,
                      db: Session = Depends(get_db),
                      current_user: User = Depends(auth_service.get_current_user)) -> List[Type[Group]]:

    """
    The read_groups function returns a list of groups.

    :param skip: int: Skip the first n groups
    :param limit: int: Limit the number of groups returned
    :param db: Session: Pass the database session to the repository layer
    :param current_user: User: Get the current user
    :return: A list of groups
    """
    groups = await repository_groups.get_groups(skip, limit, db)
    return groups


@router.get("/{group_id}", response_model=GroupResponse,
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_group(group_id: int,
                     db: Session = Depends(get_db),
                     current_user: User = Depends(auth_service.get_current_user)) -> Type[Group]:
    """
    The read_group function will return a group with the given ID.

    :param group_id: int: Get the group from the database
    :param db: Session: Get the database session
    :param current_user: User: Check if the user is a member of the group
    :return: A group
    """
    group = await repository_groups.get_group(group_id, db)
    if group is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    return group


@router.post("/", response_model=GroupResponse, status_code=status.HTTP_201_CREATED)
async def create_group(body: GroupModel,
                       db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)) -> Group:
    if current_user.role.name == "admin" or current_user.role.name == "moderator":
        return await repository_groups.create_group(body, current_user, db)
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Does not have access")


@router.put("/{group_id}", response_model=GroupResponse)
async def update_group(body: GroupUpdate,
                       group_id: int,
                       db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)) -> Group:
    """
    The update_group function updates a group in the database.

    :param body: GroupUpdate: Update the group
    :param group_id: int: Find the group to be deleted
    :param db: Session: Get the database session
    :param current_user: User: Check if the user is an admin or moderator
    :return: A group object
    """
    if not (current_user.role.name == "admin" or current_user.role.name == "moderator"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Does not have access")

    group = await repository_groups.update_group(group_id, body, current_user, db)
    if group is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    return group


@router.delete("/{group_id}", response_model=GroupResponse, status_code=status.HTTP_202_ACCEPTED)
async def remove_group(group_id: int,
                       db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)) -> Group:
    """
    The remove_group function removes a group from the database.
        It requires an admin or moderator to be logged in, and it takes a group_id as input.
        If the user is not an admin or moderator, they will receive a 403 error code.
        If there is no such group with that id, they will receive a 404 error code.

    :param group_id: int: Find the group to be updated
    :param db: Session: Get a database session
    :param current_user: User: Get the user that is currently logged in
    :return: The removed group
    """
    if not (current_user.role.name == "admin" or current_user.role.name == "moderator"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Does not have access")

    group = await repository_groups.remove_group(group_id, current_user, db)
    if group is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    return group
