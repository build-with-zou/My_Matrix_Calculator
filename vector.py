# Vector class implementation
# 作为minimatrix中的一个重要组件，Vector类提供了向量的基本操作和功能。
# 包括向量的创建、加法、减法、标量乘法、点积、叉积等常见的向量运算。
class Vector():
    def __init__(self,data):
        r"""
        通过传入一个列表或元组来创建一个向量对象。
        """
        self.data = data

    def __add__(self, other):
        r"""
        定义向量的加法运算

        Return: 一个新的Vector对象，表示两个向量的和。
        """
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be of the same length")
        return Vector([a + b for a, b in zip(self.data, other.data)])
    
    def __sub__(self, other):
        r"""
        定义向量的减法运算

        Return: 一个新的Vector对象，表示两个向量的差。
        """
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be of the same length")
        return Vector([a - b for a, b in zip(self.data, other.data)])
    
    def __mul__(self, scalar):
        r"""
        定义向量的标量乘法运算

        Return: 一个新的Vector对象，表示向量与标量的乘积。
        """
        return Vector([a * scalar for a in self.data])
    
    def dot(self, other):
        r"""
        定义向量的点积运算，即内积

        Return: 一个标量，表示两个向量的点积。
        """
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be of the same length")
        return sum(a * b for a, b in zip(self.data, other.data))
    
    def Schmitt(self, other):
        r"""
        定义向量的Schmitt正交化运算

        Input: 一个可迭代的对象other，用一个list表示正交化的基向量集合。
        Return: 一个新的Vector对象，表示向量经过Schmitt正交化后的结果。
        """
        
        for item in other:
            cnt = self.dot(item) / item.dot(item)
            self = self - item * cnt

        # 接下来可以对self进行归一化处理，使其成为一个单位向量
        norm = self.dot(self) ** 0.5
        if norm > 0:
            self = self * (1 / norm)
        return self

    def transpose(self):
        r"""
        定义向量的转置运算

        Return: 一个新的Vector对象，表示向量的转置。
        """
        data = []    
        for i in range(len(self.data)):
            data.append([self.data[i]])
        return Vector(data)