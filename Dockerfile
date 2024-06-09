ARG NETBOX_VARIANT=v4.0

FROM netboxcommunity/netbox:${NETBOX_VARIANT}

RUN mkdir -pv /plugins/netbox-vrf-ext
COPY . /plugins/netbox-vrf-ext

RUN /opt/netbox/venv/bin/pip3 install --editable /plugins/netbox-vrf-ext/ && \
    cp -rf /plugins/netbox-vrf-ext/netbox_vrf_ext/ /opt/netbox/venv/lib/python3.11/site-packages/netbox_vrf_ext
