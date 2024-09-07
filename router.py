from typing import Annotated
from fastapi import APIRouter, Depends

from schemas import STask, STaskAdd
from repository import TaskRepository


router = APIRouter(
    prefix='/tasks'
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    task_id = await TaskRepository.add_one(task)
    return {'OK': True, 'task_id': task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
