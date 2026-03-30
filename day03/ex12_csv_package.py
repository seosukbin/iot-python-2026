##ex13_csv_package.py

import csv  # 기본 라이브러리

with open ('./day02/부산시_해운대구_도서정보.csv','r',encoding = 'cp949') as f:
    reader = csv.reader(f)

    for now in reader:
        print(now)