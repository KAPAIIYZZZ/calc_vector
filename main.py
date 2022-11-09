class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sum(self, vector):
        x=self.x+vector.x
        y = self.y + vector.y
        z = self.z + vector.z
        return Vector(x, y, z)
    def subtract(self, vector):
        x=self.x-vector.x
        y = self.y - vector.y
        z = self.z - vector.z
        return Vector(x, y, z)
    def multiply_scalar(self, vector):
        x=self.x*vector
        y = self.y * vector
        z = self.z * vector
        return Vector(x, y ,z)
    def scalar_multiply(self, vector):
        scalar_multiply_result = self.x*vector.x+self.y * vector.y+self.z * vector.z
        return (scalar_multiply_result)
    def render(self):
        return (f'Координаты нового вектора: ({self.x};{self.y};{self.z})')
def main():
    print('Для сложения векторов введите символ +\nДля вычитания вектора из вектора введите символ -\nДля умножения вектора на скаляр введите символ ^\nДля скалярного умножения векторов введите символ *\nВедите координаты вектора_1')
    x_1=int(input('Введите x_1: '))
    y_1 = int(input('Введите y_1: '))
    z_1 = int(input('Введите z_1: '))
    vector_1=Vector(x_1,y_1,z_1)
    action = input('введите действие: ')
    if action == '+':
        print('Ведите координаты вектора_2')
        x_2 = int(input('Введите x_2: '))
        y_2 = int(input('Введите y_2: '))
        z_2 = int(input('Введите z_2: '))
        vector_2 = Vector(x_2, y_2, z_2)
        vector_3=vector_1.sum(vector_2)
        print(vector_3.render())
    elif action == '-':
        print('Ведите координаты вектора_2')
        x_2 = int(input('Введите x_2: '))
        y_2 = int(input('Введите y_2: '))
        z_2 = int(input('Введите z_2: '))
        vector_2 = Vector(x_2, y_2, z_2)
        vector_3=vector_1.subtract(vector_2)
        print(vector_3.render())
    elif action == '*':
        print('Ведите координаты вектора_2')
        x_2 = int(input('Введите x_2: '))
        y_2 = int(input('Введите y_2: '))
        z_2 = int(input('Введите z_2: '))
        vector_2 = Vector(x_2, y_2, z_2)
        vector_3=vector_1.scalar_multiply(vector_2)
        print(vector_3.render())
    elif action == '^':
        scalar = int(input('Введите число: '))
        vector_3=vector_1.multiply_scalar(scalar)
        print(vector_3.render())
    else:
        print('Неверное действие')
main()