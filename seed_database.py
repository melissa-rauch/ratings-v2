"""A file to seed database"""

import os
import json
from random import choice, randint
from datetime import datetime
import server, model, crud



os.system('dropdb ratings')
os.system('createdb ratings')