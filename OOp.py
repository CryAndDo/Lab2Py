class Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return f'x: {self.x}, y: {self.y}'

    def cube_of_max(self):
        max_value = max(self.x, self.y)
        return max_value ** 3


class ExtendedNumber(Number):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def sum_cube_and_max(self):
        max_xy = max(self.x, self.y)
        return self.z ** 3 + max_xy


class University:
    def __init__(self, name, first_year_students, graduates):
        self.name = name
        self.first_year_students = first_year_students
        self.graduates = graduates

    def quality(self):
        if self.first_year_students == 0:
            return 0
        else:
            return self.graduates / self.first_year_students

    def info(self):
        print(f'Название университета: {self.name}')
        print(f'Количество студентов на первом курсе: {self.first_year_students}')
        print(f'Количество выпускников: {self.graduates}')
        print(f'Качество: {self.quality():.2f}\n')


class SpecializedUniversity(University):
    def __init__(self, name, first_year_students, graduates, percentage_working_in_field):
        super().__init__(name, first_year_students, graduates)
        self.percentage_working_in_field = percentage_working_in_field

    def quality(self):
        base_quality = super().quality()
        return base_quality * self.percentage_working_in_field / 100


num_obj = Number(x=5, y=8)
print(num_obj.to_string())
print(num_obj.cube_of_max())

ext_num_obj = ExtendedNumber(x=6, y=9, z=12.5)
print(ext_num_obj.sum_cube_and_max())

university = University(name='Университет А', first_year_students=200, graduates=150)
university.info()


special_uni = SpecializedUniversity(
    name='СпецУниверситет Б',
    first_year_students=300,
    graduates=250,
    percentage_working_in_field=80
)
special_uni.info()
