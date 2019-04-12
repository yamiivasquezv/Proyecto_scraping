import requests

#import nltk
#nltk.download('vader_lexicon') # do this once: grab the trained model from the web
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
import smtplib
import pysftp

from textblob import TextBlob
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Analyzer = SentimentIntensityAnalyzer()

count_pos_reviews = 0
count_neg_reviews = 0
count_neu_reviews = 0
very_objetive = 0
medio_objetive = 0
medio_subjective = 0
very_subjective = 0
promedio = 0
nombre_producto =''
dir_correo = ''
lista_rating = []
lista_reviews = []

ARCHIVO_PLANTILLA = R"C:\Users\Minombre\Documentos\plantilla.txt"

MI_CORREO = 'micorreo@gmail.com'
PASSWORD = 'mipassword123'

MTA_HOST = 'smtp.gmail.com'
MTA_PORT = 587 # SSL: 465, TLS: 587


def lee_plantilla(filename):
    """
    Retorna un objeto Template que encapsula el contenido de filename
    """
    with open(filename, 'r', encoding='iso-8859-1') as archivo:
        contenido3 = archivo.read()
    return Template(contenido3)

def main():
    global count_pos_reviews
    global count_neg_reviews
    global count_neu_reviews
    global very_objetive
    global medio_objetive
    global medio_subjective
    global very_subjective

    scrapy_pagina()
    message_template = lee_plantilla(ARCHIVO_PLANTILLA)

    nombre = 'Luis'
    correo = "luis@gmail.com"

    # crea sesión SMTP
    s = smtplib.SMTP(host=MTA_HOST, port=MTA_PORT)
    s.starttls()
    s.set_debuglevel(1) # esto se debería de remover en un ambiente real
    s.login(MI_CORREO, PASSWORD)

    # Para cada contacto, envía correo:

    msj = MIMEMultipart()       # create a message

    # agrega el nombre de la persona en el mensaje de la plantilla
    mensaje = message_template.substitute(NOMBRE_PERSONA=nombre.title(),NOMBRE_PRODUCTO=nombre_producto.title(),CANT_COMENT=str(len(lista_reviews)).title(),
                                          CALI_PROM=str(promedio).title(),CANT_COMENT_POS=str(count_pos_reviews).title(),CANT_COMENT_NEG=str(count_neg_reviews).title(),
                                          CANT_COMENT_NEU=str(count_neu_reviews).title(),VERY_OBJT=str(very_objetive).title(),MED_OBJT=str(medio_objetive).title(),
                                          MED_SUBJT=str(medio_subjective).title(),VERY_SUBJT=str(very_subjective).title())

    # Imprime el mensaje
    # print(mensaje)

    # asigna parámetros al correo
    msj['From']=MI_CORREO
    msj['To']=correo
    msj['Subject']="Puntuación de Productos con Milka Search Engine"

    # agrega mensaje al cuerpo del correo
    msj.attach(MIMEText(mensaje, 'plain'))

    # envía mensaje usando sesión creada anteriormente
    s.send_message(msj)
    del msj

    # Termina la sesión SMTP y cierra la conexión
    s.quit()
#****************************FUNCIÓN PARA ANALISIS DE SENTIMIENTOS DEL COMENTARIO**********************************

def sentiment_analyzer_scores(sentence):
    global count_pos_reviews
    global count_neg_reviews
    global count_neu_reviews
    global very_objetive
    global medio_objetive
    global medio_subjective
    global very_subjective

    blob = TextBlob(sentence)
    var1 = blob.sentiment.subjectivity
    var2 = blob.sentiment.polarity
    var1 = float(var1)
    var2 = float(var2)

    if var2 >= 0.5:
        print("CONCLUSIÓN: POSITIVO")
        count_pos_reviews = count_pos_reviews + 1
        if var1 < 0.25:
            very_objetive = very_objetive+1
        elif var1 >= 0.25 and var1 < 0.5:
            medio_objetive = medio_objetive+1
        elif var1 >= 0.5 and var1 < 0.75:
            medio_subjective = medio_subjective+1
        elif var1 >=0.75:
            very_subjective = very_subjective+1

    elif var2 <= (-0.5):
        print("CONCLUSIÓN: NEGATIVO")
        count_neg_reviews = count_neg_reviews + 1
        if var1 < 0.25:
            very_objetive = very_objetive+1
        elif var1 >= 0.25 and var1 < 0.5:
            medio_objetive = medio_objetive+1
        elif var1 >= 0.5 and var1 < 0.75:
            medio_subjective = medio_subjective+1
        elif var1 >=0.75:
            very_subjective = very_subjective+1
    else:
        print("CONCLUSIÓN: NEUTRAL")
        count_neu_reviews = count_neu_reviews + 1
        if var1 < 0.25:
            very_objetive = very_objetive+1
        elif var1 >= 0.25 and var1 < 0.5:
            medio_objetive = medio_objetive+1
        elif var1 >= 0.5 and var1 < 0.75:
            medio_subjective = medio_subjective+1
        elif var1 >=0.75:
            very_subjective = very_subjective+1

