#Class to encrypt and decrypt
import numpy as np

class Cript:
    #constructor
    def __init__(self):
        self.matTransformation = np.array([[3,5,2],[2,3,1],[4,6,3]],int)
        self.matTrasfomationInv = np.linalg.inv(self.matTransformation).astype(int).copy()
        
    def clave(self, caracter):
        if(caracter == ' '): return 55
        if(caracter == 'a'): return 1
        if(caracter == 'b'): return 2
        if(caracter == 'c'): return 3
        if(caracter == 'd'): return 4
        if(caracter == 'e'): return 5
        if(caracter == 'f'): return 6
        if(caracter == 'g'): return 7
        if(caracter == 'h'): return 8
        if(caracter == 'i'): return 9
        if(caracter == 'j'): return 10
        if(caracter == 'k'): return 11
        if(caracter == 'l'): return 12
        if(caracter == 'm'): return 13
        if(caracter == 'n'): return 14
        if(caracter == 'ñ'): return 15
        if(caracter == 'o'): return 16
        if(caracter == 'p'): return 17
        if(caracter == 'q'): return 18
        if(caracter == 'r'): return 19
        if(caracter == 's'): return 20
        if(caracter == 't'): return 21
        if(caracter == 'u'): return 22
        if(caracter == 'v'): return 23
        if(caracter == 'w'): return 24
        if(caracter == 'x'): return 25
        if(caracter == 'y'): return 26
        if(caracter == 'z'): return 27
        if(caracter == 'A'): return 28
        if(caracter == 'B'): return 29
        if(caracter == 'C'): return 30
        if(caracter == 'D'): return 31
        if(caracter == 'E'): return 32
        if(caracter == 'F'): return 33
        if(caracter == 'G'): return 34
        if(caracter == 'H'): return 35
        if(caracter == 'I'): return 36
        if(caracter == 'J'): return 37
        if(caracter == 'K'): return 38
        if(caracter == 'L'): return 39
        if(caracter == 'M'): return 40
        if(caracter == 'N'): return 41
        if(caracter == 'Ñ'): return 42
        if(caracter == 'O'): return 43
        if(caracter == 'P'): return 44
        if(caracter == 'Q'): return 45
        if(caracter == 'R'): return 46
        if(caracter == 'S'): return 47
        if(caracter == 'T'): return 48
        if(caracter == 'U'): return 49
        if(caracter == 'V'): return 50
        if(caracter == 'W'): return 51
        if(caracter == 'X'): return 52
        if(caracter == 'Y'): return 53
        if(caracter == 'Z'): return 54
        
    def CreateArray(self, frase):
        cadena = str(frase)
        array = np.zeros(len(cadena))
        for i in range(0, len(cadena)):
            array[i] = self.clave((cadena[i]))
        return array
            
        
    def Encrypt(self, frase):
        array = self.CreateArray(frase)
        print(array)
        if(array.size%3==0):
            col = array.size/3
        else:
            col = array.size/3+1
            
        MatA = np.zeros([int(col),3], dtype=int)
        cont = 0
        
        for i in range(0, int(col)):
            for j in range(0, 3):
                if(cont < array.size):
                    MatA[i, j] = array[cont] 
                    cont = cont+1    
            
        MatA = MatA.T
        self.Enc = self.matTransformation.dot(MatA)
        print(self.Enc)
        
    def Decrypt(self):
        self.B = self.matTrasfomationInv.dot(self.Enc)
        print(self.B)
    

        
            