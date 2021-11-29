# import filename
import a
import c
#from module import Something
from string import Template

#filename.functionName()
x = a.calculate(20,30) # 20 and 30 are actual argment
print('The result is %s'%(x))

y = a.subtration(70,10) # 10 and 10 are actual arg
print('The result is {}'.format(y))

z = a.multiply(40,2)

obj = Template('The result is $zz')
print(obj.substitute(zz=z))
print(a.PI)

a.greet("Anil sir","Good Evening")

# module_name.function_name.

print(c.student1['name'])
print(c.student1['surname'])
print(c.student1['mobile'])