from typing import List, Tuple

class Callback:
    def __init__(self): pass
    def on_train_begin(self, model, **kwargs): pass
    def on_train_end(self, model, **kwargs): pass
    def on_epoch_begin(self, model, **kwargs): pass
    def on_epoch_end(self, model, **kwargs): pass
    def on_batch_begin(self, model, **kwargs): pass
    def on_batch_end(self, model, **kwargs): pass
    def on_loss_begin(self, model, **kwargs): pass
    def on_loss_end(self, model, **kwargs): pass
    def on_step_begin(self, model, **kwargs): pass
    def on_step_end(self, model, **kwargs): pass


class CallbackHandler:
    def __init__(self, callbacks: List[Callback], model):
        self.model = model
        self.callbacks = callbacks

    def __call__(self, current_state, **kwargs):
        for cb in self.callbacks:
            _ = getattr(cb, current_state)(self.model, **kwargs)

"""
class Callback:
    def __init__(self): pass
    def on_train_begin(self): pass
    def on_train_end(self): pass
    def on_epoch_begin(self): pass
    def on_epoch_end(self): pass
    def on_batch_begin(self): pass
    def on_batch_end(self): pass
    def on_loss_begin(self): pass
    def on_loss_end(self): pass
    def on_step_begin(self): pass
    def on_step_end(self): pass

class Callback:
    def on_epoch_start(self, model, **kwargs):
        return

    def on_epoch_end(self, model, **kwargs):
        return

    def on_train_epoch_start(self, model, **kwargs):
        return

    def on_train_epoch_end(self, model, **kwargs):
        return

    def on_valid_epoch_start(self, model, **kwargs):
        return

    def on_valid_epoch_end(self, model, **kwargs):
        return

    def on_train_step_start(self, model, **kwargs):
        return

    def on_train_step_end(self, model, **kwargs):
        return

    def on_valid_step_start(self, model, **kwargs):
        return

    def on_valid_step_end(self, model, **kwargs):
        return

    def on_test_step_start(self, model, **kwargs):
        return

    def on_test_step_end(self, model, **kwargs):
        return

    def on_train_start(self, model, **kwargs):
        return

    def on_train_end(self, model, **kwargs):
        return


class CallbackHandler:
    def __init__(self, callbacks: List[Callback], model):
        self.model = model
        self.callbacks = callbacks

    def __call__(self, current_state, **kwargs):
        for cb in self.callbacks:
            _ = getattr(cb, current_state.value)(self.model, **kwargs)
"""