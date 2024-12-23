from random import randint

def main():
    ROWS = 4
    COLUMNS = 4
    print("Esta en la matrix que he creado:")
    matrix = generate_matrix(ROWS, COLUMNS)
    print_matrix(matrix)


def generate_matrix(ROWS, COLUMNS):
    return [[randint(0, 100) for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == '__main__':
    main()
