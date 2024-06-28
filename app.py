from src.WasteDetectionYOLOv5.logger import logging
from src.WasteDetectionYOLOv5.exception import AppException
import sys

try:
    s= 3/0
except Exception as e:
    raise AppException(e,sys)