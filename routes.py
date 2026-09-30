from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
import urllib.parse, random

router = APIRouter()

HOME_HTML = """
<!DOCTYPE html><html><head><title>ComicCraft</title>
<style>
body{margin:0;font-family:Arial;background:url('https://images.unsplash.com/photo-1502082553048-f009c37129b9') center/cover fixed;min-height:100vh;display:flex;align-items:center;justify-content:center;}
.card{background:white;padding:25px;border-radius:12px;width:360px;box-shadow:0 10px 30px rgba(0,0,0,0.3);}
h2{text-align:center;} input,select,textarea{width:100%;padding:10px;margin:6px 0 12px 0;border:1px solid #ccc;border-radius:6px;box-sizing:border-box;}
button{width:100%;padding:12px;background:#0d6efd;color:white;border:none;border-radius:6px;font-weight:bold;cursor:pointer;font-size:16px;}
label{font-size:13px;font-weight:bold;}
</style></head><body><div class="card">
<h2>Create Your Comic</h2>
<form action="/generate" method="post">
<label>Story Prompt</label><textarea name="prompt" rows="3">A brave hero saves the city</textarea>
<label>Main Character Name</label><input name="character" value="Finn"/>
<label>Setting</label><select name="setting"><option>school</option><option selected>forest</option><option>space</option><option>city</option></select>
<label>Story Tone</label><select name="tone"><option>light-hearted</option><option>dramatic</option><option>poetic</option><option selected>funny</option></select>
<label>Art Style</label><select name="art_style"><option selected>anime</option><option>pixel art</option><option>comic book</option><option>realistic</option></select>
<button type="submit">Generate 5-Panel Comic</button>
</form></div></body></html>
"""

@router.get("/", response_class=HTMLResponse)
def home():
    return HOME_HTML

@router.post("/generate", response_class=HTMLResponse)
def generate(prompt: str = Form(...), character: str = Form(...), setting: str = Form(...), tone: str = Form(...), art_style: str = Form(...)):
    def img_url(text):
        seed = random.randint(1,99999)
        q = urllib.parse.quote(f"{art_style} style, {text}, {setting}, comic panel, vibrant, high quality")
        return f"https://image.pollinations.ai/prompt/{q}?seed={seed}&width=700&height=450&nologo=1"

    s1 = f"In the quiet {setting}, {character} woke up. '{prompt}' thought {character}. A new day begins!"
    s2 = f"Suddenly, danger! The {setting} was in trouble. '{character}, help us!' someone cried. {character} felt nervous but brave."
    s3 = f"Adventure time! {character} jumped into action. In {tone} style, {character} faced the challenge head-on."
    s4 = f"Plot twist! Things got harder. {character} almost gave up, but remembered: '{prompt}'. With funny courage, {character} tried again!"
    s5 = f"Victory! {character} saved the {setting}! Everyone cheered. '{character} is our hero!' they shouted. The {tone} ending was perfect!"

    return f"""
    <html><head><title>5-Panel Comic</title>
    <style>
    body{{font-family:Arial;background:#eef6ff;padding:20px;}} 
    .box{{max-width:850px;margin:auto;background:white;padding:25px;border-radius:14px;box-shadow:0 5px 20px rgba(0,0,0,0.1);}}
    .panel{{border:3px solid #111;margin:22px 0;border-radius:14px;overflow:hidden;background:white; box-shadow:5px 5px 0 #111;}}
    .panel img{{width:100%; height:400px; object-fit:cover; display:block; background:#ddd;}}
    .caption{{padding:14px 16px; background:#fffef0; border-top:2px dashed #333;}}
    .bubble{{background:#ffeb3b; display:inline-block; padding:6px 12px; border-radius:18px; border:2px solid #000; font-weight:bold; font-size:13px; margin-bottom:6px;}}
    h1{{color:#0d6efd; text-align:center;}}
    </style></head><body><div class="box">
    <h1>📚 Your Comic: {character} - 5 Panels</h1>
    <p style="text-align:center;"><b>{character}</b> | {setting} | {tone} | {art_style}<br><i>{prompt}</i></p>

    <div class="panel"><img src="{img_url(f'{character} waking up peaceful {setting} morning {art_style}')}" onerror="this.src='https://picsum.photos/seed/p1{character}/700/400'"/><div class="caption"><div class="bubble">💬 {character}: "What a day!"</div><h3>Panel 1 - Beginning</h3><p>{s1}</p></div></div>
    
    <div class="panel"><img src="{img_url(f'{character} hears danger call for help {setting} {art_style}')}" onerror="this.src='https://picsum.photos/seed/p2{character}/700/400'"/><div class="caption"><div class="bubble">😱 Someone: "Help {character}!"</div><h3>Panel 2 - Call to Adventure</h3><p>{s2}</p></div></div>

    <div class="panel"><img src="{img_url(f'{character} fighting action adventure {setting} heroic {art_style}')}" onerror="this.src='https://picsum.photos/seed/p3{character}/700/400'"/><div class="caption"><div class="bubble">💥 {character}: "Let's go!"</div><h3>Panel 3 - Adventure</h3><p>{s3}</p></div></div>

    <div class="panel"><img src="{img_url(f'{character} struggle plot twist difficult moment {setting} {art_style}')}" onerror="this.src='https://picsum.photos/seed/p4{character}/700/400'"/><div class="caption"><div class="bubble">😰 {character}: "I must not fail!"</div><h3>Panel 4 - Twist</h3><p>{s4}</p></div></div>

    <div class="panel"><img src="{img_url(f'{character} victory celebration happy ending crowd cheering {setting} {art_style}')}" onerror="this.src='https://picsum.photos/seed/p5{character}/700/400'"/><div class="caption"><div class="bubble">🎉 {character}: "We did it!"</div><h3>Panel 5 - Hero Saves Day!</h3><p>{s5}</p></div></div>

    <div style="text-align:center; margin-top:25px;"><a href="/">← Create New Comic</a> <button onclick="window.print()" style="margin-left:15px; padding:10px 20px; background:#0d6efd; color:white; border:none; border-radius:8px; cursor:pointer;">📄 Export as PDF</button></div>
    </div></body></html>
    """