#*************************************************************************************************************************
#**********************************************************************************************************************
def scrapy_pagina():
    global count_pos_reviews
    global count_neg_reviews
    global count_neu_reviews
    global very_objetive
    global medio_objetive
    global medio_subjective
    global very_subjective
    global nombre_producto
    global dir_correo
    global lista_rating
    global lista_reviews
    global promedio

    url = "https://www.lorealparisusa.com/products/makeup/lip-color/lipstick/colour-riche-ultra-matte-highly-pigmented-nude-lipstick.aspx?shade=lilac-impulse"
    inicio_title = 'reviewRating'

    res = requests.get(url)

    contenido = res.content.decode('utf-8')
    contenido2 = contenido

    nombre_producto = input("Digite el nombre del producto del cual desea saber su valoración: ")

    #*******************WHILE PARA ENCONTRAR LA CALIFICACION DEL PRODUCTO***********************
    while inicio_title in contenido:
        i1 = contenido.find(inicio_title)
        contenido = contenido[i1:]
        inicio_title_verdadero = 'ratingValue">'
        i1v = contenido.find(inicio_title_verdadero) #esto me encuentra el primer
        contenido = contenido[i1v+len(inicio_title_verdadero):]
        fin_title = '</span>'
        fin_indice = contenido.find(fin_title)
        lista_rating.append(contenido[:fin_indice])
        contenido = contenido[fin_indice+len(fin_title):]
    print(lista_rating)

    #********************CALCULO DEL PROMEDIO DE LA CALIFICACION**************************
    tam = len(lista_rating)
    lista_rating = map(int,lista_rating)
    x = sum(lista_rating)
    promedio = x/tam
    #print('La calificacion promedio del producto es: '+str(promedio))
    #*****************WHILE PARA ENCONTRAR LOS COMENTARIOS********************************
    while inicio_title in contenido2:
        il2 = contenido2.find(inicio_title)
        contenido2 = contenido2[il2:]
        inicio_title_verdadero2 = '"description">'
        ilv2 = contenido2.find(inicio_title_verdadero2)
        contenido2 = contenido2[ilv2+len(inicio_title_verdadero2):]
        fin_title2 = '</span>'
        fin_indice2 = contenido2.find(fin_title2)
        lista_reviews.append(contenido2[:fin_indice2])
        contenido2 = contenido2[fin_indice2+len(fin_title2):]
    print(lista_reviews)


    #***************ANALISIS DE SENTIMIENTOS**********************************
    for index in range(len(lista_reviews)):
        sentiment_analyzer_scores(lista_reviews[index])

#*************************RESULTADOS FINALES*****************************
    f = open("proyecto_ivan.txt","w+")

    f.write("La evaluación del producto '" + nombre_producto + "' es:\n")
    f.write('-Se analizaron '+str(len(lista_reviews))+' comentarios\n')
    f.write('-Calificación promedio: '+str(promedio)+'\n')
    f.write('-De los '+str(len(lista_reviews))+ ' comentarios '+str(count_pos_reviews)+' fueron POSITIVOS, '+str(count_neg_reviews)+' fueron NEGATIVOS y '+str(count_neu_reviews)+' fueron NEUTRALES\n')
    f.write('-De estos '+str(len(lista_reviews))+' comentarios '+str(very_objetive)+' son MUY OBJETIVOS, '+str(medio_objetive)+' son MEDIO OBJETIVOS, '+str(medio_subjective)+
          ' son MEDIO SUBJETIVOS y '+str(very_subjective)+' son MUY SUBJETIVOS')
    f.close()
    with pysftp.Connection('192.168.77.43', username='root', password='20150224') as sftp:
        with sftp.cd('holaThu_sFeb_s28_s12:14:41_s2019'):
            print(sftp.listdir())
            print(sftp.pwd) # retorna directorio en el que se está trabajando actualmente
            sftp.put(R"C:\Users\Yamilka\Desktop\PUCMM\Periodo 2 2018-2019\Temas Especiales\itt-521-publico-master\itt-521-publico-master\proyecto_ivan.txt")  # cargar archivo
            sftp.get('proyecto_ivan.txt', R"C:\Users\Yamilka\Desktop\PUCMM\Periodo 2 2018-2019\Temas Especiales\itt-521-publico-master\itt-521-publico-master\proyecto_ivan.txt")         # descargar archivo

    print("La evaluación del producto '" + nombre_producto + "' es:")
    print('Se analizaron '+str(len(lista_reviews))+' comentarios')
    print('Calificación promedio: '+str(promedio))
    print('De los '+str(len(lista_reviews))+ ' comentarios '+str(count_pos_reviews)+' fueron POSITIVOS, '+str(count_neg_reviews)+' fueron NEGATIVOS y '+str(count_neu_reviews)+' fueron NEUTRALES')
    print('De estos '+str(len(lista_reviews))+' comentarios '+str(very_objetive)+' son MUY OBJETIVOS, '+str(medio_objetive)+' son MEDIO OBJETIVOS, '+str(medio_subjective)+
          ' son MEDIO SUBJETIVOS y '+str(very_subjective)+' son MUY SUBJETIVOS')


if __name__ == '__main__':
    main()










