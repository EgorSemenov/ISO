from pulp import *

def print_matr(H,n,m):
    for i in range(n):
        for j in range(m):
            print(H[i][j], end=' ')
        print()

def enter_matr(n,m):
    H = [[0] * m for i in range(n)]
    print('вводите матрицу по строчно:')
    for i in range(n):
        row = input().split()
        for j in range(m):
            H[i][j] = int(row[j])
    return H

print('введите размер матрицы H:')
print('количество столбцов H:')
m = int(input())
print('количество строк H:')
n = int(input())

H = enter_matr(n, m)
print_matr(H, n, m)
EDGES = []
COSTS = []
for i in range(n):
    EDGES.append((0, 99999))
    COSTS.append(1)
D = []
for i in range(m):
    D.append(1)
X = []
prob = LpProblem("Problem", LpMinimize)
for i in range(n):
    temp_name = 'x'+str(i)
    X.append(LpVariable(temp_name, *EDGES[i]))
prob += lpDot(COSTS, X), "Costs"
for i in range(m):
    temp = 0
    for j in range(n):
        temp += H[j][i]*X[j]
    prob += temp >= D[i]
status = prob.solve()

# PRINT SOLUTION
# print()
# print(LpStatus[status])
Ix = 0
for ind, x in enumerate(X):
    print('x' + str(ind + 1), '=', value(x), end=' ')
    Ix += value(x)

Ix = 1/Ix


EDGES = []
COSTS = []
for i in range(m):
    EDGES.append((0, 999999999))
    COSTS.append(1)
D = []
for i in range(n):
    D.append(1)
Y = []
prob = LpProblem("Problem", LpMaximize)
for i in range(m):
    temp_name = 'y'+str(i)
    Y.append(LpVariable(temp_name, *EDGES[i]))
prob += lpDot(COSTS, Y), "Costs"
for i in range(n):
    temp = 0
    for j in range(m):
        temp += H[i][j] * Y[j]
    prob += temp <= D[i]
status = prob.solve()

# PRINT SOLUTION
# print(LpStatus[status])

Iy = 0
for ind, y in enumerate(Y):
    print('y' + str(ind + 1), '=', value(y), end=' ')
    Iy += value(y)

Iy = 1/Iy

print()
print()
print('-------')
print('Ответ:')
print('I = ', Ix)
for ind, x in enumerate(X):
    print('p', end='')
    print(ind+1, ' = ', value(x) * Ix, end='\t\t')
print()
for y in enumerate(Y):
    print('q', end='')
    print(y[0]+1, ' = ', value(y[1]) * Iy, end='\t\t')


# print('Программа, определяющая в зависимости от распределения количества учеников, какого типа автобусы следует использовать на каждом отрезке пути:')
# print('Расходы топлива установлены, следует ввести количество учеников в каждом населённом пунките:')
# print('Введите количество учеников, в населенном пункте C:')
# C = int(input())
# print('Введите количество учеников, в населенном пункте B:')
# B = int(input())
# print('Введите количество учеников, находящихся между населенным пунктом C и B:')
# CB = int(input())
# print('Введите количество учеников, находящихся между населенным пунктом A и B:')
# AB = int(input())
# EDGES = [(0, 35), (0, 50), (0, 35), (0, 50), (0, 35), (0, 50)]
# COSTS = [2.5, 3.5, 2.25, 3, 2, 2.5]
# D1, D2, D3 = [C, CB, B + AB + CB]
#
# # MODEL
# prob = LpProblem("Problem", LpMinimize)
# # VARS
# AC35, AC50 = LpVariable("AC35", *EDGES[0], cat='Integer'), LpVariable("AC50", *EDGES[1], cat='Integer')
# CB35, CB50 = LpVariable("CB35", *EDGES[2], cat='Integer'), LpVariable("CB50", *EDGES[3], cat='Integer')
# BA35, BA50 = LpVariable("BA35", *EDGES[4], cat='Integer'), LpVariable("BA50", *EDGES[5], cat='Integer')
# # OBJECTIVE FUNCTION -> added before constraints => important ,
# prob += lpDot(COSTS, [AC35, AC50, CB35, CB50, BA35, BA50]), "Costs"
# # CONSTRAINTS
# prob += AC35*35 + AC50*50 >= D1
# prob += CB35*35 + CB50*50 >= D2
# prob += BA35*35 + BA50*50 >= D3
#
# # SOLVE
# status = prob.solve()
#
# # PRINT SOLUTION
# print(LpStatus[status])
# print("AC35, AC50")
# for var in [AC35, AC50]:
#     print(value(var))
# print()
# print("CB35, CB50")
# for var in [CB35, CB50]:
#     print(value(var))
# print()
# print("BA35, BA50")
# for var in [BA35, BA50]:
#     print(value(var))
# print("Total Costs = ", value(prob.objective))

#другой пример
# EDGES = [(0, 25), (0, 40), (0, 40), (0, 35), (0, 50), (0, 40), (0, 55), (0, 70)] # lower/upper flow
# COSTS = [1, 5, 1, 2, 6, 4, 1, 3]
# D1, D2, D3, D4, D5, D6 = [0, -20, 30, -40, 80, -50]
#
# # MODEL
# prob = LpProblem("Problem", LpMinimize)
# # VARS
# x31, x12, x24 = LpVariable("x31", *EDGES[0]), LpVariable("x12", *EDGES[1]), LpVariable("x24", *EDGES[2])
# x35, x56, x64 = LpVariable("x35", *EDGES[3]), LpVariable("x56", *EDGES[4]),  LpVariable("x64", *EDGES[5])
# x51, x16 = LpVariable("x51", *EDGES[6]), LpVariable("x16", *EDGES[7])
# # OBJECTIVE FUNCTION -> added before constraints => important ,
# prob += lpDot(COSTS, [x31, x12, x24, x35, x56, x64, x51, x16]), "Costs"
# # CONSTRAINTS
# prob += -x31 - x51 + x12 + x16 == D1
# prob += -x12 + x24 == D2
# prob += x31 + x35 == D3
# prob += -x24 - x64 == D4
# prob += x51 - x35 + x56 == D5
# prob += -x16 + x64 - x56 == D6
#
# # SOLVE
# status = prob.solve()
#
# # PRINT SOLUTION
# print(LpStatus[status])
# for var in [x31, x12, x24, x35, x56, x64, x51, x16]:
#     print(value(var))
# print()
#
# print("Total Costs = ", value(prob.objective))
