from typing import Any

from ...decorators.syft_decorator_impl import syft_decorator
from .primitive_interface import PyPrimitive
from .primitive_factory import PrimitiveFactory
from .util import SyPrimitiveRet


class Tuple(tuple, PyPrimitive):
    def __init__(self, *args):
        super(Tuple, self).__init__(*args)

    def __new__(cls, *args):
        return super(Tuple, cls).__new__(cls, args)

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __add__(self, other: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__add__(other))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __contains__(self, item: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__contains__(item))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __eq__(self, other: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__eq__(other))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __ne__(self) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__ne__())

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __ge__(self, other: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__ge__(other))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __gt__(self, other: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__gt__(other))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __le__(self, other: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__le__(other))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __lt__(self, other: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__lt__(other))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __mul__(self, other: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__mul__(other))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __rmul__(self, other: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__rmul__(other))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __len__(self) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__len__())

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __getitem__(self, item: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().__getitem__(item))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def count(self, __value: Any) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().count(__value))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def index(self, __value: Any, __start: Any = ..., __stop: Any = ...) -> SyPrimitiveRet:
        return PrimitiveFactory.generate_primitive(value=super().index(
            __value, __stop))

    @syft_decorator(typechecking=True, prohibit_args=False)
    def __iter__(self) -> SyPrimitiveRet:
        return self

    @staticmethod
    @syft_decorator(typechecking=True)
    def _proto2object(proto: Tuple_PB) -> "Tuple":
        pass

    @staticmethod
    @syft_decorator(typechecking=True)
    def _object2proto(self) -> Tuple_PB:
        pass

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        return Tuple_PB

class TupleWrapper(StorableObject):
    def __init__(self, value: object):
        super().__init__(
            data=value,
            id=getattr(value, "id", UID()),
            tags=getattr(value, "tags", []),
            description=getattr(value, "description", ""),
        )
        self.value = value

    def _data_object2proto(self) -> Int_PB:
        _object2proto = getattr(self.data, "_object2proto", None)
        if _object2proto:
            return _object2proto()

    @staticmethod
    def _data_proto2object(proto: Int_PB) -> "IntWrapper":
        return Tuple._proto2object(proto=proto)

    @staticmethod
    def get_data_protobuf_schema() -> GeneratedProtocolMessageType:
        return Tuple_PB

    @staticmethod
    def get_wrapped_type() -> type:
        return Tuple

    @staticmethod
    def construct_new_object(
        id: UID,
        data: StorableObject,
        description: Optional[str],
        tags: Optional[List[str]],
    ) -> StorableObject:
        setattr(data, "_id", id)
        data.tags = tags
        data.description = description
        return data

aggressive_set_attr(obj=Tuple, name="serializable_wrapper_type", attr=TupleWrapper)