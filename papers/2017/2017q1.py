# BIO 2017 Round 1
# Coloured Triangles

row = list(input())

L = [row]

for i in range(len(row)-1):
    new_row = []
    for j in range(len(L[i])-1):
        if L[i][j] == L[i][j+1]:
            new_row.append(L[i][j])
            
        elif (L[i][j] == 'R' and L[i][j+1] == 'G') or (L[i][j] == 'G' and L[i][j+1] == 'R'):
            new_row.append('B')
            
        elif (L[i][j] == 'G' and L[i][j+1] == 'B') or (L[i][j] == 'B' and L[i][j+1] == 'G'):
            new_row.append('R')
            
        elif (L[i][j] == 'B' and L[i][j+1] == 'R') or (L[i][j] == 'R' and L[i][j+1] == 'B'):
            new_row.append('G')

    L.append(new_row)


print(''.join(L[-1]))
        

# 1b) 3 - RRRBBGGRG, BGBRGBRGR, GBGGRRBBB

# 1c) 1 - The smallest row is completely known. If a complete row is known and one value is known
#         in an adjacent row, there is a single way the row can be completed / by induction there is a single way each
#         of the larger rows can be completed
#         OR given three adjacent squares in a triangular patterb, if two are known there is only one possibility
#         for the other square
