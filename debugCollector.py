
class ErrorLog(object):

    def __init__(self):
        self.errorLog = []
        self.fileName = "debug.err"
        try:
            open(self.fileName,'x').close()
        except:
            pass


    def outputLogAdd(self, error):
        error = str(error)
        self.errorLog.append(error)
        if len(self.errorLog) > 30:
            self.errorLog.pop(0)
        with open(self.fileName, 'w') as log:
            for line in self.errorLog:
                log.write(line + "\n")
