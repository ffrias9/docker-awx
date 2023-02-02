# docker-awx
Roles de Ansible para instalar Docker en CentOS 8 y luego crear un contenedor con Ansible AWX.

	- El rol "docker" se encarga de instalar Docker.
	- El rol "docker-compose" se encarga de instalar Docker-Compose.
	- El rol "awx" se encarga de crear un contenedor en Docker-Compose con Ansible AWX.

Las únicas variables que se pueden modificar son las variables "user", que se encuentra declarada en
el archivo "main.yml" dentro de la carpeta "vars" que contiene cada rol. En dicha variable, debemos
indicar el nombre del usuario al que queremos que le afecte la ejecución de los roles.

En el archivo "inventory", situado en "/roles/awx/files" podemos cambiar los siguientes valores:

	- admin_user=admin
	- admin_password=1234

Aquí deberemos indicar cuáles queremos que sean nuestras credenciales de acceso para acceder a la
interfaz de Ansible AWX. Si no se modifica el archivo "inventory", por defecto las credenciales de
acceso serán usuario "admin" con contraseña "1234".

Al ejecutar el rol de "awx" se generará una contraseña segura, y se modificará automáticamente el
valor "secret_key=secureKey" del archivo "inventory" cambiado "secureKey" por la nueva contraseña
que se ha generado anteriormente. Cuando acabe la ejecución del rol, puedes dirigirte a la ruta
"/home/{{ user }}/awx-17.1.0/installer" y visualizar el archivo "inventory" para ver cuál es la
contraseña segura que se ha generado.

Para ver los dockers en ejecución, deberás dirigirte a la ruta "~/.awx/awxcompose" y ejecutar el
comando "docker-compose ps".
