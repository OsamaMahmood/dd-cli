from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedEndpointRequest")


@_attrs_define
class PatchedEndpointRequest:
    """
    Attributes:
        tags (list[str] | Unset):
        protocol (None | str | Unset): The communication protocol/scheme such as 'http', 'ftp', 'dns', etc.
        userinfo (None | str | Unset): User info as 'alice', 'bob', etc.
        host (None | str | Unset): The host name or IP address. It must not include the port number. For example
            '127.0.0.1', 'localhost', 'yourdomain.com'.
        port (int | None | Unset): The network port associated with the endpoint.
        path (None | str | Unset): The location of the resource, it must not start with a '/'. For example
            endpoint/420/edit
        query (None | str | Unset): The query string, the question mark should be omitted.For example 'group=4&team=8'
        fragment (None | str | Unset): The fragment identifier which follows the hash mark. The hash mark should be
            omitted. For example 'section-13', 'paragraph-2'.
        product (int | None | Unset):
    """

    tags: list[str] | Unset = UNSET
    protocol: None | str | Unset = UNSET
    userinfo: None | str | Unset = UNSET
    host: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    path: None | str | Unset = UNSET
    query: None | str | Unset = UNSET
    fragment: None | str | Unset = UNSET
    product: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        protocol: None | str | Unset
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        userinfo: None | str | Unset
        if isinstance(self.userinfo, Unset):
            userinfo = UNSET
        else:
            userinfo = self.userinfo

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        fragment: None | str | Unset
        if isinstance(self.fragment, Unset):
            fragment = UNSET
        else:
            fragment = self.fragment

        product: int | None | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if userinfo is not UNSET:
            field_dict["userinfo"] = userinfo
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if path is not UNSET:
            field_dict["path"] = path
        if query is not UNSET:
            field_dict["query"] = query
        if fragment is not UNSET:
            field_dict["fragment"] = fragment
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.protocol, Unset):
            if isinstance(self.protocol, str):
                files.append(("protocol", (None, str(self.protocol).encode(), "text/plain")))
            else:
                files.append(("protocol", (None, str(self.protocol).encode(), "text/plain")))

        if not isinstance(self.userinfo, Unset):
            if isinstance(self.userinfo, str):
                files.append(("userinfo", (None, str(self.userinfo).encode(), "text/plain")))
            else:
                files.append(("userinfo", (None, str(self.userinfo).encode(), "text/plain")))

        if not isinstance(self.host, Unset):
            if isinstance(self.host, str):
                files.append(("host", (None, str(self.host).encode(), "text/plain")))
            else:
                files.append(("host", (None, str(self.host).encode(), "text/plain")))

        if not isinstance(self.port, Unset):
            if isinstance(self.port, int):
                files.append(("port", (None, str(self.port).encode(), "text/plain")))
            else:
                files.append(("port", (None, str(self.port).encode(), "text/plain")))

        if not isinstance(self.path, Unset):
            if isinstance(self.path, str):
                files.append(("path", (None, str(self.path).encode(), "text/plain")))
            else:
                files.append(("path", (None, str(self.path).encode(), "text/plain")))

        if not isinstance(self.query, Unset):
            if isinstance(self.query, str):
                files.append(("query", (None, str(self.query).encode(), "text/plain")))
            else:
                files.append(("query", (None, str(self.query).encode(), "text/plain")))

        if not isinstance(self.fragment, Unset):
            if isinstance(self.fragment, str):
                files.append(("fragment", (None, str(self.fragment).encode(), "text/plain")))
            else:
                files.append(("fragment", (None, str(self.fragment).encode(), "text/plain")))

        if not isinstance(self.product, Unset):
            if isinstance(self.product, int):
                files.append(("product", (None, str(self.product).encode(), "text/plain")))
            else:
                files.append(("product", (None, str(self.product).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_protocol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_userinfo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        userinfo = _parse_userinfo(d.pop("userinfo", UNSET))

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_fragment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fragment = _parse_fragment(d.pop("fragment", UNSET))

        def _parse_product(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        patched_endpoint_request = cls(
            tags=tags,
            protocol=protocol,
            userinfo=userinfo,
            host=host,
            port=port,
            path=path,
            query=query,
            fragment=fragment,
            product=product,
        )

        patched_endpoint_request.additional_properties = d
        return patched_endpoint_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
