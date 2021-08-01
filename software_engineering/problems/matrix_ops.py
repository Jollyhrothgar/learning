def rotate_clockwise(m):
  """
  Given a matrix m, return the numbers, rotated 90 degrees clockwise.

  Args:
    m: a matrix that has M rows and N columns
  Retuns:
    a matrix that has N rows and M colums, rotated 90 degrees clockwise.
  """

  M = len(m) # row size
  N = len(m[0]) # column size
  
  out_row = [0 for _ in range(M)]
  out_matrix = [list(out_row) for _ in range(N)]

  indices = [(i, j) for i in range(M) for j in range(N)]

  for index in indices:
    col_out = M - index[0] - 1
    # print(index[1], col_out)
    out_matrix[index[1]][col_out] = m[index[0]][index[1]]
  return out_matrix

#TODO: properly implement this later.
def rotate_counterclockwise(m):
  """
  Given a matrix m, return the numbers, rotated 90 degrees counterclockwise.

  Args:
    m: a matrix that has M rows and N columns
  Retuns:
    a matrix that has N rows and M colums, rotated 90 degrees clockwise.
  """
  return rotate_clockwise(rotate_clockwise(rotate_clockwise(m)))
