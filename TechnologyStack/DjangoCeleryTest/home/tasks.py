import time

from DjangoCeleryTest.celery import app


@app.task()
def celery_test():
   time.sleep(5)
   print("this is a test!!!")


'''
run celery
celery -A DjangoCeleryTest worker -l info
'''
'''
记一坑
celery中有async关键字做参数！！！需要修改
'''