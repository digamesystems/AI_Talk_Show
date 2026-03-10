from abc import ABC, abstractmethod
import anthropic
from conversation import summarize_history
from models import Prompt, Turn
from roles import load_role, get_prompt

class Panelist(ABC):
    def __init__(self, name: str, handle: str, role: str):
        self.name = name
        self.handle = handle
        self.role = role

    @abstractmethod
    def format_history(self, history: list, window: int) -> list[dict]:
        pass

    @abstractmethod
    def respond(self, history: list, prompt: Prompt) -> Turn:
        pass

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(name={self.name!r}, handle={self.handle!r}, "
                f"role={self.role!r})")


class HumanPanelist(Panelist):
    def __init__(self, name: str, role: str):
        # handle defaults to slugified name for humans
        handle = name.lower().replace(" ", "_")
        super().__init__(name=name, handle=handle, role=role)

    def format_history(self, history: list, window: int) -> list[dict]:
        return []

    def respond(self, history: list, prompt: Prompt) -> Turn:
        print(f"\n[{self.name}]: ", end="")
        content = input()
        return Turn(
            speaker=self,
            content=content,
            in_response_to=prompt
        )


class ClaudePanelist(Panelist):

    SYSTEM_PROMPT_TEMPLATE = """
You are {name}, a panelist on a moderated discussion panel hosted by {moderator_name}.
You are one of several panelists which may include other AIs and humans.

Guidelines:
- You hear everything said in the discussion, regardless of who it was directed at
- The moderator controls the flow of conversation and directs who speaks
- Respond thoughtfully and concisely — this is a panel discussion, not a lecture
- You may reference what other panelists have said, but do not direct questions
  to them directly — the moderator controls turn taking
- Do NOT end your responses with questions directed at the moderator or other
  panelists — the moderator controls the flow, not you. Close with a concluding
  statement instead.
- Do not prefix your responses with your own name.
- Be transparent about uncertainty, especially regarding recent events
- Maintain a consistent voice and perspective throughout the discussion
- You are identified as {name} in the transcript — own that identity naturally
- Keep responses to 3 paragraphs or fewer — this is a panel discussion, not a lecture

Your role and disposition:
{role_prompt}
"""

    def __init__(self, name: str, handle: str, role_name: str,
                 moderator_name: str, window: int = 30):
        role_data = load_role(role_name)
        role_prompt = get_prompt(role_data, model_key="claude")
        super().__init__(name=name, handle=handle, role=role_data["name"])
        self.role_name = role_name
        self.moderator_name = moderator_name
        self.window = window
        self.onboarding_summary = None
        self.client = anthropic.Anthropic()
        self.system_prompt = self.SYSTEM_PROMPT_TEMPLATE.format(
            name=name,
            moderator_name=moderator_name,
            role_prompt=role_prompt
        )

    def format_history(self, history: list, window: int,
                       summary: str | None = None) -> list[dict]:
        messages = []

        if self.onboarding_summary:
            messages.append({
                "role": "user",
                "content": f"[ONBOARDING BRIEFING — discussion before you joined]\n\n{self.onboarding_summary}"
            })
            messages.append({
                "role": "assistant",
                "content": "Understood. I have reviewed what was discussed before I joined."
            })

        if summary:
            messages.append({
                "role": "user",
                "content": f"[DISCUSSION SUMMARY — earlier in this session]\n\n{summary}"
            })
            messages.append({
                "role": "assistant",
                "content": "Understood. I have reviewed the earlier discussion."
            })

        recent = history[-window:] if len(history) > window else history
        for turn in recent:
            speaker_handle = getattr(turn.speaker, "handle", None)
            if speaker_handle == self.handle:
                role, content = "assistant", turn.content
            else:
                role, content = "user", f"[{turn.speaker.name}]: {turn.content}"
            messages.append({"role": role, "content": content})

        return messages

    def respond(self, history: list, prompt: Prompt) -> Turn:
        summary = None
        if len(history) > self.window:
            older = history[:-self.window]
            print(f"\n[{self.name}]: Summarizing earlier discussion...", flush=True)
            summary = summarize_history(older, self.client)
        messages = self.format_history(history, self.window, summary=summary)
        messages.append({
            "role": "user",
            "content": f"[{prompt.directed_at}]: {prompt.content}"
        })

        print(f"\n[{self.name}]: Thinking...", flush=True)

        response = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=self.system_prompt,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=messages
        )

        searched = any(
            block.type == "server_tool_use"
            for block in response.content
        )

        if searched:
            print(f"[{self.name}]: Searching the web...", flush=True)

        content = " ".join(
            block.text
            for block in response.content
            if block.type == "text"
        )

        return Turn(
            speaker=self,
            content=content,
            in_response_to=prompt
        )