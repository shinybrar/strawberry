from typing import Callable, Optional

from mypy.plugin import AnalyzeTypeContext, ClassDefContext, Plugin
from mypy.plugins import dataclasses
from mypy.types import Type


def lazy_type_analyze_callback(ctx: AnalyzeTypeContext) -> Type:
    type_name = ctx.type.args[0]
    type_ = ctx.api.analyze_type(type_name)

    return type_


def strawberry_pydantic_class_callback(ctx: ClassDefContext):
    # in future we want to have a proper pydantic plugin, but for now
    # let's fallback to any, some resources are here:
    # https://github.com/samuelcolvin/pydantic/blob/master/pydantic/mypy.py
    # >>> model_index = ctx.cls.decorators[0].arg_names.index("model")
    # >>> model_name = ctx.cls.decorators[0].args[model_index].name

    # >>> model_type = ctx.api.named_type("UserModel")
    # >>> model_type = ctx.api.lookup(model_name, Context())

    ctx.cls.info.fallback_to_any = True


class StrawberryPlugin(Plugin):
    def get_type_analyze_hook(self, fullname: str):
        if fullname == "strawberry.lazy_type.LazyType":
            return lazy_type_analyze_callback

        return None

    def get_class_decorator_hook(
        self, fullname: str
    ) -> Optional[Callable[[ClassDefContext], None]]:
        if any(
            strawberry_decorator in fullname
            for strawberry_decorator in {
                "strawberry.type",
                "strawberry.federation.type",
                "strawberry.input",
                "strawberry.interface",
            }
        ):
            return dataclasses.dataclass_class_maker_callback

        if "strawberry.pydantic.type" in fullname:
            return strawberry_pydantic_class_callback

        return None


def plugin(version: str):
    return StrawberryPlugin
