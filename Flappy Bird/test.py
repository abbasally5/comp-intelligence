import sys, pygame, math, random
from pygame.locals import *

pygame.init()

# Initialize global variables
FPS = 30
FPSCLOCK = pygame.time.Clock()

screen_Width = 360
screen_Height = 240

player_Width = 20
player_Height = 15

player_up = -10
player_down = 3

randRange = 80
gap = 80
baseHeight = (screen_Height - gap - randRange) / 2
pillarDiff = 120 + 25

black = 0,0,0
white = 255,255,255
red = 255,0,0


display = pygame.display.set_mode((screen_Width, screen_Height))

class Pillar(object):

	color = red
	width = 25
	pillarDiff = 120 + width
	
	def __init__(self, x1, y1, h1, y2):
		self.x1 = x1
		self.y1 = y1
		self.h1 = h1
		self.x2 = x1
		self.y2 = y2
		self.h2 = y2

def getRand():
	return random.randint(0, randRange)

def game(ann = None, screenOn = False):

	random.seed(0)
	playing = True
	score = 0

	x = screen_Width/2
	y = 0

	player_x = 50
	player_y = 0
	direction = 5

	queue = []

	#set up initial pillars
	rand = getRand()
	pillar1 = Pillar(x, 0, baseHeight + rand,
					screen_Height - baseHeight - (randRange - rand))

	rand = getRand()
	pillar2 = Pillar(x + pillarDiff, 0, baseHeight + rand, 
					screen_Height - baseHeight- (randRange - rand))

	rand = random.randint(0, 80);
	pillar3 = Pillar(x + 2 * pillarDiff, 0, baseHeight + rand, 
					screen_Height - baseHeight - (randRange - rand))

	queue.append(pillar1)
	queue.append(pillar2)
	queue.append(pillar3)

	# time in which commands cannot be given
	wait = 0

	while score < 50 and playing == True:		

		# if loop because we still want the pillars to be moving
		if (wait > 0):
		    wait -= 1

		pillarNum = 0;
		if (queue[0].x1 + queue[0].width < player_x):
			pillarNum = 1;

		distanceTop = math.sqrt((queue[pillarNum].x1 - player_x)**2 + \
			(queue[pillarNum].h1 - player_y)**2) / 400.0
		distanceBottom = math.sqrt((queue[pillarNum].x2 - player_x)**2 + \
			(queue[pillarNum].y2 - player_y)**2) / 400.0
		x1Dist = abs(queue[pillarNum].x1 - player_x)
		x2Dist = abs(queue[pillarNum].x2 - player_x)
		y1Dist = abs(queue[pillarNum].y1 - player_y)
		y2Dist = abs(queue[pillarNum].y2 - player_y)
		
		# send the distance to the neural network
		sensors = [distanceTop, distanceBottom, wait, 1.0]
		#print "x1Dist: {0}\tx2Dist: {1}\ty1Dist: {2}\ty2Dist: {3}\n".format(x1Dist, x2Dist, y1Dist, y2Dist) 
		#sensors = [x1Dist/200.0, x2Dist/200.0, y1Dist/25.0, y2Dist/25.0]

		# get the output from the ann
		if (ann is not None):
			output = ann.run(sensors);

			# move the flappy bird		
			if (output < 0 and wait == 0):
				direction = player_up
				#TODO: find out why having greater thatn 4 wait time ruins results
				wait = 4 
			else:
				direction = player_down 

		# move the pillars
		for i in range(0, len(queue)):
			queue[i].x1 -= 2;
			queue[i].x2 -= 2;

		# checks if pillars have left the screen
		# if so remove pillars and increment score 
		if (queue[0].x1 < -5 - queue[0].width):			
			rand = random.randint(0, 80);
			pillarN = Pillar(queue[2].x1 + pillarDiff, 0, baseHeight + rand, 
					screen_Height - baseHeight - (randRange - rand))
			queue.append(pillarN)
			queue.pop(0);			
			score += 1;
			#print output

		player_y = player_y + 1 * direction

		#check collisions
		if (player_y > screen_Height - player_Height or 
			player_y + player_Height < 0 or
		   ((player_x + player_Width > queue[0].x1 and 
		   	player_x < queue[0].x1+queue[0].width) and 
		   (player_y < queue[0].h1 or 
		   	player_y + player_Height > queue[0].y2))):
				playing = False

		# do i show graphics
		if (screenOn):

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP and wait == 0:
						direction = player_up
						wait = 4;

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_UP:
						direction = player_down

			#draw surface / draw screen
			display.fill(black)

			#draw pillars
			for p in queue:
				pygame.draw.rect(display, p.color, (p.x1, p.y1, p.width, p.h1));
				pygame.draw.rect(display, p.color, (p.x2, p.y2, p.width, p.h2));			
				

			#draw player
			pygame.draw.rect(display, white, (player_x, player_y, player_Width, player_Height));

			#draw text
			string = "score: " + str(score)
			text = pygame.font.SysFont('monospace', 16)
			TextSurf = text.render(string, True, white)
			TextRect = TextSurf.get_rect()
			TextRect.center = ((screen_Width - 50), 20)
			pygame.draw.rect(display, black, (screen_Width - 60, 10, 50, 25))
			display.blit(TextSurf, TextRect)

			pygame.display.update()
		   	FPSCLOCK.tick(FPS)

	return score;


if (__name__=='__main__'):
	from braindna import neuron
	ann = neuron()
	print game(ann, True)
	pygame.quit()
	quit()



