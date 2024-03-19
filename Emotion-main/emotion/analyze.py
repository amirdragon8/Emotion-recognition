import menpo.io as mio
from pathlib import Path
from menpowidgets import visualize_images
from matplotlib import pyplot as plt

plt.ion()

#This has to be called with the path to the LFPW dataset
def load_database(path_to_images, crop_percentage, max_images=None):
    images = []

    for i in mio.import_images(path_to_images, max_images=max_images, verbose=True):
        #crop the image
        i = i.crop_to_landmarks_proportion(crop_percentage)

        #convert to greyscale
        if i.n_channels == 3:
            i = i.as_greyscale(mode='luminosity')

        #append to the list 
        images.append(i)
    
    return images

def warp_image(image):

    return image

def landmarked_image(image):
    retVal = image.as_masked().constrain_mask_to_landmarks().view_landmarks()
    return retVal

path_to_lfpw = Path('../lfpw_dataset/lfpw')
training_images = load_database(path_to_lfpw / 'testset', 0.5, max_images=5)

#plt save the training images
image = landmarked_image(training_images[3])
plt.savefig('image1.png')