from typing import Any, Dict, List, Optional


class YouTubeAgentOrchestrator:
    """Coordinate the full YouTube channel workflow."""

    def __init__(self, channel_id: str, channel_agent, competitor_agent, viral_agent, script_writer, thumbnail_generator, comment_manager, scheduler, uploader, drive, video_builder):
        self.channel_id = channel_id
        self.channel_agent = channel_agent
        self.competitor_agent = competitor_agent
        self.viral_agent = viral_agent
        self.script_writer = script_writer
        self.thumbnail_generator = thumbnail_generator
        self.comment_manager = comment_manager
        self.scheduler = scheduler
        self.uploader = uploader
        self.drive = drive
        self.video_builder = video_builder

    def run_channel_audit(self) -> Dict[str, Any]:
        return self.channel_agent.create_channel_report()

    def run_competitor_analysis(self, competitors: Optional[List[str]] = None) -> Dict[str, Any]:
        return self.competitor_agent.summarize_competitor_strategy(competitors=competitors)

    def generate_video_plan(self, niche: str, audience: str, objective: str) -> Dict[str, Any]:
        viral_summary = self.viral_agent.summarize_viral_mechanics(niche)
        script = self.script_writer.generate_script(topic=f"How to grow in {niche}", angle=objective, audience=audience)
        thumbnails = self.thumbnail_generator.create_thumbnail_plan(topic=f"How to grow in {niche}", angle=objective)
        calendar = self.scheduler.suggest_best_release_window(niche)
        return {
            "niche": niche,
            "audience": audience,
            "objective": objective,
            "viral_summary": viral_summary,
            "script": script,
            "thumbnails": thumbnails,
            "calendar": calendar,
        }

    def full_growth_report(self) -> Dict[str, Any]:
        channel = self.run_channel_audit()
        competitors = self.run_competitor_analysis()
        plan = self.generate_video_plan(
            niche="YouTube growth",
            audience="creators who want more reach",
            objective="increase retention and watch time",
        )
        return {
            "channel": channel,
            "competitors": competitors,
            "next_video_plan": plan,
        }

