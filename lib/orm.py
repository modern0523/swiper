
class ModelMixin:
    # 模型转换成字典
    def to_dict(self):
        attr_dict = {}
        for field in self._meta.get_fields():
            name = field.attrname  # 属性名
            value = getattr(self, name)  # 值
            attr_dict[name] = value
        return attr_dict


