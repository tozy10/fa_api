# api/detect.py
import torch

_MODEL = None
_MODEL_PATH = "best.pt"   # path to your weights

def _get_model():
    global _MODEL
    if _MODEL is None:
        # trust_repo=True avoids interactive prompt; setInsecure if needed for HTTPS
        _MODEL = torch.hub.load("ultralytics/yolov5", "custom", path=_MODEL_PATH, trust_repo=True)
    return _MODEL

def count_worms(image_path):
    model = _get_model()
    results = model(image_path)
    df = results.pandas().xyxy[0]
    return len(df)
