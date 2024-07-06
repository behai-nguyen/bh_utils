Application Logger Configuration
--------------------------------

This package uses the default ``bh_utils`` logger. This logger is set with a `‘no-op’ NullHandler 
handler <https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler>`_, 
as recommended by the official documentation on 
`Configuring Logging for a Library <https://docs.python.org/3/howto/logging.html#library-config>`_ .

The following example demonstrates how applications can enable this logger.

**The logging.yaml logger configuration:**

.. code-block:: yaml

    version: 1
    disable_existing_loggers: false

    formatters:
        standard:
            format: "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)s - %(funcName)s() - %(message)s"
    handlers:
        console:
            formatter: standard
            class: logging.StreamHandler
            stream: ext://sys.stdout
            level: DEBUG
    loggers:
        bh_utils:
            level: DEBUG
            handlers: [ console ]
            propagate: no    

**The demo.py Python script:**

.. code-block:: python

    import logging.config
    import yaml

    import bh_utils.template_funcs

    def register_loggers():
        with open('logging.yaml', 'rt') as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)

    register_loggers()

    tmpl_path = bh_utils.template_funcs.template_path("reports", source_dir="tests").lower()
    print(f"tmpl_path: {tmpl_path}")

**The command to run**::

    ▶️Windows 10: (venv) F:\\pydev>venv\\Scripts\\python.exe demo.py
    ▶️Ubuntu 22.10: (venv) behai@hp-pavilion-15:~/pydev$ ./venv/bin/python demo.py

**The output we should see**::

    (venv) behai@hp-pavilion-15:~/pydev$ ./venv/bin/python demo.py
    2024-07-06 00:52:15,813 - bh_utils - DEBUG - template_funcs.py:71 - template_root_path() - base_dir: /home/behai/pydev, source_dir: tests, project_path: pydev
    tmpl_path: /home/behai/pydev/tests/pydev/templates/reports
    (venv) behai@hp-pavilion-15:~/pydev$
