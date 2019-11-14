import tensorflow as tf
import scipy.misc
import model
import cv2
from subprocess import call
import math

sess = tf.InteractiveSession()
saver = tf.train.Saver()
saver.restore(sess, "save/model.ckpt")

img = cv2.imread('steering_wheel_image.png',0)
rows,cols = img.shape

smoothed_angle = 0


#read data.txt
xs = []
ys = []


########################################################
import os
l = []
for path, subdirs, files in os.walk('./FRAMES/'):
    for filename in files:
        
        l.append(filename)
        #f = os.path.join(path, filename)
########################################################

num_images = len(l)
#print(l)
#print(len(l))
i = math.ceil(num_images*0.5)
print("Starting frameofvideo:" +str(i))

while(cv2.waitKey(10) != ord('q')) and i<num_images:
    if i%2==0:
        print("./FRAMES/" +'frame'+str(i)+'.jpg')

        
        full_image = scipy.misc.imread("./FRAMES/" +'frame'+str(i)+'.jpg', mode="RGB")
        image = scipy.misc.imresize(full_image[-150:], [66, 200]) / 255.0
        degrees = model.y.eval(feed_dict={model.x: [image], model.keep_prob: 1.0})[0][0] * 180.0 / scipy.pi


        #call("clear")
        print("Predicted Steering angle: " + str(degrees))
    #    print("Steering angle: " + str(degrees) + " (pred)\t" + "actual cannot be calculated" + " (actual)")
        cv2.imshow("frame", cv2.cvtColor(full_image, cv2.COLOR_RGB2BGR))
        #make smooth angle transitions by turning the steering wheel based on the difference of the current angle
        #and the predicted angle

        
        smoothed_angle += 0.2 * pow(abs((degrees - smoothed_angle)), 2.0 / 3.0) * (degrees - smoothed_angle) / abs(degrees - smoothed_angle)

        M = cv2.getRotationMatrix2D((cols/2,rows/2),-smoothed_angle,1)
        dst = cv2.warpAffine(img,M,(cols,rows))

        cv2.imshow("steering wheel", dst)

    i += 1

cv2.destroyAllWindows()

