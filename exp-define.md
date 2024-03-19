::: {.cell .markdown}
### Define configuration for this experiment (one server)
:::

::: {.cell .code}
```python
slice_name="hello_linux-" + fablib.get_bastion_username()

node_conf = [
 {'name': "server",   'cores': 1, 'ram': 2, 'disk': 10, 'image': 'default_ubuntu_22', 'packages': []}
]
net_conf = []
route_conf = []
exp_conf = {'cores': 1, 'nic': 0 }
```
:::
