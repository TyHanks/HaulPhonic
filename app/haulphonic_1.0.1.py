import flet as ft
from core.main import page_config, info

def main(page: ft.page):

    #-DATA- Window and page configuration
    page_config(page, ft)

    #::FUNCTION:: Cleans the window and input back to startup
    def add_new(e):
        page.clean()
        user_input = ft.TextField(label="Enter Youtube share url")
        page.add(user_input, ft.ElevatedButton("Retrieve Url", on_click=retrieve_url))

    #::FUNCTION:: Retrieves Url from user and outputs updated window
    def retrieve_url(e):

        #-INFO- Error handling for blank input
        #-TODO- Add error handling for Youtube urls only
        if not user_input.value:
            user_input.error_text = "Please enter Youtube Url"
            page.update()
        else:
            url = user_input.value
            user_link = info(url)

            #-INFO- Displays all the url info to user panel
            page.add(ft.Divider(height = 2, color = '#03719C'))
            page.add(ft.Text(f"Title: {user_link.title}"))
            page.add(ft.Text(f"Views: {user_link.views}"))
            page.add(ft.Text(f"Time: {user_link.length} seconds"))
            page.add(ft.Text(f"Description: {user_link.description}"))
            page.add(ft.Text(f"Rating: {user_link.rating}"))

            #::FUNCTION:: Download best audio file available
            def download_phonic(e):
                audio = user_link.streams.get_audio_only()
                audio.download(output_path="app/core/audio/")

            #-INFO- Download and start over buttons
            page.add(ft.ElevatedButton("Download", on_click=download_phonic))
            page.add(ft.ElevatedButton("Start Over", on_click=add_new))

    #-INFO- Displays main display screen
    user_input = ft.TextField(label="Enter Youtube share url")
    page.add(user_input, ft.ElevatedButton("Retrieve Url", on_click=retrieve_url))

ft.app(target=main)