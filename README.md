# Entregables del proyecto PAPIIT IA106520

Este repositorio contiene los entregables del reporte final del proyecto PAPIIT IA106520 "Visión activa y robótica basada en comportamientos en el desarrollo de vehículos autónomos".
Los entregables son los que se listan a continuación:
* Tesis
  * Diseño y construcción de ambientes en el simulador de robots Gazebo para vehículos sin conductor (resultado directo, concluído)
  * Navegación autónoma para un vehículo sin conductor usando el simulador Webots (resultado directo, en desarrollo)
  * Desarrollo de interfaz cerebro computadora para robots de servicio doméstico (resultado directo, en desarrollo)
  * Mapeo y localización simultáneos en ambientes no estructurados usando el simulador Gazebo (resultado directo, en desarrollo)
  * Estimación de trayectoria a partir de imágenes RGB-D para un robot móvil autónomo (resultado colateral, en desarrollo)
  * Uso de redes neuronales artificiales para el reconocimiento de palabras clave para un robot de servicio (resultado colateral, concluído)
  * Generación de imágenes sintéticas de interiores utilizadas por robots móviles (resultado colateral, concluído)
* Reportes
  * Sistema visual para la detección de peatores usando el MS Kinect (resultado directo, concluído)
* Software
  * Simulador para vehículos sin conductor empleado en la categoría AutoModelCar del Torneo Mexicano de Robótica 2021
* Artículos 
  * Mass Estimation in Manipulation Tasks of Domestic Service Robots using Fault Reconstruction Techniques (manuscrito en ArXiv)
  * Probabilistic Logic for Driving Safety in Self-Driving Cars (manuscrito en Overleaf)
* Prototipos
  * Vehículo a escala
* Organización de eventos académicos
  * Categoría AutoModelCar del Torneo Mexicano de Robótica 2021, modalidad virtual

### Simulador del Vehículo a Escala
Se desarrolló un simulador para el vehículo a escala autoNOMOS partiendo del simulador desarrollado el ITAM (https://github.com/ITAM-Robotica/Eagle_Knights-Wiki/wiki/autonomos-gazebo). La siguiente imagen muestra un ejemplo de este simulador. 
<img src="https://github.com/mnegretev/PAPIIT_IA106520/blob/master/documentation/figures/GazeboExample.png" alt="Ejemplo del simulador" width="640"/>

### Detección y seguimiento de carril
Se han probado varios algoritmos para la detección de carriles. Las pruebas se hicieron utilizando el simulador descrito. Las siguientes imágenes muestran ejemplos de los resultados obtenidos. 
<img src="https://github.com/mnegretev/PAPIIT_IA106520/blob/master/documentation/figures/LaneSegmentation.png" alt="Ejemplo de detección de carriles" width="640"/>

### Detección de peatones
Se desarrollaron programas utilizando redes neuronales artificiales para la detección de peatones. Se probaron dos bibliotecas para esta tarea: TensorFlow y OpenVINO. En ambos casos, las redes se entrenaron usando imágenes sintéticas generadas con el mismo simulador. La siguiente imagen muestra un ejemplo de la detección lograda. 
<img src="https://github.com/mnegretev/PAPIIT_IA106520/blob/master/documentation/figures/pedestrian_detection.png" alt="Ejemplo de detección de peatones" width="640"/>

### Detección de señales de tránsito
Se desarrollaron programas para la deteccin de semáforos utilizando tanto redes neuronales como segmentación por color. La siguiente imagen muestra un ejemplo de esta detección:
<img src="https://github.com/mnegretev/PAPIIT_IA106520/blob/master/documentation/figures/traffic_ligh_detection.png" alt="Ejemplo de detección de semáforos" width="640"/>

### Lógica probabilística
Además de los desarrollos anteriores, se comenzó a explorar el modelado probabilístico mediante el uso del lenguaje ProbLog. Dentro del paquete "knowldege" se encuentran varios códigos en ProbLog para la evasión de obstáculos desde un enfoque probabilístico. 

### Torneo Mexicano de Robótica
Cabe mencionar que el software desarrollado en este proyecto sirvió para organizar la categoría AutoModelCar del Torneo Mexicano de Robótica, la cual se llevó a cabo de manera virtual. El software utilizado para esta competencia es muy parecido al de este proyecto y se encuentra en 
https://github.com/mnegretev/TMR-2021-AutoModelCar

Los códigos fuente de las aplicaciones, así como otros materiales, se encuentran en este repositorio. 
