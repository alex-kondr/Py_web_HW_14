from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User
from src.schemas.groups import GroupModel, GroupResponse, GroupUpdate
from src.repository import groups as repository_groups
from src.services.auth import auth_service


router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/", response_model=List[GroupResponse],
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                        current_user: User = Depends(auth_service.get_current_user)):
    groups = await repository_groups.get_groups(skip, limit, db)
    return groups


@router.get("/{group_id}", response_model=GroupResponse,
            description="No more than 10 requests per minute",
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_group(group_id: int, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    
    group = await repository_groups.get_groups(group_id, db)
    if group is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    return group


@router.post("/", response_model=GroupResponse, status_code=status.HTTP_201_CREATED)
async def create_group(body: GroupModel, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    
    if current_user.role.name == "admin" or current_user.role.name == "moderator":
        return await repository_groups.create_group(body, current_user, db)
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Does not have access")


@router.put("/{group_id}", response_model=GroupResponse)
async def update_group(body: GroupUpdate, group_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    
    if not (current_user.role == "admin" or current_user.role == "moderator"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Does not have access")
    
    group = await repository_groups.update_group(group_id, body, current_user, db)    
    if group is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return group


@router.delete("/{group_id}", response_model=GroupResponse, status_code=status.HTTP_202_ACCEPTED)
async def remove_group(group_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    
    if not (current_user.role == "admin" or current_user.role == "moderator"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Does not have access")
    
    group = await repository_groups.remove_group(group_id, current_user, db)
    if group is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    return group
