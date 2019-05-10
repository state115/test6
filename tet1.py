# -*- coding:UTF-8 -*-
class parent:
    count = 100;
    __privateName = "zhansan";

    def __init__(self):
        print("fu init");
        self.age = 10;
        self.num = "12234";
        self.name = "fu";

    def setName(self, name):
        print("fulei setName");
        self.name = name;

    def getName(self):
        print("fulei getName");
        return self.name;

    def getPrivateName(self):
        return self.__privateName;


class child(parent):
    def __init__(self):
        parent.__init__(self);
        print("zilei init");

    def setName(self, name):
        parent.setName(self, name);
        print("zilei setName");

    def getName(self):
        print("zilei getName");
        return parent.getName(self);

    def getPrivateName(self):
        return parent.getPrivateName(self);


a = child();
print(a.getName());
print
a.count;
print
a.getPrivateName();