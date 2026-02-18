# * MRO -> Method Resolution Order

# We should not structure our code 

class X : pass
class Y : pass
class Z : pass
class A(X,Y) : pass
class B(Y,Z) : pass
class M(B,A,Z) : pass

print(M.__mro__)

"""
OUTPUT:

(

<class '__main__.M'>, 

    <class '__main__.B'>, 

        <class '__main__.A'>,

            <class '__main__.X'>,

                <class '__main__.Y'>,

                    <class '__main__.Z'>,

                            <class 'object'>
)

"""