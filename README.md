# TCP servidor-cliente
## Ejemplo Socket TCP

En este ejemplo nos proponer a deployar el servidor en heroku y usaremos la app cliente para probarlo.

## Correr servidor

Los archivos [client.py](client.py) y [server.py](server.py) proveen una implementación de ejemplo del sistema de intercambio de archivos, utilizando el protocolo TCP para la comunicación entre el cliente y el servidor.

### Corriendo el servidor

Para correr el servidor debemos ejecutar el siguiente comando:

    python3 tcp-server.py -H <own-host> -P <own-port>

Los parámetros default son `own-host: 127.0.0.1` y `own-port: 8080`, por lo que localmente directamente podemos correr:

   python3 tcp-server.py

### Corriendo el cliente

Para correr el cliente debemos ejecutar el siguiente comando:

    python3 tcp-client.py -H <server-host> -P <server-port> -f <file>

Los parámetros default son `server-host: 127.0.0.1` y `server-port: 8080`, por lo que localmente solo debemos especificar el archivo a enviar.
En el repo esta incluido un archivo de ejemplo, por lo que, para utilizar ese archivo corremos:

    python3 tcp-client.py -f ./example.txt
