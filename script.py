import sys

from cwb.daemon import CWBDaemon

if __name__ == "__main__":
    daemon = CWBDaemon('/tmp/open-data-collection.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart".format(sys.argv[0]))
        sys.exit(2)
