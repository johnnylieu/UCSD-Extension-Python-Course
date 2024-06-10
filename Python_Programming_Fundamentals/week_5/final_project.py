"""This final project is designed to incorporate all the tools learned throughout the course. 
You will need to create a class that handles image and audio processing methods. Follow the steps below to complete the project:

1. Name your class MMedia_Processing

2. You will be creating two methods. Name the first method ImgProc and the second AudProc

3. Method 1 will read the image file attached hereDownload here

4. Use the following libraries for your work

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

5. Use the mpimg imread method to read in the image file attached above

6. you can view the image by using 

plt.imshow(img) where img is the image read in

7. Color images are typically store as RGB files. So a color image is composed of three separate images concatenated; a Red component, and Green component and a Blue component. 
We will use the following to select the Red component - where 1 = R, 2 = G, 3 = B. So for img[:,  :, 1] this selects all the rows and all the columns of the first component.

lum_img = img[:, :, 1]

8. View the new image and add a title using the imshow method

9. Plot a second image [your can use plt.figure(1) for the first plot, plt.figure(2) for the second and so on] that will show the histogram of the new image. Use the information below

plt.hist(lum_img.ravel(), bins=256, range=(0.0, 255), fc='k', ec='k')

10. Add a grid, title, xlabel and ylabel to the plot.

11. Method 2 will read an audio file attached Alone-Sistar.wavDownload Alone-Sistar.wav

12. Use the following libraries

import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read, write

13 You will use the read method to read in the audio file as shown below where Fs stands for sampling rate and data is the data read in from the audio file.

Fs, data = read('Alone-Sistar.wav')

14. Plot the data and title it Waveform of Test Audio. Label the Xaxis Sample Index and the Yaxis Amplitude

15. flip the entire data set around so that the track plays backwards. Save and write to a file using the write function.

16. To test out your code use any media player that supports wave files

 

Submit your code, the plots, the image files and audio files for full credit. Have fun with this one."""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.io.wavfile import read, write
import sounddevice as sd # i had to pip install sounddevice


class MMedia_Processing:

    def ImgProc():
        image = "BigDataImage-1.jpg"
        read_image = mpimg.imread(image)
        lum_img = read_image[:, :, 1]
        plt.figure(1)
        plt.imshow(lum_img)
        plt.title("Red scale image")
        plt.show()

        plt.figure(2)
        plt.imshow(read_image)
        plt.title("Original image")
        plt.xlabel("X Label")
        plt.ylabel("Y Label")
        plt.grid()
        plt.show()

        plt.hist(lum_img.ravel(), bins=256, range=(0.0, 255), fc='k', ec='k')

    def AudProc():
        fs, data = read("Alone-Sistar.wav")
        time = np.arange(0, len(data)) / fs # creates an array of equally spaced values
        # print(time) # the above line works, we have an array to plot
        plt.plot(time, data) # time is x, data is y. data is amplitutde of sound
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.title("Waveform of Test Audio")
        plt.show()

        # reversing now
        reversed_data = data[::-1]
        # saving file
        write("Reversed-Alone-Sistar.wav", fs, reversed_data)
        # going to plot it too because I am curious how this will work
        fs, data = read("Reversed-Alone-Sistar.wav")
        time = np.arange(0, len(data)) / fs
        plt.plot(time, data)
        plt.xlabel("Reversed Sample Index")
        plt.ylabel("Reversed Amplitude")
        plt.title("Reversed Waveform of Test Audio")
        plt.show()


if __name__ == "__main__":
    obj1 = MMedia_Processing
    obj1.ImgProc()
    obj1.AudProc()