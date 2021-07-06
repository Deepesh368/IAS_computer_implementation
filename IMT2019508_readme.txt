These programs are hardcoded into memory in the file. 
I commented out the first program and the second program is not commented.

Variable 'a' is stored at M(12)
Variable 'b' is stored at M(13)
Variable 'c' is stored at M(14)

Program 1:

    In python:
        a = 10
        b = 5 
        if(a+b >= 0):
            c = a + b
        else:
            c = b

    In machine language:
        LOAD M(12) ADD M(13)   -->0
        JUMP+ M(3,0:19) LOAD M(13) -->1
        STOR M(14) HALT          -->2
        STOR M(14) HALT        -->3



Program 2:

    In python:
        a = 15
        b = 3
        if(a - b >= 0):
            c = a / b
        else:
            c = a % b

    In machine language:
        LOAD M(12) SUB M(13)   -->0
        JUMP+ M(4,0:19) LOAD M(12) -->1
        DIV M(13) STOR M(14)   -->2
                  HALT        -->3
        LOAD M(12) DIV M(13)  -->4
        LOAD MQ STOR M(14)    -->5
                HALT          -->6        