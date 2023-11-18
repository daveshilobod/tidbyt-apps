load("http.star", "http")
load("render.star", "render")

def fetch_kilauea_update():
    url = "https://www.usgs.gov/programs/VHP/volcano-updates#elevated"

    # fetch html content
    response = http.get(url)
    if response.status_code != 200:
        return "HTTP Error: Status Code " + str(response.status_code), False

    # use body() method to get the response content as a string
    html_text = response.body()

    # parsing to find Kilauea update
    start_marker = "<b>Kilauea</b>"
    end_marker = "</div>"
    start_index = html_text.find(start_marker)
    if start_index != -1:
        end_index = html_text.find(end_marker, start_index)
        if end_index != -1:
            update_text = html_text[start_index:end_index].strip()
            # remove html tags
            update_text = update_text.replace("<b>", "").replace("</b>", "")
            return update_text, True
    return "Kīlauea status not found", True

def main(config):
    kilauea_status, use_marquee = fetch_kilauea_update()

    # Layout design
    if use_marquee:
        extended_status = kilauea_status + " " * 64  # trying to slow down the scroll

        content_widget = render.Marquee(
            width=64,
            child=render.Text(extended_status, color="#ffffff"),
            scroll_direction='horizontal'
        )
    else:
        content_widget = render.WrappedText(content=kilauea_status, width=64, color="#ffffff")

    return render.Root(
        child=render.Column(
            children=[
                render.Text("KILAUEA UPDATE", color="#ff0000"),
                content_widget,
            ],
            main_align="center",
        )
    )
