from pathlib import Path
from collections import defaultdict
import re

def scan_series_folder(base_path: Path) -> dict:
    """
    Escanea la carpeta base y devuelve un diccionario con el formato:
    {
        "Chowder": {
            "T01": [Path(...), Path(...)],
            "T02": [...]
        },
        "Gumball": {
            ...
        }
    }
    """
    series = defaultdict(lambda: defaultdict(list))
    pattern = re.compile(r"(.*)_T(\d{2})_E(\d{2})", re.IGNORECASE)

    for video in base_path.rglob("*"):
        if video.is_file() and video.suffix.lower() in [".mp4", ".mkv", ".avi"]:
            match = pattern.match(video.stem)
            if match:
                serie_name = match.group(1).strip()
                temporada = f"T{int(match.group(2)):02d}"
                series[serie_name][temporada].append(video)

    # Ordenar episodios por número
    for serie in series:
        for temporada in series[serie]:
            series[serie][temporada].sort()

    return series
