import copy

import numpy as np
# import pandas as pd


m = np.loadtxt("trgb3877_only_RaDec_gri_BVRI.dat")  # загружаем таблицу с координатами
field = 1.5  # размер поля в градусах
cols = [1, 2]  # выбираем столбцы с координатами
coordinates = m[:, cols]  # записываем координаты в отдельную таблицу
a2 = []  # номера строк образующих близкую пару
b2 = []
m2 = []
a3 = []
b3 = []  # номера строк образующих близкую тройку
c3 = []
m3 = []
a4 = []
b4 = []
c4 = []
d4 = []
m4 = []
a5 = []
b5 = []
c5 = []
d5 = []
e5 = []
m5 = []
a6 = []
b6 = []
c6 = []
d6 = []
e6 = []
f6 = []
m6 = []
a7 = []
b7 = []
c7 = []
d7 = []
e7 = []
f7 = []
g7 = []
m7 = []
a8 = []
b8 = []
c8 = []
d8 = []
e8 = []
f8 = []
g8 = []
h8 = []
m8 = []
a9 = []
b9 = []
c9 = []
d9 = []
e9 = []
f9 = []
g9 = []
h9 = []
i9 = []
m9 = []
for i in np.arange(len(coordinates)):
    for j in np.arange(len(coordinates)):
        if i != j:  # условие, чтобы не сравнивать строку с собой же
            if np.sqrt(np.square((coordinates[i, 0] - coordinates[j, 0])) + np.square((coordinates[i, 1] - coordinates[j, 1]))) < field:
                if i < j:  # условие, что не повторялась одна и та же пара в другом порядке строк
                    a2.append(i)
                    b2.append(j)
                    m2.append([i, j])
for k in np.arange(len(coordinates)):
    for i in np.arange(len(a2)):
        if a2[i] != k:
            if b2[i] != k:
                if np.sqrt(np.square((coordinates[a2[i], 0] - coordinates[k, 0])) + np.square((coordinates[a2[i], 1] - coordinates[k, 1]))) < field:
                    if np.sqrt(np.square((coordinates[b2[i], 0] - coordinates[k, 0])) + np.square((coordinates[b2[i], 1] - coordinates[k, 1]))) < field:
                        if a2[i] < b2[i] < k:
                            a3.append(a2[i])
                            b3.append(b2[i])
                            c3.append(k)
                            m3.append([a2[i], b2[i], k])
for q in np.arange(len(coordinates)):
    for i in np.arange(len(c3)):
        if a3[i] != q:
            if b3[i] != q:
                if c3[i] != q:
                    if np.sqrt(np.square((coordinates[a3[i], 0] - coordinates[q, 0])) + np.square((coordinates[a3[i], 1] - coordinates[q, 1]))) < field:
                        if np.sqrt(np.square((coordinates[b3[i], 0] - coordinates[q, 0])) + np.square((coordinates[b3[i], 1] - coordinates[q, 1]))) < field:
                            if np.sqrt(np.square((coordinates[c3[i], 0] - coordinates[q, 0])) + np.square((coordinates[c3[i], 1] - coordinates[q, 1]))) < field:
                                if a3[i] < b3[i] < c3[i] < q:
                                    a4.append(a3[i])
                                    b4.append(b3[i])
                                    c4.append(c3[i])
                                    d4.append(q)
                                    m4.append([a3[i], b3[i], c3[i], q])
for j in np.arange(len(coordinates)):
    for i in np.arange(len(d4)):
        if a4[i] != j:
            if b4[i] != j:
                if c4[i] != j:
                    if d4[i] != j:
                        if np.sqrt(np.square((coordinates[a4[i], 0] - coordinates[j, 0])) + np.square((coordinates[a4[i], 1] - coordinates[j, 1]))) < field:
                            if np.sqrt(np.square((coordinates[b4[i], 0] - coordinates[j, 0])) + np.square((coordinates[b4[i], 1] - coordinates[j, 1]))) < field:
                                if np.sqrt(np.square((coordinates[c4[i], 0] - coordinates[j, 0])) + np.square((coordinates[c4[i], 1] - coordinates[j, 1]))) < field:
                                    if np.sqrt(np.square((coordinates[d4[i], 0] - coordinates[j, 0])) + np.square((coordinates[d4[i], 1] - coordinates[j, 1]))) < field:
                                        if a4[i] < b4[i] < c4[i] < d4[i] < j:
                                            a5.append(a4[i])
                                            b5.append(b4[i])
                                            c5.append(c4[i])
                                            d5.append(d4[i])
                                            e5.append(j)
                                            m5.append([a4[i], b4[i], c4[i], d4[i], j])
