from reproductor import Reproductor
import pytest


@pytest.mark.parametrize("valor, expectativa", [("Stan", True), ("Gualicho", False), ("Painkiller", True), ("Bellaria", False), ("Iron Man",  True)])
def test_reprducir_cancion(valor, expectativa):
    lista = ["Enter Sandman", "Linkin Park", "Paranoid", "Stan",
             "Master of Puppets", "Painkiller", "Iron Man", "South of Heaven"]
    obj = Reproductor(lista)
    obj.set_encedido(True)
    assert obj.reproducir_cancion(valor) == expectativa


@pytest.mark.parametrize("valor, expectativa", [(1, True), (2, True), (3, True), (4, True), (5,  True), (6,  False), (7,  False), (8,  False)])
def test_siguiente_cancion(valor, expectativa):
    lista = ["Enter Sandman", "Park", "Paranoid", "Eminem",
             "Master of Puppets", "Painkiller", "Iron Man", "South of Heaven"]  # 7
    obj = Reproductor(lista)
    obj.set_encedido(True)
    obj.reproducir_cancion("Paranoid")
    assert obj.siguiente_cancion(valor) == expectativa


@pytest.mark.parametrize("valor, expectativa", [("Manijas", True), ("Lotus", True), ("Totos", True), ("Cools", True)])
def test_agregar_cancion_ok(valor, expectativa):
    lista = ["Enter Sandman", "Park", "Paranoid", "Stan",
             "Master of Puppets", "Painkiller", "Iron Man", "South of Heaven"]  # 7
    obj = Reproductor(lista)
    obj.set_encedido(True)

    assert obj.agregar_cancion(valor) == expectativa


@pytest.mark.parametrize("valor", [("Park"), ("Paranoid"), ("Stan"), ("Painkiller")])
def test_agregar_cancion_error(valor):
    lista = ["Enter Sandman", "Park", "Paranoid", "Stan",
             "Master of Puppets", "Painkiller", "Iron Man", "South of Heaven"]  # 7
    obj = Reproductor(lista)
    obj.set_encedido(True)
    with pytest.raises(ValueError, match="La cancion ya esta en lista"):
        obj.agregar_cancion(valor)
