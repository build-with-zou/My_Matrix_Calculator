# MiniMatrix 使用文档

## 简介

`minimatrix.py` 是一个轻量级的 Python 矩阵库，实现了自定义的 `Matrix` 类及其常用操作。它不依赖 NumPy，完全基于原生 Python 列表实现，适合教学演示或小型数值计算任务。

主要特性：
- 矩阵基本运算：加法、减法、点乘（对应元素相乘）、矩阵乘法（`dot`）、转置、幂运算
- 矩阵变换：重塑（`reshape`）、拼接（`concatenate`）、Kronecker 积
- 数值分解：LU 分解（无行交换）、带部分选主元的 LU 分解（PA=LU）、Cholesky 分解
- 线性代数：行列式、逆矩阵、矩阵的秩
- 方便的工厂函数：单位矩阵 `I`、全零/全一矩阵、随机矩阵、`arange` 等
- 支持切片索引和赋值（类似 NumPy 的语法）

---

## 安装与依赖

无需额外安装，直接复制 `minimatrix.py` 到你的项目中即可。

**依赖**：仅使用 Python 标准库（`random`, `copy`, `math`）。

---

## 快速开始

```python
from minimatrix import Matrix, I, zeros, ones, nrandom, concatenate

# 创建矩阵
A = Matrix(data=[[1, 2], [3, 4]])
B = Matrix(dim=(2, 3), init_value=0)   # 2x3 全零矩阵

# 基本运算
C = A.dot(A)            # 矩阵乘法
D = A + A               # 加法
E = A.T()               # 转置

# 分解
P, L, U = A.LU_decomposition_with_partial_pivoting()   # PA = LU

# 逆与行列式
invA = A.inverse()
detA = A.det()

# 索引和切片
print(A[0, 1])          # 2
A[0:2, 0:1] = Matrix([[10], [40]])   # 修改子矩阵
```

---

## 类与函数参考

### `Matrix` 类

#### 构造方法

```python
Matrix(data=None, dim=None, init_value=0)
```

- `data`：二维列表，如 `[[1,2],[3,4]]`。若提供，则忽略 `dim`。
- `dim`：元组 `(n, m)`，指定行数和列数。
- `init_value`：当 `data` 为 `None` 时，用该值填充矩阵。

若 `data` 和 `dim` 均为 `None`，抛出异常。

#### 属性

- `dim`：返回 `(行数, 列数)` 元组。
- `data`：存储矩阵数据的二维列表。

#### 主要方法

| 方法 | 描述 |
|------|------|
| `shape()` | 返回矩阵形状 `(n, m)` |
| `reshape(newdim)` | 重塑为 `newdim`，不改变原矩阵 |
| `dot(other)` | 矩阵乘法 `self · other` |
| `T()` | 转置 |
| `sum(axis=None)` | 求和：`axis=0` 按列，`axis=1` 按行，`None` 全部元素 |
| `copy()` | 深拷贝 |
| `Kronecker_product(other)` | Kronecker 积 |
| `det()` | 计算行列式（要求方阵，O(n³)） |
| `inverse()` | 求逆矩阵（要求非奇异方阵） |
| `rank()` | 计算矩阵的秩 |
| `LU_decomposition()` | 普通 LU 分解（要求所有顺序主子式非零） |
| `LU_decomposition_with_partial_pivoting()` | PLU 分解，返回 `(P, L, U)`，满足 `PA = LU` |
| `Cholesky_decomposition()` | Cholesky 分解（要求对称正定），返回下三角矩阵 `L` |

#### 索引与赋值

支持类似 NumPy 的索引语法：

```python
# 单元素访问
x = A[2, 3]

# 切片
sub = A[1:3, 2:5]

# 省略写法
row0 = A[0, :]          # 第一行
col1 = A[:, 1]          # 第二列

# 赋值
A[1, 2] = 99
A[0:2, 1:3] = Matrix([[5,6],[7,8]])
```

> 注意：切片返回的是新的 `Matrix` 对象，不是视图。

#### 运算符重载

| 运算符 | 含义 |
|--------|------|
| `+` | 矩阵加法（对应元素相加） |
| `-` | 矩阵减法 |
| `*` | **对应元素相乘**（不是矩阵乘法） |
| `**n` | 矩阵幂（方阵，n 为自然数） |
| `len()` | 返回元素总个数（行数 × 列数） |
| `str()` | 格式化输出，每个元素占 8 字符宽度 |

---

### 全局函数

