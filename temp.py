import streamlit as st
from PIL import Image
from datetime import datetime
import os


st.set_page_config(
    page_title="Our Story ❤️",
    page_icon="❤️",
    layout="wide"
)

# --------------------------
# CUSTOM CSS
# --------------------------

st.markdown("""
<style>

.big-title {
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#ff4b6e;
}

.subtitle {
    text-align:center;
    font-size:28px;
    color:#888;
}

.center-text {
    text-align:center;
    font-size:24px;
    font-weight:500;
}

div.stButton > button {
    width:100%;
    height:60px;
    font-size:22px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# COVER IMAGE
# --------------------------

cover_path = "photos/cover.jpeg"

if os.path.exists(cover_path):

    col1, col2, col3 = st.columns([3, 2, 3])

    with col2:
        st.image(cover_path, width=350)

# --------------------------
# TITLE
# --------------------------

st.markdown(
    """
    <div class='big-title'>
        ❤️ 5 May 2026 • 1:22 AM ❤️
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='subtitle'>
        The minute my life changed forever.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <div class='center-text'>
        Happy One Month My Labaad ❤️
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# --------------------------
# SONG
# --------------------------

st.subheader("🎵 Our Song")

if os.path.exists("music/our_song.mp3"):
    audio_file = open("music/our_song.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)

st.write("")
st.write("")

# --------------------------
# BUTTON
# --------------------------

st.success("👇 Scroll Down To Continue Our Story ❤️")

# --------------------------
# RELATIONSHIP TIMER
# --------------------------

st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='text-align:center; color:#ff4b6e;'>
    ❤️ We've Been Together For ❤️
    </h1>
    """,
    unsafe_allow_html=True
)

start_date = datetime(2026, 5, 5, 1, 22)

now = datetime.now()

difference = now - start_date

days = difference.days
hours = difference.seconds // 3600
minutes = (difference.seconds % 3600) // 60
seconds = difference.seconds % 60

col1, col2, col3, col4 = st.columns(4)

col1.metric("Days ❤️", days)
col2.metric("Hours ❤️", hours)
col3.metric("Minutes ❤️", minutes)
col4.metric("Seconds ❤️", seconds)

# --------------------------
# THE MOMENT
# --------------------------

st.write("")
st.write("")

st.markdown(
    """
    <h1 style='text-align:center; color:#ff4b6e;'>
    ❤️ The Moment ❤️
    </h1>
    """,
    unsafe_allow_html=True
)

st.info(
    """
❤️ 5 May 2026 • 1:22 AM ❤️

Some people remember birthdays.

Some people remember anniversaries.

I remember 1:22 AM.

Because that was the moment my Labaad became my girlfriend.

The minute my life changed forever. ❤️
"""
)


# --------------------------
# OK JAANU NIGHT
# --------------------------

st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='text-align:center; color:#ff4b6e;'>
    🌙 The Night I'll Never Forget 🌙
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
### 🎬 25 May 2026

From **12:00 AM** to **5:45 AM**

We stayed together on a video call for almost six hours.

That night we watched **Ok Jaanu** together.

Even though we were feeling sleepy,
neither of us wanted the night to end.

Six hours still felt too short.

For the world it was just a movie.

For me it became one of the most beautiful memories of my life. ❤️
"""
)

st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1;
max-width:1000px;
border:3px solid #ff4b6e;
margin:30px 0;
">

❤️ Dear Jaanu,<br><br>

That night taught me something.<br><br>

Distance can separate two people physically,<br><br>

but it can never separate two hearts that truly love each other.<br><br>

❤️

</div>
""", unsafe_allow_html=True)



st.markdown("""
<div style="
background:#1c1024;
padding:15px;
border-radius:20px;
color:#ffd6e7;
font-size:15px;
line-height:1;
border:3px solid #ff4b6e;
max-width:1000px;
margin:30px 0;
">

🎥 <b>Memory Saved Successfully</b><br><br>

📅 <b>Date:</b> 25 May 2026<br><br>

🕛 <b>Time:</b> 12:00 AM – 5:45 AM<br><br>

🎬 <b>Movie:</b> Ok Jaanu ❤️<br><br>

♾️ <b>Status:</b> One of my favorite memories forever

</div>
""", unsafe_allow_html=True)




st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='color:#ff4b6e;'>
    👻 How We Started
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<div style="
background:#1c1024;
padding:15px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.7;
border:3px solid #ff4b6e;
max-width:900px;
margin:30px 0;
">

👻 Our story started on Snapchat.

At that time, I had absolutely no idea that a simple conversation starting with a "Hey" would eventually become one of the most beautiful chapters of my life.

What started as random chats slowly turned into daily conversations, endless laughter, late-night talks, unforgettable memories, and eventually the purest love I have ever experienced.

Some people search their whole lives for a connection that feels genuine.

I got lucky enough to find mine in you. ❤️

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:#1c1024;
padding:15px;
border-radius:20px;
color:#ffd6e7;
font-size:15px;
line-height:1.5;
border:3px solid #ff4b6e;
max-width:900px;
margin:30px 0;
">

✨ Funny how one simple "Hey" on Snapchat became one of the best things that ever happened to me. ❤️

</div>
""", unsafe_allow_html=True)




