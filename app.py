from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from moviepy.editor import *
CAROUSEL_FOLDER
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
import google.generativeai as genai
from moviepy.editor import TextClip, CompositeVideoClip
import sqlite3
import os
import time
import random
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
from flask_bcrypt import Bcrypt
import stripe
from flask_jwt_extended import (

    JWTManager,

    create_access_token,

    jwt_required,

    get_jwt_identity
)
stripe.api_key = "YOUR_STRIPE_SECRET_KEY"
# =========================================
# FLASK
# =========================================

app = Flask(__name__)

CORS(app)

# =========================================
# GEMINI API
# =========================================

genai.configure(
    api_key="YOUR_GEMINI_API_KEY"
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

app.config["JWT_SECRET_KEY"] = "SUPER_SECRET_KEY"

jwt = JWTManager(app)

bcrypt = Bcrypt(app)
cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    email TEXT UNIQUE,

    password TEXT

)

""")

conn.commit()
cursor.execute("""

CREATE TABLE IF NOT EXISTS subscriptions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    email TEXT,

    customer_id TEXT,

    subscription_id TEXT,

    status TEXT

)

""")

conn.commit()
# =========================================
# FOLDERS
# =========================================

GENERATED_FOLDER = "generated_posters"
CAROUSEL_FOLDER = "generated_carousels"
VIDEO_FOLDER = "generated_videos"
scheduler = BackgroundScheduler()

scheduler.start()
def scheduled_instagram_post(

    image_url,

    caption
):

    post_to_instagram(

        image_url,

        caption
    )
os.makedirs(
    CAROUSEL_FOLDER,
    exist_ok=True
)

os.makedirs(
    GENERATED_FOLDER,
    exist_ok=True
)
VIDEO_FOLDER = "generated_videos"

os.makedirs(
    VIDEO_FOLDER,
    exist_ok=True
)
AUDIO_FOLDER = "generated_audio"

os.makedirs(
    AUDIO_FOLDER,
    exist_ok=True
)

# =========================================
# DATABASE
# =========================================

conn = sqlite3.connect(
    "posts.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS posts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    topic TEXT,

    template TEXT,

    content TEXT,

    image TEXT

)

""")

conn.commit()

# =========================================
# THEMES
# =========================================

theme = {

    "Healthcare": {

        "bg": (8, 15, 40),

        "header": (0, 191, 255)
    },

    "Fitness": {

        "bg": (35, 20, 10),

        "header": (255, 120, 0)
    },

    "Business": {

        "bg": (10, 10, 10),

        "header": (60, 60, 60)
    },

    "Education": {

        "bg": (40, 10, 70),

        "header": (150, 80, 255)
    },

    "Real Estate": {

        "bg": (30, 25, 10),

        "header": (212, 175, 55)
    }
}

# =========================================
# BACKGROUNDS
# =========================================

backgrounds = {

    "Healthcare": "assets/healthcare.jpg",

    "Fitness": "assets/fitness.jpg",

    "Business": "assets/business.jpg",

    "Education": "assets/education.jpg",

    "Real Estate": "assets/realestate.jpg"
}

# =========================================
# SERVE GENERATED POSTERS
# =========================================

@app.route("/generated_posters/<filename>")
def serve_poster(filename):

    return send_from_directory(
        GENERATED_FOLDER,
        filename
    )
@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():

    try:

        data = request.json

        email = data.get("email")

        session = stripe.checkout.Session.create(

            payment_method_types=["card"],

            line_items=[

                {

                    "price_data": {

                        "currency": "usd",

                        "product_data": {

                            "name": "AI Social Media Pro"
                        },

                        "unit_amount": 1900,

                        "recurring": {

                            "interval": "month"
                        }
                    },

                    "quantity": 1
                }
            ],

            mode="subscription",

            success_url="http://localhost:5173/success",

            cancel_url="http://localhost:5173/cancel",

            customer_email=email
        )

        return jsonify({

            "success": True,

            "url": session.url
        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)
        })
@app.route("/signup", methods=["POST"])
def signup():

    try:

        data = request.json

        username = data.get("username")

        email = data.get("email")

        password = data.get("password")

        hashed_password = bcrypt.generate_password_hash(

            password

        ).decode("utf-8")

        cursor.execute(

            """

            INSERT INTO users (

                username,
                email,
                password

            )

            VALUES (?, ?, ?)

            """,

            (

                username,
                email,
                hashed_password
            )
        )

        conn.commit()

        return jsonify({

            "success": True,

            "message": "User Registered"
        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)
        })
