from nornir import InitNornir

def question_13(nr):
    print(nr.__dict__)
    pass

def question_14(nr):
    host = nr.inventory.hosts
    print(host)
    print(type(host))
    pass

def question_15(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-B']
    print(premier)
    print(type(premier))
    pass

def question_16(nr):
    premier = nr.inventory.hosts['R1-CPE-BAT-B']
    print(dir(premier))
    name = premier.name
    password = premier.password
    ip = premier.hostname
    print(name)
    print(password)
    print(ip)
    pass

def question_17(nr):
    pass

def question_18(nr):
    pass

def question_19(nr):
    pass

def question_20(nr):
    pass

def question_21(nr):
    pass

def question_22(nr):
    pass

def question_23(nr):
    pass

def question_24(nr):
    pass

def question_25(nr):
    pass

def question_26(nr):
    pass

def question_27(nr):
    pass

def question_29(nr):
    pass

def question_30(nr):
    pass

def question_32(nr):
    pass
 
def question_33(nr):
    pass

def question_34(nr):
    pass

def question_35(nr):
    pass

def question_36(nr):
    pass

def question_37(nr):
    pass

def question_38(nr):
    pass

def question_39(nr):
    pass

def question_39_d(nr):
    pass

def question_40(nr):
    pass
    

if __name__ == "__main__":
    nr = InitNornir(config_file="inventory/config.yaml")

    #question_13(nr)
    #question_14(nr)
    #question_15(nr)
    question_16(nr)
    #question_17(nr)
    #question_18(nr)
    #question_19(nr)
    #question_20(nr)
    #question_21(nr)
    #question_22(nr)
    #question_23(nr)
    #question_24(nr)
    #question_25(nr)
    #question_26(nr)
    #question_27(nr)
    #question_29(nr)
    #question_30(nr)

    #question_32(nr)
    #question_33(nr)
    #question_34(nr)
    #question_35(nr)
    #question_36(nr)
    #question_37(nr)
    #question_38(nr)
    #question_39(nr)
    #question_39_d(nr)

    #question_40(nr)
    pass
