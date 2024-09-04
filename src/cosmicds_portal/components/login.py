import httpx
from os import getenv
import solara
from solara.alias import rv

from ..pages.state import GLOBAL_STATE
from ..utils import CDS_API_URL


@solara.component
def Login(**btn_kwargs):
    active, set_active = solara.use_state(False)
    username, set_username = solara.use_state("")
    password, set_password = solara.use_state("")

    def _login():
        r = httpx.put(
            f"{CDS_API_URL}/login",
            data={
                "username": username,
                "password": password
            },
            headers={
                "Authorization": getenv("CDS_API_KEY", "")
            })

        if r.status_code == 200:
            payload = r.json()
            GLOBAL_STATE.user.username.set(payload["user"]["username"])
            GLOBAL_STATE.user.type.set(payload["type"])
            GLOBAL_STATE.user.setup_completed.set(True)

    with rv.Dialog(
            v_model=active,
            on_v_model=set_active,
            v_slots=[{"name": "activator", "variable": "x",
                      "children": rv.Btn(v_on="x.on", v_bind="x.attrs",
                                         children=["Sign In"], **btn_kwargs)}],
            max_width=600,
    ) as login:
        with rv.Card():
            # user = await manager.get_current_user(
            #     token=request.cookies.get('token'))
            # rv.Html(tag='div', children=[f"{user}"])

            with rv.CardTitle():
                rv.Html(tag="div", class_="text-h5", children=["Login"])

            with rv.CardText():
                with rv.Container():
                    rv.Html(tag='div', children=[f"Is active? {active}"])
                    with rv.Row():
                        with rv.Col(cols=12):
                            rv.TextField(label="Username",
                                         v_model=username,
                                         on_v_model=set_username)
                        with rv.Col(cols=12):
                            rv.TextField(label="Password",
                                         v_model=password,
                                         on_v_model=set_password)

            with rv.CardActions():
                def _on_submit_clicked(*args):
                    _login()
                    if GLOBAL_STATE.user.exists():
                        set_active(False)

                rv.Spacer()

                close_btn = rv.Btn(children=["Close"], text=True)
                rv.use_event(close_btn, 'click',
                             lambda *args: set_active(False))

                submit_btn = rv.Btn(children=["Submit"], text=True)
                rv.use_event(submit_btn, 'click', _on_submit_clicked)

    return login
