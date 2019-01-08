from __future__ import unicode_literals
from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.document import Document
from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import BufferControl
from prompt_toolkit.layout.margins import ScrollbarMargin
from prompt_toolkit.shortcuts import create_eventloop


manager = KeyBindingManager()

def get_default_text():
    return '\n'.join('%s' % i for i in range(100))


@manager.registry.add_binding(Keys.ControlQ, eager=True)
@manager.registry.add_binding(Keys.ControlC, eager=True)
def _(event):
    event.cli.set_return_value(None)

app = Application(
    layout=Window(
        content=BufferControl(buffer_name=DEFAULT_BUFFER),
        right_margins=[ScrollbarMargin(display_arrows=True)]),
    buffers={
        DEFAULT_BUFFER: Buffer(
            initial_document=Document(get_default_text(), 0))
    },
    key_bindings_registry=manager.registry,
    mouse_support=True,
    use_alternate_screen=True
)

eventloop = create_eventloop()
try:
    app.run()
finally:
    eventloop.close()