from pytube import YouTube

#-INFO- ::FUNCTION:: Main Window and Page configuration settings
def page_config(page, ft):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "HaulPhonics v1.0.1"
    page.window_height = 400
    page.window_width = 600
    page.bgcolor = '#343837'

def info(url):
    user_link = YouTube(url)
    return user_link