for j in np.arange(len(coordinates)):
    for i in np.arange(len(d5)):
        if a5[i] != j:
            if b5[i] != j:
                if c5[i] != j:
                    if d5[i] != j:
                        if e5[i] != j:
                            if np.sqrt(np.square((coordinates[a5[i], 0] - coordinates[j, 0])) + np.square((coordinates[a5[i], 1] - coordinates[j, 1]))) < field:
                                if np.sqrt(np.square((coordinates[b5[i], 0] - coordinates[j, 0])) + np.square((coordinates[b5[i], 1] - coordinates[j, 1]))) < field:
                                    if np.sqrt(np.square((coordinates[c5[i], 0] - coordinates[j, 0])) + np.square((coordinates[c5[i], 1] - coordinates[j, 1]))) < field:
                                        if np.sqrt(np.square((coordinates[d5[i], 0] - coordinates[j, 0])) + np.square((coordinates[d5[i], 1] - coordinates[j, 1]))) < field:
                                            if np.sqrt(np.square((coordinates[e5[i], 0] - coordinates[j, 0])) + np.square((coordinates[e5[i], 1] - coordinates[j, 1]))) < field:
                                                                    if a5[i] < b5[i] < c5[i] < d5[i] < e5[i] < j:
                                                                        a6.append(a5[i])
                                                                        b6.append(b5[i])
                                                                        c6.append(c5[i])
                                                                        d6.append(d5[i])
                                                                        e6.append(e5[i])
                                                                        f6.append(j)
                                                                        m6.append([a5[i], b5[i], c5[i], d5[i], e5[i], j])
for j in np.arange(len(coordinates)):
    for i in np.arange(len(d6)):
        if a6[i] != j:
            if b6[i] != j:
                if c6[i] != j:
                    if d6[i] != j:
                        if e6[i] != j:
                            if f6[i] != j:
                                if np.sqrt(np.square((coordinates[a6[i], 0] - coordinates[j, 0])) + np.square((coordinates[a6[i], 1] - coordinates[j, 1]))) < field:
                                    if np.sqrt(np.square((coordinates[b6[i], 0] - coordinates[j, 0])) + np.square((coordinates[b6[i], 1] - coordinates[j, 1]))) < field:
                                        if np.sqrt(np.square((coordinates[c6[i], 0] - coordinates[j, 0])) + np.square((coordinates[c6[i], 1] - coordinates[j, 1]))) < field:
                                            if np.sqrt(np.square((coordinates[d6[i], 0] - coordinates[j, 0])) + np.square((coordinates[d6[i], 1] - coordinates[j, 1]))) < field:
                                                if np.sqrt(np.square((coordinates[e6[i], 0] - coordinates[j, 0])) + np.square((coordinates[e6[i], 1] - coordinates[j, 1]))) < field:
                                                    if np.sqrt(np.square((coordinates[f6[i], 0] - coordinates[j, 0])) + np.square((coordinates[f6[i], 1] - coordinates[j, 1]))) < field:
                                                        if a6[i] < b6[i] < c6[i] < d6[i] < e6[i] < f6[i] < j:
                                                            a7.append(a6[i])
                                                            b7.append(b6[i])
                                                            c7.append(c6[i])
                                                            d7.append(d6[i])
                                                            e7.append(e6[i])
                                                            f7.append(f6[i])
                                                            g7.append(j)
                                                            m7.append([a6[i], b6[i], c6[i], d6[i], e6[i], f6[i], j])
