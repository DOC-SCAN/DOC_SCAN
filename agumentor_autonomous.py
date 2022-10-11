from keras_preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import glob
datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
j = 0
for filename in glob.glob(r'C:\Users\Shifa\Desktop\DATASET\train\8\*.jpg'):
    j = j + 1
    img = load_img(filename)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)
    i = 0
    print("Augmenting " + filename)
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir='D:\\augdata', save_prefix='PPRO', save_format='PNG'):
        print("Gen: " + str(i))
        i += 1
        if i > 2:
            break