@app.route("/login", methods=["POST"])
def login():

    try:

        data = request.json

        email = data.get("email")

        password = data.get("password")

        cursor.execute(

            """

            SELECT * FROM users

            WHERE email = ?

            """,

            (email,)
        )

        user = cursor.fetchone()

        if not user:

            return jsonify({

                "success": False,

                "message": "User not found"
            })

        password_correct = bcrypt.check_password_hash(

            user[3],

            password
        )

        if not password_correct:

            return jsonify({

                "success": False,

                "message": "Invalid password"
            })

        token = create_access_token(

            identity=email
        )

        return jsonify({

            "success": True,

            "token": token,

            "username": user[1]
        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)
        })
@app.route("/profile")
@jwt_required()
def profile():

    current_user = get_jwt_identity()

    return jsonify({

        "success": True,

        "user": current_user
    })
@app.route("/login", methods=["POST"])
def login():

    try:

        data = request.json

        email = data.get("email")

        password = data.get("password")

        cursor.execute(

            """

            SELECT * FROM users WHERE email = ?

            """,

            (email,)

        )

        user = cursor.fetchone()

        if not user:

            return jsonify({

                "success": False,

                "message": "Invalid credentials"
            })

        if not bcrypt.check_password_hash(user[4], password):

            return jsonify({

                "success": False,

                "message": "Invalid credentials"
            })

        access_token = create_access_token(identity=user[0])

        return jsonify({

            "success": True,

            "token": access_token
        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)
        })
@app.route("/schedule_post", methods=["POST"])
def schedule_post():

    try:

        data = request.json

        image_url = data.get("image")

        caption = data.get("caption")

        run_time = data.get("time")

        scheduler.add_job(

            scheduled_instagram_post,

            "date",

            run_date=run_time,

            args=[

                image_url,

                caption
            ]
        )

        return jsonify({

            "success": True,

            "message": "Post Scheduled"
        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)
        })
@app.route("/generated_audio/<filename>")
def serve_audio(filename):

    return send_from_directory(

        AUDIO_FOLDER,

        filename
    )

@app.route("/generated_carousels/<filename>")
def serve_carousel(filename):

    return send_from_directory(

        CAROUSEL_FOLDER,

        filename
    )

# =========================================
# HISTORY API
# =========================================

subtitle_lines = [

    "Professional diagnostics",

    "Accurate reports",

    "Fast processing",

    "Trusted laboratory",

    "Book your healthcare test today"
]
@app.route("/generated_videos/<filename>")
def serve_video(filename):

    return send_from_directory(

        VIDEO_FOLDER,

        filename
    )

@app.route("/api/history", methods=["GET"])
def history():

    cursor.execute(
        "SELECT * FROM posts ORDER BY id DESC"
    )

    posts = cursor.fetchall()

    result = []

    for post in posts:

        result.append({

            "id": post[0],

            "topic": post[1],

            "template": post[2],

            "content": post[3],

            "image": post[4]
        })
    return jsonify(result)

    response = {
        "title": title,
        "caption": caption,
        "carousel_images": carousel_images,
    }            
    return {
    "title": title,
    "video": "video_url",
}

# =========================================
# GENERATE API
# =========================================

@app.route("/generate", methods=["POST"])
def generate():

    try:

        result = {
    "title": title,
    "caption": caption,
    "carousel_images": carousel_images,
    "video": video_url,
    "audio": audio_url,
}

        topic = data.get("topic")

        template = data.get("template")

        # =================================
        # GEMINI PROMPT
        # =================================

        prompt = f"""
Create short professional social media content.

Topic: {topic}

Category: {template}

Generate:

1 short caption
5 hashtags
1 CTA

Keep response short.
No markdown.
No headings.
"""

        response = model.generate_content(
            prompt
        )

        generated_text = response.text

        generated_text = generated_text.replace("*", "")
        generated_text = generated_text.replace("#", "")
        generated_text = generated_text.replace("---", "")

        # =================================
        # RANDOM STYLE
        # =================================

        style = random.choice(

            [

                "minimal",

                "luxury",

                "neon",

                "corporate",

                "gradient"

            ]
        )

        # =================================
        # STYLE COLORS
        # =================================

        if style == "minimal":

            header_color = theme[template]["header"]

        elif style == "luxury":

            header_color = (212, 175, 55)

        elif style == "neon":

            header_color = (255, 0, 255)

        elif style == "corporate":

            header_color = (40, 40, 40)

        else:

            header_color = (120, 0, 255)

        # =================================
        # TEXT COLORS
        # =================================

        if style == "neon":

            text_color = (0, 255, 255)

        elif style == "luxury":

            text_color = (212, 175, 55)

        else:

            text_color = (40, 40, 40)

        # =================================
        # BACKGROUND IMAGE
        # =================================

        bg_path = backgrounds.get(template)

        if os.path.exists(bg_path):

            img = Image.open(bg_path).convert("RGB")

            img = img.resize((1080, 1080))

        try:
    video_clips = []

    for index, img_path in enumerate(carousel_images):

        image_clip = ImageClip(img_path).set_duration(3)

        subtitle = TextClip(
            subtitle_lines[index],
            fontsize=60,
            color="white",
            bg_color="black",
            size=(900, None),
            method="caption"
        )

        subtitle = subtitle.set_position(
            ("center", "bottom")
        ).set_duration(3)

        final_clip = CompositeVideoClip(
            [image_clip, subtitle],
            size=(1080, 1080)
        )

        video_clips.append(final_clip)

