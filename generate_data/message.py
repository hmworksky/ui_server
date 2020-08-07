from common import conf


class Message:

    @classmethod
    def heart(cls, heart_value=conf.default_heart_value, **kwargs):
        """心率发送报文"""
        return f"IWAPG1,0,1@{heart_value},{conf.default_blood_oxygen_value},60#"

    @classmethod
    def blood_pressure(cls, systolic=conf.default_systolic, diastolic=conf.default_diastolic, **kwargs):
        """血压发送报文"""
        return f"IWAPG2,0{systolic}|{diastolic}#"

    @classmethod
    def blood_oxygen(cls, blood_oxygen_value=conf.default_blood_oxygen_value, **kwargs):
        """血氧发送报文"""
        return f"IWAPG1,0,1@{conf.default_heart_value},{blood_oxygen_value},60#"


if __name__ == '__main__':
    m = getattr(Message, "heart")
    print(m(5))
