import math 
'''#math 모듈을 받아온다'''
start=0

class Line:  
    '''Line 클래스를 만든다. _length 필드, __init__, set_length, get_length 의 method를 만들어서'''
    __length = 1
    if(not(__length > 0 and (type(__length) == int or type(__length) == float))):
        __length = 1
        
    '''#이거처럼 __를 써서 변수(필드)를 익명화하는 이유는 그냥 변수로 설정해서 클래스 밖에서 설정을 한다면 오류가 날 수도 있어서 클래스 안에서
       #즉 내부에서만 쓸 수 있게하고 오류나 문제 없게하려고..
       #없어도 무방한건가?
    '''
                 
    def __init__(self, length=1):   
        self.__length = length      
        '''
            #애초에 __init__이라는게 값들을 초기화해주는거라서 있긴 해야함.
            # self(생성자), __length에다가 length의 값을 대입한다. 
            #and..... 현재 이 method에서의 length는 1로 초깃값으로 두었기에 __length의 값은 1이 된다.
        '''
        
    def set_length(self, length):
        '''# length의 값을 받고 그 값을 __length에 대입한다.'''
        if(length >0 and (type(length) == int or type(length) == float)): 
             '''#수정한 값이 조건에 부합하는지 확인!'''
             self.__length = length
           
        
        
    def get_length(self):         
        '''__length의 값을 return하고 print할수있게 return해준다(값을 반환한다).'''        
        return self.__length 
     
 
    #def first_check(self): 
    #   '''#초기값이 조건에 부합하는지 확인하는코드'''
        
        #print(self.__length)
        #print(type(self.__length))
        #print(self.__length <= 0)
        #print(type(self.__length) != int)
        #print(type(self.__length) != float)
        
        #if(not(self.__length >0 and (type(self.__length) == int or type(self.__length) == float))):#조건
        #   self.__length=1
        #  '''#다시 1로 (초깃값)으로 되돌리기'''

'''   
#그냥 값을 억지로 바꿀 수도 있겠지만.... 
#클래스에서 쓰는 field(변수)는 클래스 안에서 바꾸던지 어떻게 하든지 하는게 베스트...
#그래서 클래스 안에서 method를 사용하여 값을 받고 대입을 해주는거고.    
'''
def area_square(line):
    '''제곱해서 사각형 넓이 구하는 함수'''
    if(type(line)!=Line): 
        '''#Line 클래스가 아니면 0을 반환'''
        return 0
    else:
        return line.get_length() ** 2

def area_circle(line): 
    '''#제곱하고 파이곱해서 원의 넓이 구하는 함수(파이는 import해서 들고옴)'''
    if(type(line)!=Line):
        '''#Line 클래스가 아니면 0을 반환'''
        return 0
    else:
        return line.get_length() ** 2 * math.pi

def area_regular_triangle(line):
    '''#루트도 import해서 들고오고 삼각형 넓이 구하기''' 
    if(type(line)!=Line):
        '''#Line 클래스가 아니면 0을 반환'''
        return 0
    else:
        return line.get_length() ** 2 * math.sqrt(3) / 4
