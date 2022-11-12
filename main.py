# 운동 루틴
# 전신, 상체, 하체로 나누어서 해당 루틴을 클릭하면, 루틴 목록을 보여주는 식
# 영상 링크도 같이 할 수 있으면 같이 주기

class Routine:
    # 클래스 변수
    _ROUTINE = ('전신', '상체', '하체')   # 0: 전신, 1:상체, 2:하체

    def __init__(self, name, weight, stature):
        self.name = name    # 이름
        self.weight = weight    # 체중
        self.stature = stature  # 키
        self.routine = 0    # 0:전신, 1:상체, 2:하체

    def __str__(self):
        return f'이름 : {self.name}\t키 : {self.stature}cm\t체중 : {self.weight}kg\t루틴 : {Routine._ROUTINE[self.routine]}'

    def set_routine(self):
        # 사용자에게 숫자 묻기 → 0:전신, 1:상체, 2:하체
        for index, routine_label in enumerate(Routine._ROUTINE):
            print(f'{index+1}.{routine_label}')
        routine = input('루틴을 선택하세요 : ')
        if routine == '' :   # 엔터 치면 기본값
            self.routine = 0
        else:
            self.routine = int(routine)-1   # 숫자를 제대로 입력했을 때

    def order(self):
        self.set_routine()

if __name__ == '__main__':
    member1 = Routine("양다연", 66, 161)
    member1.order()
    print(member1)