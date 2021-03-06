""" 路途逻辑 """
import logging
import uuid

from ..data import get_session
from ..models import Trace

LOGGER = logging.getLogger(__name__)


def create(json):
    """ 创建路途 """
    trace_id = str(uuid.uuid4())
    new_trace = Trace(
        id=trace_id,
        positions=json)
    sess = get_session()
    try:
        sess.add(new_trace)
        sess.commit()
        return new_trace
    except Exception as ex:
        LOGGER.error('创建路途异常')
        return None
    finally:
        sess.close()


def get(trace_id):
    """ 获取路途 """
    sess = get_session()
    try:
        return sess.query(Trace).\
            filter_by(id=trace_id).\
            first()
    except Exception as ex:
        LOGGER.error('获取路途')
        return None
    finally:
        sess.close()
