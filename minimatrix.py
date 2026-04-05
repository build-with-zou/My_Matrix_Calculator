# Framework for IEEE course final project
# Fan Cheng, 2022
import random
import copy
import math
class Matrix:
	r"""
	自定义的二维矩阵类

	Args:
		data: 一个二维的嵌套列表，表示矩阵的数据。即 data[i][j] 表示矩阵第 i+1 行第 j+1 列处的元素。
			  当参数 data 不为 None 时，应根据参数 data 确定矩阵的形状。默认值: None
		dim: 一个元组 (n, m) 表示矩阵是 n 行 m 列, 当参数 data 为 None 时，根据该参数确定矩阵的形状；
			 当参数 data 不为 None 时，忽略该参数。如果 data 和 dim 同时为 None, 应抛出异常。默认值: None
		init_value: 当提供的 data 参数为 None 时，使用该 init_value 初始化一个 n 行 m 列的矩阵，
					即矩阵各元素均为 init_value. 当参数 data 不为 None 时，忽略该参数。 默认值: 0
	
	Attributes:
		dim: 一个元组 (n, m) 表示矩阵的形状
		data: 一个二维的嵌套列表，表示矩阵的数据

	Examples:
		>>> mat1 = Matrix(dim=(2, 3), init_value=0)
		>>> print(mat1)
		>>> [[0 0 0]
			 [0 0 0]]
		>>> mat2 = Matrix(data=[[0, 1], [1, 2], [2, 3]])
		>>> print(mat2)
		>>> [[0 1]
			 [1 2]
			 [2 3]]
	"""
	def __init__(self, data=None, dim=None, init_value=0):
		self.data = data
		self.dim = dim
		self.init_value = init_value
		if self.data != None:
			self.dim =(len(self.data),len(self.data[0]))
		else:
			if self.dim == None:
				raise ValueError('Lack enough variables.')
			else:
				if self.init_value == None:
					raise ValueError('Lack init value.')
				else:
					self.data = [[self.init_value] * self.dim[1] for _ in range(self.dim[0])]
		

	def shape(self):
		r"""
		返回矩阵的形状 dim
		"""
		return self.dim
		# if self.data == None:
		# 	if self.dim == None :
		# 		raise ValueError('输入的矩阵不能没有数值也没有形状')
		# 	else:
		# 		return self.dim
		# else:
		# 	self.dim =  (len(self.data),len(self.data[0]))
		# 	return self.dim

	def reshape(self, newdim):
		r"""
		将矩阵从(m,n)维拉伸为newdim=(m1,n1)
		该函数不改变 self
		
		Args:
			newdim: 一个元组 (m1, n1) 表示拉伸后的矩阵形状。如果 m1 * n1 不等于 self.dim[0] * self.dim[1],
					应抛出异常
		
		Returns:
			Matrix: 一个 Matrix 类型的返回结果, 表示 reshape 得到的结果
		"""
		if newdim[0] * newdim[1] != self.dim[0] * self.dim[1]:
			raise ValueError('两个矩阵的数据量不一样，无法完成拉伸')
		else:
			total_lst = []
			for lst in self.data:
				for item in lst:
					total_lst.append(item)
			total_lst = total_lst[::-1]
			ans_lst = [[] for _ in range(newdim[0])]

			for i in range(newdim[0]):
				for j in range(newdim[1]):
					current = total_lst.pop()
					ans_lst[i].append(current)
			return Matrix(data = ans_lst)
		

	def dot(self, other):
		r"""
		矩阵乘法：矩阵乘以矩阵
		按照公式 A[i, j] = \sum_k B[i, k] * C[k, j] 计算 A = B.dot(C)

		Args:
			other: 参与运算的另一个 Matrix 实例
		
		Returns:
			Matrix: 计算结果
		
		Examples:
			>>> A = Matrix(data=[[1, 2], [3, 4]])
			>>> A.dot(A)
			>>> [[ 7 10]
				 [15 22]]
		"""
		if not isinstance(other,Matrix):
			raise ValueError('Other should belong to "Matrix".')
		if self.dim[1] != other.dim[0]:
			raise ValueError('The two matrixes cannot be dotted.')
		else:
			size = self.dim[1]
			ans_lst = [[] for _ in range(self.dim[0])]
			for i in range(self.dim[0]):
				for j in range(other.dim[1]):
					ans = 0
					for k in range(size):
						ans += self.data[i][k] * other.data[k][j]
					ans_lst[i].append(ans)
			return Matrix(data=ans_lst)

