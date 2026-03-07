"""List available ElevenLabs voices and their IDs."""
import os
from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key=os.environ['ELEVENLABS_API_KEY'])
voices = client.voices.get_all().voices
for v in sorted(voices, key=lambda v: v.name):
    print(f"{v.voice_id}  {v.name}")
