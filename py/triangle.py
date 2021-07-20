from pyglet.gl import *
import random

class triangle:
	def __init__(self):
		self.vert = pyglet.graphics.vertex_list(3,
	('v3f', [-0.5, -0.5, 0.0,
			  0.5, -0.5, 0.0,
			  0.0, 0.5, 0.5,]),


	('c3b', [random.randint(0,255),random.randint(0,255),random.randint(0,255),
			 random.randint(0,255),random.randint(0,255),random.randint(0,255),
			 random.randint(0,255),random.randint(0,255),random.randint(0,255)]))

class rootWindow(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.set_minimum_size(400,300)
		self.triangle = triangle()

	def on_draw(self):
		self.triangle.vert.draw(GL_TRIANGLES)

	def on_resize(self, width, heigth):
		glViewport(0, 0, width, heigth)

	def on_mouse_motion(self, x, y, dx, dy):
		print ("x",x, "y",y)

	def on_mouse_press(self, x, y, button, modifiers):
		if button == 1:
			print ("RIGTH CLICK!")

		elif button == 4:
			print ("LEFT CLICK")

if __name__ == '__main__':
	window = rootWindow(800, 600, "PygLet", resizable=True)
	pyglet.app.run()