### 矩阵乘法需要优化					

		
	
	def T(self):
		r"""
		矩阵的转置

		Returns:
			Matrix: 矩阵的转置

		Examples:
			>>> A = Matrix(data=[[1, 2], [3, 4]])
			>>> A.T()
			>>> [[1 3]
				 [2 4]]
			>>> B = Matrix(data=[[1, 2, 3], [4, 5, 6]])
			>>> B.T()
			>>> [[1 4]
				 [2 5]
				 [3 6]]
		"""
		ans_lst = []
		for i in range(self.dim[1]):
			lst = []
			for j in range(self.dim[0]): 
				lst.append(self.data[j][i])
			ans_lst.append(lst)
		return Matrix(data=ans_lst)
				


	def sum(self, axis=None): 
		r"""
		根据指定的坐标轴对矩阵元素进行求和

		Args:
			axis: 一个整数，或者 None. 默认值: None
				  axis = 0 表示对矩阵进行按列求和，得到形状为 (1, self.dim[1]) 的矩阵
				  axis = 1 表示对矩阵进行按行求和，得到形状为 (self.dim[0], 1) 的矩阵
				  axis = None 表示对矩阵全部元素进行求和，得到形状为 (1, 1) 的矩阵
		
		Returns:
			Matrix: 一个 Matrix 类的实例，表示求和结果

		Examples:
			>>> A = Matrix(data=[[1, 2, 3], [4, 5, 6]])
			>>> A.sum()
			>>> [[21]]
			>>> A.sum(axis=0)
			>>> [[5 7 9]]
			>>> A.sum(axis=1)
			>>> [[6]
				 [15]]
		"""
		if axis == 1:
			ans_lst = []
			for i in range(self.dim[0]):
				ans_lst.append([sum(self.data[i])])
			return Matrix(data = ans_lst)
		elif axis == 0:
			ans_lst = [[]]
			ans_lst_ = self.T().sum(axis=1).data
			for item in ans_lst_:
				ans_lst[0].append(item[0])
			return Matrix(data = ans_lst)
		if axis == None:
			ans = 0
			for i in range(self.dim[0]):
				for j in range(self.dim[1]):
					ans += self.data[i][j]
			return Matrix(data=[[ans]])
		


	def copy(self):
		r"""
		返回matrix的一个备份

		Returns:
			Matrix: 一个self的备份
		"""
		return Matrix(data=copy.deepcopy(self.data))

	def Kronecker_product(self, other):
		r"""
		计算两个矩阵的Kronecker积，具体定义可以搜索，https://baike.baidu.com/item/克罗内克积/6282573

		Args:
			other: 参与运算的另一个 Matrix

		Returns:
			Matrix: Kronecke product 的计算结果
		"""
		if not isinstance(other,Matrix):
			raise ValueError('Other should belong to "Matrix".')
		else:
			ans_lst = [[] for _ in range((self.dim[0] * other.dim[0]))]
			for r1 in range(self.dim[0]):
				for r2 in range(other.dim[0]):
					for l1 in range(self.dim[1]):
						for l2 in range(other.dim[1]):
							ans_lst[r2 + r1 * other.dim[0]].append(self.data[r1][l1] * other.data[r2][l2])
			return Matrix(data = ans_lst)
			

	
	def __getitem__(self, key):
		r"""
		实现 Matrix 的索引功能，即 Matrix 实例可以通过 [] 获取矩阵中的元素（或子矩阵）

		x[key] 具备以下基本特性：
		1. 单值索引
			x[a, b] 返回 Matrix 实例 x 的第 a 行, 第 b 列处的元素 (从 0 开始编号)
		2. 矩阵切片
			x[a:b, c:d] 返回 Matrix 实例 x 的一个由 第 a, a+1, ..., b-1 行, 第 c, c+1, ..., d-1 列元素构成的子矩阵
			特别地, 需要支持省略切片左(右)端点参数的写法, 如 x 是一个 n 行 m 列矩阵, 那么
			x[:b, c:] 的语义等价于 x[0:b, c:m]
			x[:, :] 的语义等价于 x[0:n, 0:m]

		Args:
			key: 一个元组，表示索引

		Returns:
			索引结果，单个元素或者矩阵切片

		Examples:
			>>> x = Matrix(data=[
						[0, 1, 2, 3],
						[4, 5, 6, 7],
						[8, 9, 0, 1]
					])
			>>> x[1, 2]
			>>> 6
			>>> x[0:2, 1:4]
			>>> [[1 2 3]
				 [5 6 7]]
			>>> x[:, :2]
			>>> [[0 1]
				 [4 5]
				 [8 9]]
		"""
		if not isinstance(key, tuple):
			raise ValueError('Key should be a "tuple".')
    
		if len(key) != 2:
			raise ValueError('Key tuple should have exactly 2 elements (row, column).')
		
		row_key, col_key = key
		
		if isinstance(row_key, int):
			if row_key < 0 or row_key >= self.dim[0]:
				raise IndexError('Row index out of range.')
			row_start = row_key
			row_stop = row_key + 1
			row_step = 1
		elif isinstance(row_key, slice):
			row_start = row_key.start if row_key.start is not None else 0
			row_stop = row_key.stop if row_key.stop is not None else self.dim[0]
			row_step = row_key.step if row_key.step is not None else 1
		else:
			raise TypeError('Row key must be int or slice.')
		
		if isinstance(col_key, int):
			if col_key < 0 or col_key >= self.dim[1]:
				raise IndexError('Column index out of range.')
			col_start = col_key
			col_stop = col_key + 1
			col_step = 1
		elif isinstance(col_key, slice):
			col_start = col_key.start if col_key.start is not None else 0
			col_stop = col_key.stop if col_key.stop is not None else self.dim[1]
			col_step = col_key.step if col_key.step is not None else 1
		else:
			raise TypeError('Column key must be int or slice.')
		
		# 处理负索引
		if row_start < 0:
			row_start += self.dim[0]
		if row_stop < 0:
			row_stop += self.dim[0]
		if col_start < 0:
			col_start += self.dim[1]
		if col_stop < 0:
			col_stop += self.dim[1]
		
		# 边界检查
		row_start = max(0, min(row_start, self.dim[0]))
		row_stop = max(0, min(row_stop, self.dim[0]))
		col_start = max(0, min(col_start, self.dim[1]))
		col_stop = max(0, min(col_stop, self.dim[1]))
		
		# 如果两个都是整数，返回单个元素
		if isinstance(row_key, int) and isinstance(col_key, int):
			return self.data[row_start][col_start]
		
		# 否则返回子矩阵
		result_data = []
		for i in range(row_start, row_stop, row_step):
			row = []
			for j in range(col_start, col_stop, col_step):
				row.append(self.data[i][j])
			if row:  # 避免空行
				result_data.append(row)
	
		return Matrix(data=result_data)

	def __setitem__(self, key, value):
		r"""
		实现 Matrix 的赋值功能, 通过 x[key] = value 进行赋值的功能

		类似于 __getitem__ , 需要具备以下基本特性:
		1. 单元素赋值
			x[a, b] = k 的含义为，将 Matrix 实例 x 的 第 a 行, 第 b 处的元素赋值为 k (从 0 开始编号)
		2. 对矩阵切片赋值
			x[a:b, c:d] = value 其中 value 是一个 (b-a)行(d-c)列的 Matrix 实例
			含义为, 将由 Matrix 实例 x 的第 a, a+1, ..., b-1 行, 第 c, c+1, ..., d-1 列元素构成的子矩阵 赋值为 value 矩阵
			即 子矩阵的 (i, j) 位置赋值为 value[i, j]
			同样地, 这里也需要支持如 x[:b, c:] = value, x[:, :] = value 等省略写法
		
		Args:
			key: 一个元组，表示索引
			value: 赋值运算的右值，即要赋的值

		Examples:
			>>> x = Matrix(data=[
						[0, 1, 2, 3],
						[4, 5, 6, 7],
						[8, 9, 0, 1]
					])
			>>> x[1, 2] = 0
			>>> x
			>>> [[0 1 2 3]
				 [4 5 0 7]
				 [8 9 0 1]]
			>>> x[1:, 2:] = Matrix(data=[[1, 2], [3, 4]])
			>>> x
			>>> [[0 1 2 3]
				 [4 5 1 2]
				 [8 9 3 4]]
		"""
		if not isinstance(key, tuple):
			raise ValueError('Key should be a "tuple".')
		if len(key) != 2:
			raise ValueError('Key tuple should have exactly 2 elements (row, column).')
		row_key , column_key = key
		if isinstance(row_key,int):
			if row_key < 0 or row_key > self.dim[0]:
				raise ValueError('The row index is out of range.')
			row_start = row_key
			row_stop = row_key + 1
			
		elif isinstance(row_key,slice):
			row_start = row_key.start if row_key.start is not None else 0
			row_stop = row_key.stop if row_key.stop is not None else self.dim[0]
			
		else:
			raise TypeError('The row index should be slice or int.')
		
		if isinstance(column_key,int):
			if column_key < 0 or column_key > self.dim[1]:
				raise ValueError('The column index is out of range.')
			column_start = column_key
			column_stop = column_key + 1

		elif isinstance(column_key,slice):
			column_start = column_key.start if column_key.start is not None else 0
			column_stop = column_key.stop if column_key.stop is not None else self.dim[1]
		else:
			raise TypeError('The column index should be slice or int.')
		
		# 处理负索引
		if row_start < 0:
			row_start += self.dim[0]
		if row_stop < 0:
			row_stop += self.dim[0]
		if column_start < 0:
			column_start += self.dim[1]
		if column_stop < 0:
			column_stop += self.dim[1]

		# 边界检查
		row_start = max(0, min(row_start, self.dim[0]))
		row_stop = max(0, min(row_stop, self.dim[0]))
		column_start = max(0, min(column_start, self.dim[1]))
		column_stop = max(0, min(column_stop, self.dim[1]))

		ans_lst = self.data

		if isinstance(value,Matrix):
			value = value.data

		if isinstance(row_key, int) and isinstance(column_key, int):
			# python 是动态类型
			ans_lst[row_key][column_key] = value
		elif isinstance(row_key,slice) and isinstance(column_key,int) :
			if not isinstance(value,list):
				raise ValueError('The value has the wrong size.')
			elif len(value) != row_stop - row_start or len(value[0]) != 1:
				raise ValueError('The value has the wrong size.')
			else:
				for i in range(len(value)):
					ans_lst[row_start + i][column_key] =  value[i][0]
				return None
		elif isinstance(row_key,int) and isinstance(column_key,slice):
			if not isinstance(value,list):
				raise ValueError('The value has the wrong size.')
			elif len(value) != 1 or len(value[0]) != column_stop - column_start:
				raise ValueError('The value has the wrong size.')
			else:
				ans_lst[row_key][column_start:column_stop] = value[0]
				return None
		else:
			size_row = row_stop - row_start
			size_column = column_stop - column_start
			if not isinstance(value,list):
				raise ValueError('The value has the wrong size.')
			elif len(value) != size_row or len(value[0]) != size_column:
				raise ValueError('The value has the wrong size.')
			else:
				for i in range(size_row):
					ans_lst[row_start + i][column_start:column_stop] = [_ for _ in value[i]]
				return None

			
		
	def __pow__(self, n):
		r"""
		矩阵的n次幂，n为自然数
		该函数应当不改变 self 的内容

		Args:
			n: int, 自然数

		Returns:
			Matrix: 运算结果
		"""
		if self.dim[0] != self.dim[1]:
			raise ValueError("Matrix must be square for exponentiation.")
		
		if n == 0:
			result = Matrix(dim=(self.dim[0], self.dim[0]), init_value=0)
			for i in range(self.dim[0]):
				result.data[i][i] = 1
			return result
		
		if n == 1:
			return self.copy()
		
		result = Matrix(dim=(self.dim[0], self.dim[0]), init_value=0)
		for i in range(self.dim[0]):
			result.data[i][i] = 1  
		base = self.copy()
		power = n
		
		while power > 0:
			if power % 2 == 1:
				result = result.dot(base)
			base = base.dot(base)
			power //= 2
		
		return result

	def __add__(self, other):
		r"""
		两个矩阵相加
		该函数应当不改变 self 和 other 的内容

		Args:
			other: 一个 Matrix 实例
		
		Returns:
			Matrix: 运算结果
		"""
		if self.dim[0] != other.dim[0] or self.dim[1] != other.dim[1] :
			raise ValueError("The two Matrix should have same size.") 
		length = self.dim[1]
		height = self.dim[0]
		result = self.copy()
		for i in range(height):
			for j in range(length):
				result.data[i][j] += other.data[i][j]
		return Matrix(data=result.data)

	def __sub__(self, other):
		r"""
		两个矩阵相减
		该函数应当不改变 self 和 other 的内容

		Args:
			other: 一个 Matrix 实例
		
		Returns:
			Matrix: 运算结果
		"""
		if self.dim[0] != other.dim[0] or self.dim[1] != other.dim[1] :
			raise ValueError("The two Matrix should have same size.") 
		length = self.dim[1]
		height = self.dim[0]
		result = self.copy()
		for i in range(height):
			for j in range(length):
				result.data[i][j] -= other.data[i][j]
		return Matrix(data=result.data)

	def __mul__(self, other):
		r"""
		两个矩阵 对应位置 元素  相乘
		注意 不是矩阵乘法dot
		该函数应当不改变 self 和 other 的内容

		Args:
			other: 一个 Matrix 实例
		
		Returns:
			Matrix: 运算结果

		Examples:
			>>> Matrix(data=[[1, 2]]) * Matrix(data=[[3, 4]])
			>>> [[3 8]]
		"""
		if self.dim[0] != other.dim[0] or self.dim[1] != other.dim[1] :
			raise ValueError("The two Matrix should have same size.") 
		length = self.dim[1]
		height = self.dim[0]
		result = self.copy()
		for i in range(height):
			for j in range(length):
				result.data[i][j] *= other.data[i][j]
		return Matrix(data=result.data)


	def __len__(self):
		r"""
		返回矩阵元素的数目

		Returns:
			int: 元素数目，即 行数 * 列数
		"""
		return self.dim[0] * self.dim[1]

	def __str__(self):
		r"""
		按照
		[[  0   1   4   9  16  25  36  49]
 		 [ 64  81 100 121 144 169 196 225]
 		 [256 289 324 361 400 441 484 529]]
 		的格式将矩阵表示为一个 字符串
 		！！！ 注意返回值是字符串
		"""
		height = self.dim[0]
		ans = ''
		for i in range(height):
			ans_row = ''
			for item in self.data[i]:
				ans_row += f'{item:>8}'
			ans_row = f'[{ans_row}]\n'
			ans += ans_row
		ans = f'[\n{ans}]'
		return ans


	def det(self):
		r"""
		计算方阵的行列式。对于非方阵的情形应抛出异常。
		要求: 该函数应不改变 self 的内容; 该函数的时间复杂度应该不超过 O(n**3).
		提示: Gauss消元
		
		Returns:
			一个 Python int 或者 float, 表示计算结果
		"""
		if self.dim[0] != self.dim[1]:
			raise ValueError('Matrix must be square.')
		change_times = 0 # 用于记录交换行的次数，交换行会改变行列式的符号
		copy_data = self.copy().data
		# 行变换过程
		for i in range(self.dim[0]):
			if copy_data[i][i] == 0: # 如果主元为0，尝试交换下面的行
				for j in range(i+1,self.dim[0]):
					if copy_data[j][i] != 0:
						copy_data[i],copy_data[j] = copy_data[j],copy_data[i]
						change_times += 1
						break
			if copy_data[i][i] == 0: # 如果交换行后主元仍然为0，说明行列式为0
				return 0
			for j in range(i+1,self.dim[0]):
				mul = copy_data[j][i] / copy_data[i][i]
				for k in range(i,self.dim[1]):
					copy_data[j][k] -= (copy_data[i][k] *mul)
			
		result = 1 
		for i in range(self.dim[0]):
			result *= copy_data[i][i]
		if change_times % 2 == 1: # 如果交换行的次数是奇数，那么行列式的符号需要改变
			result = -result
		return result
		

	def inverse(self):
		r"""
		计算非奇异方阵的逆矩阵。对于非方阵或奇异阵的情形应抛出异常。
		要求: 该函数应不改变 self 的内容; 该函数的时间复杂度应该不超过 O(n**3).
		提示: Gauss消元
		
		Returns:
			Matrix: 一个 Matrix 实例，表示逆矩阵
		"""
		if self.dim[0] != self.dim[1]:
			raise ValueError('The Matrix should be square.')
		
		n = self.dim[0]
		
		# 创建增广矩阵 [A | I]
		aug = [[0.0] * (2 * n) for _ in range(n)]
		for i in range(n):
			# 复制原矩阵A
			for j in range(n):
				aug[i][j] = float(self.data[i][j])
			# 添加单位矩阵
			aug[i][n + i] = 1.0
		
		for col in range(n):
			# 部分主元选择：找到当前列中绝对值最大的元素所在的行
			max_row = col
			max_val = abs(aug[col][col])
			
			for row in range(col + 1, n):
				if abs(aug[row][col]) > max_val:
					max_val = abs(aug[row][col])
					max_row = row
			
			# 检查矩阵是否奇异
			if max_val < 1e-12:
				raise ValueError("Matrix is singular or nearly singular")
			
			# 交换当前行和最大主元行
			if max_row != col:
				aug[col], aug[max_row] = aug[max_row], aug[col]
			
			# 归一化主元行
			pivot = aug[col][col]
			for j in range(col, 2 * n):
				aug[col][j] /= pivot
			
			# 消去其他行的当前列
			for row in range(n):
				if row != col:
					factor = aug[row][col]
					if abs(factor) > 1e-15:  # 避免不必要的计算
						for j in range(col, 2 * n):
							aug[row][j] -= factor * aug[col][j]
		
		# 提取逆矩阵
		inv_data = []
		for i in range(n):
			inv_data.append(aug[i][n:])
		
		return Matrix(data=inv_data)


	def rank(self):
		r"""
		计算矩阵的秩
		要求: 该函数应不改变 self 的内容; 该函数的时间复杂度应该不超过 O(n**3).
		提示: Gauss消元

		Returns:
			一个 Python int 表示计算结果
		"""

		mat = [row[:] for row in self.data]   # 深拷贝
		rows, cols = self.dim
		rank = 0
		row = 0 # 当前正在处理的行索引（也是下一个可能成为主元的行）
		for col in range(cols):
			# 寻找当前列从 row 行开始向下的第一个非零元素
			pivot = row
			while pivot < rows and mat[pivot][col] == 0:
				pivot += 1
			if pivot == rows:
				continue   # 当前列全为零，检查下一列
			# 交换到当前行
			if pivot != row:
				mat[row], mat[pivot] = mat[pivot], mat[row]
			# 消去下面所有行的当前列
			for r in range(row+1, rows):
				if mat[r][col] != 0:
					factor = mat[r][col] / mat[row][col]
					for c in range(col, cols):
						mat[r][c] -= factor * mat[row][c]
			rank += 1
			row += 1
			if row == rows:
				break
		return rank
