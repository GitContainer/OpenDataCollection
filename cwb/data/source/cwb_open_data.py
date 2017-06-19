from enum import Enum


class MsgType(Enum):
    issue = 0
    update = 1
    cancel = 2


class Scope(Enum):
    public = 0
    restricted = 1
    private = 2


class Status(Enum):
    actual = 0
    exercise = 1
    system = 2
    test = 3
    draft = 4


# 氣象共用資料
class CwbOpenData:
    def __init__(self, identifier, sender, sent, status, scope, msg_type):
        # 資料唯一識別碼
        self.identifier = identifier
        # 資料提供單位 email address
        self.sender = sender
        # 發布日期
        self.sent = sent
        # 資料狀態
        self.status = status
        # 資料公開對象
        self.scope = scope
        # 訊息類型 / 資料類型
        self.msg_type = msg_type
        # 類別唯一識別碼
        self.data_id = None
        # 備註
        self.note = None
        # 特殊資料碼
        self.code = None
        # 資料提供單位
        self.source = None
        # 資料集
        self.data_set_list = []
