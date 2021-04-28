import torch
import torch.nn as nn
from callbacks import Callback, CallbackHandler
from tqdm import tqdm
import numpy as np

class AverageMonitor:
    def __init__(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

class Model(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.optimizer = None
        self.scheduler = None
        self.train_loader = None
        self.valid_loader = None
        self.current_epoch = 0
        self._model_state = None
        self._train_state = None
        self.device = None
        self._cb_Handler = None
        self.metrics = {}
        self.metrics["train"] = {}
        self.metrics["valid"] = {}
        self.metrics["test"] = {}
        self.fp16 = False
        self.scaler = None

    @property
    def model_state(self):
        return self._model_state

    @model_state.setter
    def model_state(self, value):
        self._model_state = value
        
    @property
    def train_state(self):
        return self._train_state

    @train_state.setter
    def train_state(self, value):
        self._train_state = value
        if self._cb_Handler is not None:
            self._cb_Handler(value)


    def _init_model(
            self,
            device,
            train_dataset,
            valid_dataset,
            train_sampler,
            valid_sampler,
            train_bs,
            valid_bs,
            n_jobs,
            callbacks,
            fp16,
            train_collate_fn,
            valid_collate_fn,
        ):


        if callbacks is None:
            callbacks = list()

        if n_jobs == -1:
            n_jobs = psutil.cpu_count()

        self.device = device

        if next(self.parameters()).device != self.device:
            self.to(self.device)

        if self.train_loader is None:
            self.train_loader = torch.utils.data.DataLoader(
                train_dataset,
                batch_size=train_bs,
                num_workers=n_jobs,
                sampler=train_sampler,
                shuffle=True,
                collate_fn=train_collate_fn,
            )
        if self.valid_loader is None:
            if valid_dataset is not None:
                self.valid_loader = torch.utils.data.DataLoader(
                    valid_dataset,
                    batch_size=valid_bs,
                    num_workers=n_jobs,
                    sampler=valid_sampler,
                    shuffle=False,
                    collate_fn=valid_collate_fn,
                )

        if self.optimizer is None:
            self.optimizer = self.fetch_optimizer()

        if self.scheduler is None:
            self.scheduler = self.fetch_scheduler()

        self.fp16 = fp16
        if self.fp16:
            self.scaler = torch.cuda.amp.GradScaler()

        self._cb_Handler = CallbackHandler(callbacks, self)


    def monitor_metrics(self, *args, **kwargs):
        return
    
    def update_metrics(self, losses, monitor):
        self.metrics[self._model_state].update(monitor)
        self.metrics[self._model_state]["loss"] = losses.avg
    
    def fetch_optimizer(self, *args, **kwargs):
        return

    def fetch_scheduler(self, *args, **kwargs):
        return

    def forward(self, *args, **kwargs):
        return super().forward(*args, **kwargs)

    def model_fn(self, data):
        for key, value in enumerate(data):
            data[key] = value.to(self.device)
        if self.fp16:
            with torch.cuda.amp.autocast():
                output, loss, metrics = self(*data)
        else:
            output, loss, metrics = self(*data)
        return output, loss, metrics

    def train_one_step(self, data, device='cuda'):
        self.optimizer.zero_grad()
        self.train_state = 'on_loss_begin'
        _ , loss, metrics = self.model_fn(data)
        loss.backward()
        self.train_state = 'on_step_begin'
        self.optimizer.step()
        self.scheduler.step()
        self.train_state = 'on_step_end'
        return loss, metrics

    def train_one_epoch(self, dataloader, device='cuda'):
        self.train()
        self.model_state = 'train'
        losses = AverageMonitor()
        tk0 = tqdm(dataloader, total=len(dataloader))
        for b_idx, data in enumerate(tk0):
            self.train_state = 'on_batch_begin'
            loss, metrics = self.train_one_step(data, device)
            losses.update(loss.item(), dataloader.batch_size)
            if b_idx == 0:
                metrics_monitor = {k: AverageMonitor() for k in metrics}
            monitor = {}
            for m in metrics_monitor:
                metrics_monitor[m].update(metrics[m], dataloader.batch_size)
                monitor[m] = metrics_monitor[m].avg
            tk0.set_postfix(loss=losses.avg, stage="Train", **monitor)
            self.train_state = 'on_batch_end'
        tk0.close()
        self.update_metrics(losses=losses, monitor=monitor)
        return losses.avg
    
    def validate_one_step(self, data, device='cuda'):
        _, loss, metrics = self.model_fn(data) #acc = self.metrics(out, data[1])
        return loss, metrics
    
    def validate_one_epoch(self, dataloader, device='cuda'):
        self.eval()
        self.model_state = 'valid'
        losses = AverageMonitor()
        epoch_loss = 0.0
        epoch_acc = 0.0
        tk0 = tqdm(dataloader, total=len(dataloader))
        for b_idx, data in enumerate(tk0):
            with torch.no_grad():
                loss, metrics = self.validate_one_step(data, device)
            losses.update(loss.item(), dataloader.batch_size)
            if b_idx == 0:
                metrics_monitor = {k: AverageMonitor() for k in metrics}
            monitor = {}
            for m in metrics_monitor:
                metrics_monitor[m].update(metrics[m], dataloader.batch_size)
                monitor[m] = metrics_monitor[m].avg
            tk0.set_postfix(loss=losses.avg, stage="Valid", **monitor)
        tk0.close()
        self.update_metrics(losses=losses, monitor=monitor)
        return losses.avg

    def fit(
        self,
        train_dataset,
        valid_dataset=None,
        train_sampler=None,
        valid_sampler=None,
        device="cuda",
        epochs=10,
        train_bs=16,
        valid_bs=16,
        n_jobs=8,
        callbacks=None,
        fp16=False,
        train_collate_fn=None,
        valid_collate_fn=None,
        ):
        
        self._init_model(
            device=device,
            train_dataset=train_dataset,
            valid_dataset=valid_dataset,
            train_sampler=train_sampler,
            valid_sampler=valid_sampler,
            train_bs=train_bs,
            valid_bs=valid_bs,
            n_jobs=n_jobs,
            callbacks=callbacks,
            fp16=fp16,
            train_collate_fn=train_collate_fn,
            valid_collate_fn=valid_collate_fn,
        )
        self.train_state = 'on_train_begin' #self._cb_Handler('on_train_begin')
        for _ in range(epochs):
            self.train_state = 'on_epoch_begin'
            train_loss = self.train_one_epoch(self.train_loader, device=device)
            if self.valid_loader:
                valid_loss = self.validate_one_epoch(self.valid_loader, device=device)
            self.train_state = 'on_epoch_end'
            if self.model_state == "end":
                break
            self.current_epoch += 1
        self.train_state = 'on_train_end'

    def predict_one_step(self, data, device='cuda'):
        for key, value in enumerate(data):
            data[key] = value.to(device)
        out, _, _ = self(*data)
        return out

    def process_output(self, output):
        output = output.cpu().detach().numpy()
        return output

    def predict(self, dataset, device, sampler=None, batch_size=16):
        if next(self.parameters()).device != device:
            self.to(device)

        dataloader = torch.utils.data.DataLoader(
            dataset, batch_size=batch_size, sampler=sampler,
        )
        self.model_state = 'test'
        self.eval()
        tk0 = tqdm(dataloader, total=len(dataloader))
        final_out = torch.tensor([]).to(device)
        for data in tk0:
            with torch.no_grad():
                out = self.predict_one_step(data, device)
                final_out = torch.cat([final_out, out])
            tk0.set_postfix(stage="Test")        
        
        final_out = self.process_output(final_out)
        val = np.argmax(final_out, axis=1)
        tk0.close()
        return final_out, val

    def predict_one_image(self, data, device):
        if next(self.parameters()).device != device:
            self.to(device)
        
        self.model_state = 'test'
        self.eval()
        
        with torch.no_grad():
            for key, value in enumerate(data):
                data[key] = value.to(device)
            out, _, _ = self(data)
            out = self.process_output(out)
            val = np.argmax(out, axis=1)
            return out, val

    def save(self, model_path):
        model_state_dict = self.state_dict()
        if self.optimizer is not None:
            opt_state_dict = self.optimizer.state_dict()
        else:
            opt_state_dict = None
        if self.scheduler is not None:
            sch_state_dict = self.scheduler.state_dict()
        else:
            sch_state_dict = None
        model_dict = {}
        model_dict["state_dict"] = model_state_dict
        model_dict["optimizer"] = opt_state_dict
        model_dict["scheduler"] = sch_state_dict
        torch.save(model_dict, model_path)
    
    def save_model(self, model_path):
        model_state_dict = self.state_dict()
        model_dict = { "state_dict": model_state_dict }
        torch.save(model_dict, model_path)
    
    def load(self, model_path, device="cuda"):
        if next(self.parameters()).device != device:
            self.to(device)
        model_dict = torch.load(model_path, map_location=torch.device(device))
        self.load_state_dict(model_dict["state_dict"])