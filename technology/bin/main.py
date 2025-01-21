import os
import sys
from pathlib import Path

sys.path.append(os.path.abspath('..'))
from src.StockService import StockService

if __name__ == '__main__':
    dataPath = Path("../datas")
    if not dataPath.is_dir():
        dataPath.mkdir()
    StockService().startService()
