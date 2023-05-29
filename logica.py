import tkinter as tk
import tkinter.messagebox as messagebox
import numpy as np
import matplotlib.pyplot as plt
import math
import sqlite3

class Vector:
    id = 1

    def __init__(self):
        """
        Constructor de la clase Vector.
        Inicializa los atributos del vector.
        """
        self._nombre = ''
        self.id = Vector.id
        Vector.id += 1
        self._eje_x = ''
        self._eje_y = ''
        self._eje_z = ''
        self._dimensiones = 2
        self._angulo = 0

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def angulo(self):
        """
        Getter para el ángulo del vector.
        Devuelve el ángulo del vector.
        """
        return self._angulo

    @angulo.setter
    def angulo(self, nuevo_angulo):
        """
        Setter para el ángulo del vector.
        Establece el ángulo del vector con el valor proporcionado.
        """
        self._angulo = nuevo_angulo

    @property
    def eje_x(self):
        """
        Getter para la coordenada en el eje x del vector.
        Devuelve la coordenada en el eje x del vector.
        """
        return self._eje_x

    @eje_x.setter
    def eje_x(self, valor):
        """
        Setter para la coordenada en el eje x del vector.
        Establece la coordenada en el eje x del vector con el valor proporcionado.
        """
        self._eje_x = valor

    @property
    def eje_y(self):
        """
        Getter para la coordenada en el eje y del vector.
        Devuelve la coordenada en el eje y del vector.
        """
        return self._eje_y

    @eje_y.setter
    def eje_y(self, valor):
        """
        Setter para la coordenada en el eje y del vector.
        Establece la coordenada en el eje y del vector con el valor proporcionado.
        """
        self._eje_y = valor

    @property
    def eje_z(self):
        """
        Getter para la coordenada en el eje z del vector.
        Devuelve la coordenada en el eje z del vector.
        """
        return self._eje_z

    @eje_z.setter
    def eje_z(self, valor):
        """
        Setter para la coordenada en el eje z del vector.
        Establece la coordenada en el eje z del vector con el valor proporcionado.
        """
        self._eje_z = valor

    @property
    def dimension(self):
        """
        Getter para la dimensión del vector.
        Devuelve la dimensión del vector.
        """
        return self._dimensiones

    @dimension.setter
    def dimension(self, dimension):
        """
        Setter para la dimensión del vector.
        Establece la dimensión del vector con el valor proporcionado.
        """
        self._dimensiones = dimension

    @property
    def coordenadas(self):
        """
        Getter para las coordenadas del vector.
        Devuelve un arreglo numpy con las coordenadas del vector.
        """
        if self.eje_x == 0 and self.eje_y == 0 and self.eje_z == 0:
            return False

        if self.dimension == 2:
            coordenadas = np.array([self.eje_x, self.eje_y])
        else:
            coordenadas = np.array([self.eje_x, self.eje_y, self.eje_z])

        return coordenadas

    @property
    def coordenadas_rotadas(self):
        """
        Getter para las coordenadas del vector rotado.
        Devuelve un arreglo numpy con las coordenadas del vector rotado según el ángulo.
        """
        if self.angulo == 0:
            return 0

        radianes = math.radians(self.angulo)
        c = math.cos(radianes)
        s = math.sin(radianes)

        if self.dimension == 2:
            matriz_rotacion = np.array([[c, -s],
                                        [s, c]])
            vector_rotado = np.dot(matriz_rotacion, np.array([self.eje_x, self.eje_y]))
            return vector_rotado
        else:
            matriz_rotacion = np.array([[c, -s, 0],
                                        [s, c, 0],
                                        [0, 0, 1]])

            vector_rotado = np.dot(matriz_rotacion, np.array([self.eje_x, self.eje_y, self.eje_z]))
            return vector_rotado
