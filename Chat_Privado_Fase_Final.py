# IMPORTAMOS TODAS LAS LIBRERIAS QUE VAMOS A NECESITAR EN NUESTRO PROGRAMA 
import numpy as np;
import math
import os 
import serial 
import time
import re
import string


#INICIO DEL PROGRAMA 

opcion = 0

#INICIAMOS ESTABLECIENDO LA VARIABLE PARA NUESTRO SERIAL
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyS0', 57600, timeout=1)
    ser.reset_input_buffer()

#CICLO WHILE PARA NUESTRO MENU , EN ESTE CASO TENDREMOS 5 OPCIONES DIFERENTES.
while opcion != 5:
    print("1. TRANSMITIR MENSAJE EN CESAR")
    print("2. TRANSMITIR MENSAJE EN HILL")
    print("3. TRANSMITIR MENSAJE EN VIGENERE")
    print("4. RECIBIR MENSAJE")
    print("5. salir")
    opcion = int(input("Ingrese una opcion: "))

    #OPCION 1 ESTE NOS PERMITE ENVIAR UN ARCHIVO O MENSAJE CON CIFRADO CESAR. 
    if opcion == 1:
            #INICIAMOS APERTURANDO EL PUERTO SERIAL
            ser = serial.Serial(
                port = '/dev/ttyS0',
                baudrate = 57600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            msg = ""
            #IDENTIFICADOR DE TIPO DE CIFRADO
            codificacion = "1"
            ser.write(codificacion.encode('utf-8'))
            os.system('clear')
            edd = 0
            #CICLO WHILE PARA ELECCION DE ENVIO 
            while edd < 1 :
                print ("1) Archivo de texto")
                print ("2) Mensaje")
                eleccion = int (input("¿Que desea enviar?  "))

                # ENVIO DE ARCHIVO
                if eleccion == 1:
                        os.system('clear')
                        edd = 0
                        os.system ("clear")
                        print("Enviando archivo...")
                        #ABRIMOS NUESTRO ARCHIVO TXT
                        archivo = open("mensaje.txt")
                        texto = archivo.read()
                        #LLAVE DEL CESAR, EN ESTE CASO LA DEJAMOS FIJA, ESTA PODRIA SER DINAMICA IGUAL.
                        n = 5
                        abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

                        #INICIO DE CIFRADO 
                        cifrado = ""
                        for l in texto:
                            if l in abc:
                                        pos_letra = abc.index(l)
                                        nueva_pos = (pos_letra + n) % len(abc)
                                        cifrado+= abc[nueva_pos]
                            else:
                                cifrado+= l
                        print("MENSAJE CIFRADO EN CESAR CON CODIGO HAMMING Y ENVIADO: ")
                        print("--------------------------------------------------------------")
                        string = cifrado

                        #CONVERSION DE BINARIO 

                        binary_converted = ' '.join(format(ord(c), 'b') for c in string)
                        MENSAJE_CIFRADO = binary_converted
                        
                        #INICIO DE HAMMING 
                        d=MENSAJE_CIFRADO
                        d = d.replace(" ", "") 
                        data=list(d) 
                        data.reverse()
                        c,ch,j,r,h=0,0,0,0,[] 

                        while ((len(d)+r+1)>(pow(2,r))):
                            r=r+1
                        for i in range(0,(r+len(data))):
                            p=(2**c)

                            if(p==(i+1)):
                                h.append(0)
                                c=c+1

                            else:
                                h.append(int(data[j]))
                                j=j+1

                        for parity in range(0,(len(h))):
                            ph=(2**ch)
                            if(ph==(parity+1)):
                                startIndex=ph-1
                                i=startIndex
                                toXor=[]

                                while(i<len(h)):
                                    block=h[i:i+ph] 
                                    toXor.extend(block)
                                    i+=2*ph

                                for z in range(1,len(toXor)):
                                    h[startIndex]=h[startIndex]^toXor[z]
                                ch+=1

                        h.reverse()
                        Codigo_hamming_enviado = (''.join(map(str, h)))
                        print (Codigo_hamming_enviado)
                        print("--------------------------------------------------------------") 


                        ser = serial.Serial(
                            port = '/dev/ttyS0',
                            baudrate = 57600,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS,
                            timeout=1)
                        msg = ""
                        ser.write(MENSAJE_CIFRADO.encode('utf-8'))
                        time.sleep(4)
                        ser.write(Codigo_hamming_enviado.encode('utf-8'))
                        edd = 1 

                #ENVIO DE MENSAJE PERSONALIZADO DESDE LA CONSOLA.
                #ESTE CODIGO REALIZA LO MISMO QUE EL CODIGO DESCRITO ANTERIORMENTE, CON LA DIFERENCIA QUE ES UN MENSAJE PERSONALIZADO QUE EL USUARIO DEBE
                #DE ESCRIBIR DESDE LA CONSOLA.

                if eleccion == 2:
                        os.system('clear')
                        edd = 0
                        os.system ("clear")
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
                        print("MENSAJE CIFRADO EN CESAR CON CODIGO HAMMING Y ENVIADO: ")
                        print("--------------------------------------------------------------")
                        #print("MENSAJE CIFRADO EN BINARIO")
                        string = cifrado
                        binary_converted = ' '.join(format(ord(c), 'b') for c in string)
                        #print(binary_converted)
                        MENSAJE_CIFRADO = binary_converted
                        #print(MENSAJE_CIFRADO)
                        #print("--------------------------------------------------------------")

                        d=MENSAJE_CIFRADO
                        d = d.replace(" ", "") 
                        data=list(d) 
                        data.reverse()
                        c,ch,j,r,h=0,0,0,0,[] 

                        while ((len(d)+r+1)>(pow(2,r))):
                            r=r+1
                        for i in range(0,(r+len(data))):
                            p=(2**c)

                            if(p==(i+1)):
                                h.append(0)
                                c=c+1

                            else:
                                h.append(int(data[j]))
                                j=j+1

                        for parity in range(0,(len(h))):
                            ph=(2**ch)
                            if(ph==(parity+1)):
                                startIndex=ph-1
                                i=startIndex
                                toXor=[]

                                while(i<len(h)):
                                    block=h[i:i+ph] 
                                    toXor.extend(block)
                                    i+=2*ph

                                for z in range(1,len(toXor)):
                                    h[startIndex]=h[startIndex]^toXor[z]
                                ch+=1

                        h.reverse()
                        Codigo_hamming_enviado = (''.join(map(str, h)))
                        print (Codigo_hamming_enviado)
                        print("--------------------------------------------------------------") 


                        ser = serial.Serial(
                            port = '/dev/ttyS0',
                            baudrate = 57600,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS,
                            timeout=1)
                        msg = ""
                        ser.write(MENSAJE_CIFRADO.encode('utf-8'))
                        time.sleep(4)
                        ser.write(Codigo_hamming_enviado.encode('utf-8'))
                        edd = 1

    # OPCION DOS DEL MENU PRINCIPAL, EN ESTE CASO SERIA ENVIO DE ARCHIVO O MENSAJE PERSONALIZADO CON CIFRADO HILL.
    if opcion == 2:
            #INICIAMOS APERTURANDO NUESTRO PUERTO SERIAL
            ser = serial.Serial(
                port = '/dev/ttyS0',
                baudrate = 57600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            msg = ""
            #TIPO DE CODIFICACION
            codificacion = "2"
            ser.write(codificacion.encode('utf-8'))
            os.system('clear')
            edd = 0
            #INICIO DE ELECCION DE ENVIO 
            while edd < 1 :
                print ("1) Archivo de texto")
                print ("2) Mensaje")
                eleccion = int (input("¿Que desea enviar? "))

                #ENVIO DE ARCHIVO
                if eleccion == 1:
                    os.system('clear')
                    edd = 0
                    os.system ("clear")
                    def imprimir_matriz(charar):
                        for i in range(2):
                            for j in range(2):
                                print(int(charar[i][j]), "\t", end='')
                            print("\n");

                    os.system ("clear")
                    print("Enviando archivo...")
                    #ABRIMOS NUESTRO ARCHIVO 
                    archivo = open("mensaje.txt")
                    texto = archivo.read()
                    #LE QUITAMOS LOS ESPACIOS A NUESTRO MENSAJE, PARA QUE SEA SOLO CARACTERES
                    texto = texto.strip()
                    cifrado = texto
                    cifrado = cifrado.upper().replace(" ", "");
                    Clave = np.empty((4, 4));
                    msj="";
                    m_crip=np.zeros((math.ceil(len(cifrado)/2),2))

                    #LLAVE DE CIFRADO PARA EL HILL 
                    Clave[0][0] = 11;
                    Clave[0][1] = 8;
                    Clave[1][0] = 3;
                    Clave[1][1] = 7;

                   
                    diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3,'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
                    abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

                    #INICIO DE CIFRADO HILL
                    cipher="";
                    i=0
                    j=0
                    while True:
                        try:
                            if (np.size(m_crip) / 2 == j):
                                break
                            
                            m_crip[j][0]=diccionario_letras[cifrado[i]]
                            m_crip[j][1]=diccionario_letras[cifrado[i+1]]
                            i+=2
                            j+=1
                        
                        except:
                          
                            m_crip[j][0] = diccionario_letras[cifrado[i]]
                            break
                    

                    c1 = 0
                    c2 = 0
                    m1 = 0
                    m2 = 0

                    cipher=np.zeros(m_crip.shape)
                    print("MENSAJE CIFRADO EN HILL CON CODIGO HAMMING Y ENVIADO: ")
                    print("--------------------------------------------------------------")
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
                    string = salida
                    binary_converted = ' '.join(format(ord(c), 'b') for c in string)
                    MENSAJE_CIFRADO = binary_converted

                    #INICIO DE HILL
                    d=MENSAJE_CIFRADO
                    d = d.replace(" ", "") 
                    data=list(d) 
                    data.reverse()
                    c,ch,j,r,h=0,0,0,0,[] 

                    while ((len(d)+r+1)>(pow(2,r))):
                        r=r+1
                    for i in range(0,(r+len(data))):
                        p=(2**c)

                        if(p==(i+1)):
                            h.append(0)
                            c=c+1

                        else:
                            h.append(int(data[j]))
                            j=j+1

                    for parity in range(0,(len(h))):
                        ph=(2**ch)
                        if(ph==(parity+1)):
                            startIndex=ph-1
                            i=startIndex
                            toXor=[]

                            while(i<len(h)):
                                block=h[i:i+ph] 
                                toXor.extend(block)
                                i+=2*ph

                            for z in range(1,len(toXor)):
                                h[startIndex]=h[startIndex]^toXor[z]
                            ch+=1

                    h.reverse()
                    Codigo_hamming_enviado = (''.join(map(str, h)))
                    print (Codigo_hamming_enviado)
                    print("--------------------------------------------------------------") 
                    ser = serial.Serial(
                        port = '/dev/ttyS0',
                        baudrate = 57600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)
                    msg = ""
                    ser.write(MENSAJE_CIFRADO.encode('utf-8'))
                    time.sleep(4)
                    ser.write(Codigo_hamming_enviado.encode('utf-8'))
                    edd = 1 

                #ENVIO DE MENSAJE PERSONALIZADO DESDE LA CONSOLA.
                #ESTE CODIGO REALIZA LO MISMO QUE EL CODIGO DESCRITO ANTERIORMENTE, CON LA DIFERENCIA QUE ES UN MENSAJE PERSONALIZADO QUE EL USUARIO DEBE
                #DE ESCRIBIR DESDE LA CONSOLA.
                if eleccion == 2:
                    os.system('clear')
                    edd = 0
                    os.system ("clear")
                    def imprimir_matriz(charar):
                        for i in range(2):
                            for j in range(2):
                                print(int(charar[i][j]), "\t", end='')
                            print("\n");
                    cifrado = input("INTRODUCIR MENSAJE: ");
                    cifrado = cifrado.upper().replace(" ", "");
                    Clave = np.empty((4, 4));
                    msj="";
                    m_crip=np.zeros((math.ceil(len(cifrado)/2),2))

                
                    Clave[0][0] = 11;
                    Clave[0][1] = 8;
                    Clave[1][0] = 3;
                    Clave[1][1] = 7;

                    
                    diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3,'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
                    abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

                    cipher="";
                    i=0
                    j=0
                    while True:
                        try:
                            if (np.size(m_crip) / 2 == j):
                                break
                            
                            m_crip[j][0]=diccionario_letras[cifrado[i]]
                            m_crip[j][1]=diccionario_letras[cifrado[i+1]]
                            i+=2
                            j+=1
                        
                        except:
                           
                            m_crip[j][0] = diccionario_letras[cifrado[i]]
                            break
                    

                    c1 = 0
                    c2 = 0
                    m1 = 0
                    m2 = 0

                    cipher=np.zeros(m_crip.shape)
                    print("MENSAJE CIFRADO EN HILL CON CODIGO HAMMING Y ENVIADO: ")
                    print("--------------------------------------------------------------")
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
                    string = salida
                    binary_converted = ' '.join(format(ord(c), 'b') for c in string)
                    MENSAJE_CIFRADO = binary_converted
                    

                    d=MENSAJE_CIFRADO
                    d = d.replace(" ", "") 
                    data=list(d) 
                    data.reverse()
                    c,ch,j,r,h=0,0,0,0,[] 

                    while ((len(d)+r+1)>(pow(2,r))):
                        r=r+1
                    for i in range(0,(r+len(data))):
                        p=(2**c)

                        if(p==(i+1)):
                            h.append(0)
                            c=c+1

                        else:
                            h.append(int(data[j]))
                            j=j+1

                    for parity in range(0,(len(h))):
                        ph=(2**ch)
                        if(ph==(parity+1)):
                            startIndex=ph-1
                            i=startIndex
                            toXor=[]

                            while(i<len(h)):
                                block=h[i:i+ph] 
                                toXor.extend(block)
                                i+=2*ph

                            for z in range(1,len(toXor)):
                                h[startIndex]=h[startIndex]^toXor[z]
                            ch+=1

                    h.reverse()
                    Codigo_hamming_enviado = (''.join(map(str, h)))
                    print (Codigo_hamming_enviado)
                    print("--------------------------------------------------------------") 
                    ser = serial.Serial(
                        port = '/dev/ttyS0',
                        baudrate = 57600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)
                    msg = ""
                    ser.write(MENSAJE_CIFRADO.encode('utf-8'))
                    time.sleep(4)
                    ser.write(Codigo_hamming_enviado.encode('utf-8'))
                    edd = 1



    #OPCION TRES DE NUESTRO MENU PRINCIPAL, ENVIO DE ARCHIVO O MENSAJE, CIFRADO EN VEGENER.
    if opcion == 3:
            #APERTURAMOS NUESTRO PUERTO SERIAL 
            ser = serial.Serial(
                port = '/dev/ttyS0',
                baudrate = 57600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            msg = ""
            #IDENTIFICADOR DE CIFRADO
            codificacion = "3"
            ser.write(codificacion.encode('utf-8'))
            os.system('clear')


            edd = 0
            #ELECCION DE ENVIO 
            while edd < 1 :
                print ("1) Archivo de texto")
                print ("2) Mensaje")
                eleccion = int (input("¿Que desea enviar?  "))

                #INICIA EL ENVIO DE UN ARCHIVO DE TEXTO
                if eleccion == 1:
                    os.system('clear')
                    edd = 0
                    alfabetos = "abcdefghijklmnopqrstuvwxyz" 
                    alfabetos = "abcdefghijklmnopqrstuvwxyz" 

                    #FUNCION DE ENCRIPTAR. 
                    def encriptar(p, k):
                        c = ""
                        kpos = [] 
                        for x in k:
                            kpos.append(alfabetos.find(x))
                        i = 0
                        for x in p:
                            if i == len(kpos):
                                i = 0
                            pos = alfabetos.find(x) + kpos[i] 
                            if pos > 25:
                                pos = pos-26              
                            c += alfabetos[pos].capitalize()  
                            i +=1
                        
                        string = c
                        binary_converted = ' '.join(format(ord(c), 'b') for c in string)
                        MENSAJE_CIFRADO = binary_converted
                        print("MENSAJE CIFRADO EN VIGENER CON CODIGO HAMMING Y ENVIADO: ")
                        print("--------------------------------------------------------------")
     
                        #INICIO DE HAMMING 
                        d=MENSAJE_CIFRADO
                        d = d.replace(" ", "") 
                        data=list(d) 
                        data.reverse()
                        c,ch,j,r,h=0,0,0,0,[] 

                        while ((len(d)+r+1)>(pow(2,r))):
                            r=r+1
                        for i in range(0,(r+len(data))):
                            p=(2**c)

                            if(p==(i+1)):
                                h.append(0)
                                c=c+1

                            else:
                                h.append(int(data[j]))
                                j=j+1

                        for parity in range(0,(len(h))):
                            ph=(2**ch)
                            if(ph==(parity+1)):
                                startIndex=ph-1
                                i=startIndex
                                toXor=[]

                                while(i<len(h)):
                                    block=h[i:i+ph] 
                                    toXor.extend(block)
                                    i+=2*ph

                                for z in range(1,len(toXor)):
                                    h[startIndex]=h[startIndex]^toXor[z]
                                ch+=1

                        h.reverse()
                        Codigo_hamming_enviado = (''.join(map(str, h)))
                        print (Codigo_hamming_enviado)
                        print("--------------------------------------------------------------") 


                        ser = serial.Serial(
                            port = '/dev/ttyS0',
                            baudrate = 57600,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS,
                            timeout=1)
                        ser.write(MENSAJE_CIFRADO.encode('utf-8'))
                        time.sleep(4)
                        ser.write(Codigo_hamming_enviado.encode('utf-8'))
                        



                    #ABRIMOS NUESTRO ARCHIVO.  
                    archivo = open("mensaje.txt")
                    texto = str(archivo.read())

                    p = texto
                    print("Enviando archivo...")
                    p = p.replace(" ", "")  
                    p = p.strip()
                    if p.isalpha():
                        #LLAVE DE CIFRADO
                        k = "god"
                        k = k.strip()  
                        if k.isalpha():
                            c = encriptar(p, k)

                    time.sleep (5)
                    edd = 1

                #ENVIO DE MENSAJE PERSONALIZADO DESDE LA CONSOLA.
                #ESTE CODIGO REALIZA LO MISMO QUE EL CODIGO DESCRITO ANTERIORMENTE, CON LA DIFERENCIA QUE ES UN MENSAJE PERSONALIZADO QUE EL USUARIO DEBE
                #DE ESCRIBIR DESDE LA CONSOLA.
                if eleccion == 2:
                    os.system('clear')
                    edd = 0

                    alfabetos = "abcdefghijklmnopqrstuvwxyz" 
                    alfabetos = "abcdefghijklmnopqrstuvwxyz" 
                    def encriptar(p, k):
                        c = ""
                        kpos = [] 
                        for x in k:
                            kpos.append(alfabetos.find(x))
                        i = 0
                        for x in p:
                            if i == len(kpos):
                                i = 0
                            pos = alfabetos.find(x) + kpos[i] 
                            if pos > 25:
                                pos = pos-26              
                            c += alfabetos[pos].capitalize()  
                            i +=1
                       
                        string = c
                        binary_converted = ' '.join(format(ord(c), 'b') for c in string)
                        MENSAJE_CIFRADO = binary_converted
                        print("MENSAJE CIFRADO EN VIGENER CON CODIGO HAMMING Y ENVIADO: ")
                        print("--------------------------------------------------------------")

                        d=MENSAJE_CIFRADO
                        d = d.replace(" ", "") 
                        data=list(d) 
                        data.reverse()
                        c,ch,j,r,h=0,0,0,0,[] 

                        while ((len(d)+r+1)>(pow(2,r))):
                            r=r+1
                        for i in range(0,(r+len(data))):
                            p=(2**c)

                            if(p==(i+1)):
                                h.append(0)
                                c=c+1

                            else:
                                h.append(int(data[j]))
                                j=j+1

                        for parity in range(0,(len(h))):
                            ph=(2**ch)
                            if(ph==(parity+1)):
                                startIndex=ph-1
                                i=startIndex
                                toXor=[]

                                while(i<len(h)):
                                    block=h[i:i+ph] 
                                    toXor.extend(block)
                                    i+=2*ph

                                for z in range(1,len(toXor)):
                                    h[startIndex]=h[startIndex]^toXor[z]
                                ch+=1

                        h.reverse()
                        Codigo_hamming_enviado = (''.join(map(str, h)))
                        print (Codigo_hamming_enviado)
                        print("--------------------------------------------------------------") 


                        ser = serial.Serial(
                            port = '/dev/ttyS0',
                            baudrate = 57600,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS,
                            timeout=1)
                        ser.write(MENSAJE_CIFRADO.encode('utf-8'))
                        time.sleep(4)
                        ser.write(Codigo_hamming_enviado.encode('utf-8'))
                        



        
                    
                    p = input("INTRODUCIR MENSAJE: ");
                    p = p.replace(" ", "")  
                    if p.isalpha():
                        k = "god"
                        k = k.strip()  
                        if k.isalpha():
                            c = encriptar(p, k)

                    time.sleep (5)    
                    edd = 1    
        


    #OPCION CUATRO DE NUESTRO MENU PRINCIPAL, NOS QUEDAMOS ESPERANDO LA RECEPCION DE ALGUN MENSAJE A TRAVEZ DEL PUERTO DE COMUNICACION. 
    if opcion == 4:
        tiempoespera = 0
        while tiempoespera < 1:
            #SE QUEDA ESPERADO HASTA RECIBIR ALGO. 
            if ser.in_waiting > 0:
                #LO PRIMERO QUE DETECTA ES EL TIPO DE CODIFICACION QUE ESTA POR RECIBIR 
                tipo_codificacion = ser.readline().decode('utf-8').rstrip()
                if tipo_codificacion == "1":
                    os.system('clear')
                    print("Se esta esperando un mensaje en codigo CESAR")
                    tiempoespera = 0
                    while tiempoespera < 1:
                        #VUELVE A COLOCARSE EN MODO DE ESCUCHA.
                        if ser.in_waiting > 0:
                            #RECIBE EL MENSAJE CIFRADO
                                line = ser.readline().decode('utf-8').rstrip()
                                MENSAJE_CIFRADO = line;
                                numeros = MENSAJE_CIFRADO.split(" ")
                                decodificado = ""
                                #DECIFRA EL CODIGO CIFRADO EN BINARIO, A ASCII
                                for numero_binario in numeros:
                                    numero_decimal = int(numero_binario, 2)
                                    letra = chr(numero_decimal)
                                    decodificado += letra
                                
                                #TOMA EL MENSAJE EN ASCCI E INICIA A HACER LA DECODIFICACION DE CESAR. 
                                texto1 = decodificado
                                #LLAVE DE DECODIFICACION.
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
                                os.system('clear')
                                print("MENSAJE RECIBIDO:")
                                print(cifrado)

                                # VERIFICA EL HAMMING 
                                d=ser.readline().decode('utf-8').rstrip()
                                data=list(d)
                                data.reverse()
                                c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[] 
                                for k in range(0,len(data)):
                                    p=(2**c)
                                    h.append(int(data[k]))
                                    h_copy.append(data[k])
                                    if(p==(k+1)):
                                        c=c+1

                                for parity in range(0,(len(h))):
                                    ph=(2**ch)
                                    if(ph==(parity+1)):

                                        startIndex=ph-1
                                        i=startIndex
                                        toXor=[]

                                        while(i<len(h)):
                                            block=h[i:i+ph]
                                            toXor.extend(block)
                                            i+=2*ph

                                        for z in range(1,len(toXor)):
                                            h[startIndex]=h[startIndex]^toXor[z]
                                        parity_list.append(h[parity])
                                        ch+=1
                                parity_list.reverse() 
                                error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
                                if((error)==0):
                                    print('No hay ningún error en el codigo Hamming recibido')
                                    time.sleep (5)
                                    tiempoespera = 1
                                    os.system('clear')

                                elif((error)>=len(h_copy)):
                                    print('No se puede detectar el error')
                                else:
                                    print('El error esta en',error,'bit')
                                    if(h_copy[error-1]=='0'):
                                        h_copy[error-1]='1'
                                    elif(h_copy[error-1]=='1'): 
                                        h_copy[error-1]='0'
                                        print('Despues de corregir el codigo Hamming es:- ')
                                    h_copy.reverse()
                                    print(int(''.join(map(str, h_copy)))) 
                                    time.sleep (5)
                                    tiempoespera = 1
                                    os.system('clear')
                                        

                # SEGUNDO TIPO DE CODIFICACION, EN ESTE CASO ES CODIFICACION HILL.
                if tipo_codificacion == "2":
                    os.system('clear')
                    print("Se esta esperando un mensaje en codigo HILL")
                    tiempoespera = 0
                    while tiempoespera < 1:
                        if ser.in_waiting > 0:
                            line = ser.readline().decode('utf-8').rstrip()
                            MENSAJE_CIFRADO = line;
                            numeros = MENSAJE_CIFRADO.split(" ")
                            decodificado = ""
                            #DECODIFICA EL MENSAJE DE BINARIO A ASCII
                            for numero_binario in numeros:
                                numero_decimal = int(numero_binario, 2)
                                letra = chr(numero_decimal)
                                decodificado += letra
                            

                            #INICIA CON LA DECOFICIACION HILL 

                            def imprimir_matriz(charar):
                                for i in range(2):
                                    for j in range(2):
                                        print(int(charar[i][j]), "\t", end='')
                                    print("\n");

                            print("--------------------------------------------------------------")
                          
                            os.system('clear')
                            Texto = decodificado;
                            Texto = Texto.upper().strip().replace(" ", "");
                           
                            Clave = np.empty((4, 4));
                            msj = "";
                            m_crip = np.zeros((math.ceil(len(Texto) / 2), 2))
                            #LLAVE DE DECODIFICACION
                            Clave[0][0] = 11;
                            Clave[0][1] = 8;
                            Clave[1][0] = 3;
                            Clave[1][1] = 7;

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
                                    #print(Texto[i])
                                    m_crip[j][0] = diccionario_letras[Texto[i]]
                                    break
                            # for i in range(m_crip.length)

                            c1 = 0
                            c2 = 0
                            m1 = 0
                            m2 = 0

                            descipher = np.zeros(m_crip.shape)
                            print("MENSAJE RECIBIDO: ")
                            for i in range(int(np.size(m_crip) / 2)):
                                m1 = m_crip[i][0]
                                m2 = m_crip[i][1]
                                c1 = InClave[0][0] * m1 + InClave[1][0] * m2
                                c2 = InClave[0][1] * m1 + InClave[1][1] * m2
                                descipher[i][0] = c1 % 26
                                descipher[i][1] = c2 % 26

                                #print(int(cipher[i][0]), " - ", int(cipher[i][1]))
                                print(abecedario[int(descipher[i][0])], "", abecedario[int(descipher[i][1])], " ", end="")
                                palabra = abecedario[int(descipher[0][0])]+ abecedario[int(descipher[0][1])]
                                palabra2 = abecedario[int(descipher[1][0])]+ abecedario[int(descipher[1][1])]
                                palabracompleta = (palabra+palabra2)

                            print ("")

                            #INICIA CON LA COMPROBACION DEL HAMMING
                            d=ser.readline().decode('utf-8').rstrip()
                            data=list(d)
                            data.reverse()
                            c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[] 
                            for k in range(0,len(data)):
                                p=(2**c)
                                h.append(int(data[k]))
                                h_copy.append(data[k])
                                if(p==(k+1)):
                                    c=c+1

                            for parity in range(0,(len(h))):
                                ph=(2**ch)
                                if(ph==(parity+1)):

                                    startIndex=ph-1
                                    i=startIndex
                                    toXor=[]

                                    while(i<len(h)):
                                        block=h[i:i+ph]
                                        toXor.extend(block)
                                        i+=2*ph

                                    for z in range(1,len(toXor)):
                                        h[startIndex]=h[startIndex]^toXor[z]
                                    parity_list.append(h[parity])
                                    ch+=1
                            parity_list.reverse() 
                            error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
                            if((error)==0):
                                print('No hay ningún error en el codigo Hamming recibido')
                                time.sleep (5)
                                tiempoespera = 1
                                os.system('clear')
                            elif((error)>=len(h_copy)):
                                print('No se puede detectar el error')
                            else:
                                print('El error esta en',error,'bit')
                                if(h_copy[error-1]=='0'):
                                    h_copy[error-1]='1'
                                elif(h_copy[error-1]=='1'): 
                                    h_copy[error-1]='0'
                                    print('Despues de corregir el codigo Hamming es:- ')
                                h_copy.reverse()
                                print(int(''.join(map(str, h_copy)))) 

                                time.sleep (5)
                                tiempoespera = 1
                                os.system('clear')

                #TIPO DE CODIFICACION 3 VINEGER
                if tipo_codificacion == "3":
                    os.system('clear')
                    print("Se esta esperando un mensaje en codigo VIGENER")
                    tiempoespera = 0
                    while tiempoespera < 1:
                        if ser.in_waiting > 0:
                            line = ser.readline().decode('utf-8').rstrip()
                            MENSAJE_CIFRADO = line;
                            numeros = MENSAJE_CIFRADO.split(" ")
                            decodificado = ""
                            #DECODIFICA DE BINARIO A ASCII 
                            for numero_binario in numeros:
                                numero_decimal = int(numero_binario, 2)
                                letra = chr(numero_decimal)
                                decodificado += letra
                        
                            alphabets = "abcdefghijklmnopqrstuvwxyz" 
                            #FUNCION DE DESENCRIPTAR
                            def decrypt(c, k):
                                p = ""
                                kpos = []
                                for x in k:
                                    kpos.append(alphabets.find(x))
                                i = 0
                                for x in c:
                                    if i == len(kpos):
                                        i = 0
                                    pos = alphabets.find(x.lower()) - kpos[i]
                                    if pos < 0:
                                        pos = pos + 26
                                    p += alphabets[pos].lower()
                                    i +=1
                                os.system('clear')
                                print("MENSAJE RECIBIDO:")
                                print(p)
                                
                            c = decodificado
                            c = c.replace(" ", "")
                            if c.isalpha():
                                #LLAVE DE ENCRIPTACION
                                k = "god"
                                if not k.isalpha():
                                    print("algo salio mal")
                                else:
                                    p = decrypt(c, k)

                            #INICIO DE REVISION DEL HAMMING
                            d=ser.readline().decode('utf-8').rstrip()
                            data=list(d)
                            data.reverse()
                            c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[] 
                            for k in range(0,len(data)):
                                p=(2**c)
                                h.append(int(data[k]))
                                h_copy.append(data[k])
                                if(p==(k+1)):
                                        c=c+1

                            for parity in range(0,(len(h))):
                                ph=(2**ch)
                                if(ph==(parity+1)):

                                    startIndex=ph-1
                                    i=startIndex
                                    toXor=[]

                                    while(i<len(h)):
                                        block=h[i:i+ph]
                                        toXor.extend(block)
                                        i+=2*ph

                                    for z in range(1,len(toXor)):
                                        h[startIndex]=h[startIndex]^toXor[z]
                                    parity_list.append(h[parity])
                                    ch+=1
                            parity_list.reverse() 
                            error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
                            if((error)==0):
                                print('No hay ningún error en el codigo Hamming recibido')
                                time.sleep (5)
                                tiempoespera = 1
                                os.system('clear')
                            elif((error)>=len(h_copy)):
                                print('No se puede detectar el error')
                            else:
                                print('El error esta en',error,'bit')
                                if(h_copy[error-1]=='0'):
                                    h_copy[error-1]='1'
                                elif(h_copy[error-1]=='1'): 
                                    h_copy[error-1]='0'
                                    print('Despues de corregir el codigo Hamming es:- ')
                                h_copy.reverse()
                                print(int(''.join(map(str, h_copy)))) 
                                            
                                time.sleep (5)
                                tiempoespera = 1
                                os.system('clear')
                                    
    #ACCION QUE REALIZA UNA VEZ ENVIADO UN MENSAJE. 
    else:
        os.system('clear')
        print("GRACIAS POR UTILIZAR EL SERVICIO PRIVADO DE MENSAJERIA")
        time.sleep (2)
        os.system('clear')
