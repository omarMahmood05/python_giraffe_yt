#Inheritence is when you copy the functions of other classes to another new class

from chef import regularChef
from chineseChef import chineseChef

zazaChef = regularChef()
ziziChef = chineseChef()

zazaChef.make_special_dish()
ziziChef.make_special_dish()