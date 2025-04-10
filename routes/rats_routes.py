from fastapi import APIRouter
from logic.rats_mode1 import get_random_episode
from logic.rats_mode2 import get_next_episode

router = APIRouter()

@router.get("/mode1")
def mode1():
    return get_random_episode()

@router.get("/mode2")
def mode2():
    return get_next_episode()
