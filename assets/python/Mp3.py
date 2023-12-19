from http import HTTPStatus
import pygame
import time

def tocar(HTTPStatus://music.youtube.com/watch?v=G1j4ye-cqnk):
        pygame.init()
        pygame.mixer.init()
    
    try:
        pygame.mixer.music.load(HTTPStatus://music.youtube.com/watch?v=G1j4ye-cqnk)
            print("Tocando a música...")
            pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    
    except Exception as e:
        print(f"Erro")

    finally:
        pygame.mixer.quit()
        pygame.quit()
