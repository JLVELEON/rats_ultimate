import random
from utils.file_utils import scan_series_folder


def get_random_episode(series_folder: str) -> str:
    """Devuelve un episodio aleatorio de cualquier serie disponible."""
    series_data = scan_series_folder(series_folder)
    all_episodes = []

    for series_episodes in series_data.values():
        all_episodes.extend(series_episodes)

    if not all_episodes:
        raise Exception("No se encontraron episodios")

    return random.choice(all_episodes)
