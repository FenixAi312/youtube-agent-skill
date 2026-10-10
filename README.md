# YouTube Agent Skill

A production-ready starter for a Claude Code / GitHub skill that operates like a full YouTube growth and channel-management agent.

This repo is designed for creators who want an AI agent to:
- audit their channel and show performance trends
- compare against competitors
- discover viral title and hook patterns
- generate scripts and thumbnails
- moderate comments and draft responses
- plan publishing calendars
- schedule uploads and manage publishing
- store assets in Google Drive
- prepare video production workflows

## What the skill does

The skill includes 12 sub-skills:
1. Channel Analytics Auditor
2. Performance Trend Analyzer
3. Competitor Benchmark Engine
4. Viral Pattern Hunter
5. Hook & Title Formula Extractor
6. Script Generator
7. Thumbnail Concept Designer
8. Comment Insight Manager
9. Publishing Scheduler
10. YouTube Uploader
11. Google Drive Asset Sync
12. Video Production Orchestrator

## Architecture

- `youtube_agent_skill.py`: entry point and orchestration class
- `config.py`: environment config and API setup
- `modules/`: specialized analyzers and tool adapters

## Setup

1. Create a virtual environment
2. Install dependencies:
   `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`
4. Fill in:
   - GOOGLE_API_KEY
   - YOUTUBE_API_KEY
   - GOOGLE_DRIVE_CREDENTIALS_PATH
   - GOOGLE_DRIVE_FOLDER_ID
5. Run the demo:
   `python youtube_agent_skill.py --channel-id YOUR_CHANNEL_ID`

## Example output

The agent can produce a structured report like:
- channel health score
- top-performing topics
- weak retention windows
- average CTR and audience retention
- competitor summary
- viral title patterns
- script suggestions
- next 30-day publishing plan
- recommended upload schedule

## Notes

- Some features work as API adapters and require valid credentials.
- Some features are intentionally implemented as templates and logic scaffolds, ready to be extended with your custom workflows.
- This project is made for a Claude Code skill workflow and can be adapted to other agent orchestration tools.

## License

MIT
