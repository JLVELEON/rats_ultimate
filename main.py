from fastapi import FastAPI, Query
from pathlib import Path
from utils.file_utils import scan_series_folder
from utils.state_manager import load_progress, save_progress
from logic.rats_mode1 import get_random_episode
from logic.rats_mode2 import get_next_episode as get_ordered_episode
from routes.rats_routes import router as rats_router

app = FastAPI()

app.include_router(rats_router, prefix="/rats")
BASE_PATH = Path("series")
PROGRESS_PATH = Path("data/progress.json")

@app.get("/next")
def next_episode(mode: int = Query(1)):
    all_series = scan_series_folder(BASE_PATH)
    progress = load_progress(PROGRESS_PATH)

    if mode == 1:
        episode = get_random_episode(all_series)
    elif mode == 2:
        episode = get_ordered_episode(all_series, progress)
    else:
        return {"error": "Modo no válido. Usa 1 o 2."}

    if episode:
        save_progress(PROGRESS_PATH, episode, all_series)
        return episode

    return {"error": "No se encontraron episodios válidos."}

@app.post("/reset")
def reset():
    PROGRESS_PATH.write_text("{}", encoding="utf-8")
    return {"status": "Progreso reiniciado"}
