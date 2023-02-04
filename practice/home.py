from streamlit import header, write, columns, set_page_config, title, image
from pandas import read_csv

set_page_config(layout='wide')

header('The Best Company')
write('Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla dolor ab saepe obcaecati repellat iusto error repudiandae nam earum veritatis quia cum, voluptas hic. Beatae cum placeat nesciunt, magnam eaque distinctio eos doloremque dignissimos, dolor et deserunt voluptate maxime similique ipsum modi quod odio veniam delectus est temporibus ab. Tempore.')

title('Our Team')

left_member_column, empty_column_1, middle_member_column, empty_column_2, right_member_column = columns([3, 2, 3, 2, 3])

members = read_csv(filepath_or_buffer='practice/data.csv', sep=',')

with left_member_column:
    for index, singleMember in members[:4].iterrows():
        title(f"{singleMember['first name'].capitalize()} {singleMember['last name'].capitalize()}")
        write(singleMember['role'])
        image(f"practice/images/{singleMember['image']}")

with middle_member_column:
    for index, singleMember in members[4:8].iterrows():
        title(f"{singleMember['first name'].capitalize()} {singleMember['last name'].capitalize()}")
        write(singleMember['role'])
        image(f"practice/images/{singleMember['image']}")

with right_member_column:
    for index, singleMember in members[8:].iterrows():
        title(f"{singleMember['first name'].capitalize()} {singleMember['last name'].capitalize()}")
        write(singleMember['role'])
        image(f"practice/images/{singleMember['image']}")