def I(n):
	'''
	return an n*n unit matrix
	'''
	if n <= 0:
		raise ValueError("The Matrix must have a positive dim.")
	result = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if i == j:
				result [i][j] = 1
	return Matrix(data = result)

def narray(dim, init_value=1): # dim (,,,,,), init为矩阵元素初始值
	r"""
	返回一个matrix，维数为dim，初始值为init_value
	
	Args:
		dim: Tuple[int, int] 表示矩阵形状
		init_value: 表示初始值，默认值: 1

	Returns:
		Matrix: 一个 Matrix 类型的实例
	"""
	return Matrix(dim = dim, init_value = init_value)

def arange(start, end, step):
	r"""
	返回一个1*n 的 narray 其中的元素类同 range(start, end, step)

	Args:
		start: 起始点(包含)
		end: 终止点(不包含)
		step: 步长

	Returns:
		Matrix: 一个 Matrix 实例
	"""
	result = [[]]
	for i in range(start,end,step):
		result[0].append(i)
	return Matrix(data = result)

def zeros(dim):
	r"""
	返回一个维数为dim 的全0 narray

	Args:
		dim: Tuple[int, int] 表示矩阵形状

	Returns:
		Matrix: 一个 Matrix 类型的实例
	"""
	return Matrix(dim=dim,init_value=0)