| 函数 | 描述 |
|------|------|
| `I(n)` | 返回 n 阶单位矩阵 |
| `zeros(dim)` | 返回全零矩阵 |
| `zeros_like(matrix)` | 返回与给定矩阵形状相同的全零矩阵 |
| `ones(dim)` | 返回全一矩阵 |
| `ones_like(matrix)` | 返回与给定矩阵形状相同的全一矩阵 |
| `narray(dim, init_value=1)` | 返回指定形状、指定初始值的矩阵 |
| `arange(start, end, step)` | 返回 1×N 行矩阵，元素类似 `range(start,end,step)` |
| `nrandom(dim)` | 返回指定形状的随机矩阵（元素在 [0,1) 均匀分布） |
| `nrandom_like(matrix)` | 返回与给定矩阵形状相同的随机矩阵 |
| `concatenate(items, axis=0)` | 沿行（axis=0）或列（axis=1）拼接多个矩阵 |
| `vectorize(func)` | 将标量函数向量化，应用于矩阵的每个元素（可用作装饰器） |

---

## 使用示例

### 1. 创建矩阵

```python
from minimatrix import Matrix, I, zeros, ones, arange

A = Matrix(data=[[1,2],[3,4]])
B = Matrix(dim=(3,4), init_value=0)   # 3x4 零矩阵
C = I(3)                              # 3x3 单位矩阵
D = zeros((2,2))                      # 全零矩阵
E = ones((2,3))                       # 全一矩阵
F = arange(0, 10, 2)                  # 1x5 矩阵: [[0,2,4,6,8]]
```

### 2. 矩阵运算

```python
A = Matrix([[1,2],[3,4]])
B = Matrix([[5,6],[7,8]])

# 矩阵乘法
C = A.dot(B)   # 或 A @ B 需要 Python 3.5+，但未定义 @ 运算符

# 对应元素相乘
D = A * B

# 加法
E = A + B

# 转置
At = A.T()

# 幂运算
A2 = A ** 2    # A·A
```

### 3. 线性代数

```python
M = Matrix([[2,1,1],[1,2,1],[1,1,2]])

# 行列式
det = M.det()      # 4.0

# 逆矩阵
invM = M.inverse()

# 秩
rank = M.rank()    # 3

# Cholesky 分解（对称正定）
L = M.Cholesky_decomposition()
print(L.dot(L.T()))   # 应接近原矩阵
```

### 4. PLU 分解

```python
A = Matrix([[0, 2], [1, 1]])
P, L, U = A.LU_decomposition_with_partial_pivoting()

# 验证 PA = LU
PA = P.dot(A)
LU = L.dot(U)
print(PA.data)   # [[1,1],[0,2]]
print(LU.data)   # 相同
```

### 5. 使用 `vectorize`

```python
from minimatrix import vectorize

@vectorize
def my_abs(x):
    return x if x >= 0 else -x

M = Matrix([[-1, 2], [-3, 4]])
absM = my_abs(M)   # [[1,2],[3,4]]
```

### 6. 切片与赋值

```python
M = Matrix([[0,1,2],[3,4,5],[6,7,8]])

# 取子矩阵
sub = M[1:3, 0:2]     # [[3,4],[6,7]]

# 修改单个元素
M[0,0] = 99

# 修改子矩阵
M[1:, 1:] = Matrix([[40,50],[70,80]])
```

---

## 注意事项

1. **数值稳定性**：`det()` 和 `inverse()` 使用部分选主元的高斯消元，对病态矩阵可能产生较大误差。`LU_decomposition_with_partial_pivoting` 是推荐的分解方法。
2. **零阈值**：代码中使用 `1e-15` 作为判断是否为零的阈值，可根据需要修改。
3. **性能**：所有运算均为 O(n³) 或更低，但未做大规模优化，不适合超大规模矩阵。
4. **Cholesky 分解**：要求矩阵对称正定，代码会检查对角线元素非负及对称性，但未检查所有主子式。
5. **非方阵支持**：`rank()`、`reshape()`、`concatenate()`、`Kronecker_product()` 支持非方阵；但 `det`、`inverse`、`LU_decomposition` 要求方阵。
6. **切片行为**：切片返回的是新矩阵（深拷贝），不是原矩阵的视图。修改切片不会影响原矩阵。

---

## 许可证

本项目仅为教学/演示目的，无特定许可证。使用请遵守学术诚信。

---

## 更新日志

- **v1.0**：初始版本，包含 Matrix 类及基础分解功能。

---

## 作者

该代码为课程项目框架，由用户根据给定模板扩展实现。