class Menu:
    def __init__(self):
        """
        Clase que define el menú para gestionar vectores.
        """
        self.formato = ('Arial', 12)
        self.vectores = []

    def boton(self, ventana, boton_text, comando):
        """
        Crea un botón en la ventana con el texto y comando dados.

        Args:
            ventana: La ventana donde se creará el botón.
            boton_text: El texto que se mostrará en el botón.
            comando: El comando que se ejecutará cuando se presione el botón.
        """
        boton = tk.Button(ventana, text=boton_text, font=self.formato, command=comando)
        boton.pack(pady=10, side=tk.BOTTOM)

    def titulo(self, ventana, titulo):
        """
        Crea un título en la ventana con el texto dado.

        Args:
            ventana: La ventana donde se creará el título.
            titulo: El texto que se mostrará como título.
        """
        mostrar_titulo = tk.Label(ventana, text=titulo, font=self.formato, anchor='center')
        mostrar_titulo.pack(pady=5)
        
    def coordenadas(self, vector):
        """
            Muestra una ventana para ingresar las coordenadas y el ángulo de rotación de un vector.

            Args:
             vector: El vector al que se le van a ingresar las coordenadas.

        """
        ventana = tk.Toplevel()
        ventana.geometry('300x300')
        ventana.title('Coordenadas')
        
        self.titulo(ventana, 'Eje X')
        entrada_x = tk.Entry(ventana, width=30,textvariable=tk.StringVar(value=str(vector.eje_x)))
        entrada_x.pack(pady=5, padx=5)
  
        self.titulo(ventana, 'Eje y')
        entrada_y = tk.Entry(ventana, width=30, textvariable=tk.StringVar(value=str(vector.eje_y)))
        entrada_y.pack(pady=5, padx=5)

        if vector.dimension == 3:
            self.titulo(ventana, 'Eje z')
            entrada_z = tk.Entry(ventana, width=30, textvariable=tk.StringVar(value=str(vector.eje_z)))
            entrada_z.pack(pady=5, padx=5) 
        
        self.titulo(ventana, 'Angulo de rotacion')
        entrada_angulo = tk.Entry(ventana, width=30, textvariable=tk.StringVar(value=str(vector.angulo)))
        entrada_angulo.pack(pady=5, padx=5)
        
        def agregar():
            if not entrada_x.get() or not entrada_y.get:
                messagebox.showerror('Error', 'Favor digite las coornedanas del vector')
                ventana.destroy()
                return
            else:
                try:     
                    eje_y = int(entrada_y.get())
                    eje_x = int(entrada_x.get())
                    angulo = int(entrada_angulo.get())
                    if vector.dimension == 3:
                        eje_z = int(entrada_z.get())
                    vector.eje_x = eje_x
                    vector.eje_y = eje_y
                    vector.angulo = angulo
                    if vector.dimension == 3:
                        vector.eje_z = eje_z
                    
                except ValueError:
                    messagebox.showerror('Error', 'Favor digine coordenadas validas')
                    ventana.destroy()
                    return
                messagebox.showinfo('Perfecto', f'El vector de dimendion {vector.dimension} fue creatdo con exito')
                ventana.destroy()
        self.boton(ventana, 'Agregar', agregar)
         
    def dimensiones(self, vector):
        """
        Crea una ventana para seleccionar la dimensión de un vector.

        Args:
            vector: El vector al que se le seleccionará la dimensión.
        """        
        ventana = tk.Toplevel()
        ventana.geometry('300x100')
        ventana.title('Dimensiones')
        
        def dos_dimensiones():
            vector.dimension = 2
            ventana.destroy()
            self.coordenadas(vector)

        def tres_dimensiones():
            vector.dimension = 3
            ventana.destroy()
            self.coordenadas(vector)
        self.boton(ventana, '2D', dos_dimensiones)
        self.boton(ventana, '3D', tres_dimensiones)
    
    def mostrar(self, vector):
        """
        Muestra el vector en un gráfico.

        Args:
            vector: El vector que se mostrará en el gráfico.
        """
        vector_sin_rotar = vector.coordenadas
        vector_rotado = vector.coordenadas_rotadas if np.all(vector.coordenadas_rotadas != 0) else []
        if vector.dimension == 2:
            plt.quiver(0, 0, vector_sin_rotar[0], vector_sin_rotar[1], angles='xy', scale_units='xy', scale=1, color='black')
            if np.any(vector_rotado != vector_sin_rotar) and np.all(vector_rotado != []):
                plt.quiver(0, 0, vector_rotado[0], vector_rotado[1], angles='xy', scale_units='xy', scale=1, color='red')
                plt.text(0.37, 1.1, 'Vector sin rotado', color='black',ha='center', va='center', transform=plt.gca().transAxes)
                plt.text(0.6, 1.1, 'Vector rotado', color='red',ha='center', va='center', transform=plt.gca().transAxes)
            plt.xlim(-10, 10)
            plt.ylim(-10, 10)
            plt.grid()
            plt.title('Vector 2D')
            plt.show()
        else:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.quiver(0, 0, 0, vector_sin_rotar[0], vector_sin_rotar[1], vector_sin_rotar[2], color='black')
            if np.any(vector_rotado != vector_sin_rotar) and np.all(vector_rotado != []):
                ax.quiver(0, 0, 0, vector_rotado[0], vector_rotado[1], vector_rotado[2], color='red')
                ax.text2D(0.2, -0.1, 'Vector rotado', transform=ax.transAxes, color='red')
                
            ax.set_xlim([-10, 10])
            ax.set_ylim([-10, 10])
            ax.set_zlim([-10, 10])
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title('Vector 3D')
            ax.text2D(1, -0.1, 'Vector rotado', transform=ax.transAxes, color='black')


            # Mostrar el gráfico
            plt.show()
            
    def guardar(self, vector, ventana_principal):
        """
        Guarda el vector en una base de datos y muestra una ventana de confirmación.

        Args:
            vector: El vector que se guardará.
            ventana_principal: La ventana principal actual.
        """
        ventana_principal.destroy()
        ventana = tk.Tk()
        ventana.geometry('300x140')
        ventana.title('Guardar')
        
        self.titulo(ventana, 'Como desea guardar el archivo')
        entrada_nombre = tk.Entry(ventana, width=30)
        entrada_nombre.pack(pady=5, padx=5)
        
        def agregar(vector):
            if not entrada_nombre.get():
                messagebox.showerror('Error', 'Favor digite un nombre para guardar el vector')
                ventana.destroy()
                return
            else:
                nombre = entrada_nombre.get()
                vector.nombre = nombre
                conn = sqlite3.connect('data_base.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS Vectores (id INTEGER, nombre TEXT, x INTEGER, y INTEGER, z INTEGER, dimension INTEGER, angulo INTEGER)''')
                if vector.id > Vector.id:
                    self.vectores.append(vector)
                id = vector.id
                eje_x = vector.eje_x
                eje_y = vector.eje_y
                eje_z = vector.eje_z
                dimension = vector.dimension
                angulo = vector.angulo
                c.execute("SELECT id FROM Vectores WHERE id = ?", (id,))
                existe = c.fetchone()
                if existe is not None:
                    c.execute("UPDATE Vectores SET nombre=?, x=?, y=?, z=?, dimension=?, angulo=? WHERE id=?", 
                      (nombre, eje_x, eje_y, eje_z, dimension, angulo, id))
                else:
                    c.execute("INSERT INTO Vectores (id, nombre , x, y, z, dimension, angulo) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                            (id, nombre, eje_x, eje_y, eje_z, dimension, angulo))
                conn.commit()
                conn.close()
                messagebox.showinfo('Perfecto', 'Vector guardado con exito')
                ventana.destroy()
                vector = Vector()
                self.principal(vector)
            
        self.boton(ventana, 'Guardar', lambda:agregar(vector))
        

    def cargar(self):
        """
        Carga los vectores previamente creados 
        """
        try:
            conn= sqlite3.connect('data_base.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS Vectores (id INTEGER, nombre TEXT, x INTEGER, y INTEGER, z INTEGER, dimension INTEGER, angulo INTEGER)''')
            c.execute('SELECT nombre, x, y, z, dimension, angulo FROM Vectores')
            resultado = c.fetchall()
            
            for nombre, x, y, z, dimension, angulo in resultado:
                vector = Vector()
                vector.nombre = nombre
                vector.eje_x = x 
                vector.eje_y = y 
                vector.eje_z = z 
                vector.dimension = dimension
                vector.angulo = angulo
                self.vectores.append(vector)
            conn.close()
                
        except ValueError:
            pass
        nuevo_vector = Vector()
        self.principal(nuevo_vector)
    def cargar_vector(self, ventana_anterior):
        """
        Carga un vector previamente guardado y muestra la ventana principal con el vector seleccionado.

        Args:
            ventana_anterior: La ventana anterior actual.
        """
        if not self.vectores:
            messagebox.showerror('Error', 'No has creado ningun vector aun')
            return
        ventana_anterior.destroy()
        ventana = tk.Tk()
        ventana.geometry("320x300")
        
        ventana.title('Vectores creados')
        
        mostrar_titulo = tk.Label(ventana, text='Vectores', font=self.formato, anchor='center')
        mostrar_titulo.pack(pady=5)
        
        lista_frame = tk.Frame(ventana)
        lista_frame.pack(pady=5)
        lista = tk.Listbox(lista_frame, width=30, height=5, font=self.formato)
        lista.pack(expand=True, fill='both', padx=10, pady=10)
        id = 0
        for vector_seleccion in self.vectores:
            if vector_seleccion.id  != id:
                lista.insert(tk.END, f'{vector_seleccion.nombre}')
                id = vector_seleccion
        ancho_ventana = max(lista.winfo_reqwidth()+40, 320)
        ventana.geometry(f"{ancho_ventana}x300")
        
        def boton():
            seleccion = lista.curselection()
            if not seleccion:
                #Dado el caso de no haber eleccion mostrara una ventana emergente con un error 
                messagebox.showerror("Error", "Por favor seleccione una tarea.")
                return None
            else:
                vector = self.vectores[seleccion[0]]
                ventana.destroy()
                self.principal(vector)
            
        self.boton(ventana, 'Cargar', comando=lambda: boton())      
                        
        
    def principal(self, vector = Vector()):
        """
        Crea la ventana principal del programa.

        Args:
            vector: El vector actual.
        """
        print(vector.id)
        ventana = tk.Tk()
        ventana.title('Vectores')
        ventana.geometry('300x300')
        
        self.titulo(ventana, 'Estudiar es la clave del exito')
        self.boton(ventana, 'Cargar', lambda:self.cargar_vector(ventana))
        self.boton(ventana, 'Guardar', lambda:self.guardar(vector, ventana))
        self.boton(ventana, 'Graficar', lambda:self.mostrar(vector))
        self.boton(ventana, 'Dimension', lambda:self.dimensiones(vector))
        self.boton(ventana, 'Coordenadas', lambda:self.coordenadas(vector))
        
        ventana.mainloop()
    