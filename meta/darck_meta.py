class Metaticus(type):
    def __new__(cls, classname, bases, classdict):
        def create_property(self):
            _property_list = []

            for k in classdict:
                property_name = k[3:]

                def def_p_del(self, property_name):
                    return getattr(self, property_name)

                def def_p_set(self, property_name, value):
                    setattr(self, property_name, value)

                def def_p_del(self, property_name):
                    delattr(self, property_name)

                if k[:3] == 'get':
                    if property_name not in _property_list:
                        get_property_func = classdict.get(k)
                        set_property_func = classdict.get(
                            'set' + property_name, def_p_set
                            )
                        del_property_func = classdict.get(
                            'del' + property_name, def_p_del
                            )
                        print(set_property_func)

                        setattr(self, property_name, None)
                        setattr(self.__class__, property_name[1:],
                                property(get_property_func,
                                         set_property_func,
                                         del_property_func))
                        _property_list.append(property_name)
                elif k[:3] == 'set':
                    if property_name not in _property_list:
                        set_property_func = classdict.get(k)
                        get_property_func = classdict.get(
                            'get' + property_name, def_p_get
                            )
                        del_property_func = classdict.get(
                            'del' + property_name, def_p_del
                            )

                        setattr(self, property_name, None)
                        setattr(self.__class__, property_name[1:],
                                property(get_property_func,
                                         set_property_func,
                                         del_property_func))
                        _property_list.append(property_name)
                elif k[:3] == 'del':
                    if property_name not in _property_list:
                        del_property_func = classdict.get(k)
                        get_property_func = classdict.get(
                            'get' + property_name, def_p_get
                            )
                        set_property_func = classdict.get(
                            'set' + property_name, def_p_set
                            )

                        setattr(self, property_name, None)
                        setattr(self.__class__, property_name[1:],
                                property(get_property_func,
                                         set_property_func,
                                         del_property_func))
                _property_list.append(property_name)

        classdict["create_property"] = create_property

        if '__init__' in classdict:
            init = classdict['__init__']

            def aid(self):
                self.create_property()
                init(self)
            classdict['__init__'] = aid

        return type.__new__(cls, classname, bases, classdict)
