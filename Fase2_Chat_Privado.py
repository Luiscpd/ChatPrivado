import numpy as np;
import math
import os 
import serial 
import time

#-----------------------------------------------------------------------------------------------------------------------------
opcion = 0
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyS0', 57600, timeout=1)
    ser.reset_input_buffer()

while opcion != 3:
    print("1. TRANSMITIR MENSAJE")
    print("2. RECIBIR MENSAJE")
    print("3. salir")
    
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        
            os.system('cls')
            texto = input("INTRODUCIR MENSAJE > ").upper()
            n = 5
            abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            cifrado = ""
            for l in texto:
                if l in abc:
                            pos_letra = abc.index(l)
                            nueva_pos = (pos_letra + n) % len(abc)
                            cifrado+= abc[nueva_pos]
                else:
                    cifrado+= l
            print("MENSAJE CIFRADO: ", cifrado)
            print("--------------------------------------------------------------")
            #print("MENSAJE CIFRADO EN BINARIO")
            string = cifrado
            binary_converted = ' '.join(format(ord(c), 'b') for c in string)
            #print(binary_converted)

            print("--------------------------------------------------------------")
            def imprimir_matriz(charar):
                for i in range(2):
                    for j in range(2):
                        print(int(charar[i][j]), "\t", end='')
                    print("\n");
            cifrado = cifrado.upper().replace(" ", "");
            Clave = np.empty((4, 4));
            msj="";
            m_crip=np.zeros((math.ceil(len(cifrado)/2),2))

        
            Clave[0][0] = 11;
            Clave[0][1] = 8;
            Clave[1][0] = 3;
            Clave[1][1] = 7;

            #imprimir_matriz(Clave)
            diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3,'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
            abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

            cipher="";
            i=0
            j=0
            while True:
                try:
                    if (np.size(m_crip) / 2 == j):
                        break
                    print(cifrado[i], " - ", cifrado[i+1])
                    m_crip[j][0]=diccionario_letras[cifrado[i]]
                    m_crip[j][1]=diccionario_letras[cifrado[i+1]]
                    i+=2
                    j+=1
                        
                except:
                    print(cifrado[i])
                    m_crip[j][0] = diccionario_letras[cifrado[i]]
                    break
            #for i in range(m_crip.length)

            c1 = 0
            c2 = 0
            m1 = 0
            m2 = 0

            cipher=np.zeros(m_crip.shape)
            os.system('cls')
            print("MENSAJE CIFRADO CESAR Y HILL ")
            salida = ""
            for i in range(int(np.size(m_crip)/2)):

                m1 = m_crip[i][0]
                m2 = m_crip[i][1]
                c1 = Clave[0][0]*m1 + Clave[1][0]*m2
                c2 = Clave[0][1] * m1 + Clave[1][1] * m2
                cipher[i][0]=c1%26
                cipher[i][1] = c2%26

                k = abecedario[int(cipher[i][0])]
                l = abecedario[int(cipher[i][1])]

                salida += k + l
                #print(int(cipher[i][0]), " - ", int(cipher[i][1]))
                #print(abecedario[int (cipher[i][0])], "",abecedario[int(cipher[i][1])],"",end="")
            print(salida)
            print("--------------------------------------------------------------")
           
            print("MENSAJE CIFRADO EN BINARIO")

            string = salida
            binary_converted = ' '.join(format(ord(c), 'b') for c in string)
            print(binary_converted)
            print("--------------------------------------------------------------")
