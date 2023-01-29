from streamlit import columns, image, title, info, set_page_config, info

set_page_config(layout='wide')

left_column, right_column = columns(2)

with left_column:
    image('images/photo.png')

with right_column:
    title('Weiyi Lee')
    self_introduction = """
    Hi! I'm Lee. I'm a React front end engineer working in LITEON. 
    I have experience building mid-large scale web sites using React, TypeScript, redux, redux-saga, and webpack. 
    Currently I'm learning python. The photo on the left is Ardit Sulce, my python teacher.
    """
    info(self_introduction)

