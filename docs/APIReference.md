### Rendering YouTube Videos

#### Example

```python
from IPYNCRENDERERBYDIP import render_Youtube_videos

URL = "https://youtu.be/roO5VGxOw2s"
render_Youtube_videos(URL=URL, width=780, height=480)
```

This example demonstrates how to render a YouTube video in a Jupyter Notebook using the `render_Youtube_videos` function from the `IPYNCRENDERERBYDIP` package.

#### Arguments

- `URL` (str): The input URL of a YouTube video as a string.
- `height` (int): The height of the video to display in the Jupyter Notebook. Defaults to 720.
- `width` (int): The width of the video to display in the Jupyter Notebook. Defaults to 600.

#### Returns

- `Response` (str): Either "success" if the rendering was successful or "InvalidURLException" if the provided URL is invalid.

### Rendering Reference Website

#### Example

```python
from IPYNBrenderer import render_site

URL = "http://pytorch.org/"
render_site(URL=URL, width="90%", height="500")
```

This example illustrates how to render a website in a Jupyter Notebook using the `render_site` function from the `IPYNBrenderer` package.

#### Arguments

- `URL` (str): The input URL of a website as a string.
- `height` (str): The height of the website to display in the Jupyter Notebook. Defaults to "600".
- `width` (str): The width of the website to display in the Jupyter Notebook. Defaults to "100%".

#### Returns

- `Response` (str): Either "success" if the rendering was successful or "InvalidURLException" if the provided URL is invalid.
```