def zeros_like(matrix):
	r"""
	返回一个形状和matrix一样 的全0 narray

	Args:
		matrix: 一个 Matrix 实例
	
	Returns:
		Matrix: 一个 Matrix 类型的实例

	Examples:
		>>> A = Matrix(data=[[1, 2, 3], [2, 3, 4]])
		>>> zeros_like(A)
		>>> [[0 0 0]
			 [0 0 0]]
	"""
	if  not isinstance(matrix,Matrix):
		raise TypeError("The input should be in the class Matrix")
	dim1 = (matrix.dim[0],matrix.dim[1])
	return Matrix(dim = dim1,init_value=0)

def ones(dim):
	r"""
	返回一个维数为dim 的全1 narray
	类同 zeros
	"""
	return Matrix(dim=dim,init_value=1)

def ones_like(matrix):
	r"""
	返回一个维数和matrix一样 的全1 narray
	类同 zeros_like
	"""
	if  not isinstance(matrix,Matrix):
		raise TypeError("The input should be in the class Matrix")
	dim1 = (matrix.dim[0],matrix.dim[1])
	return Matrix(dim = dim1,init_value=1)

def nrandom(dim):
	r"""
	返回一个维数为dim 的随机 narray
	参数与返回值类型同 zeros
	"""
	result = [[random.random() for _ in range(dim[1])] for _ in range(dim[0])]
	return Matrix(data = result)

