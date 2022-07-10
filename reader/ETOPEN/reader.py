import os
dir = '/home/salas/Escritorio/lista_ataques/pcaps'
num_ata_det = 0
list_ata_det = []
with os.scandir(dir) as pcaps:
    for pcap in pcaps:
        print("Procesando pcap: " + pcap.name)
        folder = pcap.name.split(".")[0]
        os.system('mkdir /home/salas/Escritorio/lista_ataques/alertas/'+folder)
        os.system('chmod 777 /home/salas/Escritorio/lista_ataques/alertas/'+folder)
        os.system('snort -c /etc/snort/snort.conf -l /home/salas/Escritorio/lista_ataques/alertas/' + folder + ' -r /home/salas/Escritorio/lista_ataques/pcaps/' + pcap.name)
        os.system('chmod 666 /home/salas/Escritorio/lista_ataques/alertas/'+folder+'/*')
        if os.stat('/home/salas/Escritorio/lista_ataques/alertas/'+folder+'/alerts').st_size == 0:
            print("No alertas generadas para " + pcap.name)
        else:
            print("Alertas generadas para " + pcap.name)
            num_ata_det += 1
            list_ata_det.append(folder)
print("*****************************************************************")
print("El numero de ataques detectados es: " + str(num_ata_det) + "/18")
print("*****************************************************************")
print("Los ataques para los que se han generado alertas han sido: ")
for i in list_ata_det:
    print("--------> " + i)