except Exception as e:
    print(e)
except Exception as e:
    print(e)
for img_path in carousel_images:
    subtitle = TextClip(

    subtitle_lines[index],

    fontsize=60,

    color="white",

    bg_color="rgba(0,0,0,0.6)"

    size=(900, None),

    method="caption"
)

subtitle = subtitle.set_position(

    ("center", 850)
)

subtitle = subtitle.set_duration(3)

subtitle_clips.append(subtitle)

    filename_only = img_path.split("/")[-1]

    full_path = os.path.join(

        CAROUSEL_FOLDER,

        filename_only
    )

    clip = ImageClip(full_path)

    clip = clip.set_duration(3)

    final_clip = CompositeVideoClip(

    [

        clip,

        subtitle
    ]
)

avatar_image = "avatars/doctor.jpg"

avatar_output = f"avatar_{timestamp}.mp4"

subprocess.run(

    [

        "python",

        "SadTalker/inference.py",

        "--driven_audio",

        audio_path,

        "--source_image",

        avatar_image,

        "--result_dir",

        VIDEO_FOLDER

    ]
)
clips.append(final_clip)

    voice_text = f"""

{topic}

Professional diagnostics.

Accurate reports.

Fast processing.

Trusted laboratory.

Book your healthcare test today.

"""

tts = gTTS(text=voice_text, lang="en", slow=False)
audio_filename = f"voice_{timestamp}.mp3"
audio_path = os.path.join(AUDIO_FOLDER, audio_filename)
tts.save(audio_path)
tts = gTTS(

    text=voice_text,

    lang="en"
)

audio_filename = f"voice_{timestamp}.mp3"

audio_path = os.path.join(

    AUDIO_FOLDER,

    audio_filename
)

tts.save(audio_path)

audio_url = (

    f"http://127.0.0.1:5003/generated_audio/{audio_filename}"
)

final_video = concatenate_videoclips(

    clips,

    method="compose"
)

video_filename = f"reel_{timestamp}.mp4"

video_path = os.path.join(

    VIDEO_FOLDER,

    video_filename
)

audio_clip = AudioFileClip(audio_path)

final_video = final_video.set_audio(audio_clip)

final_video.write_videofile(

    video_path,

    fps=24
)

