class MiniCompiler:
    def __init__(self):
        self.value = 0

    def interpretar(self, programa):
        resultado = ""
        for simbolo in programa:
            if simbolo == "#":
                self.value += 1
            elif simbolo == "@":
                self.value -= 1
            elif simbolo == "*":
                self.value *= self.value
            elif simbolo == "&":
                resultado += str(self.value)
            else:
                print("Error: Caracteres no reconocidos")
                return None
        return resultado

def leer_programa_desde_archivo(archivo):
    try:
        with open(archivo, 'r') as file:
            programa = file.read().strip()
        return programa
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no existe.")
        return None

# Ejemplo de uso con archivo de entrada
compiler = MiniCompiler()

archivo_entrada = "entrada.txt"
programa_desde_archivo = leer_programa_desde_archivo(archivo_entrada)

if programa_desde_archivo is not None:
    salida = compiler.interpretar(programa_desde_archivo)
    if salida is not None:
        print(salida)