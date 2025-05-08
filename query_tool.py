import os
import azure.cognitiveservices.speech
import typing
import speech_recognition


speech_config = azure.cognitiveservices.speech.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

audio_config = azure.cognitiveservices.speech.audio.AudioOutputConfig(use_default_speaker=True)

# The neural multilingual voice can speak different languages based on the input text.
speech_config.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'

speech_synthesizer = azure.cognitiveservices.speech.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)


def query_user(question : str) -> typing.Annotated[str | None, "a transcription of the user's answer, if the function call succeeded, otherwise None"]:

    def speak_to_user(text : str) -> None:
        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == azure.cognitiveservices.speech.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == azure.cognitiveservices.speech.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == azure.cognitiveservices.speech.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")

    def listen_to_mic() -> str | None:
        recognizer = speech_recognition.Recognizer()
        # allow the speaker to leave 1.5s gaps in speech
        recognizer.pause_threshold = 1.5

        with speech_recognition.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=30)
            
        print("Recognizing...")
        try:
            text = recognizer.recognize_azure(audio, key=os.getenv("SPEECH_KEY"),location=os.getenv("SPEECH_REGION")) # SPEECH API is loaded in environment.
            print("Transcribed:",text)
            return(text)

        except speech_recognition.UnknownValueError:
            print(f"Sorry, could not recognize the phrase.")
            return None
        
        except speech_recognition.RequestError as e:
            print(f"Could not make the API call; {0}".format(e))
            return None
    # speak the question
    speak_to_user(question)
    # fetch a transcription
    text = listen_to_mic()
    # return the transcription
    return text
