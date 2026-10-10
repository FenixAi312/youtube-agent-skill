import argparse
import json
from typing import Any, Dict, List, Optional

from config import get_config
from modules.channel_analysis import ChannelAnalysisAgent
from modules.competitor_analysis import CompetitorAnalysisAgent
from modules.viral_pattern_analysis import ViralPatternAnalysisAgent
from modules.script_writer import ScriptWriter
from modules.thumbnail_generator import ThumbnailGenerator
from modules.comment_manager import CommentManager
from modules.scheduler import PublishingScheduler
from modules.uploader import YouTubeUploader
from modules.google_drive_sync import DriveSyncManager
from modules.video_builder import VideoBuilder
from modules.orchestrator import YouTubeAgentOrchestrator


class YouTubeAgentSkill:
    """High-level orchestrator for the multi-skill YouTube channel agent."""

    def __init__(self, channel_id: Optional[str] = None):
        self.config = get_config()
        self.channel_id = channel_id or self.config.channel_id
        self.channel_agent = ChannelAnalysisAgent(self.channel_id)
        self.competitor_agent = CompetitorAnalysisAgent()
        self.viral_agent = ViralPatternAnalysisAgent()
        self.script_writer = ScriptWriter()
        self.thumbnail_generator = ThumbnailGenerator()
        self.comment_manager = CommentManager()
        self.scheduler = PublishingScheduler()
        self.uploader = YouTubeUploader()
        self.drive = DriveSyncManager()
        self.video_builder = VideoBuilder()
        self.orchestrator = YouTubeAgentOrchestrator(
            channel_id=self.channel_id,
            channel_agent=self.channel_agent,
            competitor_agent=self.competitor_agent,
            viral_agent=self.viral_agent,
            script_writer=self.script_writer,
            thumbnail_generator=self.thumbnail_generator,
            comment_manager=self.comment_manager,
            scheduler=self.scheduler,
            uploader=self.uploader,
            drive=self.drive,
            video_builder=self.video_builder,
        )

    def run_channel_audit(self) -> Dict[str, Any]:
        return self.orchestrator.run_channel_audit()

    def run_competitor_analysis(self, competitors: Optional[List[str]] = None) -> Dict[str, Any]:
        return self.orchestrator.run_competitor_analysis(competitors=competitors)

    def generate_video_plan(self, niche: str, audience: str, objective: str) -> Dict[str, Any]:
        return self.orchestrator.generate_video_plan(niche=niche, audience=audience, objective=objective)

    def full_growth_report(self) -> Dict[str, Any]:
        return self.orchestrator.full_growth_report()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Agent Skill")
    parser.add_argument("--channel-id", type=str, default=None, help="Channel ID or custom handle to audit")
    parser.add_argument("--mode", type=str, default="audit", choices=["audit", "competitors", "plan", "full"], help="Mode to run")
    args = parser.parse_args()

    skill = YouTubeAgentSkill(channel_id=args.channel_id)

    if args.mode == "audit":
        result = skill.run_channel_audit()
    elif args.mode == "competitors":
        result = skill.run_competitor_analysis()
    elif args.mode == "plan":
        result = skill.generate_video_plan(
            niche="creator growth",
            audience="solo creators wanting more YouTube reach",
            objective="increase watch time and subscriber conversion",
        )
    else:
        result = skill.full_growth_report()

    print(json.dumps(result, ensure_ascii=False, indent=2))
