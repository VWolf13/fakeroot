import os
os.system('sleep 0.1')
print("\n\n<--------------------------------->")
os.system('sleep 0.1')
print("| Autor   : \/_\/\/olf            |")
os.system('sleep 0.1')
print("| Team    : https://vwolf.site    |")
os.system('sleep 0.1')
print("<--------------------------------->")
os.system('sleep 0.1')
print("\x1b[1;34m"+"\nElige la opción que desea ejecutar ^^")
os.system("sleep 0.5")
print("\x1b[1;31m"+"\n[1] Verificar Root")
print("\x1b[1;33m"+"[2] Instalar Fake Root Termux")
print("\x1b[1;32m"+"[3] Que es FakeRoot?")
print("\x1b[1;37m"+"[0] Salir")
os.system("sleep 0.5")
vw = input("\x1b[1;31m"+"\nInserte la opción que desea ejecutar: ")

for vwroot in vw:

        vwtool = vwroot.upper()

if (vwroot == "1"):
        os.system('whoami')
        print("\nSi apareció como: u0_a... ," + "No tienes privilegios root, si aparece como: root, tienes los privilegios fake root") 

if (vwroot == "2"):
        os.system('pkg install proot') | os.system('proot -0;clear')

elif (vwroot == "3"):
        print("\nFakeRoot es una herramienta que da privilegios root a scripts externos, aún así, los privilegios no los posees, se quita al reiniciar la terminal o cerrando la pestaña o con exit varias veces") 

elif (vwroot == "0"):
        os.system('exit')
