from OpenGL.GL import *
from glew_wish import *
import glfw


def main():
    if not glfw.init():
        return
    window = glfw.create_window( 800, 600, "Mi ventana", None, None)


    #Configuracion OpenGL
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
        glViewport(0,0,800,600) #window size
        glClearColor(1,0.8,0,1) #colores rgb
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        #Dibujo
        glfw.poll_events()
        glfw.swap_buffers(window)


    glfw.destroy_window(window)
    glfw.terminate()


if __name__ == "__main__":
    main()