for j in np.arange(len(coordinates)):
    for i in np.arange(len(d7)):
        if a7[i] != j:
            if b7[i] != j:
                if c7[i] != j:
                    if d7[i] != j:
                        if e7[i] != j:
                            if f7[i] != j:
                                if g7[i] != j:
                                    if np.sqrt(np.square((coordinates[a7[i], 0] - coordinates[j, 0])) + np.square((coordinates[a7[i], 1] - coordinates[j, 1]))) < field:
                                        if np.sqrt(np.square((coordinates[b7[i], 0] - coordinates[j, 0])) + np.square((coordinates[b7[i], 1] - coordinates[j, 1]))) < field:
                                            if np.sqrt(np.square((coordinates[c7[i], 0] - coordinates[j, 0])) + np.square((coordinates[c7[i], 1] - coordinates[j, 1]))) < field:
                                                if np.sqrt(np.square((coordinates[d7[i], 0] - coordinates[j, 0])) + np.square((coordinates[d7[i], 1] - coordinates[j, 1]))) < field:
                                                    if np.sqrt(np.square((coordinates[e7[i], 0] - coordinates[j, 0])) + np.square((coordinates[e7[i], 1] - coordinates[j, 1]))) < field:
                                                        if np.sqrt(np.square((coordinates[f7[i], 0] - coordinates[j, 0])) + np.square((coordinates[f7[i], 1] - coordinates[j, 1]))) < field:
                                                            if np.sqrt(np.square((coordinates[g7[i], 0] - coordinates[j, 0])) + np.square((coordinates[g7[i], 1] - coordinates[j, 1]))) < field:
                                                                if a7[i] < b7[i] < c7[i] < d7[i] < e7[i] < f7[i] < g7[i] < j:
                                                                    a8.append(a7[i])
                                                                    b8.append(b7[i])
                                                                    c8.append(c7[i])
                                                                    d8.append(d7[i])
                                                                    e8.append(e7[i])
                                                                    f8.append(f7[i])
                                                                    g8.append(g7[i])
                                                                    h8.append(j)
                                                                    m8.append([a7[i], b7[i], c7[i], d7[i], e7[i], f7[i], g7[i], j])
for j in np.arange(len(coordinates)):
    for i in np.arange(len(d8)):
        if a8[i] != j:
            if b8[i] != j:
                if c8[i] != j:
                    if d8[i] != j:
                        if e8[i] != j:
                            if f8[i] != j:
                                if g8[i] != j:
                                    if h8[i] != j:
                                        if np.sqrt(np.square((coordinates[a8[i], 0] - coordinates[j, 0])) + np.square((coordinates[a8[i], 1] - coordinates[j, 1]))) < field:
                                            if np.sqrt(np.square((coordinates[b8[i], 0] - coordinates[j, 0])) + np.square((coordinates[b8[i], 1] - coordinates[j, 1]))) < field:
                                                if np.sqrt(np.square((coordinates[c8[i], 0] - coordinates[j, 0])) + np.square((coordinates[c8[i], 1] - coordinates[j, 1]))) < field:
                                                    if np.sqrt(np.square((coordinates[d8[i], 0] - coordinates[j, 0])) + np.square((coordinates[d8[i], 1] - coordinates[j, 1]))) < field:
                                                        if np.sqrt(np.square((coordinates[e8[i], 0] - coordinates[j, 0])) + np.square((coordinates[e8[i], 1] - coordinates[j, 1]))) < field:
                                                            if np.sqrt(np.square((coordinates[f8[i], 0] - coordinates[j, 0])) + np.square((coordinates[f8[i], 1] - coordinates[j, 1]))) < field:
                                                                if np.sqrt(np.square((coordinates[g8[i], 0] - coordinates[j, 0])) + np.square((coordinates[g8[i], 1] - coordinates[j, 1]))) < field:
                                                                    if np.sqrt(np.square((coordinates[h8[i], 0] - coordinates[j, 0])) + np.square((coordinates[h8[i], 1] - coordinates[j, 1]))) < field:
                                                                        if a8[i] < b8[i] < c8[i] < d8[i] < e8[i] < f8[i] < g8[i] < h8[i] < j:
                                                                            a9.append(a8[i])
                                                                            b9.append(b8[i])
                                                                            c9.append(c8[i])
                                                                            d9.append(d8[i])
                                                                            e9.append(e8[i])
                                                                            f9.append(f8[i])
                                                                            g9.append(g8[i])
                                                                            h9.append(h8[i])
                                                                            i9.append(j)
                                                                            m9.append([a8[i], b8[i], c8[i], d8[i], e8[i], f8[i], g8[i], h8[i], j])
