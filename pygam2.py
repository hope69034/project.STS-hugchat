## 파일이름을 pygame.py으로 하면 안된다

import pygame

file_path = "./sound/sample.mp3"
# Wait until playback finishes

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(file_path)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

# Close the audio file
#pygame.mixer.music.stop()
#pygame.mixer.quit()
#pygame.quit()
