# 資源索引標籤
class Resource:
    def __init__(self):
        # 資源索引說明
        self.resource_desc = None
        # MIME類型 http://en.wikipedia.org/wiki/Internet_media_type
        self.mime_type = None
        # 資料大小
        self.size = None
        # 資源URI
        self.uri = None
        # digital digest
        self.digest = None
