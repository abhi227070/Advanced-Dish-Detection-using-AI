from page_components import setup_sidebar, display_header, get_image_input, set_page_config
from dish_analyzer import analyze_dish

# --- Main Execution ---
set_page_config()
api_key = setup_sidebar()
display_header()
uploaded_file = get_image_input()
analyze_dish(api_key, uploaded_file)