st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='color:#ff4b6e;'>
    ❤️ What Changed In My Life After My Baby Came
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<div style="
background:#1c1024;
padding:15px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.7;
border:3px solid #ff4b6e;
max-width:900px;
margin:30px 0;
">

❤️ Before you came into my life, I knew what love was only from movies and stories.

After meeting you, I finally understood what true love, pure intentions, loyalty, care, trust and genuine affection actually feel like.

Even though we are in a long-distance relationship, you somehow make me feel closer than anyone else ever has.

You came into my life when I wasn't looking for anything except genuine love.

And somehow, you gave me exactly that.

You filled my life with happiness, comfort, peace, understanding and a kind of love that I never knew existed.

You didn't just become a part of my life.

You changed it. ❤️

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="
background:#1c1024;
padding:15px;
border-radius:20px;
color:#ffd6e7;
font-size:15px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:30px 0;
">

🌸 Sometimes the right person doesn't just enter your life.

They make your life feel complete. ❤️

</div>
""", unsafe_allow_html=True)



st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='color:#ff4b6e;'>
    🥹 What I Love Most About My Baby
    </h1>
    """,
    unsafe_allow_html=True
)



st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

😊 <b>Your Smile</b><br><br>

Your smile has a special power.

No matter how bad my day is,
seeing you smile instantly makes everything feel better.

❤️

</div>
""", unsafe_allow_html=True)



st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

🥹 <b>Your Blush</b><br><br>

I love when you blush.

I don't know why,
but every time it happens,
it becomes one of the cutest things in the world to me.

❤️

</div>
""", unsafe_allow_html=True)



st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

💖 <b>You Share Everything With Me</b><br><br>

I love that you tell me about your happy days,
your bad days,
your random thoughts,
and even the smallest moments.

It makes me feel trusted,
and that means everything to me.

❤️

</div>
""", unsafe_allow_html=True)




st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

🫂 <b>Your Trust</b><br><br>

I love that you trust me enough to tell me everything.

Your trust is one of the most precious things I have ever received.

And I promise to always protect it.

❤️

</div>
""", unsafe_allow_html=True)




st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

🌸 <b>Making You Feel Safe</b><br><br>

One of the things that makes me happiest
is knowing that you feel safe,
comfortable and loved with me.

That feeling makes me proud every single day.

❤️

</div>
""", unsafe_allow_html=True)




st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

❤️ <b>Your Happiness</b><br><br>

Seeing you happy because of me
is one of the best feelings in the world.

Your happiness will always be one of my favorite things.

❤️

</div>
""", unsafe_allow_html=True)



st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='color:#ff4b6e;'>
    ❤️ The Many Names Of My Favorite Person ❤️
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.7;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

To the world, you are one person.

But to me, you are many beautiful things.

Every nickname I call you has a story.

Every nickname carries a piece of my heart. ❤️

</div>
""", unsafe_allow_html=True)



st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

😏 <b>Labaad</b><br><br>

Because you're mischievous.

You tease me.

You make me angry.

And then you smile while watching me melt completely.

❤️

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

😚❤️ <b>Baby</b><br><br>

Because that's my love language.

Whenever I think about you,

the first name that comes to my heart is Baby.

❤️

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

🎬❤️ <b>Jaanu</b><br><br>

Because of that magical Ok Jaanu night.

A movie became a memory.

And that memory became a part of us.

❤️

</div>
""", unsafe_allow_html=True)




st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

🍨💕 <b>Rasmalai</b><br><br>

Because you're sweeter than every sweet dish I know.

Your smile.

Your care.

Your love.

Everything about you adds sweetness to my life.

❤️

</div>
""", unsafe_allow_html=True)



st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

🥹🤍 <b>Mazhi Vedi</b><br><br>

A Marathi word filled with love.

A word for someone who means the world to me.

Someone I love more than words can explain so i call my love "vedi".

❤️

</div>
""", unsafe_allow_html=True)



st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='color:#ff4b6e;'>
    😂 My Favorite Thing About You
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.7;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

😂 One of my favorite things about you is how you purposely try to make me angry.

You tease me.

You annoy me.

You act innocent.

And somehow you enjoy watching my reaction. 😭❤️

But the funniest part?

I can never stay angry at you.

The moment you smile or laugh,

I completely melt.🫠

And then I end up smiling too.

❤️

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

😏 My Labaad has a special talent.

She can make me angry and happy at the same time. ❤️

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.6;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

🫠 Every time you tease me,

I lose the argument,

you win,

and somehow I still feel lucky.🥹💕

❤️

</div>
""", unsafe_allow_html=True)



st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='color:#ff4b6e;'>
    💌 A Letter To My Labaad
    </h1>
    """,
    unsafe_allow_html=True
)



st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.8;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

❤️ My Labaad,

Thank you for coming into my life when I was searching for nothing except genuine love.

