import numpy

class Numpy():
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def print_eye(self):
        #The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter . A positive  is for the upper diagonal, a negative  is for the lower, and a   (default) is for the main diagonal.
        print(numpy.eye(row, column))

if __name__ == '__main__':
    #Formats the output
    numpy.set_printoptions(sign = ' ')
    row, column = map(int, input().split())
    my_object = Numpy(row, column)
    my_object.print_eye() 
