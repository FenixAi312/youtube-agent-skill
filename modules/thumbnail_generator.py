from typing import Any, Dict, List


class ThumbnailGenerator:
    """Create thumbnail concepts and packaging direction."""

    def __init__(self):
        pass

    def create_concepts(self, topic: str, angle: str) -> List[Dict[str, Any]]:
        return [
            {
                "concept_name": "Contrast Shot",
                "layout": "Big headline + single emotional face + strong blue-red contrast",
                "headline": "I stopped doing this",
                "callout": "and my channel changed",
            },
            {
                "concept_name": "Mistake Label",
                "layout": "Large warning icon + 3-step framing + short text",
                "headline": "The mistake ruining your growth",
                "callout": "fix this before publishing again",
            },
        ]

    def create_thumbnail_plan(self, topic: str, angle: str) -> Dict[str, Any]:
        return {
            "topic": topic,
            "angle": angle,
            "brand_guidance": [
                "Keep the text short and legible.",
                "Use one emotional focal point.",
                "Apply a consistent visual style across all uploads.",
            ],
            "concepts": self.create_concepts(topic, angle),
        }

