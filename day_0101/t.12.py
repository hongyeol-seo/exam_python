class CustomClass:

    # instance method
    def add_instance_method(self, a,b):
        return a + b

    # classmethod
    @classmethod
    def add_class_method(cls, a, b):
        return a + b

    # staticmethod
    @staticmethod
    def add_static_method(a, b):
        return a + b

print(CustomClass.add_instance_method(None,3,5))
print(CustomClass().add_instance_method(3,5),"인스턴스 생성")
# print(CustomClass.add_class_method(3, 5))
# print(CustomClass.add_static_method(3, 5))

class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = "한국어"


a = KoreanLanguage.static_my_language()
b = KoreanLanguage.class_my_language()

a.print_language()
b.print_language()

# staticmethod에서는 부모클래스의 클래스속성 값을 가져오지만, classmethod에서는 
# cls인자를 활용하여 cls의 클래스속성을 가져오는 것을 알 수 있습니다.