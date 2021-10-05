import pygame
import random
import pyautogui
#---------------------------------

#---------Vars--------------------
swidth, sheight = 1000, 500
run = True
velocity = 5
x, y = 500, 475
radius = 5
color = (255, 0, 0)
#---------------------------------
print('''

Hi and welcome to PYAINT, a very low level
copy of Microsoft Paint.
You can create paintings and save them.
these are the commands:-
	r - red
	b - blue
	g - green
	w - white
	k - black
	y - yellow
	f - fill
	1 - increase brush size
	2 - decrease brush size
	s - saves a screen shot of the painting as the name given

''')
name = input("Enter the name of your painting: ")
name = name + '.png'

#---------Pygame init-------------
pygame.init()
window = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("PYAINT")
#---------------------------------

# main loop 
while run:
	pygame.time.delay(50)
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# movement commands
	if keys[pygame.K_RIGHT] and x < swidth - radius:
		x += velocity
	if keys[pygame.K_LEFT] and x >= velocity:
		x -= velocity
	if keys[pygame.K_DOWN] and y < sheight - radius:
		y += velocity
	if keys[pygame.K_UP] and y >= velocity:
		y -= velocity
	#-----------------------------------------------

	# painting and saving command/commands
	if keys[pygame.K_f]: # f - fill 
		window.fill(color)
	if keys[pygame.K_r]: # r - red
		color = (255,0,0)
	if keys[pygame.K_g]: # g - green
		color = (0,255,0)
	if keys[pygame.K_b]: # b - blue
		color = (0,0,255)
	if keys[pygame.K_y]: # y - yellow
		color = (255,255,0)
	if keys[pygame.K_w]: # w - white
		color = (255,255,255)
	if keys[pygame.K_k]: # k - black
		color = (0,0,0)
	if keys[pygame.K_1]: # 1 - increase brush size 
		radius += 2
	if keys[pygame.K_2]: # 2 - decrease brush size 
		radius -= 2
	if keys[pygame.K_s]: # s - saves a screen shot of the painting as the name given by the user
		myScreenshot = pyautogui.screenshot(name)
	#------------------------------------------------	

	pygame.draw.circle(window, color, (x, y), radius)
	pygame.display.update()
# ----------------------------------------------------------------------------	
myScreenshot = pyautogui.screenshot(name) # saves the final version as backup 
# if the user by mistake forgets to save the painting 
pygame.quit()
