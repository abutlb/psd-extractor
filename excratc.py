from psd_tools import PSDImage
import os

if not os.path.exists("out"):
    os.mkdir("out")

files = os.listdir("in\\")
i = 1

for file in files:
        psd = PSDImage.open(f'in\\{file}')
        print(f"working in file {i} of {len(files)}")
        ln = 1
        for layer in psd:
            if layer.is_group():
                print(f"working on layer {ln} of {len(psd)}")
                for l in layer:
                    layer_image = l.composite()
                    layer_image.save(f"out\\file{i}layer{ln}.png")
                    ln = ln + 1
            else:
                print(f"working on layer {ln} of {len(psd)}")
                layer_image = layer.composite()
                layer_image.save(f"out\\file{i}layer{ln}.png")
                ln = ln + 1
        i = i + 1
