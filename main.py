# 운동 루틴
# 전신, 상체, 하체로 나누어서 해당 루틴을 클릭하면, 루틴 목록을 보여주는 식
# 영상 링크도 같이 할 수 있으면 같이 주기

class Main:
    def __init__(self):
        self.name = '없음'    # 이름
        self.weight = 0    # 체중
        self.stature = 0  # 키

    def __str__(self):
        return f'이름 : {self.name}\t키 : {self.stature}cm\t체중 : {self.weight}kg'

    def set_name(self):
        # 사용자에게 이름 묻기
        name = input('이름을 입력하세요 : ')
        while True :
            if name == '':  # 엔터 치면 다시 묻기
                name = input('이름을 입력하세요 : ')
            else:
                self.name = name
                break

    def set_stature(self):
        # 사용자에게 키 묻기
        stature = input('키를 입력하세요 : ')
        while True :
            if stature == '':  # 엔터 치면 다시 묻기
                stature = input('키를 입력하세요 : ')
            else:
                self.stature = stature
                break

    def set_weight(self):
        # 사용자에게 키 묻기
        weight = input('몸무게를 입력하세요 : ')
        while True :
            if weight == '':  # 엔터 치면 다시 묻기
                weight = input('몸무게를 입력하세요 : ')
            else:
                self.weight = weight
                break
    def order(self):
        self.set_name()
        self.set_stature()
        self.set_weight()

if __name__ == '__main__':
    member1 = Main()
    member1.order()
    print(member1)