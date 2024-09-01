"""
Registro de Tareas. Crea una clase Tarea que almacene información sobre
tareas pendientes. Implementa los métodos __str__ y __len__ para mostrar
detalles de la tarea y contar cuántas tareas hay en la lista.
"""


class Tarea:
    def __init__(self, tareas):
        self.__tareas = tareas

    def __len__(self):
        return len(self.__tareas)

    def __str__(self):
        return f"{self.__tareas}"


tareas = {"Leer un libro": "completo", "plantar un arbol": "En proceso",
          "Barrer la terraza": "No completado"}
lunes = Tarea(tareas)

print("Hay", len(lunes), "tareas en la lista.")
print(lunes)
