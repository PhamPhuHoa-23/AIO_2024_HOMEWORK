import torch


class Softmax(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x_exp = torch.exp(x)
        partition = x_exp.sum()
        return x_exp / partition


class SoftmaxStable(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self,  x: torch.Tensor):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdim=True)
        return x_exp / partition


if __name__ == '__main__':
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    print(output)  # tensor([0.0900, 0.2447, 0.6652])

    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    print(output)  # tensor([0.0900, 0.2447, 0.6652])

    data = torch.Tensor([1, 2, 300000000])
    output = softmax(data)
    print(output)
