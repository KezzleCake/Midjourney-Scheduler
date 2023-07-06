from itertools import combinations
import os, time, api
from pymongo import MongoClient

data = [
    'hallyu',
    'in the style of hallyu',
    'smilecore',
    '32k uhd',
    'tondo',
    'embroidery',
    'spiral group',
    'y2k aesthetic',
    'ready-made',
    'happycore',
    'high quality',
    'rounded',
    'simple',
    'cranberrycore',
    'in the style of joong keun lee',
    'the snapshot aesthetic',
    'princesscore',
    'oshare kei',
    'subtle surface decoration',
    'sandara tang'
]

# 모든 조합 생성
all_combinations = []
for r in range(1, len(data) + 1):
    for combination in combinations(data, r):
        all_combinations.append(', '.join(combination))
        
db_url = os.environ.get('MONGODB_URI')
db_username = os.environ.get('MONGODB_USERNAME')
db_password = os.environ.get('MONGODB_PASSWORD')
db_name = os.environ.get('MONGODB_DBNAME')

mongo_client = MongoClient(
            db_url,
            username=db_username,
            password=db_password
        )

db = mongo_client[db_name]

# 조합된 파라미터로 요청하기
for combination in all_combinations:
    prompt = 'cake, ' + combination
    
		# 이미지 정보가 없는 경우에만 요청
    if (db['images2'].find_one({'prompt': prompt}) == None):
        api.post(prompt)
        # 4분 간격으로 요청
        time.sleep(60 * 4)
    else:
        continue