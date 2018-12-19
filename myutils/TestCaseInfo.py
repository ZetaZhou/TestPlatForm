class TestCaseInfo(object):
    """description of class"""
    def __init__(self,CASE_ID="",CASE_NAME_DETAIL="",MODEL_NAME = "", CASE_OWNER="",TEST_RESULT="Hang On",STARTTIME="",ENDTIME="",DURATION="",MESSAGE=""):
        self.CASE_ID = CASE_ID
        self.MODEL_NAME = MODEL_NAME
        self.CASE_NAME_DETAIL = CASE_NAME_DETAIL
        self.CASE_OWNER = CASE_OWNER
        self.TEST_RESULT = TEST_RESULT
        self.STARTTIME = STARTTIME
        self.ENDTIME = ENDTIME
        self.DURATION = DURATION
        self.MESSAGE = MESSAGE


if __name__ == '__main__':
    tt = TestCaseInfo()
    print (tt.__dict__)

