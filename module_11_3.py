# # Интроспекция:
# #   - Тип объекта.
# #   - Атрибуты объекта.
# #   - Методы объекта.
# #   - Модуль, к которому объект принадлежит.
#
import inspect

def introspection_info(obj):  # функция, проводящая интроспекцию объекта
    obj_type = type(obj)  # тип объекта.__name__#тип объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]  # атрибуты  объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]  # методы объекта
    obj_module = inspect.getmodule(obj)  # модуль, к которому принадлежит объект
    info = f"type: {obj_type}, attributes: {', '.join(attributes)}, methods: {', '.join(methods)}, module: {obj_module}"  # строка с данными об объекте
    return info


class SomeClass:#создание класса
    def __init__(self):
        self.attribute_1 = "attribute_1"


my_object = SomeClass()#создание объекта класса

object_info = introspection_info(my_object)
print(object_info)

number_info = introspection_info(42)
print(number_info)
