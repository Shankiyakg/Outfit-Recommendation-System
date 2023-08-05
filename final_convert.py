import os
from bs4 import BeautifulSoup

# path to the HTML file
html_path = 'C:/Users/DELL/Downloads/Outfit Recommendation System/recommendation_system.html'

# create a new directory to store the images
img_dir = 'C:/Users/DELL/Downloads/Outfit Recommendation System/images'
os.makedirs(img_dir, exist_ok=True)

# open the HTML file and parse it with BeautifulSoup
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('img')

# iterate through the image tags and append each image tag to a single HTML file
output_html = '<html><body>'
for img_tag in img_tags:
    # get the image source URL
    img_src = img_tag['src']
    # create a new image tag with the same source URL
    new_img_tag = BeautifulSoup(f'<img src="{img_src}">', 'html.parser').img
    # append the new image tag to the output HTML
    
    output_html += str(new_img_tag)
output_html += '</body></html>'

# write the output HTML to a file
output_file = os.path.join(img_dir, 'all_images18.html')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(output_html)