#
#  LumberDoctor
# ========================================
# [] File Name : lumber_doc.py
#
# [] Creation Date : 4/8/2017
#
# [] Created By : Ali Gholami (aligholami7596@gmail.com)
# ========================================
#

import wx



# Take an screenshot of the current page
surface = pygame.display.set_mode((100, 100), 0, 32)
surface.fill((255, 255, 255))
pygame.draw.circle(surface, (0, 0, 0), (10, 10), 15, 0)
pygame.display.update()
pygame.image.save(surface,os.path.expanduser("pic1.png"))