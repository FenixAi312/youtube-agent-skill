from typing import Any, Dict, List


class ScriptWriter:
    """Generate YouTube scripts based on viral patterns and the channel’s style."""

    def __init__(self):
        pass

    def build_outline(self, topic: str, angle: str, audience: str) -> List[str]:
        return [
            "Hook: open with the exact pain or promise the audience feels.",
            "Reframe: explain why the problem is more common than people think.",
            "Evidence: share a concrete example or case study.",
            "Framework: break it into 3 steps or 3 mistakes.",
            "Action: give the audience one clear next step.",
            "CTA: encourage the next action, comment, or follow.",
        ]

    def generate_script(self, topic: str, angle: str, audience: str, tone: str = "clear and punchy") -> Dict[str, Any]:
        return {
            "topic": topic,
            "angle": angle,
            "audience": audience,
            "tone": tone,
            "hook": f"If you’re still struggling with {topic}, here’s why most creators get stuck.",
            "outline": self.build_outline(topic, angle, audience),
            "cta": "Comment the exact problem you want solved next, and I’ll break it down in the next video.",
            "notes": "Use plain language, keep tension high, and lead with proof before advice.",
        }
