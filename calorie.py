# 칼로리 계산
from Routine import Routine
from main import Main


class Calorie(Routine):
    Korean_food = ('떡볶이 - 500kcal', '튀김 - 600kcal', '순대 - 700kcal', '김밥 - 400kcal', '어묵 - 300kcal','X')
    Korean_food_calorie = (500, 600, 700, 400, 300, 0)

    Western_food = ('피자 - 1000kcal', '스파게티 - 800kcal', '햄버거 - 700kcal', '치킨 - 600kcal', '샐러드 - 300kcal','X')
    Western_food_calorie = (1000, 800, 700, 600, 300, 0)

    Chinese_food = ('짜장면 - 700kcal', '짬뽕 - 800kcal', '탕수육 - 1000kcal', '볶음밥 - 600kcal', '군만두 - 500kcal','X')
    Chinese_food_calorie = (700, 800, 1000, 600, 500 , 0)

    Japanese_food = ('초밥 - 500kcal', '라멘 - 700kcal', '우동 - 600kcal', '돈까스 - 800kcal', '오므라이스 - 900kcal ','X')
    Japanese_food_calorie = (500, 700, 600, 800, 900, 0)

    calorie_add = 0

    def __init__(self):
        super().__init__()
        self.k = 5
        self.w = 5
        self.c = 5
        self.j = 5

    def __str__(self):
        return super().__str__() + \
            f'\n-칼로리 계산-' + \
               f'\n{self.name}님이 섭취하신 음식은 \n' \
               f'한식 : {Calorie.Korean_food[self.k]} \n' \
                  f'양식 : {Calorie.Western_food[self.w]} \n' \
                    f'중식 : {Calorie.Chinese_food[self.c]} \n' \
                        f'일식 : {Calorie.Japanese_food[self.j]} \n' \
                            f'이므로, \n' \
               f'{self.name}님의 총 섭취 칼로리는 {Calorie.calorie_add}kcal 입니다.'



    def Korean(self):
        for index, Food in enumerate(Calorie.Korean_food[0:5]) :
            print(f'{index + 1}. {Food}')
        k = input("오늘 먹은 음식을 선택하세요(엔터 누르면 패스) : ")
        if k == '':
            Calorie.calorie_add += 0
        else:
            Calorie.calorie_add += Calorie.Korean_food_calorie[int(k) - 1]
            self.k = int(k) - 1

    def Western(self):
        for index, Food in enumerate(Calorie.Western_food[0:5]):
            print(f'{index + 1}. {Food}')
        w = input("오늘 먹은 음식을 선택하세요(엔터 누르면 패스) : ")

        if w == '':
            Calorie.calorie_add += 0
        else:
            Calorie.calorie_add += Calorie.Western_food_calorie[int(w) - 1]
            self.w = int(w) - 1

    def Chinese(self):
        for index, Food in enumerate(Calorie.Chinese_food[0:5]):
            print(f'{index + 1}. {Food}')
        c = input("오늘 먹은 음식을 선택하세요(엔터 누르면 패스) : ")

        if c == '':
            Calorie.calorie_add += 0
        else:
            Calorie.calorie_add += Calorie.Chinese_food_calorie[int(c) - 1]
            self.c = int(c) - 1

    def Japanese(self):
        for index, Food in enumerate(Calorie.Japanese_food[0:5]):
            print(f'{index + 1}. {Food}')
        j = input("오늘 먹은 음식을 선택하세요(엔터 누르면 패스) : ")
        if j == '':
            Calorie.calorie_add += 0
        else:
            Calorie.calorie_add += Calorie.Japanese_food_calorie[int(j) - 1]
            self.j = int(j) - 1

    def Meals(self):
        self.Korean()
        self.Western()
        self.Chinese()
        self.Japanese()
        super().order()


if __name__ == '__main__':
    # name = input("이름을 입력하세요 : ")
    caloric_calculator = Calorie()
    caloric_calculator.Meals()
    print(caloric_calculator)
