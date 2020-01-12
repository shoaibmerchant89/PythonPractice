"""
create a parent class to map the following attributes for a device - region, dc, env
create a derived class to build on the above class and add the following attributes - router, switch, firewall, loadbalancer, proxy, ddi
create a derived class to build on the above derived class and add the following attributes - vendor, model, version
create a list of region, dc, env, router, switch, firewall, loadbalancer, proxy, ddi, vendor, model, version.
"""
import math


class Base:
    def __init__(self, region='amer', dc='pic', env='campus'):
        super(Base, self).__init__()
        self.region = region
        self.dc = dc
        self.env = env

    def __str__(self):
        return 'This is the Base class'


class ProductCategory:
    def __init__(self, category='router'):
        super(ProductCategory, self).__init__()
        self.category = category

    def __str__(self):
        return 'This is the ProductCategory class'


class ProductAttr(Base, ProductCategory):
    def __init__(self):
        super(ProductAttr, self).__init__()

    def print(self):
        return self.region + self.dc + self.env + self.category


product1 = ProductAttr()
print(product1.print())

print('-'.center(100, '-'))


class NameBreed:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    def __str__(self):
        return 'This is the Base class'


class Cat(NameBreed):
    def speak(self):
        return self.name + ' says meow!' + ' I am a ' + self.breed

    def __str__(self):
        s = f'My name is {self.name} and I am a {self.breed}!'
        return s

    def __len__(self):
        return len(s)

class Dog(NameBreed):
    def speak(self):
        return '%s says woof! I am a %s' % (self.name, self.breed)

    def __str__(self):
        s = f'My name is {self.name} and I am a {self.breed}!'
        return s

    def __len__(self):
        return len(s)

benny = Cat('Benny', 'persian cat!')
jimmy = Dog('Jimmy', 'bull dog!')

print(benny.speak())
print(jimmy.speak())

# OR
for instance in [benny,jimmy]:
    print(instance.speak())
# OR


def instancespeak(pet):
    print(pet.speak())

instancespeak(benny)


print('-'.center(100, '-'))
print(benny.__str__())
print(str(benny))

print('HOMEWORK CLASSES'.center(100, '='))
print('Problem 1'.center(100, '='))


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        distance = math.sqrt(((self.coor2[0]-self.coor1[0])**2)+((self.coor2[1]-self.coor1[1])**2))
        return distance

    def slope(self):
        pass


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li.distance())


print('Problem 2'.center(100, '='))


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        v = (3.14 * (((self.radius**2))*self.height))
        return v

    def surface_area(self):
        sa = (2*(3.14*(self.radius * self.height)))+(2*(3.14*(self.radius**2)))
        return sa


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())

