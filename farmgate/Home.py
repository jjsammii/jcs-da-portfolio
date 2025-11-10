# farmgate/Home.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from pathlib import Path
from typing import Optional
from PIL import Image
import os

# -------------------- App config --------------------
st.set_page_config(page_title="Home", layout="wide")

# -------------------- Single-file path & asset helpers --------------------
BASE_DIR    = Path(__file__).resolve().parent              # .../jcs-da-portfolio/farmgate
REPO_ROOT   = BASE_DIR.parent                              # .../jcs-da-portfolio
IMAGES_DIRS = [BASE_DIR / "images", REPO_ROOT / "images"]  # try farmgate/images, then repo/images
STYLE_DIRS  = [BASE_DIR / "style", REPO_ROOT / "style"]    # try farmgate/style, then repo/style

def find_case_insensitive(directory: Path, filename: str) -> Optional[Path]:
    """Find filename in directory ignoring case; return Path or None."""
    try:
        target = filename.lower()
        if directory.exists():
            for p in directory.iterdir():
                if p.name.lower() == target:
                    return p
    except Exception:
        pass
    return None

def open_image_safe(filename: str) -> Optional[Image.Image]:
    """Open an image by checking multiple candidate directories; warn if missing."""
    for d in IMAGES_DIRS:
        p = find_case_insensitive(d, filename)
        if p and p.is_file():
            try:
                return Image.open(p)
            except Exception as e:
                st.warning(f"Failed to open image '{p.name}' in '{d.relative_to(REPO_ROOT)}': {e}")
                return None
    tried = ", ".join(str(d.relative_to(REPO_ROOT)) for d in IMAGES_DIRS if d.exists())
    st.warning(f"Image '{filename}' not found. Searched: {tried or '(no image dirs present)'}")
    return None

def inject_local_css(filename: str) -> None:
    """Inject CSS from the first directory where it exists; warn if missing."""
    for d in STYLE_DIRS:
        p = d / filename
        if p.is_file():
            try:
                st.markdown(f"<style>{p.read_text()}</style>", unsafe_allow_html=True)
                return
            except Exception as e:
                st.warning(f"Failed to load CSS '{p}': {e}")
                return
    tried = ", ".join(str(d.relative_to(REPO_ROOT)) for d in STYLE_DIRS if d.exists())
    st.warning(f"CSS '{filename}' not found. Searched: {tried or '(no style dirs present)'}")

# -------------------- Network helpers --------------------
def load_lottieurl(url: str):
    """Safely load a Lottie JSON from URL (TLS verify on)."""
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None

# -------------------- Debug panel (toggle with ?debug=1) --------------------
debug = st.query_params.get("debug", ["0"])[0] in {"1", "true", "yes"}
if debug:
    st.info("Debug panel enabled (remove ?debug=1 to hide).")
    st.write("Repo root:", REPO_ROOT.as_posix())
    st.write("Base dir (farmgate):", BASE_DIR.as_posix())
    st.write("CWD:", Path.cwd().as_posix())
    st.write("IMAGES_DIRS:", [p.as_posix() for p in IMAGES_DIRS])
    st.write("STYLE_DIRS:", [p.as_posix() for p in STYLE_DIRS])
    for d in IMAGES_DIRS:
        st.write(f"Contents of {d.relative_to(REPO_ROOT) if d.exists() else d}:", 
                 [p.name for p in d.glob("*")] if d.exists() else "DIR MISSING")
    for d in STYLE_DIRS:
        st.write(f"Contents of {d.relative_to(REPO_ROOT) if d.exists() else d}:", 
                 [p.name for p in d.glob("*")] if d.exists() else "DIR MISSING")

# -------------------- Assets --------------------
lottie_coding = load_lottieurl(
    "https://assets7.lottiefiles.com/private_files/lf30_ijvfbn98.json"
)

# Case-insensitive load; looks in farmgate/images then repo/images
techtalk = open_image_safe("Video.PNG")

# CSS from farmgate/style or repo/style
inject_local_css("style.css")

# -------------------- UI --------------------
st.title("Welcome to Farmgate Dashboard")
st.write("---")
st.sidebar.success("Select a Report Above.")

left_column, right_column = st.columns(2)
with left_column:
    st.write(
        "This dashboard showcases reports in relation to Farmgate data available on Jamis Website "
        "[Web link](https://www.ja-mis.com/companionsite/reportsarchive.aspx)"
    )
    st.write(
        "A prediction report was added to forecast Crop Prices across Jamaica for the next three years (2023 - 2025) "
        "as the last data extracted was done December 2022"
    )
    st.write("**👈 Select a Report from the sidebar menu options and choose the appropriate filters below")
    st.markdown(
        """
        ### Please see details of each dash board listed below?
        - Article: Describes Basic Streamlit deployment, data collection and visualization for JAMIS farmgate data.
        - Dashboard: Interactive dashboard that allows users to manipulate and visualize datasets.
        - Prediction Report: Contains prediction prices for crops for each month with the ability to 
          filter results based on year and parish.
        """
    )
with right_column:
    st_lottie(lottie_coding, height=400, key="crops")

with st.container():
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("---")
    st.header("Youtube Expert Hour")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if techtalk:
            st.image(techtalk)
    with text_column:
        st.subheader("Tech Expert Hour")
        st.write(
            """This Tech Expert illustration shows how to establish data pipelines within the azure cloud platform. 
               In this illustration I'll show you how to build data pipelines and more using azure data factory"""
        )
        st.markdown("[Watch Now...](https://www.youtube.com/watch?v=mWW-OsELCn0&t=1400s)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact Form")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/jc.samuels21@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

# ---- Hide Streamlit chrome ----
st.markdown(
    """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)
