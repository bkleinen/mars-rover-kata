## Crossing the poles

n: number of longitudes 

The longitudes are represented by the x values.
The x value is determined to describe the direction
on the poles; it serves as a history for where the
rover came from.
Without a turn, it moves along the same line - that is
the opposite


new_tests = [pytest.param(*t,marks=pytest.mark.xfail) for t in new_tests]

  N
W   E
  S


0 1 2 3

von oben (N):
  2
3   1
  0 
r: E 1 turns , x + 1
l: W 3 turns , x - 1

von unten (S):
  0
3   1
  2
S
l: E 1 turns , x + 1
r: W 3 turns , x - 1
