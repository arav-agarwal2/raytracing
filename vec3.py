"""Class Definition and Implementation of Vec3, a 3 tuple-like that acts as single 3-dimensional vector"""
import math
class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """Initialize pixel with default values set to 0"""
        self.data = [float(x),float(y),float(z)]

    def __len__(self):
        """Get length of vec3 (for internal use to allow iterators)"""
        return 3

    def __abs__(self):
        """Get the 2-norm of vec3"""
        return math.sqrt(self.data[0]^2 + self.data[1]^2 + self.data[2]^2)

    def __getitem__(self, key):
        """Access pixel items as a list"""
        return self.data[key]

    def __str__(self):
        """Get a nice string version of the Vec3"""
        return " ".join(str(item) for item in self.data)

    def type_safety_decorator(func):
        """Check if the second object is a Vec3"""
        def wrapper(*args, **kwargs):
            if isinstance(args[1], self.__class__):
                return func(*args, **kwargs)
            else:
                raise TypeError("unsupported operand types for Vec3")
        return wrapper

    def reverse_safety_decorator(func):
        """Check if the second object is a float"""
        def wrapper(*args, **kwargs):
            if isinstance(args[1], float):
                return func(*args, **kwargs)
            else:
                raise TypeError("unsupported operand types for Vec3")
        return wrapper

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vec3(*tuple(self.data[idx]+other.data[idx] for idx in range(3)))
        elif isinstance(other, float):
            return Vec3(*tuple(self.data[idx]+other for idx in range(3)))
        else:
            raise TypeError("unspported operand types for Vec3")

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vec3(*tuple(self.data[idx]*other.data[idx] for idx in range(3)))
        elif isinstance(other, float):
            return Vec3(*tuple(self.data[idx]*other for idx in range(3)))
        else:
            raise TypeError("unspported operand types for Vec3")

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return Vec3(*tuple(self.data[idx]/other.data[idx] for idx in range(3)))
        elif isinstance(other, float):
            return Vec3(*tuple(self.data[idx]/other for idx in range(3)))
        else:
            raise TypeError("unspported operand types for Vec3")

    @reverse_safety_decorator
    def __radd__(self, other):
        return Vec3(*tuple(self.data[idx]+other for idx in range(3)))

    @reverse_safety_decorator
    def __rmul__(self, other):
        return Vec3(*tuple(self.data[idx]*other for idx in range(3)))

    @reverse_safety_decorator
    def __rtruediv__(self, other):
        return Vec3(*tuple(other/self.data[idx] for idx in range(3)))

    @type_safety_decorator
    def dot(self, other):
        return sum(self.data[idx]*other.data[idx] for idx in range(3))

    @type_safety_decorator
    def cross(self, other):
        return Vec3(self.data[1]*other.data[2] - self.data[2]*other.data[1],
                    self.data[2]*other.data[0] - self.data[0]*other.data[2],
                    self.data[0]*other.data[1] - self.data[1]*other.data[0])

    def unit(self):
        return self / abs(self)

    def color(self):
        return " ".join(str(int(item*255.999)) for item in self.data) + "\n"

    def x(self):
        return self.data[0]

    def y(self):
        return self.data[1]

    def z(self):
        return self.data[2]


if __name__ == "__main__":
    v1 = Vec3(1,2,3)
    print(v1)
    v1 = v1 * 2.0
    print(v1)
    v1 = v1 + 2.0
    print(v1)
    v2 = Vec3(1,2,3)
    print(v2)
    print(v2 * v1)
    print(v1 + v1)
    print(v1 / v2)
    print(v1 / 2.0)
    print(2.0 / v1)

