import torch


_initialized = False
_scope = locals()


def extend_scope(module):
    _scope.update({k: getattr(module, k) for k in dir(module) if not k.startswith('_')})


def init_process_group(backend):
    global _initialized
    if _initialized:
        raise RuntimeError("trying to initialize torch.distributed twice!")
    torch._C._dist_init_process_group(backend)
    _initialized = True
    import torch.distributed.collectives as collectives
    extend_scope(collectives)
    assert torch._C._dist_init_extension(reduce_op)


def init_master_worker(backend):
    global _initialized
    if _initialized:
        raise RuntimeError("trying to initialize torch.distributed twice!")
    torch._C._dist_init_master_worker(backend)
    _initialized = True
    import torch.distributed.collectives as collectives
    # import torch.distributed.remote_types as remote_types
    extend_scope(collectives)
    # extend_scope(remote_types)
    assert torch._C._dist_init_extension(reduce_op)
