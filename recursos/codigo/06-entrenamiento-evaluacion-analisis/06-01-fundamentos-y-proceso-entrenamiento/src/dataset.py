from pathlib import Path
import numpy as np
import cv2
import torch
from torch.utils.data import Dataset

class PetSegmentationDataset(Dataset):

    def __init__(self, dataframe, directorio_imagenes, transform):
        self.dataframe = dataframe.reset_index(drop=True)
        self.directorio_imagenes = Path(directorio_imagenes)
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        # Seleccionar una fila del CSV
        fila = self.dataframe.iloc[idx]

        # Construir rutas (el CSV contiene rutas relativas a images/)
        ruta_imagen = self.directorio_imagenes / fila["image_path"]
        ruta_mascara = self.directorio_imagenes / fila["mask_path"]

        # Leer imagen BGR y máscara de etiquetas
        imagen = cv2.imread(str(ruta_imagen), cv2.IMREAD_COLOR)
        mascara = cv2.imread(str(ruta_mascara), cv2.IMREAD_GRAYSCALE)

        if imagen is None:
            raise FileNotFoundError(f"No se pudo leer la imagen: {ruta_imagen}")
        if mascara is None:
            raise FileNotFoundError(f"No se pudo leer la máscara: {ruta_mascara}")

        # Convertir BGR a RGB
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

		# Convertir la máscara a binaria (1=animal, 2=fondo, 3=contorno)
        mascara_binaria = (mascara == 1).astype(np.uint8)  # 1=animal, 2=fondo, 3=contorno

        # Aplicar transformaciones sincronizadas
        resultado = self.transform(image=imagen, mask=mascara_binaria)
        imagen = resultado["image"]
        mascara_binaria = resultado["mask"]

        # Convertir tipos y normalizar imagen
        imagen = imagen.astype(np.float32) / 255.0
        mascara_binaria = mascara_binaria.astype(np.float32)

        # Convertir HWC -> CHW y construir tensores
        imagen = torch.from_numpy(imagen.transpose(2, 0, 1).copy())
        mascara = torch.from_numpy(mascara_binaria.copy())
        mascara = mascara.unsqueeze(0)  # Añadir dimensión de canal para la máscara

        return imagen, mascara