import whisper
import os

WHISPER_MODEL = os.getenv("WHISPER_MODEL","small")

_model = None

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
SARVAM_STT_TRANSLATE_URL = "https://api.sarvam.ai/speech-to-text-translate"
SARVAM_MODEL = os.getenv("SARVAM_STT_MODEL", "saaras:v2.5")

def load_model():

    global _model

    if _model is None:
        print(f"loading model ... ")
        _model = whisper.load_model(WHISPER_MODEL)
        print("whisper model loaded successfully ")

    return _model

def transcribe_chunk_whisper(chunk_path: str) -> str:

    model = load_model()
    result = model.transcribe(chunk_path, task="transcribe")
    return result["text"]

def transcribe_chunk_sarvam(chunk_path: str) -> str:
    if not SARVAM_API_KEY:
    raise RuntimeError("SARVAM_API_KEY is not set in environment / .env")

headers = {"api-subscription-key": SARVAM_API_KEY}

with open(chunk_path, "rb") as f:
files = {"file": (os.path.basename(chunk_path), f, "audio/wav")}
data = {"model": SARVAM_MODEL, "with_diarization": "false"}
response = requests.post(
SARVAM_STT_TRANSLATE_URL,
headers=headers,
files=files,
data=data,
timeout=300,

A

response. raise_for_status ()

def transcribe_chunk(chunk_path :str , translate : bool = False ) -> str:
    model = load_model()
    task = "translate" if translate else "transcribe"
    result = model.transcribe(chunk_path , task = task)
    return result['text' ]

def transcribe_all(chunks : list , translate :bool = False) -> str:
    full_transcript = ""

    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i+1} ")
        text = transcribe_chunk(chunk, translate= translate)
        full_transcript += text + " "

    print("Transcription completed")

    return full_transcript