video_url = (

    f"http://127.0.0.1:5003/generated_videos/{video_filename}"
)

        # =================================
        # DARK OVERLAY
        # =================================

        overlay = Image.new(

            "RGBA",

            (1080, 1080),

            (0, 0, 0, 120)
        )

        img = img.convert("RGBA")

        img.paste(

            overlay,

            (0, 0),

            overlay
        )

        draw = ImageDraw.Draw(img)

        # =================================
        # FONTS
        # =================================

        try:

            title_font = ImageFont.truetype(
                "arial.ttf",
                55
            )

            text_font = ImageFont.truetype(
                "arial.ttf",
                38
            )

            small_font = ImageFont.truetype(
                "arial.ttf",
                24
            )

        except:

            title_font = ImageFont.load_default()

            text_font = ImageFont.load_default()

            small_font = ImageFont.load_default()

        # =================================
        # HEADER
        # =================================

        draw.rectangle(

            [(0, 0), (1080, 170)],

            fill=header_color
        )

        draw.text(

            (60, 55),

            f"{template.upper()} AI POST",

            fill="white",

            font=title_font
        )

        # =================================
        # MAIN CARD
        # =================================

        draw.rounded_rectangle(

            [(70, 220), (1010, 900)],

            radius=40,

            fill=(255, 255, 255, 230)
        )

        # =================================
        # TOPIC BADGE
        # =================================

        draw.rounded_rectangle(

            [(120, 260), (420, 330)],

            radius=20,

            fill=header_color
        )

        draw.text(

            (145, 280),

            f"TOPIC : {topic.upper()}",

            fill="white",

            font=text_font
        )

        # =================================
        # CONTENT
        # =================================

        content_lines = [

            "Professional diagnostics",

            "for better healthcare.",

            "",

            "• Accurate Reports",

            "• Fast Processing",

            "• Trusted Laboratory",

            "",

            "Book your test today."
        ]

        y = 420

        for line in content_lines:

            draw.text(

                (150, y),

                line,

                fill=text_color,

                font=text_font
            )

            y += 65

        # =================================
        # FOOTER
        # =================================

        draw.rectangle(

            [(0, 950), (1080, 1080)],

            fill=theme[template]["bg"]
        )

        draw.text(

            (320, 995),

            "@AI SOCIAL MEDIA GENERATOR",

            fill="white",

            font=small_font
        )

        # =================================
        # SAVE IMAGE
        # =================================

        timestamp = int(time.time())

        filename = f"poster_{timestamp}.png"

        filepath = os.path.join(
            GENERATED_FOLDER,
            filename
        )

        img = img.convert("RGB")

        img.save(filepath)

        image_url = f"http://127.0.0.1:5003/generated_posters/{filename}"

        # =================================
        # SAVE DATABASE
        # =================================

        cursor.execute(

            """

            INSERT INTO posts (

                topic,
                template,
                content,
                image

            )

            VALUES (?, ?, ?, ?)

            """,

            (

                topic,

                template,

                generated_text,

                image_url
            )
        )

        conn.commit()

        # =================================
        # CAROUSEL
        # =================================

        carousel = [

            {

                "title": "Problem",

                "text": "Many people ignore routine healthcare tests."
            },

            {

                "title": "Risk",

                "text": "Late diagnosis increases health complications."
            },

            {

                "title": "Solution",

                "text": "Regular diagnostics improve prevention."
            },

            {

                "title": "Benefits",

                "text": "Fast reports and accurate insights."
            },

            {

                "title": "CTA",

                "text": "Book your healthcare test today."
            }
        ]
        carousel_images = []

for index, slide in enumerate(carousel):

    slide_img = Image.new(

        "RGB",

        (1080, 1080),

        color=theme[template]["bg"]
    )

    slide_draw = ImageDraw.Draw(slide_img)

    # HEADER

    slide_draw.rectangle(

        [(0, 0), (1080, 180)],

        fill=header_color
    )

    slide_draw.text(

        (80, 60),

        f"SLIDE {index + 1}",

        fill="white",

        font=title_font
    )

    # MAIN CARD

    slide_draw.rounded_rectangle(

        [(80, 240), (1000, 860)],

        radius=40,

        fill=(255, 255, 255)
    )

    # TITLE

    slide_draw.text(

        (140, 340),

        slide["title"],

        fill=header_color,

        font=title_font
    )

    # TEXT

    slide_draw.text(

        (140, 500),

        slide["text"],

        fill=(40, 40, 40),

        font=text_font
    )

    # FOOTER

    slide_draw.rectangle(

        [(0, 940), (1080, 1080)],

        fill=theme[template]["bg"]
    )

    slide_draw.text(

        (280, 990),

        "@AI SOCIAL MEDIA GENERATOR",

        fill="white",

        font=small_font
    )

    slide_filename = (

        f"slide_{index}_{timestamp}.png"
    )

    slide_filepath = os.path.join(

        CAROUSEL_FOLDER,

        slide_filename
    )

    slide_img.save(slide_filepath)

    carousel_images.append(

        f"http://127.0.0.1:5003/generated_carousels/{slide_filename}"
    )

        # =================================
        # RESPONSE
        # =================================

        return jsonify({

            "avatar_video": video_url,

            "success": True,

            "content": generated_text,

            "image": image_url,

            "carousel": carousel,

            "style": style
        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)
        })

# =========================================
# RUN APP
# =========================================

if __name__ == "__main__":

    app.run(

        debug=True,

        port=5003
    )