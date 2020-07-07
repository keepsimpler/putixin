# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/000_hamilton.ipynb (unless otherwise specified).

__all__ = ['HamLinear']

# Cell
# server
import torch
import torch.nn as nn
import torch.nn.functional as F

# Cell
class HamLinear(nn.Module):
    """
    Hamilonian Linear Module.
    Args:
    -- row, col:
    -- alpha:
    -- std:
    -- act:
    -- is_alpha_trainable:
    """
    def __init__(self, row:int, col:int, alpha:float, std:float=None, act:nn.Module=nn.ReLU, is_alpha_trainable:bool=False):
        super(HamLinear, self).__init__()
        if std is None:
            self.std = torch.sqrt(2*torch.tensor(row+col, dtype=torch.float))
        else:
            self.std = torch.tensor(std, dtype=torch.float)

        self.W = nn.Parameter(torch.randn(row, col) / self.std)

        if is_alpha_trainable:
            self.alpha = nn.Parameter(torch.tensor(alpha))
        else:
            self.alpha = torch.tensor(alpha)

        self.act = act()

    def forward(self, x, y:torch.tensor=None):
        if y is None:
            y = self.alpha / 2 * self.act(x).matmul(-self.W.T)
        else:
            x = x + self.alpha * self.act(y).matmul(self.W)
            y = y + self.alpha * self.act(x).matmul(-self.W.T)
        return x, y