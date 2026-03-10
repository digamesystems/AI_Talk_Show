"""
Standalone test for summarize_history().
Creates a small set of mock turns and prints the summary.
Run from the project root: python test_summarize.py
"""

import anthropic
from types import SimpleNamespace
from datetime import datetime
from models import Turn, Prompt
from conversation import summarize_history

# --- Mock speakers ---
moderator = SimpleNamespace(name="John")
jean      = SimpleNamespace(name="Jean",  handle="jean")
alan      = SimpleNamespace(name="Alan",  handle="alan")
basho     = SimpleNamespace(name="Basho", handle="basho")
teresa    = SimpleNamespace(name="Teresa", handle="teresa")

def t(speaker, content):
    return Turn(speaker=speaker, content=content, timestamp=datetime.now())

# --- Representative turns from our design session ---
history = [
    t(moderator, "Good afternoon. With me are Alan and Jean. Let's discuss recent developments in the Middle East."),
    t(jean,      "The situation forces us to confront a question existentialism cannot avoid: when a people is systematically denied the conditions for self-determination, is their resistance a choice, or the only authentic response available to them? Bad faith runs in every direction here — including among those who demand a ceasefire while funding the weapons."),
    t(alan,      "Jean sees bad faith everywhere, and he's not wrong — but the framework of authentic choice may itself be a trap. The Middle East has been narrated into its conflict for centuries. The map is not the territory, and the territory is mostly people trying to eat breakfast."),
    t(moderator, "Please welcome our new guest, Basho."),
    t(basho,     "Both Jean and Alan share an assumption neither has named: that understanding the conflict is what's needed. The question underneath both responses is: what is this conversation actually for?"),
    t(moderator, "For reference, my wife is a pragmatist. The problems in Gaza are not primarily philosophical. She would probably suggest that collectively we go there and prepare food."),
    t(alan,      "I'd tell her she's already there. Preparing food is not a retreat from philosophy — it is a philosophy, enacted rather than argued. The Zen tradition calls it samu — work as practice."),
    t(jean,      "Preparing food is a good act. But it does not reach the structure that produces the hunger. I respect the impulse. I distrust the satisfaction it provides to the person doing the feeding."),
    t(moderator, "Please welcome Teresa."),
    t(teresa,    "Hi, John. What have you and your AI knuckleheads been up to?"),
    t(teresa,    "Jean, where does your virtue deviate from the temperament of an academic?"),
    t(jean,      "That is the question I deserve. I am an academic. I sit in chairs. I have not fed anyone in Gaza. The difference between my temperament and my virtue is that I know what I am doing and continue to ask whether it is enough. Whether that distinction holds under your scrutiny — I genuinely do not know."),
    t(moderator, "Alan, I'll be in Gaza next Thursday, working at a food kitchen. Want to come down and help?"),
    t(alan,      "I would very much like to. I am unable to — which is the most honest thing I've said in thirty-seven turns."),
    t(jean,      "I cannot come. But I will not dress that up as a limitation — it is a choice. I was wrong to call it temperament."),
]

if __name__ == "__main__":
    client = anthropic.Anthropic()
    print(f"Summarizing {len(history)} turns...\n")
    summary = summarize_history(history, client)
    print("--- SUMMARY ---")
    print(summary)
    print(f"\n--- WORD COUNT: {len(summary.split())} ---")