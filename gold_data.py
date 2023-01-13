import pandas as pd # pd.read_html함수를 사용하기 위해 호출
import seaborn as sns # sns함수를 사용해 그래프를 생성 후 디자인하기 위한 호출
import matplotlib.pyplot as plt # plt함수를 사용해 한글 깨짐과 그래프 x,y 축, title 라벨 설정을 위해 설정
import numpy as np # np함수를 사용해 배열 뒤집기 위해 호출
import schedule # schedule.every().seconds.do()함수를 사용해 반복하기 위해 호출
import datetime # datetime.datetime.now()함수를 사용해 현재 시간 출력하기 위해 호출
import subprocess
import time

def get_table_data():                         # 커스텀 함수를 이용해 get_table_data설정

    url = "https://finance.naver.com/marketindex/goldDailyQuote.naver?&page=1" # url 변수 안에 링크 삽입

    tables = pd.read_html(url)                # url 호출 후 tables 변수에 삽입

    gold_table = tables[0]                    # tables 변수 안에있는 url의 0번째 테이블 만을 가져온 후 gold_table 변수에 삽입

    return gold_table                         # gold_table 변수를 반환하여 함수 외부에서 사용

def create_plot_data(gold_table):             # 커스텀 함수 create_plot_data에 gold_table을 매변수로 지정

    date = gold_table["날짜"].values.flatten()     # values로 가져온 list 값을 flatten 함수를 사용해서 2차원 배열에서 1차원 배열로 바꿈
    prev = gold_table["매매기준율"].values.flatten() 

    date = np.flip(date)                      # np.flip() 함수를 사용해서 date값 뒤집기
    
    return date, prev                         # date, prev 변수를 반환하여 함수 외부에서 사용

def draw_plot(date, prev):                    # 커스텀 함수 draw_plot에 date, prev을 매변수로 지정
    sns.set(style = "darkgrid")               # 도표 스타일 변경

    sns.set(rc = {"figure.figsize":(20,8)})   # 도표 사이즈 변경 

    sns.set(font_scale = 1)                   # font size 변경

    plt.rc("font",family="Malgun Gothic")     # 한글 깨짐현상 해결

    sns.set_style(rc = {'axes.facecolor': 'lightsteelblue'})

    sns.lineplot(x = date, y = prev,          # line 그래프로 설정

                marker = "o",                 # 일별 마다 점으로 표시
             
                color = "k",                  # line 색을 Blue로 설정
                 
                linestyle = "-",              # line style을 실선으로 변경
                    
                linewidth = 3)                # line width를 조절

    sns.barplot(x = date, y = prev,
                    
                width = 0.3)

    plt.title("일별 금 시세", fontsize = 25)  # title만 별도로 사이즈 지정
    
    plt.xlabel("날짜")                        # xlabel 설정

    plt.ylabel("매매기준율")                    # ylabel 설정

    plt.ylim(70000,80000)

    plt.pause(3)                              # 그래프를 실행 시키고 3초 뒤에 꺼지게 함

def main_app():                               # 커스텀 함수로 main_app을 설정

    print("갱신: ", datetime.datetime.now())  # 현재 시간을 출력
    print("----------------------------------")

    gold_table = get_table_data()             # get_table_data()이 return 해주는 데이터를 gold_table 변수에 선언

    date, prev = create_plot_data(gold_table) # create_plot_data()은 매개변수로 gold_table을 받은 후 필요한 데이터만 선별해 
                                              # return 해주는 데이터 2개를 변수에 선언

    draw_plot(date, prev)                     # draw_plot()은 매개변수로 date, prev을 받은 후 데이터를 그래프로 그려줌

schedule.every(2).seconds.do(main_app)        # 1초마다 main_app함수를 실행 시킴
        
while True:                                   # 반복적으로 실행
    schedule.run_pending()                    # schedule을 실행