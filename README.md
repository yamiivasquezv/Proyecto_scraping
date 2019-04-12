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

1.

