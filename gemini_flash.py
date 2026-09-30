from app.models import ComicOutline

def generate_outline(story_prompt, character_name="Hero", setting="Adventure", tone="heroic", art_style="comic"):
    return ComicOutline(title="Test Comic", character_name=character_name, panels=[{"title":"Panel 1","description":story_prompt,"dialogue":"Hello","image_prompt":"hero"}]*5)