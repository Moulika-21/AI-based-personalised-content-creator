def build_prompt(profile, topic, platform):
    return f"""
You are an AI content creation assistant.

User role: {profile['role']}
Preferred tone: {profile['tone']}
Target platform: {platform}

Task:
Create engaging, clear, and professional content about:
{topic}
"""
