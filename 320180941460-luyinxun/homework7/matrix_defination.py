'''
this class method is only can be uesd to calculate
the one-dimensional or two-dimensinal matrix
'''

class Matrix:
    def __init__(self,row=0,col=0,l=[]):  #define the information of matrix
        if isinstance(row,int) and isinstance(col,int) and row>=0 and col>=0:
            self.row = row
            self.col = col
            self.l = l
            self.shape = (row,col)
        else:
            raise Exception('error data')


    def array(self):

        '''
        translate the list into the matrix
                create the matrix
        '''
        try:
            if len(self.l) == self.row*self.col:      #verify the list about it's length
                if self.row == 1:
                    return self.l
                else:
                    array = []
                    count = self.col
                    for i in range(self.row):
                        a = self.l[i*count:i*count + self.col]  #split the list
                        array.append(a)
                    return array
            else:
                return '\nThis list {} isn\'t translated into a matrix!\n'.format(self.l)
        except:
            return 'error'

    def T(self):

        '''transpose the matrix'''

        a = []
        for i in range(self.col):
            for j in range(self.row):
                a.append(self.array()[j][i])
        return Matrix(self.col,self.row,a)

    def reshape(self,new_row,new_col):

        '''reshape the matrix'''

        try:
            if self.row*self.col == new_row*new_col \
                    and isinstance(new_col,int) and isinstance(new_row,int):  #clear the type of data's parameter
                return Matrix(new_row,new_col,self.l)
            else:
                raise Exception('it can\'t be reshaped')
        except Exception as e:
            return e

    def add(self,other):
        if self.shape == other.shape:
            if self.row == 1:
                return function_add_sub(self.array(), other.array())
            if self.row == 2:
                return function_add_sub(self.array(), other.array())
        else:
            return 'can\'t add'

    def sub(self,other):
        if self.shape == other.shape:
            if self.row == 1:
                return function_add_sub(self.array(), other.array(),1)
            if self.row == 2:
                return function_add_sub(self.array(), other.array(),1)
        else:
            return 'can\'t subtract'

    def mul(self,other):
        if self.col == other.row:
            return function_mul(self.array(),other.array())
        else:
            return 'can\'t multiply'


def dcp(row,col,a,b):  #a is original matrix, b is new list

    '''function of decompose the matrix'''

    for i in range(row):
        for j in range(col):
            b.append(a[i][j])


def function_add_sub(arr1,arr2,flag=-1):   #flag=-1 means add,flag=1 means subtrct

    '''function of add and subtract '''

    a = []
    for i in range(len(arr1)):
        if isinstance(arr1[0],list):
            a1 = []
            for j in range(len(arr1[0])):
                a1.append(arr1[i][j] + (-1) * flag * arr2[i][j])
            a.append(a1)
        else:
            a.append(arr1[i] + (-1) * flag * arr2[i])
    b=[]
    dcp(len(arr1),len(arr1[0]),a,b)
    return Matrix(len(arr1),len(arr1[0]),b)


def function_mul(arr1,arr2):

    '''function of multiply '''

    a = []
    for i in range(len(arr1)):  # create the original matrix
        a1 = []
        for j in range(len(arr2[0])):
            a1.append(0)
        a.append(a1)

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            for k in range(len(arr2[0])):
                a[i][k] += arr1[i][j] * arr2[j][k]
    b=[]
    dcp(len(arr1), len(arr2[0]),a, b)
    return Matrix(len(arr1),len(arr2[0]),b)
