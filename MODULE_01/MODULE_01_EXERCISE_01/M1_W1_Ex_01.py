import sys


def is_interger(var):
    try:
        if int(var) != var:
            return False
        return True
    except ValueError:
        return False


def evaluate_model(tp: int, fp: int, fn: int) -> None:
    # CHECK TYPE OF VARIABLES
    if not is_interger(tp):
        sys.exit("TP must be int!")
    if not is_interger(fp):
        sys.exit("FP must be int!")
    if not is_interger(fn):
        sys.exit("FN must be int!")

    # VALIDATION VARIABLE VALUES
    if tp <= 0:
        sys.exit("TP must be greater than 0")
    if fp <= 0:
        sys.exit("FP must be greater than 0")
    if fn <= 0:
        sys.exit("FN must be greater than 0")

    # PROCESSING
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f"Precision is {precision:2f}")
    print(f"Recall is {recall:2f}")
    print(f"F1-Score is {f1_score:2f}")


# Unit test
if __name__ == '__main__':
    evaluate_model(tp=2, fp=3, fn=4)
    # evaluate_model(tp='a', fp=3, fn=4)
    # evaluate_model(tp=2, fp='a', fn=4)
    # evaluate_model(tp=2, fp=3, fn='a')
    # evaluate_model(tp=2, fp=3, fn=0)
    # evaluate_model(tp=2.1, fp=3, fn=0)