from enum import Enum


class MsgType(Enum):
    Issue = 0
    Update = 1
    Cancel = 2


class Scope(Enum):
    Public = 0
    Restricted = 1
    Private = 2


class Status(Enum):
    Actual = 0
    Exercise = 1
    System = 2
    Test = 3
    Draft = 4


# 氣象共用資料
class CwbOpenData:
    def __init__(self, identifier, sender, sent, status, scope, msg_type):
        # 資料唯一識別碼
        self.Identifier = identifier
        # 資料提供單位 email address
        self.Sender = sender
        # 發布日期
        self.Sent = sent
        # 資料狀態
        self.Status = status
        # 資料公開對象
        self.Scope = scope
        # 訊息類型 / 資料類型
        self.MsgType = msg_type
        # 類別唯一識別碼
        self.DataId = None
        # 備註
        self.Note = None
        # 特殊資料碼
        self.Code = None
        # 資料提供單位
        self.Source = None
        # 資料集
        self.DataSetList = []
