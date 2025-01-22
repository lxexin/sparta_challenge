import pandas as pd
import requests
import xml.etree.ElementTree as ET

import requests
import pandas as pd

# API URL 및 인증 키
url = 'https://openapi.gg.go.kr/LogisticsHousingComplexFacilit'
api_key = 'ce5e1b1985834244948af25feb0d44f4'

# 요청 매개변수 설정
params = {
    'Key': api_key,
    'Type': 'json',
    'pIndex': 1,
    'pSize': 10
}

# API 요청
response = requests.get(url, params=params)

# 결과 처리
if response.status_code == 200:
    data = response.json()  # JSON 데이터를 파싱
    
    # row_dict 초기화
    row_dict = {
        'SIGUN_NM': [],  # 시군명
        'LOGIST_HSCOMPLEX_NM': [],     # 물류단지명
        'COMPLTN_YN': [],      # 준공여부
        'REFINE_ZIP_CD': [],      # 소재지우편번호
        'REFINE_LOTNO_ADDR': [],      # 소재지지번주소
        'REFINE_ROADNM_ADDR': []       # 소재지도로명주소
    }

    # 데이터 파싱
    for item in data['LogisticsHousingComplexFacilit'][1]['row']:  # 필요한 데이터 계층
        row_dict['SIGUN_NM'].append(item.get('SIGUN_NM', ''))
        row_dict['LOGIST_HSCOMPLEX_NM'].append(item.get('LOGIST_HSCOMPLEX_NM', ''))
        row_dict['COMPLTN_YN'].append(item.get('COMPLTN_YN', ''))
        row_dict['REFINE_ZIP_CD'].append(item.get('REFINE_ZIP_CD', ''))
        row_dict['REFINE_LOTNO_ADDR'].append(item.get('REFINE_LOTNO_ADDR', ''))
        row_dict['REFINE_ROADNM_ADDR'].append(item.get('REFINE_ROADNM_ADDR', ''))

    # Pandas 데이터프레임으로 변환
    df = pd.DataFrame(row_dict)

    # 데이터 출력
    print(df.head(10))
