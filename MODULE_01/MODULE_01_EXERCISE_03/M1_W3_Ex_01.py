import torch
from math import exp


class Softmax(torch.nn.Module):
    def forward(self, tensor_lst: torch.Tensor) -> torch.t:
        total = 0
        for x in tensor_lst:
            total += exp(x)

        return torch.Tensor([exp(x) / total for x in tensor_lst])


class SoftmaxStable(torch.nn.Module):
    def forward(self, tensor_lst: torch.Tensor):
        c = tensor_lst.max()
        total = 0
        for x in tensor_lst:
            total += exp(x - c)

        return torch.Tensor([exp(x - c) / total for x in tensor_lst])


if __name__ == '__main__':
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    print(output)  # tensor([0.0900, 0.2447, 0.6652])

    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    print(output)  # tensor([0.0900, 0.2447, 0.6652])
