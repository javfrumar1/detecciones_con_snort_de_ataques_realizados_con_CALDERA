# Análisis de la capacidad de detección de Snort para ataques de red realizados con CALDERA bajo la Matriz MITRE ATT&CK.
Este repositorio pretende recoger información importante sobre el trabajo fin de grado "Análisis de la capacidad de detección del IDS Snort de ataques realizados mediante CALDERA bajo la matriz MITRE ATT&amp;CK". 
Está información está estructurada en 5 directorios principales:
-pcaps: contiene un pcap por cada ataque realizado con el tráfico que ha generado dicho ataque.
-alertas_ETOPEN: contiene un directorio por cada ataque realizado, donde se encuentran las alertas obtenidas para dicho ataque con el paquete de reglas ETOPEN. Además, se incluye un script en python que permite realizar una decodificación de las alertas obtenidas. Este script muestra los identificadores de las alertas obtenidas junto a la regla que ha generado dicha alerta.
-alertas_TALOS: este directorio es similar al anterior, pero conteniendo las alertas obtenidas para el paquete de reglas TALOS.
-reader: contiene los scripts utilizados para pasar los pcaps de los ataques por el IDS Snort y almacenar las alertas obtenidas en sus correspondientes carpetas.
-csv: contiene un conjunto de ficheros con la extensión csv que contienen información sobre los valores de los campos que provocan la generación de las alertas en cada uno de los ataques.
