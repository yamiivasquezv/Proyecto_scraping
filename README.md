# Proyecto_scraping
Descripción: este proyecto es una implementación a pequeña escala de un search engine para obtener el rating de los diferentes
productos de belleza que se encuentran en el mercado. Utilizando como herramientas scraping de las paginas web, envío de informe
con los resultados del analisis por correo electrónico y transfiriendo dicho informe por ftp a otro servidor.

Especificaciones Técnicas para CentOS7

1. Instalar python 3.4 (si no lo tienes):

        sudo yum install wget -y
    
    wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz
    
    tar xf Python-3.*
    
    cd Python-3.*
    
    sudo yum -y install @development
    
    ./configure
    
    make
    
    sudo make

2. Instalar PIP para Python3.4

-Primero actualice la caché del repositorio de paquetes de yum package manager con el siguiente comando:

    sudo yum makecache

-Python PIP no está disponible en el repositorio oficial de paquetes de CentOS 7.
Pero está disponible en el repositorio de paquetes de EPEL. Antes de poder instalar Python PIP en CentOS 7,
debe añadir el repositorio EPEL a su CentOS 7. Para añadir un repositorio de paquetes EPEL en CentOS 7,
ejecute el siguiente comando:

    sudo yum install epel-release

-Ahora actualice de nuevo la caché del repositorio de paquetes de su CentOS 7 con el siguiente comando:

    sudo yum makecache

-Puede ejecutar el siguiente comando para buscar un paquete Python3.4 PIP:

    sudo yum search pip | grep python3

-Ahora puedes instalar Python 3 PIP con el siguiente comando:

    sudo yum install python34-pip

-Ahora puede comprobar si Python 3 PIP funciona con el siguiente comando:

    pip3.4 -V

3. Instalar los paquetes requests, smtplib, pysftp, textblob y nltk con el siguiente comando:

        sudo pip3.4 install PACKAGE_NAME

-Para desintalar algún paquete ejecute el comando:

    sudo pip3.4 uninstall PACKAGE_NAME

MANUAL DE USUARIO PARA EL PROGRAMA:

1. Crear un archivo .txt con el nombre de su preferencia el cual será la plantilla donde se almacenarán los datos obtenidos del análisis. Dicha plantilla tendrá el siguiente formato:
*****************************INICIO DEL FORMATO DE LA PLANTILLA****************************
¡Hola ${NOMBRE_PERSONA}!

Este es un mensaje con la información sobre la calificacion del producto ${NOMBRE_PRODUCTO}:

-Se analizaron ${CANT_COMENT} comentarios.
-La calificación promedio fue : ${CALI_PROM}
-De los ${CANT_COMENT} comentarios, ${CANT_COMENT_POS} fueron POSITIVOS, ${CANT_COMENT_NEG} fueron NEGATIVOS y ${CANT_COMENT_NEU} fueron NEUTRALES.
-De estos ${CANT_COMENT} comentarios, ${VERY_OBJT} son MUY OBJETIVOS, ${MED_OBJT} son MEDIO OBJETIVOS, ${MED_SUBJT} son MEDIO SUBJETIVOS y ${VERY_SUBJT} son muy SUBJETIVOS.


Atentamente,
Milka Search Engine.


*****************************FIN DEL FORMATO DE LA PLANTILLA****************************
2. Sustituir las variables:

ARCHIVO_PLANTILLA = *poner aquí la ruta hacia el archivo .txt creado*
MI_CORREO = *poner aquí el correo desde el cual se enviará la informacion*
PASSWORD = *poner aquí la contraseña del correo de arriba*

nombre = *nombre de la persona*
correo = *poner aquí el correo de la persona a la cual enviara la informacion*

 

3. Dirección URL de la pagina a la cual desea hacer scraping. Verificar primero si esta se le puede hacer scraping chequeando el source code y buscar ahí los comentarios. Si la información no está ahí el scraping no funcionara.  



Esto es todo,
Yamilka Vasquez.
