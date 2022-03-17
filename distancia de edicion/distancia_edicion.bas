'Integrantes:'
'Julian David tarazona
'Fabian Rojas
'Carlos Escobar

DECLARE FUNCTION d (A() AS STRING, B() AS STRING,i,j)
DECLARE FUNCTION Dm(A() AS STRING, B() AS STRING,i,j)
DECLARE FUNCTION DM_aux(A() AS STRING, B() AS STRING,i,j, M() AS INTEGER)
DECLARE FUNCTION minimo(a AS INTEGER,b AS INTEGER, c AS INTEGER)
DECLARE FUNCTION Dbup_B(A() AS STRING, B() AS STRING,i,j)
DECLARE FUNCTION Dbup_Baux(A() AS STRING, B() AS STRING,i,j, M() AS INTEGER, Ba() AS INTEGER) 
DECLARE FUNCTION print_way(Ba() AS INTEGER, A() AS STRING, B() AS STRING,i,j)            
    
DIM A(5) AS STRING
DIM B(5) AS STRING

A(1) = "t"
A(2) = "r"
A(3) = "i"
A(4) = "g"
A(5) = "o"

B(1) = "t"
B(2) = "i"
B(3) = "g"
B(4) = "r"
B(5) = "e"

PRINT "evidente:",d(A(), B(),5,5)
PRINT "memoizado:", Dm(A(), B(), 5, 5)
PRINT "Bactraking:", Dbup_B(A(), B(), 5, 5)
  
FUNCTION d (A() AS STRING, B() AS STRING,i,j)
    IF i = -1 AND j = -1 THEN
      d = 0
    ELSE IF i = -1 AND j > -1 THEN
      d = j
    ELSE IF i > -1 AND j = -1 THEN
      d = i
    ELSE IF A(i) = B(j) THEN
      d = d(A, B,i - 1,j - 1)
    ELSE IF A(i) <> B(j) THEN        
      a = d(A, B,i - 1,j - 1) + 1
      b = d(A, B,i - 1,j) + 1
      c = d(A, B,i,j - 1) + 1
      d = minimo(a,b,c)
    END IF
END FUNCTION

FUNCTION minimo(a AS INTEGER,b AS INTEGER, c AS INTEGER)
  IF a < b AND a < c THEN
        minimo = a
      ELSE IF b < a AND b < c THEN
        minimo = b
      ELSE 
        minimo = c
  END IF
END FUNCTION

'-----------------memoizado-------------------------'
FUNCTION Dm(A() AS STRING, B() AS STRING,i,j)
 DIM M(i+1,j+1) AS INTEGER
 FOR k = 0 TO i
   FOR l = 0 TO j
      M(k,l) = 10000
   NEXT l                
 NEXT k
 Dm = DM_aux(A, B,i,j, M)
END FUNCTION

FUNCTION DM_aux(A() AS STRING, B() AS STRING,i,j, M() AS INTEGER)
  IF M(i,j) = 10000 THEN                    
    IF i = 0 AND j = 0 THEN
      M(i,j) = 0
    ELSE IF i = 0 AND j > 0 THEN
      M(i,j) = j
    ELSE IF i > 0 AND j = 0 THEN
      M(i,j) = i
    ELSE IF A(i) = B(j) THEN
      M(i,j) = DM_aux(A, B,i - 1,j - 1, M)
    ELSE IF A(i) <> B(j) THEN
      a = DM_aux(A, B,i - 1,j - 1, M) + 1
      b = DM_aux(A, B,i - 1,j, M) + 1
      c = DM_aux(A, B,i,j - 1, M) + 1
      M(i,j) = minimo(a,b,c) 
    END IF
  END IF
  DM_aux = M(i,j)
END FUNCTION
'--------bottom up y backtracking--------------'
FUNCTION Dbup_B(A() AS STRING, B() AS STRING,i,j)
 DIM M(i+1,j+1) AS INTEGER
 DIM Ba(i+1,j+1) AS INTEGER
 FOR k = 0 TO i
   FOR l = 0 TO j
      M(k,l) = 10000
      Ba(k,l) = 10000
   NEXT l                
 NEXT k
 Dbup_B = Dbup_Baux(A, B,i,j, M,Ba)                               
END FUNCTION

FUNCTION Dbup_Baux(A() AS STRING, B() AS STRING,i,j, M() AS INTEGER, Ba() AS INTEGER)
 FOR k = 0 TO i
   FOR l = 0 TO j
     IF M(k,l) = 10000 THEN                    
      IF k = 0 AND l = 0 THEN
        M(k,l) = 0
        Ba(k,l) = k
      ELSE IF k = 0 AND l > 0 THEN
        M(k,l) = l
        Ba(k,l) = l                                  
      ELSE IF k > 0 AND l = 0 THEN
        M(k,l) = k
        Ba(k,l) = k                                    
      ELSE IF A(k) = B(l) THEN
        M(k,l) = M(k - 1,l - 1)
      ELSE IF A(i) <> B(j) THEN
        a = M(k - 1,l - 1) + 1
        b = M(k - 1,l) + 1
        c = M(k,l - 1) + 1
        M(k,l) = minimo(a,b,c)
        IF minimo(a,b,c) = a THEN
          Ba(k,l) = 1 
        ELSE IF minimo(a,b,c) = b THEN 
          Ba(k,l) = 2
        ELSE 
          Ba(k,l) = 3
        END IF                                          
    END IF
  END IF 
   NEXT l                
 NEXT k
 print_way(Ba,A,B,i,j)                                         
END FUNCTION

FUNCTION print_way(Ba() AS INTEGER, A() AS STRING, B() AS STRING,i,j)
  IF i = j THEN
    FOR k = 0 TO i
      l = k
      IF Ba(k , l) = 1 THEN
        PRINT "Cambiar ", B(l), " por ", A(k)
      ELSE IF Ba(k , l) = 2 THEN
        PRINT "Insertar ", A(k)
      ELSE IF Ba(k , l) = 3 THEN
        PRINT "Borrar ", B(l)                                     
      END IF
    NEXT k


  ELSE IF i > j THEN
   FOR k = 0 TO i
    IF k < j THEN
       l = k
    ELSE 
       l = j - 1                                             
    END IF
    IF Ba(k,l) = 1 THEN
      PRINT "Cambiar ", B(l), " por ", A(k)
    ELSE IF Ba(k,l) = 2 THEN
      PRINT "Insertar ", A(k)
    ELSE IF Ba(k,l) = 3 THEN
      PRINT "Borrar ", B(l)       
    END IF                                                  
   NEXT k 
                                                        
  ELSE IF j > i THEN
   FOR l = 0 TO j
    IF l < i THEN
       k = l
    ELSE 
       k = i - 1                                             
    END IF
    IF Ba(k,l) = 1 THEN
      PRINT "Cambiar ", B(l), " por ", A(k)
    ELSE IF Ba(k,l) = 2 THEN
      PRINT "Insertar ", A(k)
    ELSE IF Ba(k,l) = 3 THEN                                              
      PRINT "Borrar ", B(l)       
    END IF                                                  
   NEXT l                                                       
  END IF                                              
END FUNCTION