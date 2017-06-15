from enum import Enum


class ReportStatus(Enum):
    actual = 0
    exercise = 1
    system = 2
    Test = 3


class ReportMsgType(Enum):
    alert = 0
    issue = 1
    update = 2
    cancel = 3
    error = 4


class Report:
    def __init__(self):
        # (報告)類型
        self.report_type = None
        # (報告)xml識別碼
        self.report_identifier = None
        # (報告)xml版本
        self.report_schema_ver = None
        # (報告)使用語言
        self.report_language = None
        # (報告)事件類型
        self.report_event = None
        # (報告)發布單位
        self.report_sender = None
        # (報告)事件公告時間
        self.report_sent = None
        # (報告)事件公告種類
        self.report_status = None
        # (報告)事件公告狀況
        self.report_msg_type = None
        # 先前(報告)事件參考
        self.report_references = None
        # (報告)事件公告報號
        self.report_no = None
        # 事件內容描述
        self.report_description = None
        # 自訂標籤群組
        self.parameter_set_list = []
        # 自訂標籤
        self.parameter_list = []
        # 發震時間
        self.report_origin_time_list = []
        # 地震資訊
        self.earthquake_list = []
