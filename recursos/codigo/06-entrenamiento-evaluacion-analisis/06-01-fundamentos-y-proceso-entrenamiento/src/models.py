import torch
import torch.nn as nn

class DoubleConv(nn.Module):
	def __init__(self, in_channels, out_channels):
		super(DoubleConv, self).__init__()

		self.bloque = nn.Sequential(
			nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
			nn.ReLU(inplace=True),
			nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
			nn.ReLU(inplace=True)
		)

	def forward(self, x):
		return self.bloque(x)

class MiniUNet(nn.Module):
	def __init__(self, in_channels=3, num_classes=1):
		super().__init__()

		# Encoder
		self.enc1 = DoubleConv(in_channels, 16)
		self.enc2 = DoubleConv(16, 32)

		# Pooling layer
		self.pool = nn.MaxPool2d(2)

		# Bottleneck
		self.bottleneck = DoubleConv(32, 64)

		# Decoder
		self.up2 = nn.ConvTranspose2d(64, 32, 2, stride=2)
		self.dec2 = DoubleConv(64, 32)

		self.up1 = nn.ConvTranspose2d(32, 16, 2, stride=2)
		self.dec1 = DoubleConv(32, 16)

		# Capa de salida
		self.final = nn.Conv2d(16, num_classes, 1)

	def forward(self, x):
		# Encoder: guardar características para skip connections
		e1 = self.enc1(x)
		e2 = self.enc2(self.pool(e1))
		# Bottleneck
		b = self.bottleneck(self.pool(e2))
		# Decoder: upsampling + concatenación
		d2 = self.up2(b)
		d2 = torch.cat((e2, d2), dim=1)
		d2 = self.dec2(d2)
		d1 = self.up1(d2)
		d1 = torch.cat((e1, d1), dim=1)
		d1 = self.dec1(d1)

		return self.final(d1)