You didn't just bring love.

You poured it into my life every single day.

<br><br>

Thank you for understanding my emotions, my anger, my efforts, my loyalty and my heart.

Thank you for listening to my endless talks.

Thank you for supporting me during difficult days.

Thank you for guiding me whenever I needed someone beside me.

<br><br>

Even when you're having a bad day yourself, you still somehow find the strength to care about me and make sure I'm okay.

That is something I will never take for granted.

<br><br>

The truth is...

I could keep writing forever and still not be able to explain how important you are to me.

No paragraph.

No website.

No amount of words.

Could ever fully describe what you mean to me.

<br><br>
            
 Don't ever forget that I Loved You from the first day of our conversation and i will love you forever to the moon till jupiter, wait jupiter is also very small thing to describe how much i love you, I LOVE YOU FROM THE MOON TILL EVERY GALAXY and UNIVERSE which i guess is the most big thing on this universe right? I LOVE YOU INFINITELY. ♾️🧿💓💕🫂🥹😘

<br><br>

You came into my life and made it brighter, happier, safer and more complete.

And for that,

I will always be grateful.

❤️

</div>
""", unsafe_allow_html=True)



st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.8;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

🫂 Thank you for being my Labaad.

💓 Thank you for being my Baby.

💕 Thank you for being my Jaanu.

😘 Thank you for being my Rasmalai.

🥹 Thank you for being my Vedi.

<br><br>

Most importantly...

<br><br>

❤️ Thank you for being mine. ❤️
            
With Love💕, <br>
                       
Your Tirsat🫂💓

</div>
""", unsafe_allow_html=True)




st.markdown("""
<div style="
text-align:center;
padding:40px;
font-size:24px;
color:#ff4b6e;
">

❤️ 5 May 2026 • 1:22 AM ❤️

<br>

The minute my life changed forever. Thankyou for coming into my life.🥹🫂💓

<br><br>

Happy One Month, My Labaad Baby. 🥹💓

<br><br>

🧿♾️ Forever Yours ♾️🧿

</div>
""", unsafe_allow_html=True)




st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='color:#ff4b6e;'>
    📸 Our Memories Gallery
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.7;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

Every photo tells a story.

Every memory holds a feeling.

And every picture here reminds me how lucky I am to have you in my life. ❤️

</div>
""", unsafe_allow_html=True)



st.write("")
st.write("")
st.divider()

st.markdown(
    """
    <h1 style='color:#ff4b6e;'>
    📸 Our Memories Gallery
    </h1>
    """,
    unsafe_allow_html=True
)



st.markdown("""
<div style="
background:#1c1024;
padding:16px;
border-radius:20px;
color:#ffd6e7;
font-size:16px;
line-height:1.7;
border:3px solid #ff4b6e;
max-width:400px;
margin:25px 0;
">

Every photo tells a story.

Every memory holds a feeling.

And every picture here reminds me how lucky I am to have you in my life. ❤️

</div>
""", unsafe_allow_html=True)


gallery = [

    ("photos/photo3.jpeg", "📞 One Of Our Precious Video Calls"),
    ("photos/photo4.jpeg", "💖 Looking At You Makes Me Smile"),
    ("photos/photo5.jpeg", "😊 My Favorite Selfie"),
    ("photos/photo7.jpeg", "🫂 A Memory I Never Want To Forget"),
    ("photos/photo9.jpeg", "👶 Baby Labaad"),
    ("photos/photo1.jpeg", "🥹 The Night We Didn't Felt Asleep especially you"),
    ("photos/photo2.jpeg", "🌻 My Beautiful Girl"),
    ("photos/photo6.jpeg", "🌸 The Smile I Fell In Love With"),
    ("photos/photo8.jpeg", "✨ Just You Being Beautiful"),
    ("photos/photo10.jpeg", "😌 One More Reason I Feel Lucky"),
    ("photos/photo11.jpeg", "♾️ Forever My Favorite Person")
]

for i in range(0, len(gallery), 3):

    cols = st.columns(3)

    for j in range(3):

        if i + j < len(gallery):

            img_path, caption = gallery[i + j]

            with cols[j]:

                img = Image.open(img_path)

                if "photo11.jpeg" in img_path:
                    img = img.rotate(90, expand=True)

                left, center, right = st.columns([1, 3, 1])

                with center:
                    st.image(img, width=280)

                    st.markdown(
                        f"""
                        <div style="
                            text-align:center;
                            font-size:18px;
                            font-weight:bold;
                            color:#ffb6c1;
                            margin-top:12px;
                            margin-bottom:35px;
                        ">
                            {caption}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )



st.markdown("""
<div style="
background:#1c1024;
padding:20px;
border-radius:20px;
color:#ffd6e7;
font-size:20px;
line-height:1.7;
border:3px solid #ff4b6e;
max-width:900px;
margin:25px 0;
">

📸 These are not just photos.

They are pieces of our story.

A story that started with a simple "Hey" and became one of the most beautiful parts of my life.

❤️

</div>
""", unsafe_allow_html=True)
