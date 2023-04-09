import urllib.request

# Get the next node of the linked list
def get_next_node (cur_node):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % (cur_node)
    with urllib.request.urlopen(url) as response:
        content = response.read()       # Get the bytes of the page
        html = content.decode("utf8")   # Decode to UTF-8
        #print(html)
        next_node = html.split()[-1]
        return next_node

def print_html (cur_node):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % (cur_node)
    with urllib.request.urlopen(url) as response:
        content = response.read()       # Get the bytes of the page
        html = content.decode("utf8")   # Decode to UTF-8
        print(html)

# First part
cur_node = "12345"
for i in range(400):
    next_node = get_next_node(cur_node)
    print("[i = %d] Next node is %s" % (i, next_node))
    if (next_node == "going."):
        break
    cur_node = next_node

# Second part
cur_node = str(16044/2)     # First part end of the trail: we need to divide the nothing content by 2
for i in range(400):
    next_node = get_next_node(cur_node)
    print("[i = %d] Next node is %s" % (i, next_node))
    if (next_node == "peak.html"):
        break
    cur_node = next_node

print_html(cur_node)

# Answer: peak.html