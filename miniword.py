import os
from PySide6.QtGui import QAction, QIcon, QKeySequence, QFont, QTextCursor, QTextDocument
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QDockWidget, QPushButton, QTextEdit, QWidget, QVBoxLayout, QFileDialog, QInputDialog, QMessageBox, QStatusBar, QLabel, QColorDialog, QFontDialog, QLineEdit
from PySide6.QtCore import Qt, QTimer

class VentanaMiniWord(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cuadrotextoprincipal = QTextEdit()
        self.setWindowTitle("Miniword")
        self.resize(1280, 1024)
        self.crear_acciones()
        self.crear_menus()
        self.herramientas()
        self.barra_estado = QStatusBar()
        self.setStatusBar(self.barra_estado)
        self.panelr()

        self.etiqueta_palabras = QLabel("Palabras: ")
        self.barra_estado.addPermanentWidget(self.etiqueta_palabras)
        self.cuadrotextoprincipal.textChanged.connect(self.contador)


         # Menu arriba
        contenedor = QWidget()
        layout = QVBoxLayout(contenedor)

        layout.addWidget(self.cuadrotextoprincipal)
        layout.setContentsMargins(200, 20, 200, 20)

        # ✨Autoguardado FUNCION EXTRA✨

        self.autoguardadotimer =  QTimer(self)
        self.autoguardadotimer.setInterval(50000)
        self.autoguardadotimer.timeout.connect(self.guardar_archivo)
        self.autoguardadotimer.start()
        self.setCentralWidget(contenedor)


    def crear_acciones(self):

        # Nuevo archivo
        self.acccion_nuevo = QAction("Nueva", self)
        self.acccion_nuevo.setShortcut(QKeySequence.New)
        self.acccion_nuevo.triggered.connect(self.nuevo_archivo)

        # Abrir

        self.accion_abrir = QAction("Abrir", self)
        self.accion_abrir.setShortcut(QKeySequence.Open)
        self.accion_abrir.triggered.connect(self.abrir_archivo)

        # Guardar

        self.accion_guardar = QAction("Guardar", self)
        self.accion_guardar.setShortcut(QKeySequence.Save)
        self.accion_guardar.triggered.connect(self.guardar_archivo)

        # Salir

        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut(QKeySequence.Quit)
        self.accion_salir.triggered.connect(self.close)

        # Deshacer

        self.accion_deshacer = QAction("Deshacer", self)
        self.accion_deshacer.setShortcut(QKeySequence.Undo)
        self.accion_deshacer.triggered.connect(self.cuadrotextoprincipal.undo)

        # Rehacer

        self.accion_rehacer = QAction("Rehacer", self)
        self.accion_rehacer.setShortcut(QKeySequence.Redo)
        self.accion_rehacer.triggered.connect(self.cuadrotextoprincipal.redo)

        # Cortar

        self.accion_cortar = QAction("Cortar", self)
        self.accion_cortar.setShortcut(QKeySequence.Cut)
        self.accion_cortar.triggered.connect(self.cuadrotextoprincipal.cut)
        
        # Copiar

        self.accion_copiar = QAction("Copiar", self)
        self.accion_copiar.setShortcut(QKeySequence.Copy)
        self.accion_copiar.triggered.connect(self.cuadrotextoprincipal.copy)

        # Pegar

        self.accion_pegar = QAction("Pegar", self)
        self.accion_pegar.setShortcut(QKeySequence.Paste)
        self.accion_pegar.triggered.connect(self.cuadrotextoprincipal.paste)

        # Buscar

        self.accion_buscar = QAction("Buscar", self)
        self.accion_buscar.setShortcut(QKeySequence.Find)
        # self.accion_buscar.triggered.connect(self.buscar_texto)
        self.accion_buscar.triggered.connect(lambda: self.panelri.show()) #Lambda es para abrir el panel


        # Reemplazar

        self.accion_reemplazar = QAction("Reemplazar", self)
        self.accion_reemplazar.setShortcut(QKeySequence.Replace)
        self.accion_reemplazar.triggered.connect(self.reemplazar_texto)

        self.accion_colorfondo = QAction("Color de fondo", self)
        self.accion_colorfondo.triggered.connect(self.color_fondo)

        self.accion_cambiarfuente = QAction("Cambiar fuente", self)
        self.accion_cambiarfuente.triggered.connect(self.cambiar_fuente)

    def nuevo_archivo(self):
        self.cuadrotextoprincipal.clear()
        self.barra_estado.showMessage("Nuevo documento creado", 3000)

    def abrir_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")

        if ruta:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                self.cuadrotextoprincipal.setText(contenido)
        
        self.ruta_actual = ruta  # Guarda la ruta
        self.barra_estado.showMessage("Archivo abierto correctamente", 3000)

    
    def guardar_archivo(self):
        ruta = getattr(self, "ruta_actual", None)  #  Obtiene la ruta actual si existe

        if ruta is None:
            ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
            if not ruta:
                return 

            self.ruta_actual = ruta

        with open(self.ruta_actual, "w", encoding="utf-8") as archivo:
            archivo.write(self.cuadrotextoprincipal.toPlainText())

        self.barra_estado.showMessage("Archivo guardado", 3000)

    # Guarda en la ruta actual YA selecionada
        with open(self.ruta_actual, "w", encoding="utf-8") as archivo:
            archivo.write(self.cuadrotextoprincipal.toPlainText())
        self.barra_estado.showMessage("Archivo guardado", 3000)
        
    def crear_menus(self):
        
        menu_archivos = self.menuBar().addMenu("&Archivo")

        menu_archivos.addAction(self.acccion_nuevo)
        menu_archivos.addAction(self.accion_abrir)
        menu_archivos.addAction(self.accion_guardar)

        menu_archivos.addSeparator() # Añade "---"

        menu_archivos.addAction(self.accion_salir)

        # Menu editar

        menu_editar = self.menuBar().addMenu("&Editar")
        menu_editar.addAction(self.accion_deshacer)
        menu_editar.addAction(self.accion_rehacer)
        menu_editar.addAction(self.accion_cortar)
        menu_editar.addAction(self.accion_copiar)
        menu_editar.addAction(self.accion_pegar)

        menu_editar.addAction(self.accion_buscar)
        menu_editar.addAction(self.accion_reemplazar)

        # PERSONALIZACION

        menu_custom = self.menuBar().addMenu("&Personalización")
        menu_custom.addAction(self.accion_colorfondo)
        menu_custom.addAction(self.accion_cambiarfuente)


    
    def herramientas(self):
        barraherramientas = QToolBar("Barra de herramientas")
        self.addToolBar(barraherramientas)
        
        barraherramientas.addAction(self.acccion_nuevo)
        barraherramientas.addAction(self.accion_abrir)
        barraherramientas.addAction(self.accion_guardar)
        barraherramientas.addAction(self.accion_salir)
        barraherramientas.addAction(self.accion_deshacer)
        barraherramientas.addAction(self.accion_rehacer)
        barraherramientas.addAction(self.accion_cortar)
        barraherramientas.addAction(self.accion_copiar)
        barraherramientas.addAction(self.accion_pegar)
        barraherramientas.addAction(self.accion_buscar)
        barraherramientas.addAction(self.accion_reemplazar)

    def buscar_texto(self):
        texto, okbuscar = QInputDialog.getText(self, "Buscar", "Texto a buscar:")

        if not okbuscar or texto.strip() == "":
            return  # Usuario cancelo o campo vacío

        encontrado = self.cuadrotextoprincipal.find(texto)

        if not encontrado:
            QMessageBox.information(self, "Buscar", "No se encontró el texto.")




    def reemplazar_texto(self):
        buscar, okreemplazar = QInputDialog.getText(self, "Reemplazar", "Texto a buscar:")

        if not okreemplazar or not buscar:
            return
        
        reemplazar, okreemplazar1 = QInputDialog.getText(self, "Reemplazar", "Texto de reemplazo:")
        if not okreemplazar1:
            return
        
        contenido = self.cuadrotextoprincipal.toPlainText()
        nvcontenido = contenido.replace(buscar, reemplazar)
        self.cuadrotextoprincipal.setText(nvcontenido)
    def contador(self):
        texto = self.cuadrotextoprincipal.toPlainText().strip()

        if texto == "":
            nmpalabras = 0
        else:
            nmpalabras = len(texto.split())

        self.etiqueta_palabras.setText(f"Palabras: {nmpalabras}")

    def color_fondo(self):

        color = QColorDialog.getColor()
        if color.isValid():
            # self.cuadrotextoprincipal.setStyleSheet(f"background-color: {color.name()}; color: black;") # Color BLACK para probar que no se bugee
            # self.cuadrotextoprincipal.setFont(self.cuadrotextoprincipal.font())  #  actualiza para arreglar bug
            pcolor = self.cuadrotextoprincipal.palette()
            pcolor.setColor(self.cuadrotextoprincipal.viewport().backgroundRole(), color)
            self.cuadrotextoprincipal.setPalette(pcolor)

            self.barra_estado.showMessage(f"Color de fondo cambiado a: {color.name()}", 3000)

    def cambiar_fuente(self):
        # fuente, validarfuente = QFontDialog.getFont()
        # if validarfuente:
        #    self.cuadrotextoprincipal.setFont(fuente)
        fuente, valido = QFontDialog.getFont()
        if valido and isinstance(fuente, QFont):
            self.cuadrotextoprincipal.setFont(fuente)
            self.barra_estado.showMessage("Fuente cambiada", 3000)
        else:
            self.barra_estado.showMessage("No se por que no funciona ya me aburri", 3000)

    def panelr(self):
        self.panelri = QDockWidget("Buscar y/o Reemplazar", self)
        self.panelri.setAllowedAreas(Qt.RightDockWidgetArea)

        contenedor = QWidget()
        layout = QVBoxLayout(contenedor)

        # Campo de texto para buscar
        #self.campoabuscar = QTextEdit()
        self.campoabuscar = QLineEdit()
        self.campoabuscar.setFixedHeight(30)
        self.campoabuscar.setPlaceholderText("¿Que buscas?")
        layout.addWidget(self.campoabuscar)

        # Boton buscar siguiente
        btnsiguiente = QPushButton("Siguiente")
        btnsiguiente.clicked.connect(self.buscarsiguiente)
        layout.addWidget(btnsiguiente)

        # Boton buscar anterior
        btnatras = QPushButton("Anterior")
        btnatras.clicked.connect(self.buscaranterior)
        layout.addWidget(btnatras)

        # Boton buscar todo
        btnall = QPushButton("Buscar todo")
        btnall.clicked.connect(self.buscarTodo)
        layout.addWidget(btnall)

        layout.addStretch()


        self.panelri.setWidget(contenedor)
        self.addDockWidget(Qt.RightDockWidgetArea, self.panelri)

        self.panelri.hide()


    def buscarsiguiente(self):
        texto = self.campoabuscar.text().strip()
        if texto:
            self.cuadrotextoprincipal.setFocus()
            self.cuadrotextoprincipal.find(texto)

    def buscaranterior(self):
        texto = self.campoabuscar.text().strip()
        if texto:
            self.cuadrotextoprincipal.setFocus()
            self.cuadrotextoprincipal.find(texto, QTextDocument.FindBackward)

    def buscarTodo(self):
        texto = self.campoabuscar.text().strip()
        # # mouse = self.cuadrotextoprincipal.textCursor()
        if not texto:
            return

        self.cuadrotextoprincipal.setFocus()
        self.cuadrotextoprincipal.moveCursor(QTextCursor.Start)

        contador = 0
        while self.cuadrotextoprincipal.find(texto):
            contador += 1

        QMessageBox.information(self, "Buscar todos", f"Se encontraron {contador} coincidencias.")




if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaMiniWord()
    ventana.show()
    app.exec()