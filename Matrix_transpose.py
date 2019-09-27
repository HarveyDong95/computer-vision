# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#

## this program is use for transpose any unregular matrix, and put 0 at place where there is no number.

#%%
# import numpy as np
def main(mat):
    max_len = 0
    row = len(mat)
    
    for i in range(row):
        # print(row)
        if len(mat[i]) > max_len:
            max_len = len(mat[i])
    # print(max_len)
    new_mat = [[0 for x in range(row)] for y in range(max_len)]
    # print(new_mat)
    for a in range(row):
        # if len(mat[a]) < max_len:
        for b in range(len(mat[a])):
            # print(mat[a][b])
            # print(max_len - 1 - b)
            new_mat[max_len - 1 - b][a] = mat[a][b]
    return new_mat


#%%
if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6,7],[8,9,10],[1,3,3,2]]
    print(main(mat))



#%%
