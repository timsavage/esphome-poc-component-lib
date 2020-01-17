##############
ESPHome Extras
##############

This is a proof of concept external library for ESPHome. Specifically for pull
request `#957 <https://github.com/esphome/esphome/pull/957>`_.

This utilises setuptools entry points to register itself as a component provider.

See the ``options.entry_points`` section of the ``setup.cfg`` file for an example.

To try out this library you will need to:

- Clone of ESPHome from `https://www.github.com/timsavage/esphome`_ and fetch the 
  ``feature/component-entry-points`` branch (unless this has been merged!)

- Clone this repository and use ``python setup.py develop`` to "install" the package
  into your current Python environment (strongly recommend a virtual env).

See the file ``sample/temp_sensor.yaml`` for an example of using a TMP102 sensor.
In this case you need to set the platform to ``tmp102x`` (the tmp102 sensor is 
currently awaiting PR approval) to ensure it's unique.

Compile away!

