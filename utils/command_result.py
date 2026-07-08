from dataclasses import dataclass

@dataclass
class CommandResult:
    handled: bool
    ai_prompt: str | None = None
    target_file: str | None = None