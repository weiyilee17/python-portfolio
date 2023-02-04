from streamlit import columns, image, title, write, set_page_config, info, header
from pandas import read_csv

set_page_config(layout='wide')

photo_column, self_introduction_column = columns(2)

with photo_column:
    image('images/photo.png')

with self_introduction_column:
    title('Weiyi Lee')
    self_introduction = """
    Hi! I'm Lee. I'm a React front end engineer working in LITEON. 
    I have experience building mid-large scale web sites using React, TypeScript, redux, redux-saga, and webpack. 
    Currently I'm learning Python. The photo on the left is Ardit Sulce, my Python teacher.
    """
    info(self_introduction)

app_introduction = """
Below you can find some of the apps I've built in Python. Feel free to contact me! 
Place holders to see if they can pass the limit of the photo above.
"""

write(app_introduction)

# list of numbers representing the ratio of columns width
app_left_hand_side_column, empty_column, app_right_hand_side_column = columns([3, 1, 3])

apps = read_csv(filepath_or_buffer='data.csv', sep=';')

for index, row in apps.iterrows():
    if index % 2 == 0:
        with app_left_hand_side_column:
            header(row['title'])
            write(row['description'])
            image(f"images/{row['image']}")
            write(f"[Source Code]({row['url']})")
    else:
        with app_right_hand_side_column:
            header(row['title'])
            write(row['description'])
            image(f"images/{row['image']}")
            write(f"[Source Code]({row['url']})")


