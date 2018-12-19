from django.db import models

class TestCase(models.Model):
    CASE_ID = models.IntegerField()
    CASE_NAME = models.CharField(max_length=40)
    MODEL_NAME = models.CharField(max_length=40)
    ADDR = models.CharField(max_length=256)
    ADDTIME = models.DateTimeField(null=True)
    SIGN = models.CharField(max_length=5, null=True)
    STATUS = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.CASE_NAME

class TestCaseTMP(models.Model):
    CASE_ID = models.IntegerField()
    CASE_NAME = models.CharField(max_length=40)
    MODEL_NAME = models.CharField(max_length=40)
    ADDR = models.CharField(max_length=256)
    ADDTIME = models.DateTimeField(null=True)
    SIGN = models.CharField(max_length=5, null=True)
    STATUS = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.CASE_NAME

class TestCaseDetail(models.Model):
    ID = models.ForeignKey(TestCase, on_delete=models.PROTECT, default='')
    CASE_ID = models.IntegerField()
    CASE_NAME_DETAIL = models.CharField(max_length=128)
    MODEL_NAME = models.CharField(max_length=128)
    CASE_OWNER = models.CharField(max_length=128, null=True)
    ADDR = models.CharField(max_length=256)
    TEST_RESULT = models.CharField(max_length=20, null=True)
    MESSAGE = models.CharField(max_length=512, null=True)
    DURATION = models.CharField(max_length=20, null=True)
    STARTTIME = models.CharField(max_length=20, null=True)
    ENDTIME = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.CASE_NAME_DETAIL