def nrandom_like(matrix):
	r"""
	返回一个维数和matrix一样 的随机 narray
	参数与返回值类型同 zeros_like
	"""
	dim = matrix.dim[0],matrix.dim[1]
	return nrandom(dim = dim)

def concatenate(items, axis=0):
	r"""
	将若干矩阵按照指定的方向拼接起来
	若给定的输入在形状上不对应，应抛出异常
	该函数应当不改变 items 中的元素

	Args:
		items: 一个可迭代的对象，其中的元素为 Matrix 类型。
		axis: 一个取值为 0 或 1 的整数，表示拼接方向，默认值 0.
			  0 表示在第0维即行上进行拼接
			  1 表示在第1维即列上进行拼接
	
	Returns:
		Matrix: 一个 Matrix 类型的拼接结果

	Examples:
		>>> A, B = Matrix([[0, 1, 2]]), Matrix([[3, 4, 5]])
		>>> concatenate((A, B))
		>>> [[0 1 2]
			 [3 4 5]]
		>>> concatenate((A, B, A), axis=1)
		>>> [[0 1 2 3 4 5 0 1 2]]
	"""

	if axis == 1:
		size = items[0].dim[0]
		result = items[0].copy().data
		for i in range(1,len(items)):
			if items[i].dim[0] != size :
				raise ValueError("The Matrixes can't be concatenated together.")
		for i in range(size):
			for j in range(1,len(items)):
				result[i] += items[j].data[i]
		return Matrix(data = result)
	else:
		size = items[0].dim[1]
		result = items[0].copy().data
		for i in range(1,len(items)):
			if items[i].dim[1] != size:
				raise ValueError("The Matrixes can't be concatenated together.")
		for i in range(1,len(items)):
			for j in range(items[0].dim[0]):
				result .append(items[i].data[j])
		return Matrix(data = result)




