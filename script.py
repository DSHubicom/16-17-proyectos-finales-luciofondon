import time
import json
import paho.mqtt.publish as publish
import requests


while 2 > 1:

    #Api  
    print "Publicando fecha: " + time.strftime("%H:%M:%S, %d-%m-%Y")
    publish.single('fecha/formato_completo',time.strftime("%H:%M:%S, %d-%m-%Y"),hostname='localhost')

    print "Publicando hora: " + time.strftime("%H")
    publish.single('fecha/hora',time.strftime("%H"),hostname='localhost')

    print "Publicando minuto: " + time.strftime("%M")
    publish.single('fecha/minuto',time.strftime("%M"),hostname='localhost')

    print "Publicando segundo: " + time.strftime("%S")
    publish.single('fecha/segundo',time.strftime("%S"),hostname='localhost')

    print "Publicando dia: " + time.strftime("%d")
    publish.single('fecha/dia',time.strftime("%d"),hostname='localhost')

    print "Publicando mes: " + time.strftime("%m")
    publish.single('fecha/mes',time.strftime("%m"),hostname='localhost')

    print "Publicando anio: " + time.strftime("%Y")
    publish.single('fecha/anio',time.strftime("%Y"),hostname='localhost')

    print "Publicando dia de la semana: " + time.strftime("%w")
    publish.single('fecha/dia_de_la_semana',time.strftime("%w"),hostname='localhost')

    print "Publicando semana del anio: " + time.strftime("%U")
    publish.single('fecha/semana_del_anio',time.strftime("%U"),hostname='localhost')

    #Api tiempo meteorologico
    response = requests.get('http://api.wunderground.com/api/0046ff2a3c970790/conditions/q/ES/caceres.json')
    assert response.status_code == 200
    data = response.json()

    print 'Publicando temperatura grados celsius: ' + str(data['current_observation']['temp_c'])
    publish.single('tiempo/celsius',data['current_observation']['temp_c'],hostname='localhost')

    print 'Publicando temperatura grados farenheit: ' + str(data['current_observation']['temp_f'])
    publish.single('tiempo/farenheit',data['current_observation']['temp_f'],hostname='localhost')

    print 'Publicando humedad: ' + data['current_observation']['relative_humidity']
    publish.single('tiempo/humedad',str(data['current_observation']['relative_humidity']),hostname='localhost')

    print 'Publicando presion: ' + data['current_observation']['pressure_in']
    publish.single('tiempo/presion',str(data['current_observation']['pressure_in']),hostname='localhost')

    print 'Publicando velocidad viento (mph): ' + str(data['current_observation']['wind_mph'])
    publish.single('tiempo/viento/velocidad',data['current_observation']['wind_mph'],hostname='localhost')

    print 'Publicando direccion viento: ' + data['current_observation']['wind_dir']
    publish.single('tiempo/viento/direccion',data['current_observation']['wind_dir'],hostname='localhost')

    print 'Publicando estacion atmosferica: ' + data['current_observation']['observation_location']['full']
    publish.single('tiempo/estacion',data['current_observation']['observation_location']['full'],hostname='localhost')


    
    time.sleep(5)
