import cv2
import albumentations as A

def get_train_transform(tamano):
	return A.Compose([
		A.LongestMaxSize(
			max_size=tamano,
			interpolation=cv2.INTER_LINEAR,
			mask_interpolation=cv2.INTER_NEAREST
		),
		A.PadIfNeeded(
			min_height=tamano,
			min_width=tamano,
			border_mode=cv2.BORDER_CONSTANT,
			fill=0,        # Negro en la imagen RGB
			fill_mask=0,   # Fondo cero para mascara binaria
			position="center"
		),
		A.Rotate(
			limit=20,
			interpolation=cv2.INTER_LINEAR,
			mask_interpolation=cv2.INTER_NEAREST,
			border_mode=cv2.BORDER_CONSTANT,
			fill=0,
			fill_mask=0,
			p=0.5
		),
		A.HorizontalFlip(p=0.5),
		A.RandomBrightnessContrast(
			brightness_limit=0.20,
			contrast_limit=0,
			p=0.5
		),
		A.RandomBrightnessContrast(
			brightness_limit=0,
			contrast_limit=0.20,
			p=0.5
		)
	])

def get_val_transform(tamano):
	return A.Compose([
		A.LongestMaxSize(
			max_size=tamano,
			interpolation=cv2.INTER_LINEAR,
			mask_interpolation=cv2.INTER_NEAREST
		),
		A.PadIfNeeded(
			min_height=tamano,
			min_width=tamano,
			border_mode=cv2.BORDER_CONSTANT,
			fill=0,        # Negro en la imagen RGB
			fill_mask=0,   # Fondo cero para mascara binaria
			position="center"
		)
	])
