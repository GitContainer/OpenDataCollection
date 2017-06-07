# 氣象共用資料
class CwbOpenData:
    def __init__(self, data_set):
        # 資料唯一識別碼
        self.Identifier = None

        self.Sender = None
        self.Sent = None
        self.Status = None
        self.MsgType = None
        self.Source = None
        self.DataId = None
        self.Scope = None
        self.Note = None
        self.Code = None
        self.DataSet = data_set
