import sys
import json
import urllib
import uuid
import os
import datetime
import boto3
import time

from datetime import datetime
from pytz import timezone

import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

from general import *

def lambda_handler(event, context):
	print("Done")