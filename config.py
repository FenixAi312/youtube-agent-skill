import os
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional

from dotenv import load_dotenv

load_dotenv()


@dataclass
class AppConfig:
    google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
    youtube_api_key: str = os.getenv("YOUTUBE_API_KEY", "")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
    google_drive_credentials_path: str = os.getenv("GOOGLE_DRIVE_CREDENTIALS_PATH", "")
    google_drive_folder_id: str = os.getenv("GOOGLE_DRIVE_FOLDER_ID", "")
    channel_id: str = os.getenv("CHANNEL_ID", "")
    default_language: str = os.getenv("DEFAULT_LANGUAGE", "en")
    default_region: str = os.getenv("DEFAULT_REGION", "US")
    default_publish_time: str = os.getenv("DEFAULT_PUBLISH_TIME", "18:00")
    max_competitors: int = int(os.getenv("MAX_COMPETITORS", "5"))
    max_videos_per_analysis: int = int(os.getenv("MAX_VIDEOS_PER_ANALYSIS", "20"))

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)


CONFIG = AppConfig()


def get_config() -> AppConfig:
    return CONFIG
