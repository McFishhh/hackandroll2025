# import streamlit as st
# from PIL import Image
# import base64
# from io import BytesIO

# st.set_page_config(
#     page_title="Cute Calorie Tracker",
#     page_icon=":doughnut:",
#     layout="wide"
# )

# def set_cute_dark_theme():
#     custom_css = """
#     <style>
#     .stApp {
#         background-color: #000000 !important; 
#         font-family: 'Comic Sans MS', cursive, sans-serif;
#         color: #FFFFFF;
#     }

#     /* Title in pastel pink with a soft glow */
#     .title-style {
#         color: #FF99CC;  
#         text-align: center;
#         font-size: 3rem;
#         margin-top: 20px;
#         margin-bottom: 30px;
#         text-shadow: 0 0 8px #FF99CC;
#     }

#     /* Card container with text-align center */
#     .food-card {
#         /*background-color: #1A1A1A;
#         border-radius: 15px;
#         padding: 10px;
#         margin-bottom: 20px;*/
#         text-align: center;  /* Ensure all text is centered */
#         /*border: 2px dashed #FF99CC;*/
#         box-shadow: 0 0 10px rgba(255,153,204,0.1);
#     }

#     .food-card p {
#         margin: 0 auto;
#         display: block;
#         text-align: center;
#     }

#     /* Food title in a slightly brighter pink */
#     .food-title {
#         color: #FFC0DB;
#         font-size: 1.2rem;
#         font-weight: bold;
#         margin: 10px 0 5px 0;
#         text-shadow: 0 0 5px #FFC0DB;
#         text-align: center;
#     }

#     .food-calories {
#         color: #FFFFFF;
#         font-size: 1rem;
#         margin: 5px 0;
#         text-align: center;
#     }

#     /* Pastel pink button with black text */
#     .eat-button button {
#         background-color: #FFBEE8 !important; 
#         color: #000000 !important;
#         border-radius: 10px !important;
#         border: 2px solid #FF99CC !important;
#         font-size: 1rem !important;
#         font-weight: bold !important;
#         padding: 6px 12px !important;
#         cursor: pointer !important;
    
        
        
        
#     }
#     .eat-button button:hover {
#         background-color: #FF99CC !important;
#         color: #000 !important;
    
        
#     }

#     /* Status or message style */
#     .info-style {
#         text-align: center;
#         color: #fff;
#         padding: 10px 20px;
#         border-radius: 10px;
#         display: inline-block;
#         margin-top: 20px;
#         background-color: rgba(255,153,204,0.2);
#         box-shadow: 0 0 10px rgba(255,153,204,0.3);
#     }
#     </style>
#     """
#     st.markdown(custom_css, unsafe_allow_html=True)

# def to_base64(pil_img):
#     """Convert a PIL image to base64-encoded PNG."""
#     buf = BytesIO()
#     pil_img.save(buf, format="PNG")
#     data = base64.b64encode(buf.getvalue()).decode('utf-8')
#     return data

# def load_image(image_path):
#     """Load a local image (as PIL) without resizing it yet."""
#     return Image.open(image_path)

# def load_and_resize(image_path, size=(250, 250)):
#     """Load a local image with Pillow, resize, then return it."""
#     img = Image.open(image_path)
#     return img.resize(size)

# # Apply our dark + cute theme
# set_cute_dark_theme()

# # Initialize the calorie counter if not done
# if "calories" not in st.session_state:
#     st.session_state.calories = 0

# # -- Load your images for the food items (resized to 250x250) --
# pizza_img    = load_and_resize("pizzaz.jpg")
# burger_img   = load_and_resize("borger.png")
# donut_img    = load_and_resize("donut.jpeg")
# fries_img    = load_and_resize("fries.jpg")
# icecream_img = load_and_resize("icecream.jpg")
# soda_img     = load_and_resize("soda.jpeg")


# food_items = [
#     {
#         "name": "Pizza Slice",
#         "calories": 285,
#         "img_b64": to_base64(pizza_img)
#     },
#     {
#         "name": "Burger",
#         "calories": 354,
#         "img_b64": to_base64(burger_img)
#     },
#     {
#         "name": "Soda (12oz)",
#         "calories": 140,
#         "img_b64": to_base64(soda_img)
#     },
#     {
#         "name": "French Fries (med)",
#         "calories": 312,
#         "img_b64": to_base64(fries_img)
#     },
#     {
#         "name": "Donut",
#         "calories": 195,
#         "img_b64": to_base64(donut_img)
#     },
#     {
#         "name": "Ice Cream (1 scoop)",
#         "calories": 137,
#         "img_b64": to_base64(icecream_img)
#     },
# ]

# # --- Load the fat man & explosion images (not resized) ---
# # Make sure these are in the same directory
# fat_man_img = load_image("fatman.jpg")
# explosion_img = load_image("explosion.gif")  # or .gif

# # Convert them to base64
# fat_man_b64 = to_base64(fat_man_img)
# explosion_b64 = to_base64(explosion_img)

