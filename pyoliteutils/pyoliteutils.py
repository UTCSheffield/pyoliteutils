from js import fetch
import base64
from IPython.display import Image, display
import matplotlib.pyplot as plt
 
async def load_file_into_in_mem_filesystem(url, fn=None):
    """Load a file from a URL into an in-memory filesystem."""
     
    # Create a filename if required
    fn = fn if fn is not None else url.split("/")[-1]
     
    # Fetch file from URL
    res = await fetch(url)
     
    # Buffer it
    buffer = await res.arrayBuffer()
     
    # Write file to in-memory file system
    open(fn, "wb").write(bytes(buffer.valueOf().to_py()))
 
    return fn

def mm(graph):
    graphbytes = graph.encode("utf8")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    display(Image(url="https://mermaid.ink/img/" + base64_string))