def vectorize(func):
	r"""
	将给定函数进行向量化
	
	Args:
		func: 一个Python函数
	
	Returns:
		一个向量化的函数 F: Matrix -> Matrix, 它的参数是一个 Matrix 实例 x, 返回值也是一个 Matrix 实例；
		它将函数 func 作用在 参数 x 的每一个元素上
	
	Examples:
		>>> def func(x):
				return x ** 2
		>>> F = vectorize(func)
		>>> x = Matrix([[1, 2, 3],[2, 3, 1]])
		>>> F(x)
		>>> [[1 4 9]
			 [4 9 1]]
		>>> 
		>>> @vectorize
		>>> def my_abs(x):
				if x < 0:
					return -x
				else:
					return x
		>>> y = Matrix([[-1, 1], [2, -2]])
		>>> my_abs(y)
		>>> [[1, 1]
			 [2, 2]]
	"""
	def f(x):
		result = x.copy().data
		for i in range(x.dim[0]):
			for j in range(x.dim[1]):
				result [i][j] = func(result[i][j])
		return Matrix(data = result)
	return f

def LU_decomposition(self):
	r"""
	计算矩阵的LU分解

	Returns:
		L: 一个 Matrix 实例，表示下三角矩阵
		U: 一个 Matrix 实例，表示上三角矩阵
	"""
	if self.dim[0] != self.dim[1]: # 不是方阵
		raise ValueError("Matrix must be square.") 
	L_Matrix = I(self.dim[0])
	U_Matrix = self.copy()
	# 进行高斯消元，得到 U_Matrix 的上三角形式，同时记录下三角矩阵 L_Matrix
	cnt_row = 0 # 记录当前正在用于处理的行
	while True:
		if U_Matrix.data[cnt_row][cnt_row] == 0:
			raise ValueError("This matrix can't be decomposited by LU decomposition.") # 由于一般LU分解不考虑行交换，因此只要主元是0就无法分解
		for i in range(cnt_row+1,self.dim[0]):
			mul = U_Matrix.data[i][cnt_row] / U_Matrix.data[cnt_row][cnt_row]
			for j in range(cnt_row,self.dim[0]):
				U_Matrix.data[i][j] -= mul * U_Matrix.data[cnt_row][j]
				L_Matrix.data[i][j] = mul# 在L中乘上U中变换的逆
		cnt_row += 1
		if cnt_row == self.dim[0]:
			break
	return L_Matrix,U_Matrix
		

def LU_decomposition(self):
    n = self.dim[0]
    L = I(n)
    U = self.copy()
    for k in range(n):
        if abs(U.data[k][k]) < 1e-12:
            raise ValueError("Zero pivot")
        for i in range(k+1, n):
            mul = U.data[i][k] / U.data[k][k]
            # 对 U 做行减法
            for j in range(k, n):
                U.data[i][j] -= mul * U.data[k][j]
            # 对 L 做行加法（逆变换）
            for j in range(n):
                L.data[i][j] += mul * L.data[k][j]
    return L, U

def Cholesky_decomposition(self):
	if self.dim[0] != self.dim[1]:
		raise ValueError("The matrix should be square.")
	for i in range(self.dim[0]):
		if self[i,i] < 0:
			raise ValueError("This is not a ZHENGDING matrix.")
		for j in range(self.dim[0]):
			if self[i,j] != self[j,i] :
				raise ValueError("This is not a ZHENGDING matrix.")
	ans_L = zeros_like(self) # ans_L 是一个下三角矩阵
	cnt_row = cnt_col = 0
	for cnt_row in range(self.dim[0]):
		for cnt_col in range(cnt_row + 1): # 由于是上三角所以只要处理这些
			if cnt_col == 0:
				ans_L[cnt_row,cnt_col] = math.sqrt(self[0,0])  if cnt_row == 0 else self[cnt_row,cnt_col] / ans_L[0,0]
			elif cnt_col == cnt_row:
				cnt = self[cnt_row,cnt_col]
				for i in range(cnt_col):
					cnt -= ans_L[cnt_row,i] * ans_L[cnt_row,i]
				ans_L[cnt_row,cnt_col] = math.sqrt(cnt)
			else:
				cnt = self[cnt_row,cnt_col]
				for i in range(cnt_col):
					cnt -= ans_L[cnt_row,i] * ans_L[cnt_col,i]
				ans_L[cnt_row,cnt_col] = cnt / ans_L[cnt_col,cnt_col]
	
	return ans_L

					

				 


			
			
# def QR_decomposition(self):
# 	r"""
# 	计算矩阵的QR分解

# 	Returns:
# 		Q: 一个 Matrix 实例，表示正交矩阵
# 		R: 一个 Matrix 实例，表示上三角矩阵
# 	"""
# 	if self.dim[0] != self.dim[1]:
# 		raise ValueError('Matrix must be square for QR decomposition.')
	
# 	n = self.dim[0]
# 	Q = I(n)
# 	R = self.copy()
	
# 	for i in range(n):
# 		for j in range(i + 1, n):
# 			if R.data[j][i] != 0:
# 				r = (R.data[i][i] ** 2 + R.data[j][i] ** 2) ** 0.5
# 				c = R.data[i][i] / r
# 				s = -R.data[j][i] / r
				
# 				G = I(n)
# 				G.data[i][i] = c
# 				G.data[j][j] = c
# 				G.data[i][j] = -s
# 				G.data[j][i] = s
				
# 				R = G.dot(R)
# 				Q = Q.dot(G.T())
	
	# return Q, R			
if __name__ == "__main__":
	print("test here")
	# a = Matrix(data = [[1,2,3],[4,5,6],[7,8,9],])
	# b = Matrix(data = [[2,3,5],[6,8,9],[3,7,0]])
	# c = Matrix(data = [[1,1,1],[1,1,1],[1,1,1]])
	# print(a.shape())
	# print(a.reshape([1,9]).data)
	# print(a.dot(a).data)
	# print(a.T().data)
	# print(a.sum(axis= None).data)
	# print(a.copy().data)
	# print(a.Kronecker_product(a).data)
	# print(a.__pow__(3).data)
	# print(a.__add__(b).data)
	# print(a.__sub__(b).data)
	# print(a.__mul__(b).data)
	# print(a.__len__())
	# print(a.__str__())
	# print(b.det())
	# print(b.rank())
	# print(I(4))
	# print(narray(dim = (4,4),init_value=3))
	# print(ones((5,5)))
	# print(ones_like(b))
	# print(nrandom(dim = (3,3)).data)
	# print(nrandom_like(b))
	# print(concatenate((a,b,c),axis= 0))
	# def func(x):
	# 	return x + 1
	# F =vectorize(func)
	# print(F(b).data)
	a = Matrix(data = [[1,0.5,0.2],[0.5,1,0.3],[0.2,0.3,1]])
	print(Cholesky_decomposition(a))