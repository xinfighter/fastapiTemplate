from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

from .token import token_router
from .user import user_router
from settings import settings


def routers_init(app: FastAPI):
    if settings.debug:
        _custom_swagger_ui(app)
        _custom_redoc(app)

    app.include_router(token_router)
    app.include_router(user_router)


def _custom_swagger_ui(app: FastAPI):
    """
    自定义docs接口
        1. 解决swagger-ui静态文件加载失败问题
        2. 不显示schema
    """

    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=f"{app.title} - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui/swagger-ui.css",
            swagger_ui_parameters={"defaultModelsExpandDepth": -1}
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()


def _custom_redoc(app: FastAPI):
    """
    自定义redoc接口 解决静态文件加载失败问题
    """

    @app.get("/redoc", include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title=f"{app.title} - ReDoc",
            redoc_js_url="/static/redoc/redoc.standalone.js",
        )
