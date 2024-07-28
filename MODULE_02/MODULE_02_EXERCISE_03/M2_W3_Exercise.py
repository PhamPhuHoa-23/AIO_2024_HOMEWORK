import numpy as np


def main():
    x = ['Sunny', 'Cool', 'High', 'Strong']
    data = create_train_data()
    # print(f'Data: \n {data} \n')
    prior_probability, conditional_probability, list_x_name = train_naive_bayes(data)
    # print(f'Prior Probability: P(no) = {prior_probability[0]}, P(yes) = {prior_probability[1]}')
    # print(f'\nList attribute name: {list_x_name}')
    # print(f'\nConditional Probability: \n{conditional_probability}')
    prediction_play_tennis(x, list_x_name, prior_probability, conditional_probability)
    if prediction_play_tennis == 1:
        print('Ad should play tennis')
    else:
        print('Ad should not play tennis')


def create_train_data():
    data = [
        ['Sunny','Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes'],
    ]

    return np.array(data)


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))

    for i, pr in enumerate(y_unique):
        prior_probability[i] = np.sum(train_data[:, -1] == y_unique[i]) / len(train_data)

    return prior_probability


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']

    conditional_probability = []

    list_x_name = []

    prior_probability = compute_prior_probability(train_data)

    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])

        list_x_name.append(x_unique)

        list_x_given_y_probability = []

        for index, y_name in enumerate(y_unique):
            x_conditional_probability = []
            for x_name in x_unique:
                pr_x_name = np.sum(train_data[:, i] == x_name) / len(train_data)

                pr_x_name_and_y_name = np.sum((train_data[:, - 1] == y_name) & (train_data[:, i] == x_name)) / len(train_data)

                pr_x_given_y_name = pr_x_name_and_y_name / prior_probability[index]

                x_conditional_probability.append(pr_x_given_y_name)

            list_x_given_y_probability.append(x_conditional_probability)

        conditional_probability.append(np.array(list_x_given_y_probability))

    return conditional_probability, list_x_name


def get_index_from_value(feature_name , list_features):
    return np.where(list_features == feature_name)[0][0]


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    y_unique = ['no', 'yes']
    prior_probability = compute_prior_probability(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(train_data)

    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    # x1 = get_index_from_value(X[0], list_x_name[0])
    # x2 = get_index_from_value(X[0], list_x_name[1])
    # x3 = get_index_from_value(X[0], list_x_name[2])
    # x4 = get_index_from_value(X[0], list_x_name[3])
    list_of_index = []

    for i, condition in enumerate(X):
        list_of_index.append(get_index_from_value(condition, list_x_name[i]))

    p_no, p_yes = prior_probability

    p_x_given_yes = 1
    p_x_given_no = 1

    for i, index in enumerate(list_of_index):
        p_x_given_yes *= conditional_probability[i][1, index]
        p_x_given_no *= conditional_probability[i][0, index]

    if p_x_given_yes * p_yes > p_x_given_no * p_no:
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()
