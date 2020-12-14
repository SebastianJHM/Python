import PIL
import os

# ## Rotation of image
# im = PIL.Image.open("potro.jpg")
# new_im = im.rotate(90)
# new_im.save("potro_rotado.jpg")
# new_im.show()

# ## Resize image
# im = PIL.Image.open("potro.jpg")
# new_im = im.resize((640, 480))
# new_im.save("potro_redim.jpg")
# new_im.show()

# ## Resize and rotate image
# im = PIL.Image.open("potro.jpg")
# new_im = im.rotate(180).resize((640, 480))
# new_im.save("potro_rot_and_redim.jpg")
# new_im.show()

path = "tmp//mx"
try:
    os.makedirs(path)
except:
    pass

print(os.listdir("f"))
for im_name in os.listdir("f"):
    print(os.path.splitext(im_name)[0])
    im = PIL.Image.open("f//" + im_name)
    im.save("tmp//mx//" + im_name)