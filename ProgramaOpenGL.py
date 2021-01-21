from OpenGL.GL import *
from glew_wish import *
import glfw
import random


def main():

    #inicia glfw 
    if not glfw.init():
        return

    #crea ventana independientemente del SO que usemos
    window = glfw.create_window( 800, 600, "Mi ventana", None, None)


    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)


    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    
   #Establecemos el contexto, creamos la ventana pero aun no se muestra
    glfw.make_context_current(window)


    #Activamos la vadilacion de funciones modernas de OpenGL
    glewExperimental = True 


    #Inicializar Glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return


    #Versiones de OpenGL y shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        
        c1= random.random()
        c2= random.random()
        c3= random.random()

        glViewport(0,0,800,600) 
        glClearColor(c1, c2, c3,1 )


        #borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #Dibujo

        #preguntar si hubo entradas de perifericos (teclado, mouse, gamepad, etc)
        glfw.poll_events()
        #intercambia los buffers
        glfw.swap_buffers(window)

    #se destruye la ventana para liberar memoria
    glfw.destroy_window(window)

    #termina los procesos que inicio glfw.init
    glfw.terminate()


if __name__ == "__main__":
    main()


