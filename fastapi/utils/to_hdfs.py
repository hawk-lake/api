import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, f'../lib')
data_dir = os.path.join(current_dir, f'../datas')
sys.path.append(lib_dir)

from spotify import *
from database import *


def artists_to_hdfs(date):
    from files import files_to_hdfs

    files_to_hdfs("artists", date)


def albums_to_hdfs(date):
    from files import files_to_hdfs

    files_to_hdfs("albums", date)


def tracks_to_hdfs(date):
    from files import files_to_hdfs

    files_to_hdfs("tracks", date)