import logging

from sqlalchemy.exc import OperationalError
from wxcloudrun import db
from wxcloudrun.model import Counters, Tab, Video

# 初始化日志
logger = logging.getLogger('log')


def get_tabs():
    """
    查询已定义Tabs
    :return: Tabs
    """
    try:
        tabs = db.session.query(Tab.id, Tab.name, Tab.index).filter(Tab.deleted == 0).order_by(Tab.index.asc()).all()
        tabs_format = format_data(tabs, ['id', 'name', 'index'])
        return tabs_format
    except OperationalError as e:
        logger.info("get_tabs errorMsg= {} ".format(e))
        return None
    

def get_videos():
    """
    查询已定义Videos
    :return: Videos
    """
    try:
        videos = db.session.query(Video.tab_id, Video.name, Video.cover_src, Video.src, Video.index).filter(Video.deleted == 0).order_by(Video.index.asc()).all()
        videos_format = format_data(videos, ['tab_id', 'name', 'cover_src', 'src', 'index'])
        return videos_format
    except OperationalError as e:
        logger.info("get_videos errorMsg= {} ".format(e))
        return None


def query_counterbyid(id):
    """
    根据ID查询Counter实体
    :param id: Counter的ID
    :return: Counter实体
    """
    try:
        return Counters.query.filter(Counters.id == id).first()
    except OperationalError as e:
        logger.info("query_counterbyid errorMsg= {} ".format(e))
        return None


def delete_counterbyid(id):
    """
    根据ID删除Counter实体
    :param id: Counter的ID
    """
    try:
        counter = Counters.query.get(id)
        if counter is None:
            return
        db.session.delete(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("delete_counterbyid errorMsg= {} ".format(e))


def insert_counter(counter):
    """
    插入一个Counter实体
    :param counter: Counters实体
    """
    try:
        db.session.add(counter)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_counter errorMsg= {} ".format(e))


def update_counterbyid(counter):
    """
    根据ID更新counter的值
    :param counter实体
    """
    try:
        counter = query_counterbyid(counter.id)
        if counter is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_counterbyid errorMsg= {} ".format(e))

        
def format_data(query_res, columns):
    format_res = []
    if (len(query_res)):
        for x in range(len(query_res)):
            format_res.append({})
            for i in range(len(columns)):
                format_res[x][columns[i]] = query_res[x][columns[i]]
    return format_res                
