# 資源索引標籤
class Resource:
    def __init__(self):
        # 資源索引說明
        self.ResourceDesc = None
        # MIME類型 http://en.wikipedia.org/wiki/Internet_media_type
        self.MimeType = None
        # 資料大小
        self.Size = None
        # 資源URI
        self.Uri = None
        # digital digest
        self.digest = None