FC = []
filmed = []
lastfilmed = []
FCx = []
FCy = []
A = {9: m9, 8: m8, 7: m7, 6: m6, 5: m5, 4: m4, 3: m3, 2: m2}


def filmedrange(x):
    lastfilmed.clear()
    for i in np.arange(len(A[x])):
        if len(A[x][i]) == x:
            lists = copy.copy(A[x][i])
            FC.append(lists)
            lst = []
            lst.append(lists)
            xxx = 0
            yyy = 0
            for k in np.arange(len(lists)):
                xxx = xxx + coordinates[lists[k], 0]
                yyy = yyy + coordinates[lists[k], 1]
            FCx.append(xxx/x)
            FCy.append(yyy/x)
            for v in np.arange(x):
                filmed.append(lst[0][v])
                lastfilmed.append(lst[0][v])
            break
    for j in np.arange(len(lastfilmed)):
        (A[x])[i].remove(lastfilmed[j])


def removeoverlap(x, ll):
    for l in np.arange(ll, len(A[x])):
        if not A[x][l]:
            continue  # если список пустой, то следующая итерация
        else:
            if len(A[x][l]) < x:
                continue  # если список короткий, то следующая итерация
            else:
                break
        ll = l
    ll = remove1(ll, x)
    return ll


def remove1(ll, x):
    for n in np.arange(len(lastfilmed)):
        if (lastfilmed[n]) in A[x][ll]:
            A[x][ll].remove(lastfilmed[n])
    ll += 1
    return ll


def removelilmed(x):
    ll = 0
    for j in np.arange(len(A[x])):
        ll = removeoverlap(x, ll)

def removefilmed(x):
    for q in np.arange(x, 1, -1):
        removelilmed(q)

def sort(x):
    for i in np.arange(x, 1, -1):
        for j in np.arange(len(A[i])):
            if not A[i][j]:
                continue  # если список пустой, то следующая итерация
            else:
                if len(A[i][j]) == 1:
                    continue  # если список c одним элементом, то следующая итерация
                else:
                    if len(A[i][j]) == i:
                        filmedrange(i)
                        return i
                    else:
                        A[len(A[i][j])].append(A[i][j])
                        A[i][j].clear()
    return -1

def main(x):
    for i in np.arange(1000):
    # while 1 == 1:
        zz = sort(x)
        if zz == -1:
            break
        removefilmed(zz)
        x = zz


zz = 0
main(9)
combined_x_y_arrays = np.column_stack([FCx, FCy])
nofilmedc = np.delete(coordinates, [filmed], 0)
allFC = np.append(combined_x_y_arrays, nofilmedc, axis=0)
# indexx = copy.copy(m[:, 0])
# nofilmedi = np.delete(indexx, [filmed], 0)
# ind.tolist()
nofilmedi = []
nofilmedi = np.arange(len(coordinates))
print(nofilmedi)
print(filmed)
nofilmedi = np.delete(nofilmedi, filmed, 0)
nofilmedi = nofilmedi + 1
zzz = np.zeros((len(allFC), len(FC[0])))
allFC2 = np.append(allFC, zzz, axis=1)
for i in np.arange(len(FC)):
    for j in np.arange(len(FC[i])):
        allFC2[i][2+j] = FC[i][j]
# nofilmedi = np.where(filmed not in nofilmedi, nofilmedi, None)
for i in np.arange(len(combined_x_y_arrays), len(allFC)):
    allFC2[i][2] = nofilmedi[i-len(combined_x_y_arrays)]
# allFC2 = np.where(allFC2 != 0, allFC2, '-')
# allFC2 = allFC2.ravel()[np.flatnonzero(allFC2)]

np.savetxt('test.csv', allFC2, fmt=['%3.4f', '%3.4f', '%i', '%i', '%i', '%i', '%i', '%i', '%i', '%i'])
# allFC2.to_csv('test.csv')

print(FCx)
print(FCy)
print(len(FCy))
print(filmed)
print(FC)
print(m8)
print(m7)
# print(nofilmedi)
print(allFC2)

