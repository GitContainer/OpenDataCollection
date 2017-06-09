from enum import Enum


class ReportStatus(Enum):
    Actual = 0
    Exercise = 1
    System = 2
    Test = 3


class ReportMsgType(Enum):
    Alert = 0
    Issue = 1
    Update = 2
    Cancel = 3
    Error = 4


class Report:
    def __init__(self):
        # (報告)類型
        self.ReportType = None
        # (報告)xml識別碼
        self.ReportIdentifier = None
        # (報告)xml版本
        self.ReportSchemaVer = None
        # (報告)使用語言
        self.ReportLanguage = None
        # (報告)事件類型
        self.ReportEvent = None
        # (報告)發布單位
        self.ReportSender = None
        # (報告)事件公告時間
        self.ReportSent = None
        # (報告)事件公告種類
        self.ReportStatus = None
        # (報告)事件公告狀況
        self.ReportMsgType = None
        # 先前(報告)事件參考
        self.ReportReferences = None
        # (報告)事件公告報號
        self.ReportNo = None
        # 事件內容描述
        self.ReportDescription = None
        # 自訂標籤群組
        self.ParameterSetList = []
        # 自訂標籤
        self.ParameterList = []
        # 發震時間
        self.ReportOriginTimeList = []
        # 地震資訊
        self.EarthquakeList = []
