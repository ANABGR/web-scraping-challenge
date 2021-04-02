
def scrape():
name_of_dict = {}
<scrape code from jupyter notebook>
return name_of_dict



# # NASA Mars News

# In[5]:


# URL of page to be scraped
url = "https://mars.nasa.gov/news/"


# In[6]:


# Retrieve page with the requests module
response = requests.get(url)


# In[7]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[8]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[9]:



# Retrieve the latest news title
news_title=soup.find_all('div', class_='content_title')[0].text
# Retrieve the latest news paragraph
news_p=soup.find_all('div', class_='rollover_description_inner')[0].text
news_title
news_p


# # JPL Mars Space Images - Featured Image

# In[18]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[19]:


url = 'https://spaceimages-mars.com/#'
browser.visit(url)


# In[21]:


html_image = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_image, "html.parser")

# Retrieve background-image url from style tag 
image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

# Website Url 
main_url = "https://www.jpl.nasa.gov"

# Concatenate website url with scrapped route
image_url = main_url + image_url

# Display full link to featured image
image_url


# # Mars Facts

# In[22]:



# Visit the Mars Facts webpage and use Pandas to scrape the table
url_facts = "https://space-facts.com/mars/"

# Use Pandas - read_html - to scrape tabular data from a page
mars_facts = pd.read_html(url_facts)
mars_facts


# In[23]:



mars_df = mars_facts[0]

# Create Data Frame
mars_df.columns = ["Description", "Value"]

# Set index to Description
mars_df.set_index("Description", inplace=True)

# Print Data Frame
mars_df


# In[24]:



# Save html code to folder Assets
html_table = mars_df.to_html()

# Strip unwanted newlines to clean up the table
html_table.replace("\n", '')

# Save html code
mars_df.to_html("mars_facts_data.html")


# # Mars Hemispheres

# In[25]:


# Visit the USGS Astrogeology Science Center url through splinter
url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_hemisphere)


# In[27]:



# HTML Object
html_hemisphere = browser.html
soup = BeautifulSoup(html_hemisphere, "html.parser")


# In[29]:



# Scrape all items that contain mars hemispheres information
hemispheres = soup.find_all("div", class_="item")

# Create empty list
hemispheres_info = []

# Sign main url for loop
hemispheres_url = "https://astrogeology.usgs.gov"

# Loop through the list of all hemispheres information
for i in hemispheres:
    title = i.find("h3").text
    hemispheres_img = i.find("a", class_="itemLink product-item")["href"]
    
    # Visit the link that contains the full image website 
    browser.visit(hemispheres_url + hemispheres_img)
    
    # HTML Object
    image_html = browser.html
    web_info = BeautifulSoup(image_html, "html.parser")
    
    # Create full image url
    img_url = hemispheres_url + web_info.find("img", class_="wide-image")["src"]
    
    hemispheres_info.append({"title" : title, "img_url" : img_url})

# Display titles and images ulr
#hemispheres_info

# Or Display titles and images ulr this way
    print("")
    print(title)
    print(img_url)
    print("-----------------------------------------")


# In[ ]:




