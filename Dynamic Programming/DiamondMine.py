# Diamond Mine is your new favorite game. Its map is represented as an n × n matrix, and the value of each cell corresponds
# to some property of the map:
#   - A value ≥ 0 represents a path.
#   - A value of 1 represents a diamond in a path that can be picked up by the player.
#   - A value of −1 represents a wall (path obstruction).
# The basic rules for playing Diamond Mine are as follows:
# 1. The player starts at (0, 0) and reaches (n−1, n−1), by moving right (→) or down (↓) through valid path cells.
# 2. After reaching (n−1, n−1), the player must travel back to (0, 0) by moving left (←) or up (↑) through valid path cells.
# 3. When passing through a path cell containing a diamond, the diamond is picked up. Once picked up, the cell becomes 
# an empty path cell(meaning you cannot pick up the same diamond twice).
# 4. If there is no valid path between (0, 0) and (n−1, n−1), then no diamonds can be collected.
# 5. A player wins the game by collecting the maximum number of diamonds possible when following the above rules.

# Complete the collect_max function in your editor. It has 1 parameter: a 2D array of integers, mat, describing the game map. 
# It must return an integer denoting the maximum number of diamonds you can collect in the given Diamond Mine game map.

# Constraints
# 1 ≤ size of mat ≤ 100
# −1 ≤ mati,j ≤ 1
# Output Format

# Your function must return an integer denoting the maximum number of diamonds you can collect in the given map. 

def game(mat): # mat is two dimension matrix
              mat,score1 = forward(mat)
              if score1 < 0:
                            print "No path possible"
                            return
              mat,score2 = backward(mat)
              return score1+score2
def forward(mat):
              i = 0
              j = 0
              d = {}
              #d [position in mat] = [val calculated till that index,from which position I reached here]
              d[(i,j)] = [mat[0][0],-1]

              s = len(mat)
              if mat [s-1][s-1] < 0: # if end co-ordinates are negative 
                            return mat,-1
              for i in range(s):
                            for j in range(s):
                                          if i == 0 and j == 0:
                                                        continue
                                          if mat[i][j] == -1:
                                                        d[(i,j)] = [(-1 * (s ** 2)) - 1,-1] # -200 is just any random value
                                                        continue
                                          xc1 = i
                                          yc1 = j - 1
                                          xc2 = i - 1
                                          yc2 = j

                                          if yc1 <  0:
                                                        val1 = 2*(-1 * (s ** 2))
                                          else:
                                                        val1 = d[(xc1,yc1)][0] + mat[i][j]
                                          if xc2 < 0:
                                                        val2 = 2*(-1 * (s ** 2))
                                          else:
                                                        val2 = d[(xc2,yc2)][0] + mat[i][j]
                                          if val1 > val2:
                                                        d[(i,j)] = [val1,(xc1,yc1)]
                                          else:
                                                        d[(i,j)] = [val2,(xc2,yc2)]
                                          
              i = s-1
              j = s-1
              maxScore = d[(i,j)][0]
              if maxScore < 0:
                return mat,maxScore
              while True:
                           mat[i][j] = 0
                           t= d[(i,j)][1]
                           if t == -1:
                                         break
                           else:
                                          i = t[0]
                                          j = t[1]
              return mat,maxScore

def backward(mat):
              s = len(mat)
              i = s-1
              j = s-1
              d = {}
              d[(i,j)] = [0,-1]# d [coord] = [ val , how i reached]                    

              
              for i in range(s-1,-1,-1):
                            for j in range(s-1,-1,-1):
                                          if i == s-1 and j == s-1:
                                                        continue
                                          if mat[i][j] == -1:
                                                        d[(i,j)] = [(-1 * (s ** 2)) - 1,-1] # -200 is just any random value
                                                        continue
                                          xc1 = i +1
                                          yc1 = j
                                          xc2 = i
                                          yc2 = j +1
                                          if xc1 >=  s:
                                                        val1 = 2*(-1 * (s ** 2))
                                          else:
                                                        val1 = d[(xc1,yc1)][0] + mat[i][j]
                                          if yc2 >= s:
                                                        val2 = 2*(-1 * (s ** 2))
                                          else:
                                                        val2 = d[(xc2,yc2)][0] + mat[i][j]
                                          if val1 > val2:
                                                        d[(i,j)] = [val1,(xc1,yc1)]
                                          else:
                                                        d[(i,j)] = [val2,(xc2,yc2)]
              i = 0
              j = 0
              maxScore = d[(i,j)][0]
              #print d
              while True:
                           mat[i][j] = 0
                           t= d[(i,j)][1]
                           if t == -1:
                                         break
                           else:
                                          i = t[0]
                                          j = t[1]
              return mat,maxScore




                                          
