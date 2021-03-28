import base64
from io import BytesIO
from google.cloud import vision_v1p2beta1
import google.cloud.translate as g_translate
from pathlib import Path
from google.oauth2 import service_account
import google.auth
import sys
from .application_dir import application_dir


log_dir = application_dir / "Log"
log_dir.mkdir(exist_ok=True)
error_log_path = log_dir / "error.log"
responselog_path = log_dir / "response.txt"
imagelog_path = log_dir / "clip.png"
config_path = application_dir / "config.json"
default_config_path = application_dir / "config_default.json"
key_dir = application_dir / "key"

class SSTRAuthException(Exception):
    def __init__(self, message):
        super().__init__(message)

def GetImageBase64(filepath):
    with open(str(filepath), "rb") as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
        return b64

def GetPILImageBase64(pilImg):
    buffer = BytesIO()
    pilImg.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def GetPILImageBytes(pilImg):
    buffer = BytesIO()
    pilImg.save(buffer, format="PNG")
    return buffer.getvalue()

def get_credential():
    keys = list(key_dir.glob("*.json"))

    #キーが存在しない場合
    if len(keys) == 0:
        #DACの使用を試みる
        try:
            cred, _ = google.auth.default()
            return cred
        except:
            raise SSTRAuthException(f"【エラー】GCPサービスアカウントキーがありません。キーをkeyフォルダに格納してください：{key_dir.resolve()}")

    key = keys[0]

    cred = service_account.Credentials.from_service_account_file(str(key))

    return cred

def OCRfromPILImage(pilImg):
    img_data = GetPILImageBytes(pilImg)
    req_body = {
        'image': {
            'content': img_data
        },
        'features': [{
            'type': 'TEXT_DETECTION'
        }]
    }

    try:
        cred = get_credential()
    except SSTRAuthException as sstrex:
        return str(sstrex)

    client = vision_v1p2beta1.ImageAnnotatorClient(credentials=cred)
    result = client.annotate_image(req_body)


    fw = open(str(responselog_path), "w", encoding="utf-8")
    fw.write(str(result))
    fw.close()
    pilImg.save(imagelog_path)
    # jsonl = json.loads(res.text)
    jsonl = result
    try:
        if len(jsonl.text_annotations) == 0:
            return ""
        ocr = jsonl.text_annotations[0].description
        ocr = ocr.replace("\n"," ")
        return ocr
    except:
        import traceback
        traceback.print_exc()
        #jsonl内容はLogを見ること
        return "OCR ERROR!!"


def Translate(en):
    try:
        cred = get_credential()
    except SSTRAuthException as sstrex:
        return str(sstrex)
    translate_client = g_translate.Client(credentials=cred)
    target = 'ja'
    translation = translate_client.translate(
        en,
        target_language=target)
    translated = translation['translatedText']

    return translated