# # --- Page Title ---
# st.markdown("<h1 class='title-style'>Cute Calorie Tracker</h1>", unsafe_allow_html=True)

# # --- Food item display in rows of 3 columns ---
# for i in range(0, len(food_items), 3):
#     cols = st.columns(3)
#     for idx, col in enumerate(cols):
#         if i + idx < len(food_items):
#             item = food_items[i + idx]
#             with col:
#                 st.markdown("<div class='food-card'>", unsafe_allow_html=True)
                
#                 # Insert centered <img> for the food item
#                 img_html = f"""
#                 <img 
#                     src="data:image/png;base64,{item['img_b64']}" 
#                     style="display:block; margin: 0 auto;" 
#                     width="250" height="250"
#                 />
#                 """
#                 st.markdown(img_html, unsafe_allow_html=True)

#                 st.markdown(f"<p class='food-title'>{item['name']}</p>", unsafe_allow_html=True)
#                 st.markdown(f"<p class='food-calories'>{item['calories']} cal per serving</p>", unsafe_allow_html=True)

#                 # Eat button increments the calorie count
#                 button_label = f"Eat (+{item['calories']})"
#                 if st.button(button_label, key=f"eat_{item['name']}", help=f"Add {item['calories']} calories"):
#                     st.session_state.calories += item['calories']

#                 st.markdown("</div>", unsafe_allow_html=True)

# # --- Display the Fat Man or Explosion depending on calories ---
# total_cals = st.session_state.calories

# # A fraction in [0..1] to scale the fat man from 100px width to 500px width
# # At 0 calories -> width = 100
# # At 2000 calories -> width = 500
# min_width = 100
# max_width = 500
# fraction = min(total_cals / 2000, 1.0)
# fat_width = int(min_width + (max_width - min_width) * fraction)

# if total_cals <= 2000:
#     # Show the scaled fat man
#     scale_html = f"""
#     <div style="text-align:center; margin-top:30px;">
#       <img 
#         src="data:image/png;base64,{fat_man_b64}"
#         width="{fat_width}"
#         style="border: 2px dashed #FF99CC; border-radius:10px;"
#       />
#     </div>
#     """
#     st.markdown(scale_html, unsafe_allow_html=True)
# else:
#     # Show the explosion
#     explode_html = f"""
#     <div style="text-align:center; margin-top:30px;">
#       <img 
#         src="data:image/png;base64,{explosion_b64}"
#         width="400"
#         style="border: 2px dashed #FF99CC; border-radius:10px;"
#       />
#     </div>
#     """
#     st.markdown(explode_html, unsafe_allow_html=True)

# # --- Display the dynamic calorie status ---
# if total_cals > 2000:
#     status_message = "you're fat! (he exploded!)"
# else:
#     status_message = f"Total Calories: {total_cals}"

# info_html = f"""
# <p class="info-style" style="font-size:1.4rem; text-align:center;">
#   {status_message}
# </p>
# """
# st.markdown(info_html, unsafe_allow_html=True)

import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(
    page_title="Cute Calorie Tracker",
    page_icon=":doughnut:",
    layout="wide"
)

