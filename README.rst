用Python整理Open Data匯入MariaDB
=================================
這是一個用於彙整open data並且部署在linux上成為daemon的專案。歡迎分解改造成你喜歡的架構，可商用免宣告授權。

在中央氣象局氣象資料開放平台上，我目前只用到"單一鄉鎮市區預報資料"；礙於我其他專案的業務邏輯尚未成形(與本專案有所關聯)，故天氣預報的鄉鎮部分並未寫成活的，請見諒。

設定
----
在 setup.conf 中的更改 EveryDayAt 為每天固定執行的時間。

用法
----
- 開始服務 $python script.py start
- 停止服務 $python script.py stop
- 重開服務 $python script.py restart

`Learn more <http://blog.driveinto.com>`_.