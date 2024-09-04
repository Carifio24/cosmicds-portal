from pathlib import Path
from dotenv import load_dotenv

import ipyvuetify as v
import solara
from solara.alias import rv
from solara_enterprise import auth

from ..components.login import Login
from .state import GLOBAL_STATE

v.theme.dark = True

IMG_PATH = Path("static") / "public" / "images"

load_dotenv()


@solara.component
def Hero():
    with rv.Parallax(src=str(IMG_PATH / "opo0006a.jpg")) as hero:
        with rv.Container(style_="max-width: 1200px"):
            with rv.Row():
                with rv.Col(cols=9):
                    # with rv.Container():
                    rv.Html(tag="div", children=["Cosmic Data Stories"],
                            class_="display-4",
                            style_="text-shadow: 1px 1px 8px black")
                    rv.Html(tag="div", children=[
                        "Interactive data stories designed by NASA "
                        "astronomers to inspire learners of all ages "
                        "to explore the universe."], class_="display-1",
                            style_="text-shadow: 1px 1px 8px black")

    return hero




@solara.component
def Page():
    with solara.Row(classes=['fill-height']) as main:
        with solara.Columns([8, 4]):
            with solara.Column():
                solara.Text("Our Mission", classes=["display-1"])
                solara.Markdown(
                    """
    The world is fast-becoming a place driven by data.  To address dire shortages 
    of data-competency in the workforce, industry leaders are calling for 
    educational pathways that teach people how to interact with data.  The Cosmic 
    Data Stories (CosmicDS) project promotes public understanding of data science 
    through engaging, interactive data stories.
    
    The project facilitates connections between astronomers who want to tell the 
    story of a discovery and learners who can interrogate the data behind the 
    story on their own, using easy-to-use but powerful data science and 
    visualization techniques."""
                )

            with solara.Column():
                with rv.Card(flat=True, outlined=True):
                    with rv.CardTitle():
                        solara.Text("Getting Started")

                    with rv.ExpansionPanels(flat=True):
                        with rv.ExpansionPanel():
                            with rv.ExpansionPanelHeader():
                                solara.Text("Why create an account?")

                            with rv.ExpansionPanelContent():
                                solara.Markdown("""
In Cosmic Data Stories, students collect and analyze their own astronomy data. 
Students’ measurements are stored anonymously in the CosmicDS database. Creating an account will:

- Associate student data with their class cohort.
- Allow students to view their results within the context of their class’s dataset and the full participant dataset.
- Keep track of students’ place within the data story if they aren’t able to finish the story within one class period
""")
                        with rv.ExpansionPanel():
                            with rv.ExpansionPanelHeader():
                                solara.Text("How do accounts work?")

                            with rv.ExpansionPanelContent():
                                solara.Markdown("""
Educators complete a brief form to receive a CosmicDS educator key by email.

Educators and Students access the CosmicDS portal and Data Story app by logging 
on through the OAuth authentication service. You can use credentials from 
common services like gmail or microsoft.

Educators enter their educator key to create classroom keys that associates 
students’ accounts with you and their classmates.

""")
                        with rv.ExpansionPanel():
                            with rv.ExpansionPanelHeader():
                                solara.Text("Privacy Policy")

                            with rv.ExpansionPanelContent():
                                solara.Markdown("""
Educator contact information is stored according to 
<link to Harvard privacy policy>. Used for …

Student contact information is anonymized by …
""")

    return main


@solara.component
def Layout(children=[]):
    router = solara.use_router()
    snackbar, set_snackbar = solara.use_state(True)
    route_current, routes = solara.use_route()

    with rv.App(dark=True) as main:
        solara.Title("Cosmic Data Stories")

        with rv.AppBar(elevate_on_scroll=True, app=True):
            with solara.Link(solara.resolve_path("/")):
                rv.Avatar(class_="me-10 ms-4", color="#cccccc", size="32")

            solara.Button("Data Stories", text=True,
                          on_click=lambda: router.push("/data_stories"))
            solara.Button("Mini Stories", text=True,
                          on_click=lambda: router.push("/"))

            rv.Spacer()

            if not GLOBAL_STATE.user.authorized():
                Login()
            else:
                # TODO: avoid constant DB class on reload
                GLOBAL_STATE.user.check_database()

                if not GLOBAL_STATE.user.exists_and_setup():
                    if route_current.path != 'account_setup':
                        def _to_account_setup():
                            router.push(f"/account_setup")

                        rv.Snackbar(v_model=snackbar, on_v_model=set_snackbar,
                                    timeout=0,
                                    # Indefinitely: 0 for veutify < 2.3
                                    children=[
                                        "Your account has not been setup.",
                                        solara.Button("Setup",
                                                      on_click=_to_account_setup)])
                else:
                    if GLOBAL_STATE.user.is_educator():
                        solara.Button("Create Class",
                                      text=True,
                                      elevation=0,
                                      # outlined=True,
                                      color='green',
                                      on_click=lambda: router.push(
                                          "/create"))
                        solara.Button("Dashboard",
                                      text=True,
                                      elevation=0,
                                      # outlined=True,
                                      # color='green',
                                      on_click=lambda: router.push(
                                          "/dashboard"))
                    elif GLOBAL_STATE.user.is_student():
                        solara.Button("Join Class",
                                      text=False,
                                      elevation=0,
                                      outlined=True,
                                      color='green',
                                      on_click=lambda: router.push(
                                          "/join"))

            if GLOBAL_STATE.user.exists():
                rv.Divider(vertical=True, class_="ml-4")

                solara.Button(icon_name="mdi-account",
                              text=False,
                              icon=True,
                              outlined=False,
                              on_click=lambda: router.push(
                                  "/account"),
                              classes=['ml-2'])

                def _logout():
                    GLOBAL_STATE.user.logout()

                solara.Button(
                    # "Logout",
                    icon_name="mdi-logout",
                    text=False,
                    icon=True,
                    outlined=False,
                    href=auth.get_logout_url(),
                    on_click=lambda: _logout(),
                    depressed=True,
                )

        with rv.Content():
            if route_current.path == '/':
                Hero()

            with rv.Container(children=children, class_="pt-8",
                              style_="max-width: 1200px"):
                pass

        with rv.Footer(app=False, padless=True):
            with rv.Container():
                with rv.Row():
                    with rv.Col(class_="d-flex justify-center"):
                        rv.Btn(children=["About"], text=True)
                        rv.Btn(children=["Team"], text=True)
                        rv.Btn(children=["Contact"], text=True)
                        rv.Btn(children=["Privacy"], text=True)
                        rv.Btn(children=["Digital Accessibility"], text=True)

                rv.Divider()

                with rv.Row():
                    with rv.Col(class_="d-flex justify-center"):
                        rv.Html(
                            tag="p",
                            children=[
                                "Copyright © 2023 The President and Fellows of Harvard College"
                            ],
                        )

    return main
