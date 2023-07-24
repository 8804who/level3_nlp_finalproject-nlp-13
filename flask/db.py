from distutils.log import INFO
from hashlib import new
import pymongo
import re
from datetime import datetime

db_api=""
client = pymongo.MongoClient(db_api)
db = client.boostcamp
collection = db.users
    
def check(id_info):
    """
    DB�� �ش� ������ �ִ��� Ȯ���ϴ� �Լ�
    user�� ���ٸ� ���� �����ϱ�
    id_info : google token
    """
    user = collection.find_one({'email': id_info['email']})

    if not user:
        # �� user ����
        user_data = {
            'email': id_info['email'],
            'name': id_info['name'],
        }
        collection.insert_one(user_data)

def attendance(target_email):
    new_date=datetime.today() 
    existing_data = collection.find_one({'email': target_email})
    # �̹� �ش� id�� ���� document�� �����ϴ� ���
    if existing_data:
        # 'date' �ʵ尡 �̹� �����ϴ��� Ȯ���մϴ�.
        if 'date' in existing_data:
            # 'date' �ʵ忡 ���ο� ��¥�� �߰��մϴ�.
            existing_data['date'].append(new_date)
        else:
            # 'date' �ʵ尡 �������� ������ ���� �����մϴ�.
            existing_data['date'] = [new_date]

        # ������Ʈ�� document�� �����մϴ�.
        collection.update_one({'email': target_email}, {'$set': existing_data})