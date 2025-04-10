import random
from typing import Dict, List
from utils.state_manager import load_progress, save_progress
from utils.file_utils import scan_series_folder

MAX_CONSECUTIVE = 3  # No más de 3 episodios seguidos de la misma serie

def get_next_episode(series_folder: str, state_file: str) -> str:
    series_data = scan_series_folder(series_folder)
    state = load_progress(state_file)

    history = state.get("history", [])
    series_progress = state.get("progress", {})

    # Contar repeticiones consecutivas
    last_series = history[-1] if history else None
    count = 0
    for s in reversed(history):
        if s == last_series:
            count += 1
        else:
            break

    # Filtrar series candidatas
    candidates = []
    for series, episodes in series_data.items():
        idx = series_progress.get(series, 0)
        if idx < len(episodes):
            if count >= MAX_CONSECUTIVE and series == last_series:
                continue
            candidates.append(series)

    if not candidates:
        raise Exception("No hay series disponibles para reproducir")

    # Elegir una serie aleatoria válida
    next_series = random.choice(candidates)
    next_index = series_progress.get(next_series, 0)
    next_episode = series_data[next_series][next_index]

    # Actualizar progreso
    series_progress[next_series] = next_index + 1
    history.append(next_series)
    if len(history) > 10:
        history = history[-10:]

    state["progress"] = series_progress
    state["history"] = history
    save_progress(state_file, state)

    return next_episode
