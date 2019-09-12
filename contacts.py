# -*- coding: utf-8 -*-
import os
import csv

# Clases

class Contacto:

    def __init__(self, nombre, telefono, email):
        # variables inicializadas en publicas
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


class Agenda:

    def __init__(self):
        # Guarda una variable privada
        self._contactos = []

    # Metodo para Agregar
    def add(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        # append agrega datos al final de la lista
        self._contactos.append(contacto)
        self._save()

    # Metodo para actualizar
    def update(self, nombre):
        for idx, contacto in enumerate(self._contactos):
            if contacto.nombre.lower() == nombre.lower():
                command = str(raw_input('''
                --------------------------------
                *    ¿Qué Vamos a Actualizar?  *
                *                              *
                *    [an] = Nombre             *
                *    [at] = Telefono           *
                *    [ae] = E-mail             *
                *    [to] = Todo               *
                *    [xx] = Salir              *
                ---------------------------------
                '''))

                if command == 'an':
                    newName = str(raw_input('Ingresa el nuevo nombre: '))
                    newContact = Contacto(newName, contacto.telefono, contacto.email)
                    self._contactos[idx] = newContact
                    self._save()
                    print('*** NOMBRE ACTUALIZADO ***')
                    break

                elif command == 'at':
                    newPhone = str(raw_input('Ingresa el nuevo numero de telefono: '))
                    newContact = Contacto(contacto.nombre, newPhone, contacto.email)
                    self._contactos[idx] = newContact
                    self._save()
                    print('*** TELEFONO ACTUALIZADO ***')
                    break

                elif command == 'ae':
                    newEmail = str(raw_input('Ingresa el nuevo E-mail: '))
                    newContact = Contacto(contacto.nombre, contacto.telefono, newEmail)
                    self._contactos[idx] = newContact
                    self._save()
                    print('*** E-MAIL ACTUALIZADO ***')
                    break

                elif command == 'to':
                    newName = str(raw_input('Ingresa el nuevo nombre: '))
                    newPhone = str(raw_input('Ingresa el nuevo numero de telefono: '))
                    newEmail = str(raw_input('Ingresa el nuevo E-mail: '))
                    newContact = Contacto(newName, newPhone, newEmail)
                    self._contactos[idx] = newContact
                    self._save()
                    print('*** CONTACTO ACTUALIZADO ***')
                    break

                elif command == 'xx':
                    print('SALIENDO...')
                    break

                else:
                    print('Comando no encontrado')
                    break

        else:
            self._not_found()

    # Metodo para eliminar por nombre
    def delete(self, nombre):
        for idx, contacto in enumerate(self._contactos):
            # Comparamos nombre del contacto en minuscula y mayuscula
            if contacto.nombre.lower() == nombre.lower():
                del self._contactos[idx]
                self._save()
                break

    # Metodo para buscar
    def search(self, nombre):
        for contacto in self._contactos:
            # Comparamos nombre del contacto en minuscula y mayuscula
            if contacto.nombre.lower() == nombre.lower():
                self._print_contact(contacto)
                break
        # Este else pertenece al for
        else:
            self._not_found()

    # Metodo para mostrar
    def show_all(self):
        for contacto in self._contactos:
            self._print_contact(contacto)

    # Escribir a disco (exportar)
    def _save(self):
        with open('contactos.csv', 'w') as f:
            writer = csv.writer(f)
            # primera columna de valores
            writer.writerow( ('nombre', 'telefono', 'email'))

            for contacto in self._contactos:
                writer.writerow( (contacto.nombre, contacto.telefono, contacto.email))

    # Metodo para mostrar contactos creados
    def _print_contact(self, contacto):
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        print('Nombre: {}'.format(contacto.nombre))
        print('Telefono: {}'.format(contacto.telefono))
        print('Email: {}'.format(contacto.email))
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

    def _not_found(self):
        print('*********************')
        print('* ¡ No Encontrado ! *')
        print('*********************')

# Interfaz


def main():
    # Instancias
    agenda = Agenda()

    # importar CSV
    with open('contactos.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            agenda.add(row[0], row[1], row[2])

    while True:
        command = str(raw_input('''
        *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
        *    ¿Me diras que hacer?    *
        *                            *
        *    [a] Agregar Contacto    *
        *    [b] Modificar Contacto  *
        *    [c] Buscar un Contacto  *
        *    [d] Eliminar Contacto   *
        *    [e] Mostrar Contactos   *
        *    [x] Cerrar              *
        *                            *
        *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.

        '''))

        if command == 'a':
            nombre = str(raw_input('Digita el nombre: '))
            telefono = str(raw_input('Digita el Telefono: '))
            email = str(raw_input('Digita el Email: '))

            # Metodos
            agenda.add(nombre, telefono, email)

        elif command == 'b':
            nombre = str(raw_input('Digita el nombre: '))
            # Metodo
            agenda.update(nombre)

        elif command == 'c':
            nombre = str(raw_input('Digita el nombre: '))
            # Metodo
            agenda.search(nombre)

        elif command == 'd':
            nombre = str(raw_input('Digita el nombre: '))
            # Metodo
            agenda.delete(nombre)

        elif command == 'e':
            agenda.show_all()

        elif command == 'x':
            break

        else:
            print('Comando no encontrado')


if __name__ == '__main__':
    os.system('clear')
    print('B I E N V E N I D O  A  L A  A G E N D A  V 0.1')
    main()
