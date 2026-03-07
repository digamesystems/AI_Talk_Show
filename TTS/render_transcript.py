"""
Render a panel discussion transcript to audio using ElevenLabs TTS.

Usage:
    python render_transcript.py <transcript.txt> [--voices tts_voices.yaml] [--output output.mp3]

Requirements:
    pip install elevenlabs pydub
    ffmpeg installed and on PATH (https://ffmpeg.org/download.html)
    ELEVENLABS_API_KEY environment variable set
"""

import re
import os
import argparse
import yaml
from io import BytesIO
from pathlib import Path
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
from pydub import AudioSegment


HEADER_END = re.compile(r'^=+$')
TURN_START = re.compile(r'^\[([^\]→]+?)(?:\s*→\s*([^\]]+))?\]:\s*(.*)')
STAGE_DIR = re.compile(r'\*([^*]+)\*')

# Pause durations (ms) keyed on stage direction keywords
PAUSE_MS = {
    'pause':        1200,
    'sits quietly': 1200,
    'laughs':        600,
    'chuckles':      600,
    'smiles':        400,
}
DEFAULT_PAUSE_MS = 600


def parse_transcript(path):
    """Parse transcript file into a list of turn dicts."""
    lines = Path(path).read_text(encoding='utf-8').split('\n')

    # Skip header block (up to and including the ===...=== separator line)
    start = 0
    for i, line in enumerate(lines):
        if HEADER_END.match(line.strip()):
            start = i + 1
            break

    turns = []
    current = None
    for line in lines[start:]:
        m = TURN_START.match(line)
        if m:
            if current:
                turns.append(current)
            current = {
                'speaker': m.group(1).strip(),
                'target':  m.group(2).strip() if m.group(2) else None,
                'lines':   [m.group(3)] if m.group(3) else [],
            }
        elif current is not None:
            current['lines'].append(line)
    if current:
        turns.append(current)

    result = []
    for t in turns:
        raw = '\n'.join(t['lines']).strip()
        directions = STAGE_DIR.findall(raw)
        content = STAGE_DIR.sub('', raw).strip()
        if content:
            result.append({
                'speaker':    t['speaker'],
                'target':     t['target'],
                'content':    content,
                'directions': directions,
            })
    return result


def pause_duration(directions):
    """Return appropriate pause length in ms based on stage directions."""
    for d in directions:
        for keyword, ms in PAUSE_MS.items():
            if keyword in d.lower():
                return ms
    return DEFAULT_PAUSE_MS


def synthesize(client, text, voice_cfg):
    """Call ElevenLabs and return raw MP3 bytes."""
    audio_gen = client.text_to_speech.convert(
        voice_id=voice_cfg['voice_id'],
        text=text,
        model_id=voice_cfg.get('model', 'eleven_turbo_v2'),
        voice_settings=VoiceSettings(
            stability=voice_cfg.get('stability', 0.5),
            similarity_boost=voice_cfg.get('similarity_boost', 0.75),
            style=voice_cfg.get('style', 0.0),
        ),
    )
    return b''.join(audio_gen)


def render(transcript_path, voices_path, output_path):
    turns = parse_transcript(transcript_path)

    with open(voices_path) as f:
        voices = yaml.safe_load(f)['voices']

    client = ElevenLabs(api_key=os.environ['ELEVENLABS_API_KEY'])

    assembled = AudioSegment.empty()
    skipped = []

    for i, turn in enumerate(turns):
        speaker = turn['speaker']
        if speaker not in voices:
            skipped.append(speaker)
            continue

        preview = turn['content'][:60].replace('\n', ' ')
        print(f"[{i+1}/{len(turns)}] {speaker}: {preview}...")

        try:
            audio_bytes = synthesize(client, turn['content'], voices[speaker])
            segment = AudioSegment.from_mp3(BytesIO(audio_bytes))
            assembled += AudioSegment.silent(duration=pause_duration(turn['directions']))
            assembled += segment
        except Exception as e:
            print(f"  [Warning]: Turn {i+1} failed — {e}")
            skipped.append(f"{speaker} (turn {i+1})")

    if len(assembled) == 0:
        print("\nNo audio generated — nothing to save.")
        return

    assembled.export(output_path, format='mp3')
    print(f"\nSaved: {output_path}")

    if skipped:
        print(f"Skipped: {'; '.join(skipped)}")


def main():
    parser = argparse.ArgumentParser(description='Render transcript to audio')
    parser.add_argument('transcript', help='Transcript .txt file')
    parser.add_argument('--voices', default='tts_voices.yaml', help='Voice config YAML')
    parser.add_argument('--output', default=None, help='Output .mp3 file')
    args = parser.parse_args()

    output = args.output or Path(args.transcript).stem + '.mp3'
    render(args.transcript, args.voices, output)


if __name__ == '__main__':
    main()
