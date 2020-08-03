class Message:


    @classmethod
    def heart(cls, value):
        return f"IWAPG1,0,1@{value},95,60#"

    @classmethod
    def blood_pressure(cls, low, high):
        return f"IWAPG2,0{low}|{high}"


if __name__ == '__main__':
    m = getattr(Message, "heart")
    print(m(5))
