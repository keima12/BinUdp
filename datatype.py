#from ctypes import *
import ctypes
class TestStructure(ctypes.BigEndianStructure):
    _fields_ = (
        ('test_num1',ctypes.c_int32),
        ('test_num2',ctypes.c_int32),
        ('test_code1', ctypes.c_uint8),
        ('test_code2', ctypes.c_uint8),
        ('test_num3', ctypes.c_uint16),
        ('test_num4', ctypes.c_uint32)
    )
    def __str__(self):
      return '{0},{1},{2},{3},{4},{5}'.format(self.test_num1, self.test_num2, self.test_code1,self.test_code2, self.test_num3, self.test_num4)