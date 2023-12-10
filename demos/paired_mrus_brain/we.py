import SimpleITK as sitk 
import matplotlib.pyplot as plt

mask_id = sitk.ReadImage("2b.mat_nib.nii", imageIO="NiftiImageIO")
masks = sitk.GetArrayFromImage(mask_id)
#print(masks[0][0])

import matplotlib.pyplot as plt
for slice in range(masks.shape[0]):
    plt.imshow(masks[slice])
    plt.show()
