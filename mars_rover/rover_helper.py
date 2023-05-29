

def string_to_matrix(world_rep):
    rows = world_rep.strip().split('\n')
    field = [list(row) for row in rows]
    field.reverse()
    return field
    
        
def matrix_to_string(field):
    rows = [ ''.join(r) for r in field ]
    rows.reverse()
    world_str = '\n' + '\n'.join(rows) + '\n'
    return world_str

def create_field(width, height):
    return [['.' for i in list(range(0, width))] for j in  list(range(0, height))]