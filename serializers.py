import fields


class Generation(object):
    name = fields.String()
    url = fields.String()

    def __init__(self, response):
        fields.set_attributes_from_fields(self, response)
    
    def __str__(self):
        return str(self.name)


class Type(object):
    id = fields.Integer()
    name = fields.String()
    generation = fields.Parent(Generation)

    def __init__(self, response):
        fields.set_attributes_from_fields(self, response)

    def __str__(self):
        return str(self.name)