def set_cute_dark_theme():
    custom_css = """
    <style>
    .stApp {
        background-color: #000000 !important; 
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #FFFFFF;
    }

    /* Title in pastel pink with a soft glow */
    .title-style {
        color: #FF99CC;  
        text-align: center;
        font-size: 3rem;
        margin-top: 20px;
        margin-bottom: 30px;
        text-shadow: 0 0 8px #FF99CC;
    }

    /* Card container with text-align center */
    .food-card {
        /*background-color: #1A1A1A;
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 20px;*/
        text-align: center;  /* Ensure all text is centered */
        /*border: 2px dashed #FF99CC;*/
        box-shadow: 0 0 10px rgba(255,153,204,0.1);
    }

    .food-card p {
        margin: 0 auto;
        display: block;
        text-align: center;
    }

    /* Food title in a slightly brighter pink */
    .food-title {
        color: #FFC0DB;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 10px 0 5px 0;
        text-shadow: 0 0 5px #FFC0DB;
        text-align: center;
    }

    .food-calories {
        color: #FFFFFF;
        font-size: 1rem;
        margin: 5px 0;
        text-align: center;
    }

    /* Pastel pink button with black text */
    .eat-button button {
        background-color: #FFBEE8 !important; 
        color: #000000 !important;
        border-radius: 10px !important;
        border: 2px solid #FF99CC !important;
        font-size: 1rem !important;
        font-weight: bold !important;
        padding: 6px 12px !important;
        cursor: pointer !important;
    }
    .eat-button button:hover {
        background-color: #FF99CC !important;
        color: #000 !important;
    }

    /* 
       1) Specifically center the st.button inside .stButton
       2) Also ensure it is centered within .food-card if nested 
    */
    .food-card .stButton button {
        margin: 0 auto !important; 
        display: block !important;
    }

    /* Status or message style */
    .info-style {
        text-align: center;
        color: #fff;
        padding: 10px 20px;
        border-radius: 10px;
        display: inline-block;
        margin-top: 20px;
        background-color: rgba(255,153,204,0.2);
        box-shadow: 0 0 10px rgba(255,153,204,0.3);
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def to_base64(pil_img):
    """Convert a PIL image to base64-encoded PNG."""
    buf = BytesIO()
    pil_img.save(buf, format="PNG")
    data = base64.b64encode(buf.getvalue()).decode('utf-8')
    return data

def load_image(image_path):
    """Load a local image (as PIL) without resizing it yet."""
    return Image.open(image_path)

def load_and_resize(image_path, size=(250, 250)):
    """Load a local image with Pillow, resize, then return it."""
    img = Image.open(image_path)
    return img.resize(size)

# Apply our dark + cute theme
set_cute_dark_theme()

# Initialize the calorie counter if not done
if "calories" not in st.session_state:
    st.session_state.calories = 0

# -- Load your images for the food items (resized to 250x250) --
pizza_img    = load_and_resize("pizzaz.jpg")
burger_img   = load_and_resize("borger.png")
donut_img    = load_and_resize("donut.jpeg")
fries_img    = load_and_resize("fries.jpg")
icecream_img = load_and_resize("icecream.jpg")
soda_img     = load_and_resize("soda.jpeg")


food_items = [
    {
        "name": "Pizza Slice",
        "calories": 285,
        "img_b64": to_base64(pizza_img)
    },
    {
        "name": "Burger",
        "calories": 354,
        "img_b64": to_base64(burger_img)
    },
    {
        "name": "Soda (12oz)",
        "calories": 140,
        "img_b64": to_base64(soda_img)
    },
    {
        "name": "French Fries (med)",
        "calories": 312,
        "img_b64": to_base64(fries_img)
    },
    {
        "name": "Donut",
        "calories": 195,
        "img_b64": to_base64(donut_img)
    },
    {
        "name": "Ice Cream (1 scoop)",
        "calories": 137,
        "img_b64": to_base64(icecream_img)
    },
]

# --- Load the fat man & explosion images (not resized) ---
fat_man_img = load_image("fatman.jpg")
explosion_img = load_image("explosion.gif")

# Convert them to base64
fat_man_b64 = to_base64(fat_man_img)
explosion_b64 = to_base64(explosion_img)

# --- Page Title ---
st.markdown("<h1 class='title-style'>Cute Calorie Tracker</h1>", unsafe_allow_html=True)

# --- Food item display in rows of 3 columns ---
for i in range(0, len(food_items), 3):
    cols = st.columns(3)
    for idx, col in enumerate(cols):
        if i + idx < len(food_items):
            item = food_items[i + idx]
            with col:
                st.markdown("<div class='food-card'>", unsafe_allow_html=True)
                
                # Insert centered <img> for the food item
                img_html = f"""
                <img 
                    src="data:image/png;base64,{item['img_b64']}" 
                    style="display:block; margin: 0 auto;" 
                    width="250" height="250"
                />
                """
                st.markdown(img_html, unsafe_allow_html=True)

                st.markdown(f"<p class='food-title'>{item['name']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='food-calories'>{item['calories']} cal per serving</p>", unsafe_allow_html=True)

                # Eat button increments the calorie count
                button_label = f"Eat (+{item['calories']})"
                if st.button(button_label, key=f"eat_{item['name']}", help=f"Add {item['calories']} calories"):
                    st.session_state.calories += item['calories']

                st.markdown("</div>", unsafe_allow_html=True)

# --- Display the Fat Man or Explosion depending on calories ---
total_cals = st.session_state.calories
min_width = 100
max_width = 500
fraction = min(total_cals / 2000, 1.0)
fat_width = int(min_width + (max_width - min_width) * fraction)

if total_cals <= 2000:
    # Show the scaled fat man
    scale_html = f"""
    <div style="text-align:center; margin-top:30px;">
      <img 
        src="data:image/png;base64,{fat_man_b64}"
        width="{fat_width}"
        style="border: 2px dashed #FF99CC; border-radius:10px;"
      />
    </div>
    """
    st.markdown(scale_html, unsafe_allow_html=True)
else:
    # Show the explosion
    explode_html = f"""
    <div style="text-align:center; margin-top:30px;">
      <img 
        src="data:image/png;base64,{explosion_b64}"
        width="400"
        style="border: 2px dashed #FF99CC; border-radius:10px;"
      />
    </div>
    """
    st.markdown(explode_html, unsafe_allow_html=True)

# --- Display the dynamic calorie status ---
if total_cals > 2000:
    status_message = "you're fat! (he exploded!)"
else:
    status_message = f"Total Calories: {total_cals}"

info_html = f"""
<p class="info-style" style="font-size:1.4rem; text-align:center;">
  {status_message}
</p>
"""
st.markdown(info_html, unsafe_allow_html=True)