#comunicacion UART
            ser = serial.Serial(
                port = '/dev/ttyS0',
                baudrate = 57600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            msg = ""
            print("Counter {} - Hola desde Raspberry Pi".format(i))
            ser.write(salida.encode('utf-8'))
            time.sleep(2)

    if opcion == 2:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()

                def imprimir_matriz(charar):
                    for i in range(2):
                        for j in range(2):
                            print(int(charar[i][j]), "\t", end='')
                        print("\n");

                print("--------------------------------------------------------------")
    #            else:
                    #Descifrar
                    # Solicitar Datos
                os.system('cls')
                Texto = line;
                Texto = Texto.upper().strip().replace(" ", "");
                #print("INTRODUCIR LA CLAVE (MATRIZ 2x2)");
                Clave = np.empty((4, 4));
                msj = "";
                m_crip = np.zeros((math.ceil(len(Texto) / 2), 2))

                Clave[0][0] = 11;
                Clave[0][1] = 8;
                Clave[1][0] = 3;
                Clave[1][1] = 7;

                #imprimir_matriz(Clave)
                diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3,'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
                abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

                #Inversa de una matriz A^-1=1/[A] * (A*)^T
                #Sacar determinante
                Determinante=Clave[0][0]*Clave[1][1]-Clave[0][1]*Clave[1][0]
                Adjunta=np.zeros((2,2))
                Adjunta[0][0] = Clave[1][1]
                Adjunta[1][1] = Clave[0][0]
                Adjunta[0][1] = -1*Clave[1][0]
                Adjunta[1][0] = -1*Clave[0][1]

                TAdj = np.zeros((2,2))
                TAdj[0][0] = Adjunta[0][0]
                TAdj[1][1] = Adjunta[1][1]
                TAdj[0][1] = Adjunta[1][0]
                TAdj[1][0] = Adjunta[0][1]

                Determinante=Determinante%26
                InClave = np.zeros((2, 2))
                InClave[0][0]= ((1/Determinante)*TAdj[0][0])%26
                InClave[0][1]= ((1 / Determinante) * TAdj[0][1])%26
                InClave[1][0]= ((1 / Determinante) * TAdj[1][0])%26
                InClave[1][1]= ((1 / Determinante) * TAdj[1][1])%26

                i = 0
                j = 0
                while True:
                    try:
                        if (np.size(m_crip) / 2 == j):
                            break
                        #print(Texto[i], " - ", Texto[i + 1])
                        m_crip[j][0] = diccionario_letras[Texto[i]]
                        m_crip[j][1] = diccionario_letras[Texto[i + 1]]
                        i +=2
                        j +=1

                    except:
                        print(Texto[i])
                        m_crip[j][0] = diccionario_letras[Texto[i]]
                        break
                # for i in range(m_crip.length)

                c1 = 0
                c2 = 0
                m1 = 0
                m2 = 0

                descipher = np.zeros(m_crip.shape)
                #print("MENSAJE DESCIFRADO: ")
                for i in range(int(np.size(m_crip) / 2)):
                    m1 = m_crip[i][0]
                    m2 = m_crip[i][1]
                    c1 = InClave[0][0] * m1 + InClave[1][0] * m2
                    c2 = InClave[0][1] * m1 + InClave[1][1] * m2
                    descipher[i][0] = c1 % 26
                    descipher[i][1] = c2 % 26

                        #print(int(cipher[i][0]), " - ", int(cipher[i][1]))
                    #print(abecedario[int(descipher[i][0])], "", abecedario[int(descipher[i][1])], " ", end="")
                    palabra = abecedario[int(descipher[0][0])]+ abecedario[int(descipher[0][1])]
                    palabra2 = abecedario[int(descipher[1][0])]+ abecedario[int(descipher[1][1])]
                    palabracompleta = (palabra+palabra2)
                #print (palabracompleta)


                texto1 = palabracompleta
                n = 5
                abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
                cifrado = ""
                for l in texto1:
                    if l in abc:
                        pos_letra = abc.index(l)
                        nueva_pos = (pos_letra - n) % len(abc)
                        cifrado+= abc[nueva_pos]
                    else:
                        cifrado+= l
                os.system('cls')
                print("MENSAJE CIFRADO: ", cifrado)
                print("--------------------------------------------------------------")
            
                # Defining BinarytoDecimal() function 
                #def BinaryToDecimal(binary): 
                        
                        # Using int function to convert to 
                        # string 
                        #string = int(binary, 2) 
                        
                        #return string 
                        
                # Driver's code 
                # initializing binary data 
                #tex = input("ingrese: ")
                #bin_data = tex

                # print binary data 
                #print("The binary value is:", bin_data) 

                # initializing a empty string for 
                # storing the string data 
                #str_data =' '

                # slicing the input and converting it 
                # in decimal and then converting it in string 
                #for i in range(0, len(bin_data), 7): 
                        
                        # slicing the bin_data from index range [0, 6] 
                        # and storing it in temp_data 
                        #temp_data = bin_data[i:i + 7] 
                        
                        # passing temp_data in BinarytoDecimal() function 
                        # to get decimal value of corresponding temp_data 
                        #decimal_data = BinaryToDecimal(temp_data) 
                        
                        # Deccoding the decimal value returned by 
                        # BinarytoDecimal() function, using chr() 
                        # function which return the string corresponding 
                        # character for given ASCII value, and store it 
                        # in str_data 
                    # str_data = str_data + chr(decimal_data) 

                # printing the result 
                        #print("The Binary value after string conversion is:", str_data)



    else:
        print("FIN")


