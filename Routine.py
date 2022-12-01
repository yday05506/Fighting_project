# 운동 루틴
# 전신, 상체, 하체로 나누어서 해당 루틴을 클릭하면, 루틴 목록을 보여주는 식
# 영상 링크도 같이 할 수 있으면 같이 주기
from random import random
from main import Main


class Routine(Main):
    # 클래스 변수
    _ROUTINE = ('전신', '상체', '하체')   # 0: 전신, 1:상체, 2:하체
    _WHOLEBODY = ('전신 찐 핵핵매운맛\thttps://youtu.be/gMaB-fG4u4g', '20분 층간소음 X\thttps://youtu.be/6sYMrAWBxs0', '30분 근력 유산소\thttps://youtu.be/4kZHHPH6heY', '20분 유산소\thttps://youtu.be/46vQnzaZ6aU', '32분 근력 유산소\thttps://youtu.be/WHK2SxCiTBw')
    _UPPERBODY = ('덤벨 상체\thttps://youtu.be/xoWKLNwNva0', '20분 층간소움 X\thttps://youtu.be/e1DHt9wfQOA', '15분 상체\thttps://youtu.be/wmxQhM7fnFA', '11분 상체\thttps://youtu.be/RGfAAhZsKc4', '상체 올킬\thttps://youtu.be/XjEfUcZLbG4')
    _LOWERBODY = ('25분 힙업\thttps://youtu.be/0s9W3-CD0cE', '하체 핵매운맛\thttps://youtu.be/NDsjmxTROEo', '스쿼트 10가지 동작\thttps://youtu.be/DWYDL-WxF1U', '18분 덤벨 하체\thttps://youtu.be/4qqBQ0Xs4nc', '전설의 하체토닝\thttps://youtu.be/y7H-9qI-qtw')

    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자 호출
        self.routine = 0    # 0:전신, 1:상체, 2:하체

    def __str__(self):
        return super().__str__() + f'\t루틴 : {Routine._ROUTINE[self.routine]}'

    def set_routine(self):
        # 사용자에게 숫자 묻기 → 0:전신, 1:상체, 2:하체
        for index, routine_label in enumerate(Routine._ROUTINE):
            print(f'{index+1}.{routine_label}')
        routine = input('루틴을 선택하세요 : ')
        if routine == '' :   # 엔터 치면 기본값
            self.routine = 0
        else:
            self.routine = int(routine)-1   # 숫자를 제대로 입력했을 때

    def set_body_routine(self):
        #전신이면 전신 루틴 중 인덱스 랜덤 출력
        if self.routine == 0:
            index = int(random()*len(Routine._WHOLEBODY))
            print("-" * 80 + f'\n-추천 루틴-\n{Routine._WHOLEBODY[index]}')
        # 상체면 상체 루틴 중 인덱스 랜덤 출력
        if self.routine == 1:
            index = int(random()*len(Routine._UPPERBODY))
            print("-" * 80 + f'\n-추천 루틴-\n{Routine._UPPERBODY[index]}')
        # 하체면 하체 루틴 중 인덱스 랜덤 출력
        if self.routine == 2:
            index = int(random()*len(Routine._LOWERBODY))
            print("-" * 80 + f'\n-추천 루틴-\n{Routine._LOWERBODY[index]}')

    def order(self):
        super().order()     # 부모 클래스의 order() 호출
        self.set_routine()
        self.set_body_routine()

if __name__ == '__main__':
    member1 = Routine()
    member1.order()
    print(member1)