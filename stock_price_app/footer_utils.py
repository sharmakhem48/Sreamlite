import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb



def footer_content(text, **style):
    return div(style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 70px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="green", 
        text_align="center",
        height="auto",
        opacity=1, 
    )
    body = p()
    foot = div(
        style=style_div
    )(
        body
    )


    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)
    
    
def footer():
    myargs = [
    "Created by ",
    br(),
    footer_content("Khem Sharma")
    ]
    layout(*myargs)