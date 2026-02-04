import whisper

print("Loading PEU listening module...")

model = whisper.load_model("base")

print("Speak now (5 seconds)...")

result = model.transcribe("test.wav")

print("PEU heard:")
print(result["text"])
