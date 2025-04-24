from typing import Tuple, Dict, List
from pathlib import Path

cwd = Path.cwd()

DATA_FOLDER: str = "data"

CONCRETE_DATA_FILE: str = "concrete_data.xls"
CONCRETE_7_DAYS_SCALED: str = "concrete_7_days_scaled.csv"
CONCRETE_28_DAYS_SCALED: str = "concrete_28_days_scaled.csv"

TEMPERATURE_DATA_FILE: str = "daily-min-temperatures.csv"

PATH_CONCRETE_DATA_FILE = cwd / DATA_FOLDER / CONCRETE_DATA_FILE
PATH_CONCRETE_7_DAYS_SCALED = cwd / DATA_FOLDER / CONCRETE_7_DAYS_SCALED
PATH_CONCRETE_28_DAYS_SCALED = cwd / DATA_FOLDER / CONCRETE_28_DAYS_SCALED
PATH_TEMPERATURE_DATA_FILE = cwd / DATA_FOLDER / TEMPERATURE_DATA_FILE