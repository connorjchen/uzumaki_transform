from engine import Engine
from pencilSketch import PencilSketch
import swirl

if __name__ == '__main__':
    image_path = "data/connorScared.jpg"
    swirl_image_path = "data/connorScared_out.jpg"

    pencil_sketch = PencilSketch(blur_simga=5, sharpen_value=20)
    engine = Engine(image_path=image_path, show=False, custom_objects=[pencil_sketch])
    engine.run()
    swirl.swirl_image(swirl_image_path)


