from typing import Optional
from aiohttp_apispec import setup_aiohttp_apispec
from aiohttp.web import Application as AiohttpApplication, \
    run_app as aiohttp_run_app, \
    View as AiohttpView, Request as AiohhtpRequest

from app.store.crm import setup_accessors
# from app.store.crm.accessor import CrmAccessor
from app.web.routes import setup_routes
from app.web.middlewares import setup_middlewares


class Application(AiohttpApplication):
    database: dict = {}
    # crm_accessor: Optional[CrmAccessor] = None


class Request(AiohhtpRequest):
    @property
    def app(self) -> "Application":
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    setup_routes(app)
    setup_aiohttp_apispec(app, title="CRM Application", url="/docs/json",
                          swagger_path="/docs")
    setup_middlewares(app)
    setup_accessors(app)
    aiohttp_run_app(app)



