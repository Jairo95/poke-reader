class Integer(object):
    pass


class String(object):
    pass


class Parent(object):
    def __init__(self, class_name):
        self.class_name = class_name


def set_attributes_from_fields(instance, data):
    for key, item in instance.__class__.__dict__.items():
            if isinstance(item, Integer):
                setattr(instance, key, int(data.get(key)))

            elif isinstance(item, String):
                setattr(instance, key, str(data.get(key)))
                
            elif isinstance(item, Parent):
                setattr(instance, key, item.class_name(data.get(key)))