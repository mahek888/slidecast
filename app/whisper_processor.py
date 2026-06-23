import whisper


class WhisperProcessor:

    def __init__(
        self,
        model_name="base"
    ):
        self.model = whisper.load_model(
            model_name
        )

    def transcribe(
        self,
        audio_path
    ):
        return self.model.transcribe(
            audio_path,
            language="hi"
        )