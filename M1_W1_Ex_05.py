def md_nre_single_sample(target: float, predict: float, n: int, p: int):
    print(((target) ** (1 / n) - predict ** (1 / n)) ** p)


# Unit test
if __name__ == '__main__':
    md_nre_single_sample(target=100, predict=95, n=2, p=1)
    md_nre_single_sample(target=50, predict=49.5, n=2, p=1)
    md_nre_single_sample(target=20, predict=19.5, n=2, p=1)
    md_nre_single_sample(target=0.6, predict=0.1, n=2, p=1)