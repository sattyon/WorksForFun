import random
def syori(SSS):
     inputText = SSS

     ROT = [
          "5",
          "4",
          "6",
          "2",
          "2",
          "3",
     ]

     WID = [
          "1050",
          "950",
          "200",
          "40",
     ]

     import imageFuncMojiire as IMGf
     from PIL import Image
     bg_path = "img/background.png"
     tomei_path = "img/tomei.png"
     bgf = "img/saisyuu.png"
     BGf = Image.open(bgf).copy()
     BG1 = Image.open(bg_path).copy()
     BG2 = Image.open(bg_path).copy()
     TOMEI1 = Image.open(tomei_path).copy()
     TOMEI2 = Image.open(tomei_path).copy()

     numba2 = 0
     StoreText = inputText.rsplit("/")
     while numba2 < len(StoreText):
          theText = StoreText[numba2]
          font_path = "C:\Windows\Fonts\YUMINDB.TTF"
          font_size = int(700 / len(theText)) + (random.randint(1,10) )
          font_color = (255, 255, 255)
          i = 0
          while(i < int(len(theText))):
               print (theText)
               font_size = int((int(700 / len(theText)) + random.randint(1,2)))
               height = 600 / int(len(theText)) * i
               if (numba2 == 0 and i == 0):
                    height = -30
                    font_size = int((int(400 / len(theText)) * 1.2))
               #2kaime dattara
               if (numba2 != 0):
                    font_size = int((int(510 / len(theText)) * (random.randint(10,18)))/10)
                    height = 540 / int(len(theText)) * i 
               #3kaime no saisyo dattara
               if (numba2 == 2 and i == 0):
                    font_size = 340
                    height = -50
               if (numba2 == 2 and i != 0):
                    height = 450 / int(len(theText)) * i
               if (numba2 == 3):
                    font_size = int(600 / len(theText)) + (random.randint(1,7) )
                    height = 500 / int(len(theText)) * i + 140             
               width = int(WID[numba2])
               Mozi = IMGf.add_text_to_image(TOMEI1, theText[i], font_path, font_size, font_color, height, width)
               textImg = Mozi.rotate(int(random.randint(-1,1) * 2))
               if (numba2 == 1):
                    textImg = Mozi.rotate(int(random.randint(-3,2) * 1.3))
               if (numba2 == 3):
                    textImg = Mozi.rotate(int(random.randint(-5,7) * 1.2))
               i += 1
               TOMEI2.paste(textImg, (0,0), textImg)
               TOMEI1 = Image.open(tomei_path).copy()
               BG1.paste(TOMEI2, (0,0), TOMEI2)
          numba2 += 1
          print("Tried to " + str(numba2) + "--")
     BGf.paste(BG1, (0,0), BG1)
     BGf.save("saved/savedImage.png")